// 페이지에 나오는 기대 수치를 node로 다시 계산한다: node code/check_numbers.js
const LM=require('../build/labmath.js');
const D=LM.makeLine(39,1000);
const o=LM.ols(D), H=LM.hessian(D);
console.log('바닥(최소제곱) w=%s b=%s 오차=%s',o.w.toFixed(3),o.b.toFixed(3),o.L.toFixed(3));
console.log('헤시안 고유값 %s %s · 학습률 한계 2/λmax=%s · 길쭉함 λmax/λmin=%s',H.lmin.toFixed(2),H.lmax.toFixed(2),(2/H.lmax).toFixed(3),(H.lmax/H.lmin).toFixed(2));
console.log('출발점 (-1,-1) 오차=%s',LM.loss(D,-1,-1).toFixed(3));
for(const s of [1000,100,10]){const R=LM.runBatch(D,s,{steps:100,lr:0.1});
  console.log('배치 %s: 1에포크 뒤 %s · 100걸음 뒤 %s · 오르막 %s걸음 · 끝 w=%s b=%s',s,R.afterEpoch.toFixed(3),R.last.toFixed(3),R.up,R.path[100][0].toFixed(3),R.path[100][1].toFixed(3));}
for(const lr of [0.01,0.1,0.3,0.33,0.34,0.5]){const R=LM.runBatch(D,1000,{steps:100,lr});console.log('풀배치 lr %s: 100걸음 뒤 %s %s',lr,R.blow?'발산':R.last.toFixed(3),R.blow?'':'');}
const a=LM.saddleRun(false),b=LM.saddleRun(true);
console.log('안장 대결 주판봇(기울기만): 끝 (%s,%s) 오차 %s 걸음 %s',a.end[0].toFixed(3),a.end[1].toFixed(3),a.L.toFixed(3),a.steps);
console.log('안장 대결 초파리(굽음 확인): 끝 (%s,%s) 오차 %s 걸음 %s 한발 %s',b.end[0].toFixed(3),b.end[1].toFixed(3),b.L.toFixed(3),b.steps,b.kicks);
