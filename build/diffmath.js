/* diffmath.js — 최적화 첫걸음(미분편 ①·②)의 계산 모듈. 브라우저·node 공용.
   모든 숫자는 설명용 예시값이다. 실제 공장·시장 자료가 아니다. */
var DM=(function(){
'use strict';
function d(f,x,h){h=h||1e-4;return (f(x+h)-f(x-h))/(2*h);}
function root(f,a,b){var fa=f(a);for(var i=0;i<80;i++){var m=(a+b)/2,fm=f(m);if(fa*fm<=0)b=m;else{a=m;fa=fm;}}return (a+b)/2;}
function argmin(f,a,b){for(var i=0;i<120;i++){var m1=a+(b-a)/3,m2=b-(b-a)/3;if(f(m1)<f(m2))b=m2;else a=m1;}return (a+b)/2;}

/* ① 1.1 자전거 위치 s(t) = t² (미터, 초) */
var bike={s:function(t){return t*t;},v:function(t){return 2*t;},sec:function(t,h){return ((t+h)*(t+h)-t*t)/h;}};

/* ① 3장 빵 공장: 고정비 FC, 가변비 VC(Q) = aQ − bQ² + cQ³ (Q는 하루 생산량, 단위 10개; 돈은 천 원) */
var bakery={FC:60,a:20,b:3,c:0.2,cap:15};
bakery.VC=function(Q){var B=bakery;return B.a*Q-B.b*Q*Q+B.c*Q*Q*Q;};
bakery.TC=function(Q){return bakery.FC+bakery.VC(Q);};
bakery.MC=function(Q){var B=bakery;return B.a-2*B.b*Q+3*B.c*Q*Q;};
bakery.AVC=function(Q){var B=bakery;return B.a-B.b*Q+B.c*Q*Q;};
bakery.ATC=function(Q){return bakery.AVC(Q)+bakery.FC/Q;};
bakery.profit=function(Q,P){return P*Q-bakery.TC(Q);};
/* MR = MC의 두 교점 (완전경쟁이라 MR = P). 없으면 null */
bakery.cross=function(P){var B=bakery,A=3*B.c,Bq=-2*B.b,C=B.a-P,D=Bq*Bq-4*A*C;if(D<0)return null;var s=Math.sqrt(D);return [(-Bq-s)/(2*A),(-Bq+s)/(2*A)];};
bakery.avcMin=function(){var B=bakery,q=B.b/(2*B.c);return {Q:q,v:B.AVC(q)};};
bakery.atcMin=function(){var q=argmin(bakery.ATC,0.5,30);return {Q:q,v:bakery.ATC(q)};};
/* 단기 최선: MR = MC의 오른쪽 교점(능력 한도 안), 그 이윤이 −FC보다 나쁘면 문 닫기(Q = 0) */
bakery.best=function(P){var x=bakery.cross(P),q=x?Math.min(Math.max(x[1],0),bakery.cap):0,pr=bakery.profit(q,P);
  if(pr< -bakery.FC||!x)return {Q:0,profit:-bakery.FC,open:false,qx:q,prx:pr};return {Q:q,profit:pr,open:true,qx:q,prx:pr};};
/* 대결 ①: 세 가격에서 주판봇(능력 한도까지 생산) vs 초파리(MR = MC, 손해가 고정비보다 크면 중단) */
var DUEL1=[20,14,7];
function duel1(){return DUEL1.map(function(P){var B=bakery,robo=B.profit(B.cap,P),f=B.best(P);return {P:P,roboQ:B.cap,robo:robo,flyQ:f.Q,fly:f.profit,open:f.open};});}

/* ② 4장 공장: Q = 2√(L·K), 가격 P, 임금 w, 기계 사용료(이자) r. 단위: 사람·대·톤·만원(하루) */
var fac={P:10,w:5,r:10,K0:4};
fac.Q=function(L,K){return 2*Math.sqrt(L*K);};
fac.MPL=function(L,K){return Math.sqrt(K/L);};
fac.MPK=function(L,K){return Math.sqrt(L/K);};
fac.shortRun=function(P,w,K){var L=K*Math.pow(P/w,2);return {L:L,Q:fac.Q(L,K),profit:P*fac.Q(L,K)-w*L-fac.r*K};};
/* 목표 생산량 Qt를 가장 싸게: K/L = w/r, 비용 C*(Qt) = Qt·√(w·r) */
fac.costMin=function(Qt,w,r){w=w||fac.w;r=r||fac.r;var L=Qt/2*Math.sqrt(r/w),K=Qt/2*Math.sqrt(w/r);return {L:L,K:K,C:w*L+r*K,lam:Math.sqrt(w*r)};};
fac.MCnum=function(Qt){return fac.costMin(Qt+0.5).C-fac.costMin(Qt-0.5).C;};

/* ② 4.4 미분방정식: 커피 식기 dT/dt = −k(T − 20) */
var cool={k:0.1,Ta:20,T0:90,exact:function(t){return cool.Ta+(cool.T0-cool.Ta)*Math.exp(-cool.k*t);},
  euler:function(dt,tEnd){var T=cool.T0,t=0,out=[[0,T]];while(t<tEnd-1e-9){T+=dt*(-cool.k*(T-cool.Ta));t+=dt;out.push([t,T]);}return out;}};

/* ② 5.1 경사하강: 손실 L(w) = (w − 3)² + 1 */
var loss={L:function(w){return (w-3)*(w-3)+1;},dL:function(w){return 2*(w-3);},
  run:function(w0,lr,n){var w=w0,out=[w];for(var i=0;i<n;i++){w=w-lr*loss.dL(w);out.push(w);}return out;}};

/* ② 5.2 연쇄법칙: x → u = 2x + 1 → v = u² → y = 3v */
var chain={f:function(x){var u=2*x+1;return 3*u*u;},links:function(x){var u=2*x+1,v=u*u;return {u:u,v:v,y:3*v,du:2,dv:2*u,dy:3,prod:3*2*u*2};}};

/* ② 5.3 특성공학: 씨앗 고정 데이터, 참 모형 y = 1 + x1 + 0.5x2 + 0.8x1² + 1.5x1x2 + 잡음 */
function rng(seed){var s=seed>>>0;return function(){s=(s*1664525+1013904223)>>>0;return s/4294967296;};}
function gauss(r){var u=Math.max(r(),1e-12),v=r();return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v);}
var TRUE={b0:1,b1:1,b2:0.5,b11:0.8,b22:0,b12:1.5,sd:0.3};
function trueY(x1,x2){var T=TRUE;return T.b0+T.b1*x1+T.b2*x2+T.b11*x1*x1+T.b22*x2*x2+T.b12*x1*x2;}
function makeData(n,seed){var r=rng(seed),out=[];for(var i=0;i<n;i++){var x1=r()*4-2,x2=r()*2;out.push([x1,x2,trueY(x1,x2)+TRUE.sd*gauss(r)]);}return out;}
var FEATS={lin:{name:'일차항만',f:function(a,b){return [1,a,b];},lab:['1','x₁','x₂']},
  robo:{name:'제곱항 추가 (주판봇)',f:function(a,b){return [1,a,b,a*a,b*b];},lab:['1','x₁','x₂','x₁²','x₂²']},
  fly:{name:'교차항 추가 (초파리)',f:function(a,b){return [1,a,b,a*a,a*b];},lab:['1','x₁','x₂','x₁²','x₁·x₂']}};
function solve(A,y){var n=A.length,M=A.map(function(r,i){return r.concat([y[i]]);});for(var c=0;c<n;c++){var p=c;for(var r2=c+1;r2<n;r2++)if(Math.abs(M[r2][c])>Math.abs(M[p][c]))p=r2;var t=M[c];M[c]=M[p];M[p]=t;
  for(var r3=0;r3<n;r3++){if(r3===c)continue;var k=M[r3][c]/M[c][c];for(var j=c;j<=n;j++)M[r3][j]-=k*M[c][j];}}return M.map(function(r,i){return r[n]/r[i];});}
function fit(key,data){var F=FEATS[key].f,p=F(0,0).length,A=[],b=[];for(var i=0;i<p;i++){A.push(new Array(p).fill(0));b.push(0);}
  data.forEach(function(r){var x=F(r[0],r[1]);for(var i=0;i<p;i++){b[i]+=x[i]*r[2];for(var j=0;j<p;j++)A[i][j]+=x[i]*x[j];}});return solve(A,b);}
function predict(key,w,a,b){var x=FEATS[key].f(a,b),s=0;for(var i=0;i<x.length;i++)s+=w[i]*x[i];return s;}
function mse(key,w,data){var s=0;data.forEach(function(r){var e=predict(key,w,r[0],r[1])-r[2];s+=e*e;});return s/data.length;}
var TRAIN=makeData(80,20261116),VALID=makeData(200,777);
function duel2(){var out={};['lin','robo','fly'].forEach(function(k){var w=fit(k,TRAIN);out[k]={w:w,train:mse(k,w,TRAIN),valid:mse(k,w,VALID)};});return out;}
/* 모형의 두 번 미분: 숫자로 재기 */
function second(fn,x1,x2){var h=1e-3;var fxx=(fn(x1+h,x2)-2*fn(x1,x2)+fn(x1-h,x2))/(h*h);var fxy=(fn(x1+h,x2+h)-fn(x1+h,x2-h)-fn(x1-h,x2+h)+fn(x1-h,x2-h))/(4*h*h);return {xx:fxx,xy:fxy};}

/* ② 5.4 규제항: 손실 (w − a)ᵀA(w − a), 벌점 λ|w|² → w(λ) = (A + λI)⁻¹ A a */
var ridge={A:[[3,1],[1,1.2]],a:[2.4,1.6]};
ridge.loss=function(w){var A=ridge.A,d=[w[0]-ridge.a[0],w[1]-ridge.a[1]];return d[0]*(A[0][0]*d[0]+A[0][1]*d[1])+d[1]*(A[1][0]*d[0]+A[1][1]*d[1]);};
ridge.w=function(l){var A=ridge.A,M=[[A[0][0]+l,A[0][1]],[A[1][0],A[1][1]+l]],Aa=[A[0][0]*ridge.a[0]+A[0][1]*ridge.a[1],A[1][0]*ridge.a[0]+A[1][1]*ridge.a[1]],det=M[0][0]*M[1][1]-M[0][1]*M[1][0];
  return [(M[1][1]*Aa[0]-M[0][1]*Aa[1])/det,(-M[1][0]*Aa[0]+M[0][0]*Aa[1])/det];};
/* 같은 반지름 c 안에서 손실 최소(제약 문제)를 직접 찾기: 원 둘레를 훑는다 */
ridge.constrained=function(c){if(Math.hypot(ridge.a[0],ridge.a[1])<=c)return ridge.a.slice();var best=null,bv=Infinity;for(var i=0;i<7200;i++){var t=2*Math.PI*i/7200,w=[c*Math.cos(t),c*Math.sin(t)],v=ridge.loss(w);if(v<bv){bv=v;best=w;}}return best;};

return {d:d,root:root,argmin:argmin,bike:bike,bakery:bakery,duel1:duel1,DUEL1:DUEL1,fac:fac,cool:cool,loss:loss,chain:chain,
  TRUE:TRUE,trueY:trueY,FEATS:FEATS,fit:fit,predict:predict,mse:mse,TRAIN:TRAIN,VALID:VALID,duel2:duel2,second:second,ridge:ridge};
})();
if(typeof module!=='undefined')module.exports=DM;
