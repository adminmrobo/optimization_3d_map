/* vecmath.js — 3편 화살표 밭 편의 계산 모듈 (브라우저·node 공용)
   숫자 밭(스칼라장) f(x,y,z), 화살표 밭(벡터장) F(x,y,z), 그리고 ∇로 만드는 네 연산을
   "이웃 점을 찍어 보는" 차분으로 계산한다. 정확한 값(식)도 함께 둔다. */
var VM=(function(){
'use strict';
var E=Math.exp;
/* 숫자 밭: f, 정확한 기울기 g, 정확한 라플라시안 lap */
var SF={
 heater:{name:'난로 둘레 온도',unit:'℃',
   f:function(x,y,z){return 20+30*E(-(x*x+y*y+z*z)/2);},
   g:function(x,y,z){var e=30*E(-(x*x+y*y+z*z)/2);return [-x*e,-y*e,-z*e];},
   lap:function(x,y,z){var r2=x*x+y*y+z*z;return 30*E(-r2/2)*(r2-3);}},
 bowl:{name:'그릇 x² + y² + z²',unit:'',
   f:function(x,y,z){return x*x+y*y+z*z;},g:function(x,y,z){return [2*x,2*y,2*z];},lap:function(){return 6;}},
 dome:{name:'돔 −(x² + y² + z²)',unit:'',
   f:function(x,y,z){return -(x*x+y*y+z*z);},g:function(x,y,z){return [-2*x,-2*y,-2*z];},lap:function(){return -6;}},
 tilt:{name:'기울어진 판 x + 2y + z/2',unit:'',
   f:function(x,y,z){return x+2*y+0.5*z;},g:function(){return [1,2,0.5];},lap:function(){return 0;}},
 saddle:{name:'안장 x² + y² − 2z²',unit:'',
   f:function(x,y,z){return x*x+y*y-2*z*z;},g:function(x,y,z){return [2*x,2*y,-4*z];},lap:function(){return 0;}}
};
/* 화살표 밭: F, 정확한 발산 div, 정확한 회전 curl */
var VF={
 source:{name:'샘 (x, y, z)',F:function(x,y,z){return [x,y,z];},div:function(){return 3;},curl:function(){return [0,0,0];}},
 sink:{name:'빨아들임 −(x, y, z)',F:function(x,y,z){return [-x,-y,-z];},div:function(){return -3;},curl:function(){return [0,0,0];}},
 uniform:{name:'균일한 흐름 (1, 0.5, 0)',F:function(){return [1,0.5,0];},div:function(){return 0;},curl:function(){return [0,0,0];}},
 stretch:{name:'빨라지는 흐름 (x, 0, 0)',F:function(x){return [x,0,0];},div:function(){return 1;},curl:function(){return [0,0,0];}},
 swirl:{name:'소용돌이 (−y, x, 0)',F:function(x,y){return [-y,x,0];},div:function(){return 0;},curl:function(){return [0,0,2];}},
 roll:{name:'옆으로 누운 소용돌이 (0, −z, y)',F:function(x,y,z){return [0,-z,y];},div:function(){return 0;},curl:function(){return [2,0,0];}},
 shear:{name:'층밀림 (y, 0, 0)',F:function(x,y){return [y,0,0];},div:function(){return 0;},curl:function(){return [0,0,-1];}},
 twist:{name:'비틀린 밭 (y, x, 0)',F:function(x,y){return [y,x,0];},div:function(){return 0;},curl:function(){return [0,0,0];}},
 vortex:{name:'배수구 소용돌이 (−y, x, 0)/(x² + y²)',F:function(x,y){var r2=x*x+y*y;if(r2<1e-6)return [0,0,0];return [-y/r2,x/r2,0];},div:function(){return 0;},curl:function(){return [0,0,0];}}
};
function add(p,i,h){var q=p.slice();q[i]+=h;return q;}
/* 편미분: 한 축으로만 h만큼 앞뒤를 찍어 본다 */
function pd(f,p,i,h){h=h||1e-3;return (f.apply(null,add(p,i,h))-f.apply(null,add(p,i,-h)))/(2*h);}
function grad(f,p,h){return [pd(f,p,0,h),pd(f,p,1,h),pd(f,p,2,h)];}
function comp(F,k){return function(x,y,z){return F(x,y,z)[k];};}
function div(F,p,h){return pd(comp(F,0),p,0,h)+pd(comp(F,1),p,1,h)+pd(comp(F,2),p,2,h);}
function curl(F,p,h){var Fx=comp(F,0),Fy=comp(F,1),Fz=comp(F,2);
  return [pd(Fz,p,1,h)-pd(Fy,p,2,h),pd(Fx,p,2,h)-pd(Fz,p,0,h),pd(Fy,p,0,h)-pd(Fx,p,1,h)];}
/* 라플라시안: 이웃 6개의 평균 − 가운데 = (h²/6)·∇²f */
function lap6(f,p,h){var c=f.apply(null,p),s=0,nb=[];for(var i=0;i<3;i++)[h,-h].forEach(function(d){var q=add(p,i,d),v=f.apply(null,q);nb.push([q,v]);s+=v;});
  var avg=s/6;return {c:c,avg:avg,diff:avg-c,est:6*(avg-c)/(h*h),nb:nb};}
/* 상자(한 변 a, 가운데 c)의 여섯 면으로 나가는 양: 면마다 m×m 점의 중점 규칙 */
function flux(F,c,a,m){m=m||6;var faces=[],out=0,inn=0,A=a*a;
  for(var i=0;i<3;i++)[1,-1].forEach(function(sg){var s=0;for(var u=0;u<m;u++)for(var v=0;v<m;v++){var p=c.slice(),j=(i+1)%3,k=(i+2)%3;
      p[i]+=sg*a/2;p[j]+=-a/2+a*(u+.5)/m;p[k]+=-a/2+a*(v+.5)/m;s+=F(p[0],p[1],p[2])[i]*sg;}
    var fl=s/(m*m)*A;faces.push({axis:i,sign:sg,flux:fl});if(fl>0)out+=fl;else inn+=-fl;});
  return {faces:faces,out:out,inn:inn,net:out-inn,perVol:(out-inn)/(a*a*a)};}
/* 바람개비: 축 n에 수직인 반지름 r의 고리를 따라 흐름을 더한 값(순환) ÷ 넓이 = 회전의 n 성분. 바람개비는 그 절반의 빠르기로 돈다 */
function basis(n){var a=Math.abs(n[0])<0.9?[1,0,0]:[0,1,0];var u=[n[1]*a[2]-n[2]*a[1],n[2]*a[0]-n[0]*a[2],n[0]*a[1]-n[1]*a[0]],m=Math.hypot(u[0],u[1],u[2]);u=u.map(function(x){return x/m;});
  var v=[n[1]*u[2]-n[2]*u[1],n[2]*u[0]-n[0]*u[2],n[0]*u[1]-n[1]*u[0]];return [u,v];}
function circ(F,c,n,r,m){m=m||72;var B=basis(n),u=B[0],v=B[1],s=0;for(var k=0;k<m;k++){var t=2*Math.PI*(k+.5)/m,ct=Math.cos(t),st=Math.sin(t);
    var p=[0,1,2].map(function(i){return c[i]+r*(ct*u[i]+st*v[i]);}),T=[0,1,2].map(function(i){return -st*u[i]+ct*v[i];}),f=F(p[0],p[1],p[2]);s+=(f[0]*T[0]+f[1]*T[1]+f[2]*T[2])*(2*Math.PI*r/m);}
  var cn=s/(Math.PI*r*r);return {circ:s,curlN:cn,omega:cn/2};}
/* 점 하나를 흐름 따라 옮기기 (RK4) */
function step(F,p,dt){function f(q){return F(q[0],q[1],q[2]);}function ad(a,b,k){return [a[0]+b[0]*k,a[1]+b[1]*k,a[2]+b[2]*k];}
  var k1=f(p),k2=f(ad(p,k1,dt/2)),k3=f(ad(p,k2,dt/2)),k4=f(ad(p,k3,dt));return [0,1,2].map(function(i){return p[i]+dt/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i]);});}
/* 상자 꼭짓점 8개(직선 흐름이면 상자는 평행육면체로 남는다) → 부피 = 세 모서리 벡터의 행렬식 */
function corners(c,a){var L=[];[-1,1].forEach(function(i){[-1,1].forEach(function(j){[-1,1].forEach(function(k){L.push([c[0]+i*a/2,c[1]+j*a/2,c[2]+k*a/2]);});});});return L;}
function vol(C){var o=C[0],e1=C[4].map(function(v,i){return v-o[i];}),e2=C[2].map(function(v,i){return v-o[i];}),e3=C[1].map(function(v,i){return v-o[i];});
  return Math.abs(e1[0]*(e2[1]*e3[2]-e2[2]*e3[1])-e1[1]*(e2[0]*e3[2]-e2[2]*e3[0])+e1[2]*(e2[0]*e3[1]-e2[1]*e3[0]));}
/* 대결: 바람개비(축 z)가 도는가 — 네 곳 */
var DUEL=[
 {key:'swirl',p:[1,0,0],look:'화살표가 원을 그리며 돈다'},
 {key:'shear',p:[0,1,0],look:'화살표가 모두 나란하다'},
 {key:'vortex',p:[1,0,0],look:'화살표가 원을 그리며 돈다'},
 {key:'source',p:[1,0,0],look:'화살표가 바깥으로 뻗는다'}];
function duel(){return DUEL.map(function(d){var F=VF[d.key].F,real=circ(F,d.p,[0,0,1],0.08).omega,spin=Math.abs(real)>1e-3;
  var robo=d.look.indexOf('돈다')>=0,fly=Math.abs(curl(F,d.p,1e-3)[2])>1e-3;return {key:d.key,p:d.p,look:d.look,omega:real,spin:spin,robo:robo,fly:fly,roboOk:robo===spin,flyOk:fly===spin};});}
return {SF:SF,VF:VF,pd:pd,grad:grad,div:div,curl:curl,lap6:lap6,flux:flux,circ:circ,step:step,corners:corners,vol:vol,duel:duel,DUEL:DUEL};
})();
if(typeof module!=='undefined')module.exports=VM;
