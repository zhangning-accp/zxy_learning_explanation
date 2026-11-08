const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const html = fs.readFileSync(path.join(__dirname, '..', '数学小课堂', '14-动点问题.html'), 'utf8');
let script = html.match(/<script>([\s\S]*?)<\/script>/)[1];
assert.match(script, /render\(\);\s*\}\)\(\);\s*$/);
// Expose the calculations in an isolated context; do not alter the delivered HTML.
script = script.replace(/render\(\);\s*\}\)\(\);\s*$/, `
globalThis.subject = { lessons, parseNumber, correct, makeExam, sceneData,
  setScene(value, view = 'ground') { sceneValue = value; frame = view; }, state };
})();`);
function load(saved) {
  const context = vm.createContext({
    document: { querySelector: () => ({}), addEventListener() {} },
    window: { addEventListener() {} },
    localStorage: { getItem: () => saved ?? null },
  });
  vm.runInContext(script, context);
  return context.subject;
}
const app = load();
for (const [input, expected] of [['-2', -2], ['−２', -2], ['8/2', 4], ['16/3', 16/3], ['-3/-2', 1.5], ['.5', .5], [' 2 / 4 ', .5]]) {
  assert.equal(app.parseNumber(input), expected, input);
}
for (const input of ['', '1/0', '0/0', '1/2/3', 'Infinity', '2+3', 'alert(1)', 'abc', '.', '--2']) {
  assert.equal(app.parseNumber(input), null, input);
}
assert.equal(app.correct({answer:16/3}, app.parseNumber('16/3')), true);
assert.equal(app.correct({answer:16/3}, app.parseNumber('5.33')), false);
assert.equal(app.correct({answer:0}, null), false);

for (const lesson of app.lessons) {
  for (const step of lesson.steps) {
    if (step.type === 'choice') {
      assert.ok(step.answer >= 0 && step.answer < step.choices.length);
      step.choices.forEach((_, i) => { if (i !== step.answer) assert.ok(step.wrong[i]); });
    }
    if (step.target !== undefined) {
      app.setScene(step.target);
      const scene = app.sceneData(step);
      assert.ok(step.target >= scene.controlMin && step.target <= scene.controlMax);
    }
  }
}
for (let p = -4; p <= 12; p++) {
  app.setScene(p);
  const d = app.sceneData({scene:'sum'});
  const pa = Number(d.reads[0][1]), pb = Number(d.reads[1][1]);
  assert.ok(pa >= 0 && pb >= 0);
  assert.equal(pa + pb, p < 0 ? 8 - 2*p : p > 8 ? 2*p - 8 : 8);
}
for (const mode of ['meet', 'chase']) {
  const end = mode === 'meet' ? 2 : 5;
  for (let t=0; t<=end; t+=.5) {
    app.setScene(t, 'ground'); const ground = app.sceneData({scene:'relative', mode});
    app.setScene(t, 'q'); const relative = app.sceneData({scene:'relative', mode});
    assert.equal(ground.b-ground.p, relative.b-relative.p);
    assert.equal(relative.b, 12);
    if (t===end) assert.equal(ground.b,ground.p);
  }
}
for (let run=0;run<100;run++) {
  const exam=app.makeExam();
  const nums = q => [...q.text.matchAll(/[−-]?\d+/g)].map(m=>Number(m[0].replace('−','-')));
  let n=nums(exam[0]); assert.equal(exam[0].answer,n[0]-n[1]);
  n=nums(exam[1]); assert.equal(exam[1].answer,n[0]+n[1]*n[2]);
  n=nums(exam[2]); assert.equal(exam[2].answer,Math.abs(n[1]-n[0]));
  n=nums(exam[3]); assert.equal(exam[3].answer,n[1]-n[0]);
  n=nums(exam[5]); assert.equal(exam[5].answer,n[0]/(n[1]-n[2]));
}
assert.equal(load('broken json').state.lesson, 0);
assert.equal(load('{"lesson":100,"step":0}').state.lesson, 0);
const resumed=load('{"lesson":2,"step":3,"done":[0,0,1,99]}').state;
assert.equal(resumed.lesson,2);assert.equal(resumed.step,3);assert.deepEqual(Array.from(resumed.done),[0,1]);
console.log('PASS: answer parsing, curriculum data, distance invariants, both reference frames, 100 generated challenges, saved progress validation.');
