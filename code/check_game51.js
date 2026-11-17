// 첫걸음 ② 5.1 미니 게임 검산: node code/check_game51.js
// 손실 L = a·w₁² + b·w₂², 한 걸음 v ← β·v − η∇L, θ ← θ + v. 성공 = 바닥까지 < 0.15, 실패 = 걸음 소진 또는 L > 25
const ST=[{nm:'1 둥근',a:1,b:1,s:[3.2,2.4],N:10,star:[2,5]},{nm:'2 길쭉',a:0.5,b:4,s:[-4,1.5],N:25,star:[15,20]},{nm:'3 안개',a:0.5,b:4,s:[3.5,-1.8],N:25,star:[15,20]},{nm:'4 모멘텀',a:0.5,b:12.5,s:[-4.5,1],N:20,star:[13,17]}];
const RIM=25,HOLE=0.15,L=(S,x,y)=>S.a*x*x+S.b*y*y;
function run(S,eta,beta){let x=S.s[0],y=S.s[1],vx=0,vy=0;for(let k=1;k<=S.N;k++){vx=beta*vx-eta*2*S.a*x;vy=beta*vy-eta*2*S.b*y;x+=vx;y+=vy;if(!(L(S,x,y)<=RIM))return 'out';if(Math.hypot(x,y)<HOLE)return k;}return 'tired';}
const ok=(c,m)=>{if(!c){console.error('FAIL',m);process.exitCode=1;}else console.log('ok',m);};
const g=(S,e,b)=>run(S,+e.toFixed(2),b||0);
ok(Math.hypot(...ST[0].s)===4,'1판 출발 거리 4');
ok(g(ST[0],0.5)===1,'1판 η=0.5 → 1걸음');ok(g(ST[0],0.25)===5,'1판 η=0.25 → 5걸음(4→2→1→0.5→0.25→0.125)');
ok(g(ST[0],1.0)==='tired','1판 η=1 → 제자리 왕복');ok(g(ST[0],1.05)==='out','1판 η>1 → 튀어 나감');
let b2=99;for(let e=0.01;e<=0.4001;e+=0.01){const r=g(ST[1],e);if(typeof r==='number')b2=Math.min(b2,r);}ok(b2===14,'2판 최고 14걸음(η≈0.21~0.22) → 별 3개 가능');
ok(g(ST[1],0.26)==='out','2판 η=0.26 → 튀어 나감 (한계 1/4)');
let b4=99;for(let e=0.01;e<=0.1201;e+=0.01){const r=g(ST[3],e,0);if(typeof r==='number')b4=Math.min(b4,r);}ok(b4===99,'4판 β=0이면 20걸음 안에 불가');
ok(g(ST[3],0.06,0.7)===11,'4판 η=0.06, β=0.7 → 11걸음');
ST.forEach(S=>ok(L(S,...S.s)<=RIM,S.nm+' 출발점이 그릇 안 (L='+L(S,...S.s).toFixed(2)+')'));
