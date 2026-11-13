/* labmath.js — 「좌표축 위의 그릇」 두 편이 함께 쓰는 계산 모듈.
   페이지 안에 그대로 들어가고(build.js), node로도 돌려 기대 수치를 확인한다(code/check_numbers.js).
   난수는 시드 고정 mulberry32 + 박스-뮬러. Math.random()은 쓰지 않는다. */
var LM=(function(){
'use strict';
function rng(seed){var a=seed>>>0;return function(){a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function gauss(r){var u=0,v=0;while(u<1e-12)u=r();v=r();return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v);}

/* ── 데이터: 직선 y = 2x + 1 주변의 점 n개 (x는 -3~3 균등, 잡음은 표준정규) ── */
function makeLine(seed,n){var r=rng(seed),x=new Float64Array(n),y=new Float64Array(n);
  for(var i=0;i<n;i++){x[i]=-3+6*r();y[i]=2*x[i]+1+gauss(r);} return {x:x,y:y,n:n};}

/* 오차(평균제곱) — 뉴런 하나: 예측 = w·x + b */
function loss(D,w,b){var s=0;for(var i=0;i<D.n;i++){var e=w*D.x[i]+b-D.y[i];s+=e*e;}return s/D.n;}
/* 묶음(인덱스 배열)에서 잰 기울기 [∂L/∂w, ∂L/∂b] */
function gradOn(D,w,b,idx,from,to){var gw=0,gb=0,m=to-from;for(var k=from;k<to;k++){var i=idx[k];var e=2*(w*D.x[i]+b-D.y[i])/m;gw+=e*D.x[i];gb+=e;}return [gw,gb];}
/* 헤시안: 이 그릇은 2차 함수라 어디서나 같다 */
function hessian(D){var sx=0,sxx=0;for(var i=0;i<D.n;i++){sx+=D.x[i];sxx+=D.x[i]*D.x[i];}
  var a=2*sxx/D.n,b=2*sx/D.n,d=2; var tr=a+d,det=a*d-b*b,q=Math.sqrt(tr*tr/4-det);
  return {H:[[a,b],[b,d]],lmin:tr/2-q,lmax:tr/2+q};}
/* 최소제곱 해 = 그릇의 바닥 */
function ols(D){var sx=0,sy=0,sxx=0,sxy=0,n=D.n;for(var i=0;i<n;i++){sx+=D.x[i];sy+=D.y[i];sxx+=D.x[i]*D.x[i];sxy+=D.x[i]*D.y[i];}
  var w=(n*sxy-sx*sy)/(n*sxx-sx*sx),b=(sy-w*sx)/n;return {w:w,b:b,L:loss(D,w,b)};}

/* 미니배치 경사하강: 걸음 수(steps)를 같게. 에포크마다 카드를 새로 섞는다.
   돌려주는 것: path[k]=[w,b,전체 데이터 오차], 오르막 걸음 수, 1 에포크(데이터 한 바퀴) 뒤의 오차 */
function runBatch(D,size,o){o=o||{};var steps=o.steps||100,lr=o.lr==null?0.1:o.lr,w=o.w0==null?-1:o.w0,b=o.b0==null?-1:o.b0;
  var r=rng(o.seed==null?7:o.seed),idx=new Int32Array(D.n),per=Math.floor(D.n/size),path=[[w,b,loss(D,w,b)]],up=0,k=0,blow=false;
  for(var i=0;i<D.n;i++)idx[i]=i;
  while(k<steps){for(var j=D.n-1;j>0;j--){var t=Math.floor(r()*(j+1)),s=idx[j];idx[j]=idx[t];idx[t]=s;}
    for(var m=0;m<per&&k<steps;m++,k++){var g=gradOn(D,w,b,idx,m*size,(m+1)*size);w-=lr*g[0];b-=lr*g[1];
      var L=loss(D,w,b);if(!isFinite(L)||L>1e9){blow=true;L=1e9;}
      if(L>path[path.length-1][2]+1e-9)up++;path.push([w,b,L]);if(blow)break;}
    if(blow)break;}
  var ep=Math.min(per,path.length-1);
  return {path:path,up:up,afterEpoch:path[ep][2],last:path[path.length-1][2],blow:blow,size:size};}

/* ── 안장점 대결: f(w1,w2) = (w1² − 1)² + w2² ──
   (0,0)은 기울기 0인 안장, (±1,0)은 바닥(오차 0) */
function sf(p){var a=p[0]*p[0]-1;return a*a+p[1]*p[1];}
function sg(p){return [4*p[0]*(p[0]*p[0]-1),2*p[1]];}
function sh(p){return [[12*p[0]*p[0]-4,0],[0,2]];}
/* checkCurv=false: 기울기만 본다 (주판봇) / true: 기울기가 0에 가까우면 헤시안 고유값을 보고, 음수면 그 방향으로 한 발 (초파리) */
/* 2×2 대칭 행렬의 가장 작은 고유값과 그 고유벡터(단위) */
function eig2(H){var a=H[0][0],b=H[0][1],d=H[1][1],tr=a+d,q=Math.sqrt((a-d)*(a-d)/4+b*b),lmin=tr/2-q,v=Math.abs(b)>1e-12?[lmin-d,b]:(a<=d?[1,0]:[0,1]),m=Math.hypot(v[0],v[1]);return {lmin:lmin,lmax:tr/2+q,v:[v[0]/m,v[1]/m]};}
function saddleRun(checkCurv,o){o=o||{};var p=[o.x0==null?0:o.x0,o.y0==null?1.5:o.y0],lr=o.lr||0.05,steps=o.steps||200,path=[[p[0],p[1],sf(p)]],kicks=0;
  for(var k=0;k<steps;k++){var g=sg(p),gn=Math.hypot(g[0],g[1]);
    if(gn<1e-3){ if(!checkCurv)break;
      var E=eig2(sh(p)); if(E.lmin<0&&kicks<3){p=[p[0]+0.05*E.v[0],p[1]+0.05*E.v[1]];kicks++;path.push([p[0],p[1],sf(p)]);continue;} break; }
    p=[p[0]-lr*g[0],p[1]-lr*g[1]];path.push([p[0],p[1],sf(p)]);}
  return {path:path,end:p,L:sf(p),kicks:kicks,steps:path.length-1};}

return {eig2:eig2,rng:rng,gauss:gauss,makeLine:makeLine,loss:loss,gradOn:gradOn,hessian:hessian,ols:ols,runBatch:runBatch,sf:sf,sg:sg,sh:sh,saddleRun:saddleRun};
})();
if(typeof module!=='undefined')module.exports=LM;
