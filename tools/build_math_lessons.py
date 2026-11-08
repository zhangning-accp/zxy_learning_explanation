"""Build portable lessons: each output embeds its own content, style and runtime."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '数学小课堂'
OUT.mkdir(exist_ok=True)
lessons = []
def q(text, options, answer, why, hint):
    return dict(text=text, options=options, answer=answer, why=why, hint=hint)
def lesson(slug, title, source, goal, logic, demo, steps, exam):
    lessons.append(dict(slug=slug,title=title,source=source,goal=goal,logic=logic,demo=demo,steps=steps,exam=exam))

lesson('01-同类项','同类项：先认种类，再数份数','第 6 题','认清字母和指数，不被顺序、系数迷惑。',
 ['3mn² 就是 3 份 mn²。系数回答“几份”，字母和各自指数回答“什么东西”。','乘法交换顺序不改变乘积：n²m = mn²。逐个字母比指数，不比书写顺序。','只有种类相同才能合并：3mn² − 4n²m = (3−4)mn² = −mn²。常数之间也都是同类项。'], 'terms', [
 q('先猜：3mn² 与 −4n²m 能合并吗？',['能，字母及各字母指数相同','不能，系数不同','不能，字母顺序不同'],0,['对，都是 mn² 这一种。','系数只影响份数，不决定种类。','乘法可交换顺序，n²m = mn²。'],'先把两项都按 m、n 的顺序写。'),
 q('2m²n 与 5mn² 为什么不能合并？',['因为系数不相同','m、n 的指数对应不同','因为都有两个字母'],1,['系数不同仍可能是同类项。','对，第一项是 m×m×n，第二项是 m×n×n。','有几个字母不是判断标准，还要比每个指数。'],'展开成连乘，看看重复的是哪个字母。'),
 q('回到原题：第 6 题哪一组是同类项？',['⅔m²n 与 ³⁄₂mn²','5² 与 x²','3mn² 与 −4n²m','2abc 与 3ab'],2,['m 和 n 的指数对应不同。','5² 是常数，x² 含字母。','正确：同种类，与系数、顺序无关。','第一项多一个 c。'],'逐个比较字母及它的指数。')], [
 q('独立判断：−7a²b＋2ba² =',['−5a²b','−5a³b²','−9a²b'],0,['同类项只加系数：−7＋2 = −5。']*3,''),
 q('哪项与 4xy² 同类？',['4x²y','−y²x','4xy'],1,['认种类：都要有 x¹y²。']*3,'')])

lesson('02-乘方与符号','乘方：指数管着谁','第 14(2) 题','区分连乘、负号和绝对值的运算范围。',
 ['aⁿ 表示 n 个 a 相乘，不是 a×n。4³ = 4×4×4 = 64。','括号决定底数：(−4)² 的底数是 −4；−4² 是先算 4² 再取相反数。','|−4|³ 先取绝对值，得到 4³。负数的偶次幂为正、奇次幂为负。'], 'power', [
 q('|−4|³ 应展开成什么？',['4×3','4×4×4','−4×−4×−4'],1,['指数是因子的个数，不是乘数。','对，绝对值先变成 4，再连乘三次。','绝对值已经去掉了负号。'],'先算绝对值，再找底数。'),
 q('−4² 与 (−4)² 分别是多少？',['16、16','−16、16','−16、−16'],1,['没有括号时，前面的负号不参加平方。','正确：−(4×4) 与 (−4)×(−4)。','两个负数相乘是正数。'],'用乘法把两个式子完整展开。'),
 q('原题中的 |−4|³ ÷ (−2)⁴ =',['24÷16','64÷16 = 4','−64÷16 = −4'],1,['4³ 不是 4×3，也不是 24。','正确，两处乘方都先算。','绝对值的结果非负。'],'两边分别算出 64 和 16。')], [
 q('|−3|⁴ =',['12','−81','81'],2,['3×3×3×3 = 81。']*3,''),
 q('−3²＋(−3)³ =',['−36','−18','36'],0,['−9＋(−27) = −36。']*3,'')])

lesson('03-混合运算','混合运算：每一步只做一件事','第 14(2)(3) 题','确定先后顺序，并用正负分组检查末步。',
 ['先处理括号和绝对值，再算乘方，再算乘除，最后加减。同一级从左往右。','除以一个非零数，等于乘它的倒数。分配律必须作用于括号内每一项。','把减法改成加相反数；正数合计、负数合计，最后相抵。不要凭“看着像”跳步。'], 'order', [
 q('原题 −2³×¼＋|−4|³÷(−2)⁴，先得到哪一行？',['−8×¼＋64÷16','−2×3×¼＋4×3÷16','(−8×¼＋64)÷16'],0,['正确，先处理乘方和绝对值。','把乘方误当成乘法了。','除以 16 只作用于后面那一项。'],'先圈出每个幂的底数。'),
 q('上一式变成 −2＋4，结果是？',['−6','2','6'],1,['加正数要向右，不是继续变小。','正确，原题 14(2) 的结果为 2。','−2 仍带负号。'],'在数轴上从 −2 向右走 4 格。'),
 q('原题 14(3)：½＋(−½＋⅔−⅙)÷(1/12)−4−5。结果是？',['−8.5','−12.5','−9.5'],0,['括号内 (−3＋4−1)/6 = 0，所以 ½−4−5 = −8.5。','原卷末步没有正确合计。先确认括号内为 0。','½ 是正数，−9＋½ = −8.5。'],'也可分配得到 ½−6＋8−2−4−5，正数与负数分组。')], [
 q('18÷3×2 =',['3','12','6'],1,['乘除同级从左往右：6×2 = 12。']*3,''),
 q('¾＋(−½＋¼)÷¼−2 =',['−2.25','−1.25','0'],0,['括号为 −¼，除以 ¼ 得 −1；¾−1−2 = −2.25。']*3,'')])

lesson('04-分段计费','分段计费：每一段付自己的钱','第 10、25(1) 题','把总量拆成已包含的部分和超出部分。',
 ['先画数量条，标出分界点。超过 3 分钟时，超出量是 x−3，不是 x。','总费用 = 基础费用＋超出量×超出单价。原题前 3 分钟总共 0.22 元，不是每分钟 0.22 元。','列出有意义的式子后再化简，并注明适用范围。等价但未化简的式子并不因此在数学上错误。'], 'fee', [
 q('打了 5 分钟，超出 3 分钟的部分是多少？',['5 分钟','2 分钟','3 分钟'],1,['前 3 分钟已包含在基础费里。','对，5−3 = 2。','3 是分界点，不是超出量。'],'总量减去已包含的量。'),
 q('第 10 题 x>3 时的话费是？',['0.22x＋0.2(x−3)','0.22＋0.2x','0.22＋0.2(x−3)'],2,['0.22 是前 3 分钟的总费用。','这样把前 3 分钟重复收费了。','正确，化简为 0.2x−0.38 元，仅用于 x>3。'],'用 x=4 检验，应只多收一个 0.2 元。'),
 q('第 25 题甲店 x>10：15＋0.9(x−10) 化简为？',['0.9x＋6','0.9x＋15','0.9x−9'],0,['15＋0.9x−9 = 0.9x＋6。','括号中的 −10 也要乘 0.9。','原来的基础费 15 不能漏掉。'],'先分配，再合并常数。')], [
 q('停车前 2 小时共 6 元，之后每小时 2 元。停 5 小时付？',['10 元','12 元','16 元'],1,['6＋2×(5−2) = 12 元。']*3,''),
 q('甲店 0.9x＋6，乙店 1.2x（x>10）。买 20 支时？',['甲便宜','乙便宜','一样，都是 24 元'],2,['代入得 24 和 24；不是任何数量都甲更便宜。']*3,'')])

lesson('05-绝对值与筛选','绝对值：先找位置，再筛条件','第 12 题','把绝对值看成距离，找全后再排除不合条件的解。',
 ['|p| 是点 p 到原点的距离，所以 |p|=5 的候选位置是 5 和 −5。距离本身不会是负数。','距离相等允许左右对称，也允许同一位置。题目说“不同两点”，就必须排除重合。','第 12 题 p=m−3。先确定 p，再解 m，最后代回原题检验。'], 'absolute', [
 q('距原点 5 格的位置有哪些？',['只有 5','5 和 −5','只有 −5'],1,['原点左边也有一个位置。','对，两侧各一个。','右边也有一个位置。'],'在数轴两侧各走 5 格。'),
 q('其中与 −5 是不同点的位置是？',['−5','5','两个都保留'],1,['−5 与原来的点重合。','正确，“不同”排除了 −5。','找到候选不等于完成，要筛条件。'],'比较坐标是否相同。'),
 q('第 12 题 m−3 = 5，所以 m =？',['2','8','8 或 −2'],1,['从 m 减去 3 得 5，要加回 3。','正确，m=8；m=−2 对应重合，已舍去。','−2 使 m−3=−5，违反“不同两点”。'],'把 m 代回位置表达式检验。')], [
 q('−7 与 k＋2 是不同点且到原点等距，k =？',['5','−9','5 或 −9'],0,['不同点的位置是 7，k＋2=7，k=5。']*3,''),
 q('|p|=0 有几个不同位置？',['0 个','1 个','2 个'],1,['只有原点，＋0 与 −0 是同一个数。']*3,'')])

lesson('06-倒数相反数','倒数与相反数：把关系换成数','第 19 题','优先使用乘积、商等整体关系，再讨论绝对值。',
 ['互为倒数表示乘积为 1：mn=1，m、n 都不为 0。互为相反数表示 x=−y。','原式含 x/y，说明 y≠0，因此 x/y=−1。不能在允许 y=0 的地方直接做除法。','|z|=1 给出 z=±1。前面确定的部分先算好，最后分别代入，避免把两个答案漏成一个。'], 'relations', [
 q('m、n 互为倒数，mn =？',['−1','0','1'],2,['相反数与倒数是两种关系。','倒数不能为 0。','正确，倒数的乘积为 1。'],'如 2 与 ½。'),
 q('x、y 互为相反数且 y≠0，−3x/y =？',['−3','3','不确定'],1,['x/y=−1，前面的 −3 还要参与相乘。','正确，−3×(−1)=3。','具体值不定，但比值固定。'],'用 x=2、y=−2 检查符号。'),
 q('原式 mn−3x/y＋z，|z|=1，结果是？',['5 或 3','−3 或 1','只有 5'],0,['1＋3±1 = 5 或 3。','先把固定部分合成 4。','z 也可以取 −1。'],'把 z=1 和 z=−1 分两行。')], [
 q('ab=1，c=−d，d≠0，|e|=2。ab−2c/d＋e =？',['1 或 5','−1 或 3','只有 5'],0,['固定部分 1−2×(−1)=3，再加 ±2。']*3,''),
 q('0 与 0 互为相反数，能据此写 0/0=−1 吗？',['能','不能，除数不能是 0'],1,['互为相反数不自动保证可以相除，须检查分母非零。']*2,'')])

lesson('07-正负数求和','正负记录：基准＋变化','第 18(3) 题','分清实际量与差值，并通过两条计算路径验算。',
 ['表中 ＋5 是比计划多 5 千克，不是只卖了 5 千克。实际量=100＋差值。','一周总量=7×100＋所有差值之和。正数 5＋14＋22=41；负数绝对值 2＋5＋8＋6=21，净增 20。','也可以逐天计算实际量再求和。两种方法应相同。每千克净收入为 10−3=7 元。'], 'sum', [
 q('某天记录 −8，实际卖出多少千克？',['−8','92','108'],1,['负号记录的是差，不是实际销量。','100−8=92，正确。','负数表示不足，要减。'],'实际量=计划量＋差值。'),
 q('＋5−2−5＋14−8＋22−6 =？',['22','20','62'],1,['正数 41，负数合计 −21，相抵是 20。','正确；也可先用 ＋5 与 −5 抵消。','不能把所有绝对值相加。'],'把正数、负数分别装进两个篮子。'),
 q('本周 720 千克，每千克售价 10 元、运费 3 元，按题意纯收入为？',['5040 元','5054 元','7200 元'],0,['720×(10−3)=5040 元。','5054 来自总量误算为 722 的连锁错误。','7200 是收入，还未扣题目给出的运费。'],'先算每千克剩下多少钱。')], [
 q('每天计划 50，三天差值 ＋4、−7、＋1，总量？',['148','152','−2'],0,['150＋(4−7＋1)=148。']*3,''),
 q('上述 148 千克，每千克售价 8、费用 2，净收入？',['1184','888','296'],1,['148×(8−2)=888。']*3,'')])

lesson('08-新定义与整体代入','新定义：翻译后，寻找同一整体','第 20 题','去掉新名称的包装，把条件变成可使用的等式。',
 ['“a 与 b 互为平等数”在这道题中只表示 a=b。先按题目给的定义翻译，不猜别的性质。','4m²−2n = n＋2，移项得到 4m²−3n=2。这里不必分别求 m、n。','目标 8m²−6n＋2024 = 2(4m²−3n)＋2024，整体代入即可。'], 'definition', [
 q('“4m²−2n 与 n＋2 互为平等数”应写成？',['4m²−2n = n＋2','4m²−2n＋n＋2=0','两式互为倒数'],0,['对，直接按定义翻译。','定义没有说它们互为相反数。','不要给新名称补上题目没有的含义。'],'先把“平等数”替换成“相等”。'),
 q('由条件移项可知哪个整体等于 2？',['4m²−n','4m²−3n','m²−n'],1,['右边的 n 移到左边要减去 n。','正确：−2n−n=−3n。','系数不可随意更改。'],'两边同时减去 n。'),
 q('原题 8m²−6n＋2024 的值为？',['2026','2028','无法确定'],1,['目标中整体出现了两份。','2×2＋2024=2028。','虽然 m、n 不唯一，这个整体却已确定。'],'把前两项提取公因数 2。')], [
 q('若 3u−v=5，6u−2v＋7 =？',['17','12','不能求'],0,['2(3u−v)＋7=17。']*3,''),
 q('新定义 a★b=2a−b，则 3★4 =？',['2','10','−2'],0,['严格翻译：2×3−4=2，不套用通常乘法。']*3,'')])

lesson('09-图形规律','图形规律：数结构，不猜数字','第 22 题；联系第 13 题','从可见结构推导通式，并用小图验证。',
 ['第 n 个棋盘每边有 2n−1 格。奇数行有 n 个黑格，共 n 行；偶数行有 n−1 个黑格，共 n−1 行。','因此黑格数=n²＋(n−1)²=2n²−2n＋1。也可用“黑格比白格多 1”得到 [(2n−1)²＋1]/2。','先验证 n=1、2、3 得 1、5、13，再代入 100。第 13 题六边形是另一种结构：第一块 6 条边，以后每块多 5 条，6＋5(n−1)=5n＋1。'], 'pattern', [
 q('第 3 个棋盘，一行有多少格？',['3','5','6'],1,['序号不是边长格数。','2×3−1=5。','相邻图边长每次增加 2，不是加倍。'],'观察 1、3、5 的边长。'),
 q('第 n 个图的黑格为何是 n²＋(n−1)²？',['因为每次加 4','n 行各 n 个，另 n−1 行各 n−1 个','因为黑格总是总格数的一半'],1,['每次增加的黑格数不固定。','对，按行分类，每格只数一次。','总格数为奇数，黑格比白格多 1。'],'分别数奇数行和偶数行。'),
 q('第 100 个图黑格数为？',['401','10000','19801'],2,['401 没有体现二维棋盘面积的增长。','还漏掉另一类行的 99² 个。','100²＋99²=10000＋9801=19801。'],'用两个正方形数相加。')], [
 q('第 5 个图黑格数为？',['25','41','81'],1,['5²＋4²=41；81 是总格数。']*3,''),
 q('一排 8 个共边六边形有多少条不同线段？',['48','41','40'],1,['6＋7×5=41，共用边只数一次。']*3,'')])

lesson('10-迭代与周期','迭代：上一站的输出，是下一站的输入','第 23 题','逐项执行定义，定位循环起点，再分组求和。',
 ['奇数用 3a＋1，偶数用 a÷2。每次都看当前的数是奇是偶，不能一直用同一条规则。','从 a₁=10 开始：10、5、16、8、4、2、1、4、2、1……。从第 5 项开始，每 3 项为一组 4、2、1。','前 4 项和为 39；剩下 2015−4=2011 项，2011=3×670＋1。每组和 7，余下第一项 4，所以总和 39＋670×7＋4=4733。'], 'iteration', [
 q('当前数为 5，下一项是？',['2.5','16','6'],1,['5 是奇数，不能用偶数分支。','3×5＋1=16。','奇数分支是先乘 3 再加 1。'],'每一步重新判断奇偶。'),
 q('本题从第几项起，可以按 4、2、1 分组？',['第 1 项','第 4 项','第 5 项'],2,['10 不在循环中。','第 4 项为 8，还未进入 4、2、1。','正确，第 5 项为 4，第 8 项又是 4，后续重复。'],'给每个数标上项号，不能把数值当项号。'),
 q('2011=3×670＋1，最后剩下的那一项是？',['1','4','7'],1,['余数 1 表示剩一项，不表示这一项的值为 1。','从循环开头取 1 项，就是 4。','7 是完整一组的和。'],'从 4、2、1 的左边开始拿。')], [
 q('本题前 10 项的和为？',['53','49','46'],0,['前 4 项和 39，后 6 项是两组，39＋14=53。']*3,''),
 q('序列 8、3、1、3、1、3、1……，前 12 项和？',['31','32','24'],0,['先留 8，余 11 项=5 组(3＋1)＋3，合计 31。']*3,'')])

lesson('11-去括号与整体','去括号：每项都带着自己的符号','第 24(1) 题','用分配律理解变号，并通过整体法检查展开。',
 ['括号前的数乘里面每一项。减去一个括号，就是乘 −1：−(2a＋2b−ab)=−2a−2b＋ab。','令 U=2(a＋b)−ab，原式 3U−U=2U。先整体化简，可以减少重复展开。','|a−2| 与 (b−3)² 都非负，和为 0 时必须各为 0，因此 a=2、b=3。原式=4a＋4b−2ab=8。'], 'brackets', [
 q('−(2a＋2b−ab) 展开为？',['−2a−2b−ab','−2a−2b＋ab','−2a＋2b−ab'],1,['负负得正，最后一项应变成 ＋ab。','正确，三项全部乘 −1。','不能只改第一项的符号。'],'给每一项前都写一个 ×(−1)。'),
 q('−3ab＋ab =？',['−5ab','−2ab','−4ab'],1,['−3＋1 不是 −5。','对，系数相加为 −2。','＋ab 的系数是 ＋1，不是 −1。'],'把 ab 当作同一种积木。'),
 q('原题 a=2、b=3，U=2(a＋b)−ab，则 3U−U =？',['8','32','20'],0,['U=10−6=4，2U=8；可与展开法互检。','原卷的合并和代入符号出现了错误。','还没有减去 ab 对应的部分。'],'先求 U，再算两份 U。')], [
 q('2(3x−y)−(x−4y) =',['5x＋2y','5x−6y','7x＋2y'],0,['6x−2y−x＋4y=5x＋2y。']*3,''),
 q('|p−4|＋(q＋1)²=0，则 p＋q =？',['5','3','−3'],1,['两个非负数都为 0，p=4，q=−1。']*3,'')])

lesson('12-含参与系数','含参条件：让不该出现的项消失','第 21、24(2) 题','理解系数为零的原因，区分不含某项与整体无关。',
 ['不含 xy 项，就是合并后 xy 的系数为 0。只对指定项提出要求，其他项可以保留。','第 21 题化简为 x²＋(−6−m)xy−4y²，所以 −6−m=0，m=−6。','第 24(2) 题：2A−3B=(3n−6)x²＋(m−4)x−14。要对任意 x 都不变，x²、x 的系数都必须为 0，因此 n=2、m=4。只试几个 x 不能代替这个推理。'], 'coeff', [
 q('“不含 xy 项”意味着？',['xy=0','xy 的系数为 0','所有系数都为 0'],1,['题目没有限制 x、y 必须为 0。','正确，0×xy 才会让这一项消失。','其他项并不需要消失。'],'关心的是项前面的系数。'),
 q('第 21 题 xy 的系数为 −6−m，m =？',['6','−6','0'],1,['代入 6 得 −12，仍有这一项。','−6−(−6)=0，正确。','代入 0 得 −6，没有消失。'],'把候选 m 代回系数检查。'),
 q('第 24(2) 得 n=2、m=4。目标 (m²−3mn＋2n²)−(2m²＋mn−4n²) =？',['−24','24','−14'],0,['先化简 −m²−4mn＋6n²，再代入：−16−32＋24=−24。','括号前的减号要作用于每一项。','−14 是 2A−3B 的常数值，不是最后所求的式子。'],'区分用于找参数的式子与最后要算的式子。')], [
 q('(k−3)x²＋(h＋2)x＋7 与 x 无关，则 (k,h)=？',['(3,−2)','(−3,2)','(3,2)'],0,['分别令 k−3=0、h＋2=0。']*3,''),
 q('2x²＋(5−p)xy−y² 不含 xy，则 p=？',['−5','0','5'],2,['只令 5−p=0，不必让 x² 与 y² 的系数为 0。']*3,'')])

lesson('13-滚动与距离','滚动问题：把接触点变成数轴上的点','第 26(1)(2) 题','区分路程、位置、距离，按方向找全四种情况。',
 ['题目已给线速度：大圆 2π/秒，小圆 π/秒。直接用速度×时间求接触位置的变化，不需要再乘周长。','往返的路程把每段长度相加；最终位置把带方向的位移相加；到原点的距离是最终位置的绝对值。','同时从 0 出发，同向每秒拉开 π，异向每秒拉开 3π。相距 9π 时，同向 9 秒、异向 3 秒。每一类再分左右，才不会漏解。'], 'rolling', [
 q('依次 −1、＋2、−4、−2、＋3、＋6 秒，大圆走的总路程是？',['8π','36π','18π'],1,['8π 是最终到原点的距离。','总时间绝对值 18 秒，乘速度 2π 得 36π。','速度是 2π，不能漏掉 2。'],'路程不因折返而抵消。'),
 q('累计带符号时间 −1、1、−3、−5、−2、4。哪次结束最远，最终距离多少？',['第 4 次，8π','第 6 次，36π','第 4 次，9'],0,['最大绝对值是 5（第 4 次），最后是 |4×2π|=8π。','总路程不是最终距离。','不能把路程除以距离来作答，距离要保留长度。'],'分别看累计量的最大绝对值和最后一个值。'),
 q('按（大圆接触点，小圆接触点）的顺序，原题四组解为？',['(18π,9π)、(−18π,−9π)、(6π,−3π)、(−6π,3π)','只有 (18π,9π)','(9π,0)、(0,9π)'],0,['四组均相距 9π，且速度大小比为 2:1。','漏掉同向左和两种异向。','两圆都在运动，同一时刻位置大小比为 2:1。'],'先分同向/异向，再分谁向左、谁向右。')], [
 q('两点从 0 同时出发，速度 3、1，同向向左，相距 8 时位置（快,慢）为？',['(−12,−4)','(12,4)','(−6,2)'],0,['时间 8/(3−1)=4，两点都向左，位置为 −12、−4。']*3,''),
 q('一个点先向右走 7，再向左走 10，路程、到原点距离为？',['17、3','3、17','17、−3'],0,['路程 7＋10=17，位置 −3，距离 |−3|=3。']*3,'')])

CSS = '''
:root{--ink:#193c39;--muted:#61746c;--green:#146b56;--bg:#f5f5ed;--line:#dce5db}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.8 "Microsoft YaHei",system-ui,sans-serif}a{color:var(--green)}button,input,select{font:inherit}button,a,input,select{touch-action:manipulation}button{cursor:pointer;border:1px solid #bfcec1;border-radius:12px;background:white;color:var(--ink);padding:10px 16px}button:hover{background:#e8f2e7}button:disabled{opacity:.5;cursor:default}button:focus-visible,a:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid #c98018;outline-offset:3px}.primary{background:var(--green);color:white}.primary:hover{background:#0c5343}.shell{max-width:1100px;margin:auto;padding:30px 24px}header{display:flex;justify-content:space-between;align-items:center;gap:15px;flex-wrap:wrap;margin-bottom:25px}.small{font-size:13px;color:var(--muted)}h1{font-size:clamp(26px,4vw,38px);line-height:1.4;margin:10px 0}h2{font-size:23px;line-height:1.5}.eyebrow{font-size:12px;font-weight:bold;letter-spacing:2px;color:var(--green)}.layout{display:grid;grid-template-columns:200px minmax(0,1fr);gap:25px}aside nav{display:grid;gap:9px}nav button{text-align:left}nav button[aria-current=step]{background:#e0eddf;border-color:var(--green)}.card{background:white;border:1px solid var(--line);border-radius:22px;padding:25px;margin-bottom:20px;min-width:0}.scene{background:#f1f6ee;border:1px solid #d9e5d5;border-radius:16px;padding:20px;margin:20px 0}.controls,.actions{display:flex;gap:12px;flex-wrap:wrap;align-items:center}input[type=range]{min-width:110px;flex:1;accent-color:var(--green)}select{max-width:100%;padding:8px;border:1px solid var(--line);border-radius:8px}output{font-weight:bold}.formula{font-size:21px;background:white;border-radius:10px;padding:12px 16px;margin:14px 0;overflow-wrap:anywhere}.options{display:grid;gap:10px}.options button{text-align:left}.feedback{padding:14px;background:#fff0d6;border-radius:12px;margin-top:15px}.feedback:empty{display:none}.good{background:#e2f2df}.hint{border-left:3px solid #a9bdd0;padding-left:12px}.tiles{display:flex;flex-wrap:wrap;gap:6px;margin:12px 0}.tile{padding:6px 12px;border-radius:8px;background:white;border:1px solid #cfdbcd}.negative{color:#a5422d}.positive{color:#215e9a}svg{display:block;width:100%;height:auto}svg text{font-family:inherit}.grid{display:grid;gap:15px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}.grid a{text-decoration:none}.grid .card:hover{border-color:var(--green)}progress{width:100%;accent-color:var(--green)}details{margin:15px 0}summary{cursor:pointer}table{border-collapse:collapse;width:100%;font-size:14px}td,th{border-bottom:1px solid var(--line);padding:8px;text-align:left}.scroll{overflow:auto}.badge{background:#e5eee0;padding:3px 10px;border-radius:15px;font-size:13px}.checklist{line-height:2}.visually-hidden{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0)}@media(max-width:760px){.layout{grid-template-columns:1fr}.shell{padding:18px 14px}.card{padding:20px}aside nav{grid-template-columns:repeat(2,minmax(0,1fr))}.scene{padding:14px}h2{font-size:21px}.formula{font-size:18px}}@media(prefers-reduced-motion:reduce){*{scroll-behavior:auto!important}}
'''

ENGINE = (ROOT / 'tools' / 'math_runtime.js').read_text(encoding='utf-8')
CSS += '\n/* Mobile deployment requirements: safe areas and touch targets. */\nbody{padding:env(safe-area-inset-top,0px) env(safe-area-inset-right,0px) env(safe-area-inset-bottom,0px) env(safe-area-inset-left,0px)}\nbutton,select,input,summary{min-height:44px}button,select{min-width:44px}a{min-height:44px;min-width:44px}header a,.topnav a,.route-steps a,.secondary{display:inline-flex;align-items:center}img{max-width:100%;height:auto}\n@media(max-width:768px){.small,.eyebrow,.tag,.side-note,.scene-title,.scene-note,.readout,.lesson-footer p,.lesson-nav strong,.lesson-nav small,.header-tools button,.scene-controls label,.scene-controls button,.topnav,.meta,.caption,.route p,.route-steps a,.count,.number,.card-bottom,.method span,footer,.filters button{font-size:14px}.route-steps a{padding:0 5px}header{flex-wrap:wrap}}\n'
for i,l in enumerate(lessons):
    body=f'''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"><title>{l['title']} · 数学小课堂</title><style>{CSS}</style><body><div class="shell"><header><a href="index.html">← 数学小课堂</a><span class="small">一次弄懂一点点 · 可离线学习</span></header><div class="layout"><aside><span class="eyebrow">LESSON {i+1:02}</span><h2>一步一步来</h2><nav id="nav" aria-label="学习步骤"></nav><p class="small" id="saved"></p><button id="reset">重新学习本课</button></aside><main><h1>{l['title']}</h1><p>{l['goal']}</p><p class="small">对应周练：{l['source']} · 建议 10～15 分钟，可分次完成</p><div id="app"></div></main></div></div><script>const LESSON={json.dumps(l,ensure_ascii=False)};\n{ENGINE}</script></body></html>'''
    (OUT/(l['slug']+'.html')).write_text(body,encoding='utf-8')
NOTES = '<details class="card"><summary>给家长 / 老师：使用与证据说明</summary><p>依据这次周练中的可见题目及作答，为薄弱点设计学习支架，不重新核定分数。把答错视为本次练习信号，不推断学生固定能力。学习过程建议让孩子口头解释“为什么”，隔一天用纸笔重新做原题。</p><p>第 13 题的 6＋5(n−1) 与 5n＋1 等价；第 25(1) 的 15＋0.9(x−10) 也是正确的建模式子。化简用于提高表达与计算效率，不把“未化简”一概解释为“不懂”。第 24(1) 按原题重算结果为 8，不依赖模糊红笔；第 26(1) 总路程 36π、最终距离 8π。</p><p>本套题分辨新定义翻译、图形结构、迭代周期三个不同难点，分别教学。第 01～13 课各有 3 个引导问题与 2 个独立检查；第 14 课保留 6 个动点小课及独立挑战。答错提供原因和回学路径。独立检查首次选择即记入本轮结果。</p></details>'

# All numbered lessons appear in the same catalog; stable numbers keep old references useful.
catalog = lessons + [dict(slug='14-动点问题', title='动点问题：一步一步，学会动点', goal='从位置、距离到相遇与追赶，拖动数轴理解运动。', source='数轴与运动 · 6 个小课')]
categories = ['运算基础','运算基础','运算基础','应用与条件','数轴与运动','运算基础','运算基础','规律与推理','规律与推理','规律与推理','运算基础','应用与条件','数轴与运动','数轴与运动']
symbols = ['x²','aⁿ','±','¥','|x|','↔','Σ','=','▦','↻','( )','0x','◯','→']
cards = ''.join(f'<a class="course" data-category="{categories[i]}" href="{l["slug"]}.html"><div class="card-top"><span class="symbol" aria-hidden="true">{symbols[i]}</span><span class="number">LESSON {i+1:02}</span></div><h3>{l["title"].split("：")[0]}</h3><p>{l["goal"]}</p><div class="card-bottom"><span>{categories[i]} · {"6 个小课" if i==13 else "约 10–15 分钟"}</span><span class="arrow" aria-hidden="true">↗</span></div></a>' for i,l in enumerate(catalog))
def route(numbers):
    return ' → '.join(f'<a href="{catalog[n-1]["slug"]}.html" aria-label="第 {n:02} 课 {catalog[n-1]["title"]}">{n:02}</a>' for n in numbers)
home=(ROOT/'tools/math_home.html').read_text(encoding='utf-8')
for key,value in {'CARDS':cards,'NOTES':NOTES,'ROUTE1':route([1,2,3,7,11]),'ROUTE2':route([4,5,6,12]),'ROUTE3':route([8,9,10,14,13])}.items():
    home=home.replace('@@'+key+'@@',value)
(OUT/'index.html').write_text(home,encoding='utf-8')
# Bundle the complete classroom directory so all links stay inside the package.
from zipfile import ZipFile, ZIP_DEFLATED
with ZipFile(ROOT/'数学小课堂-离线学习包.zip','w',ZIP_DEFLATED) as bundle:
    for file in OUT.iterdir():
        if file.is_file():
            bundle.write(file,file.relative_to(ROOT))
print(f'Built {len(lessons)} lessons, catalog of {len(catalog)} topics and offline package.')
