const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');
const assert=require('node:assert/strict');
const dir=path.join(__dirname,'..','数学小课堂');
const files=fs.readdirSync(dir).filter(f=>/^\d\d-.*\.html$/.test(f)).sort();
assert.equal(files.length,14);
const lessons=files.filter(f=>!f.startsWith('14-')).map(f=>{
 const html=fs.readFileSync(path.join(dir,f),'utf8');
 assert(!/<script[^>]+src=|<link[^>]+href=/.test(html),'Must work offline');
 const js=html.match(/<script>([\s\S]*?)<\/script>/)[1];
 new vm.Script(js,{filename:f});
 const data=JSON.parse(js.match(/^const LESSON=(.*);\r?\n/)[1]);
 assert.equal(data.steps.length,3);assert.equal(data.exam.length,2);
 for(const q of [...data.steps,...data.exam]){
  assert(q.answer>=0&&q.answer<q.options.length);
  assert.equal(q.why.length,q.options.length);
  assert(q.why.every(Boolean));
 }
 return data;
});
// Recompute the original numerical problems independently of their explanations.
assert.equal(-(2**3)/4+Math.abs(-4)**3/((-2)**4),2);
assert.equal(.5+(-.5+2/3-1/6)*12-4-5,-8.5);
assert.equal((700+[5,-2,-5,14,-8,22,-6].reduce((a,b)=>a+b,0))*7,5040);
let seq=[10];while(seq.length<2015){const a=seq.at(-1);seq.push(a%2?3*a+1:a/2);}
assert.equal(seq.reduce((a,b)=>a+b,0),4733);
const altered=[8,...Array.from({length:11},(_,i)=>i%2?1:3)];
assert.equal(lessons[9].exam[1].options[lessons[9].exam[1].answer],String(altered.reduce((a,b)=>a+b,0)));
for(let n=1;n<=100;n++){
 let counted=0;for(let r=0;r<2*n-1;r++)for(let c=0;c<2*n-1;c++)if((r+c)%2===0)counted++;
 assert.equal(counted,n*n+(n-1)**2);
}
for(const [vb,vs] of [[2,1],[-2,-1],[2,-1],[-2,1]]){
 const t=9/Math.abs(vb-vs);assert.equal(Math.abs(vb*t-vs*t),9);assert.equal(Math.abs(vb*t),2*Math.abs(vs*t));
}
for(let a=-5;a<=5;a++)for(let b=-5;b<=5;b++){
 const u=2*(a+b)-a*b;assert.equal(3*u-u,4*a+4*b-2*a*b);
}
const index=fs.readFileSync(path.join(dir,'index.html'),'utf8');
for(const file of files)assert(index.includes('href="'+file+'"'));
console.log('PASS: 13 portable lessons, 65 answer/feedback records, JavaScript syntax, navigation, original arithmetic, 100 checkerboards, cycle sum, four movement cases, algebra identities.');
