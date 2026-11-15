// 3편 수치 검증: node code/check_numbers3.js
// 상자 출입 셈·바람개비 고리 셈·이웃 여섯 셈이 정확한 식과 맞는지, 대결 결과가 페이지 설명과 같은지 확인한다.
const V=require('../build/vecmath.js');let bad=0;
const ok=(name,a,b,tol=1e-3)=>{const pass=Math.abs(a-b)<=tol;if(!pass)bad++;console.log((pass?'ok  ':'FAIL')+' '+name+': '+a.toFixed(4)+' vs '+(+b).toFixed(4));};
const pts=[[0.8,0.6,0.4],[-1.2,0.3,1.1],[0.5,-1.5,-0.7]];
for(const k in V.VF){if(k==='vortex')continue;for(const p of pts){const F=V.VF[k].F;
  ok(`발산 상자 ${k} ${p}`,V.flux(F,p,0.8).perVol,V.VF[k].div(...p));
  const c=V.VF[k].curl(...p);[[1,0,0],[0,1,0],[0,0,1]].forEach((n,i)=>ok(`회전 고리 ${k} ${'xyz'[i]} ${p}`,V.circ(F,p,n,0.06).curlN,c[i]));}}
for(const k in V.SF){for(const p of pts){const S=V.SF[k];const g=V.grad(S.f,p),G=S.g(...p);g.forEach((v,i)=>ok(`편미분 ${k} ${'xyz'[i]} ${p}`,v,G[i]));
  ok(`라플라시안 ${k} ${p} (h=0.01)`,V.lap6(S.f,p,0.01).est,S.lap(...p),k==='heater'?0.05:1e-3);}}
let C=V.corners([0.5,0.5,0.5],0.6),v0=V.vol(C);for(let i=0;i<50;i++)C=C.map(q=>V.step(V.VF.source.F,q,0.01));ok('물감 부피 샘 0.5초',V.vol(C)/v0,Math.exp(1.5));
const D=V.duel();ok('대결 초파리 맞힌 수',D.filter(x=>x.flyOk).length,4,0);ok('대결 주판봇 맞힌 수',D.filter(x=>x.roboOk).length,2,0);
ok('배수구 소용돌이 (1,0,0) 바람개비',V.circ(V.VF.vortex.F,[1,0,0],[0,0,1],0.06).omega,0);
console.log(bad?`\n${bad}개 실패`:'\n모두 통과');process.exit(bad?1:0);
