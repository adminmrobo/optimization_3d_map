// 최적화 첫걸음 ①·② 수치 검증: node code/check_first_step.js
const D=require('../build/diffmath.js');let bad=0;
const ok=(n,a,b,t=1e-3)=>{const p=Math.abs(a-b)<=t;if(!p)bad++;console.log((p?'ok  ':'FAIL')+' '+n+': '+(+a).toFixed(4)+' vs '+(+b).toFixed(4));};
const B=D.bakery;
ok('① 2만 원 최선 생산량',B.best(20).Q,10);ok('① 2만 원 이윤',B.best(20).profit,40);ok('① 15판 이윤(2만 원)',B.profit(15,20),-60);
ok('① 조업중단점 AVC 최저',B.avcMin().v,8.75);ok('① 손익분기점 ATC 최저',B.atcMin().v,15.849,1e-3);
ok('① MC = 총비용 미분(Q=8)',B.MC(8),D.d(B.TC,8));ok('① 이윤 기울기 0 (Q=10)',D.d(q=>B.profit(q,20),10),0);
const d1=D.duel1();ok('① 대결 초파리 합',d1.reduce((s,x)=>s+x.fly,0),-36.762,1e-2);ok('① 대결 주판봇 합',d1.reduce((s,x)=>s+x.robo,0),-465);
const F=D.fac,sr=F.shortRun(10,5,4);ok('② 사람 수',sr.L,16);ok('② 생산량',sr.Q,16);ok('② 이윤',sr.profit,40);
const cm=F.costMin(16);ok('② 최소 비용',cm.C,113.137);ok('② λ',cm.lam,7.0711);ok('② λ = 1톤 더 비용',F.costMin(17).C-cm.C,cm.lam);
ok('② 등량선 위',F.Q(cm.L,cm.K),16);ok('② 오일러: MP_L·L + MP_K·K = Q',F.MPL(cm.L,cm.K)*cm.L+F.MPK(cm.L,cm.K)*cm.K,16);ok('② P = λ이면 이윤 0',cm.lam*16-cm.C,0);
ok('② 커피 정확해 t=10',D.cool.exact(10),20+70*Math.exp(-1));
ok('② 경사하강 학습률 0.1, 100걸음',D.loss.run(0,0.1,100)[100],3);
const c=D.chain.links(1);ok('② 연쇄법칙 x=1',c.prod,D.d(D.chain.f,1));
const r=D.duel2();console.log('   검증 오차: 일차',r.lin.valid.toFixed(3),'주판봇',r.robo.valid.toFixed(3),'초파리',r.fly.valid.toFixed(3));ok('② 대결 초파리 승',r.fly.valid<r.robo.valid?1:0,1,0);
const s=D.second(D.trueY,0,1);ok('② 참 모형 ∂²y/∂x₁²',s.xx,1.6,1e-3);ok('② 참 모형 ∂²y/∂x₁∂x₂',s.xy,1.5,1e-3);
for(const l of [0.5,2,10]){const w=D.ridge.w(l),cc=Math.hypot(...w),wc=D.ridge.constrained(cc);ok('② 벌점 답 = 울타리 답 λ='+l,Math.hypot(w[0]-wc[0],w[1]-wc[1]),0,2e-3);}
console.log(bad?`\n${bad}개 실패`:'\n모두 통과');process.exit(bad?1:0);
