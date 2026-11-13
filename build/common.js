/* common.js — 두 편이 함께 쓰는 공용 모듈 (ai-lab-explainer 12-3 대응)
   도우미 → 캐릭터(Cast) → 루프(보이는 캔버스만) → 도장 → 용어(Gloss) → 학습 도우미(Study) → 3D 지형(Surf3D) → 2D 그래프(plot) */
var U=(function(){
'use strict';
var $=function(s,r){return (r||document).querySelector(s);}, $$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s));};
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
function cssv(n){return getComputedStyle(document.documentElement).getPropertyValue(n).trim();}
var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
function fmt(x,d){if(x==null||!isFinite(x))return '—';return Number(x).toFixed(d==null?3:d);}
function clamp(x,a,b){return Math.max(a,Math.min(b,x));}

/* ── 캐릭터 ── */
var BASE={doc:'doc_front',asst:'asst_smile',fly:'fly_clip',robo:'robo_smile',sia:'sia_smile',moa:'moa_smile',x1:'x1_hint',x2:'x2_hint',x3:'x3_hint'};
function spr(k){var A=window.SPRITE_ALIAS||{},S=window.SPRITE||{};var a=A[k]||k;if(S[a])return S[a];var who=k.split('_')[0];var b=A[BASE[who]]||BASE[who];return S[b]||'';}
var NAMES={doc:'박사',asst:'조수 하루',fly:'초파리 연구원',robo:'주판봇',sia:'인턴 시아',moa:'인턴 모아',x1:'미공개',x2:'미공개',x3:'미공개'};
function say(who,key,text,right){return '<div class="say'+(right?' right':'')+'" data-who="'+who+'"><img class="who" data-who="'+who+'" data-mood="'+key+'" src="'+spr(key)+'" alt="" aria-hidden="true"><div><b class="name">'+NAMES[who]+'</b><p>'+text+'</p></div></div>';}
function dialogues(DLG){$$('[data-dlg]').forEach(function(el){var d=DLG[el.dataset.dlg];if(!d)return;el.innerHTML=d.map(function(x,i){return say(x[0],x[1],x[2],i%2===1);}).join('');});}
function fillImgs(){$$('img[data-mood]').forEach(function(im){if(!im.getAttribute('src'))im.src=spr(im.dataset.mood);});}
function setMood(img,key){if(!img)return;if(reduce){img.src=spr(key);img.dataset.mood=key;return;}img.style.transition='opacity .2s';img.style.opacity=0;setTimeout(function(){img.src=spr(key);img.dataset.mood=key;img.style.opacity=1;},200);}

/* ── 루프: requestAnimationFrame 하나, 보이는 캔버스만 ── */
var items=[],last=0;
function reg(el,fn){var it={el:el,fn:fn,vis:true};items.push(it);if('IntersectionObserver' in window){new IntersectionObserver(function(es){es.forEach(function(e){it.vis=e.isIntersecting;});},{rootMargin:'120px'}).observe(el);}return it;}
function tick(t){var dt=Math.min(0.05,(t-last)/1000||0);last=t;for(var i=0;i<items.length;i++){var it=items[i];if(it.vis)it.fn(dt);}requestAnimationFrame(tick);}
function drawAll(){items.forEach(function(it){it.fn(0);});}
function start(){drawAll();requestAnimationFrame(tick);var to;window.addEventListener('resize',function(){clearTimeout(to);to=setTimeout(drawAll,120);});}

function setup(cv){var r=cv.getBoundingClientRect();var dpr=Math.min(2,window.devicePixelRatio||1);var w=Math.max(260,r.width||cv.parentNode.clientWidth||600),h=r.height||260;
  if(cv.width!==Math.round(w*dpr)||cv.height!==Math.round(h*dpr)){cv.width=Math.round(w*dpr);cv.height=Math.round(h*dpr);}
  var g=cv.getContext('2d');g.setTransform(dpr,0,0,dpr,0,0);g.clearRect(0,0,w,h);return {g:g,w:w,h:h};}
function grid24(g,w,h){g.strokeStyle='rgba(91,95,117,.07)';g.lineWidth=1;g.beginPath();for(var x=0;x<w;x+=24){g.moveTo(x+.5,0);g.lineTo(x+.5,h);}for(var y=0;y<h;y+=24){g.moveTo(0,y+.5);g.lineTo(w,y+.5);}g.stroke();}
function stamp(g,w,text){g.save();g.font='600 11px '+cssv('--font');var tw=g.measureText(text).width+12;g.fillStyle='rgba(255,255,255,.9)';g.fillRect(w-tw-8,8,tw,18);g.strokeStyle='rgba(168,106,0,.7)';g.setLineDash([3,2]);g.strokeRect(w-tw-8+.5,8.5,tw-1,17);g.setLineDash([]);g.fillStyle=cssv('--amber');g.textAlign='left';g.textBaseline='middle';g.fillText(text,w-tw-2,17);g.restore();}
function label(g,x,y,t,col,align){g.save();g.font='600 12px '+cssv('--font');g.textAlign=align||'left';g.textBaseline='middle';var tw=g.measureText(t).width;var x0=align==='center'?x-tw/2:align==='right'?x-tw:x;g.fillStyle='rgba(255,255,255,.88)';g.fillRect(x0-4,y-9,tw+8,18);g.fillStyle=col;g.fillText(t,x,y);g.restore();}
function arrow2(g,x0,y0,x1,y1,col,w){var a=Math.atan2(y1-y0,x1-x0),L=Math.hypot(x1-x0,y1-y0);if(L<1)return;var hw=Math.min(9,L*.4);g.strokeStyle=col;g.fillStyle=col;g.lineWidth=w||2;g.beginPath();g.moveTo(x0,y0);g.lineTo(x1-Math.cos(a)*hw*.7,y1-Math.sin(a)*hw*.7);g.stroke();g.beginPath();g.moveTo(x1,y1);g.lineTo(x1-Math.cos(a-.42)*hw,y1-Math.sin(a-.42)*hw);g.lineTo(x1-Math.cos(a+.42)*hw,y1-Math.sin(a+.42)*hw);g.closePath();g.fill();}

/* ── 버튼 묶음 ── */
function btns(host,list,cur,on){host.innerHTML='';list.forEach(function(v){var b=document.createElement('button');b.className='bt';b.type='button';b.textContent=v[1];b.setAttribute('aria-pressed',String(v[0]===cur));b.onclick=function(){$$('.bt',host).forEach(function(x){x.setAttribute('aria-pressed','false');});b.setAttribute('aria-pressed','true');on(v[0]);};host.appendChild(b);});}
function ins(el,items){el.innerHTML=items.map(function(x){return '<p class="'+x[0]+'">'+x[1]+'</p>';}).join('');}

/* ── 용어 말풍선 (11-2): 범위마다 첫 등장만 밑줄. 핵심 → 전체 → 끄기 ── */
var GL={},CORE=[],glMode='core',tip;
function Gloss(dict,core){GL=dict;CORE=core||[];tip=document.createElement('div');tip.id='tip';tip.setAttribute('role','tooltip');document.body.appendChild(tip);mark();
  document.addEventListener('keydown',function(e){if(e.key==='Escape')hide();});window.addEventListener('scroll',hide,{passive:true});}
function hide(){if(tip)tip.style.display='none';}
function show(el){var d=GL[el.dataset.t];if(!d)return;tip.innerHTML='<b>'+esc(d[0])+'</b><small>'+esc(d[1])+'</small><div>'+d[2]+'</div>';tip.style.display='block';var r=el.getBoundingClientRect();var x=clamp(r.left,8,window.innerWidth-316),y=r.bottom+8;if(y+140>window.innerHeight)y=Math.max(8,r.top-150);tip.style.left=x+'px';tip.style.top=y+'px';}
function unmark(){$$('span.jt[data-gl]').forEach(function(s){s.replaceWith(document.createTextNode(s.textContent));});document.body.normalize();}
function mark(){unmark();if(glMode==='off')return;var keys=(glMode==='core'?CORE:Object.keys(GL)).slice().sort(function(a,b){return b.length-a.length;});
  $$('section.sec, header.hero').forEach(function(scope){var used={};
    $$('p, li, td, .say p',scope).forEach(function(p){if(p.closest('.quiz, .ctrl, nav, .kpis, .minis, .insight, .eq, #kg, #export, button, #tb1'))return;
      var walker=document.createTreeWalker(p,NodeFilter.SHOW_TEXT,null),nodes=[],n;while((n=walker.nextNode()))nodes.push(n);
      nodes.forEach(function(tn){if(tn.parentNode.closest('.jt, a, b.name, math'))return;var s=tn.nodeValue;
        for(var i=0;i<keys.length;i++){var k=keys[i];if(used[k])continue;var at=s.indexOf(k);if(at<0)continue;used[k]=1;
          var span=document.createElement('span');span.className='jt';span.dataset.gl='1';span.dataset.t=k;span.tabIndex=0;span.textContent=k;
          var after=tn.splitText(at);after.nodeValue=after.nodeValue.slice(k.length);tn.parentNode.insertBefore(span,after);
          span.addEventListener('pointerenter',function(){show(this);});span.addEventListener('pointerleave',hide);span.addEventListener('focus',function(){show(this);});span.addEventListener('blur',hide);
          span.addEventListener('click',function(e){e.stopPropagation();tip.style.display==='block'?hide():show(this);});break;}});});});}

/* ── 학습 도우미 (11-3, 11-4) ── */
var Q={},got={},nQ=0;
function Study(o){Q=o.quiz||{};nQ=0;Object.keys(Q).forEach(function(k){nQ+=Q[k].length;});
  var qn=0;Object.keys(Q).forEach(function(k){Q[k]=Q[k].map(function(it){var n=it.o.length,tgt=(qn++*2+1)%n,r=(tgt-it.a+n)%n,o=new Array(n);it.o.forEach(function(x,i){o[(i+r)%n]=x;});return {q:it.q,o:o,a:tgt,why:it.why,hint:it.hint};});});
  $$('.quiz[data-quiz]').forEach(function(host){var list=Q[host.dataset.quiz]||[];host.innerHTML='';list.forEach(function(it,qi){var box=document.createElement('div');box.style.marginBottom='10px';
    box.innerHTML='<div class="q">Q. '+it.q+'</div><div class="opts"></div><div class="fb" aria-live="polite"></div>';var ops=$('.opts',box),fb=$('.fb',box),id=host.dataset.quiz+qi;
    it.o.forEach(function(t,oi){var b=document.createElement('button');b.className='bt';b.type='button';b.innerHTML=t;b.onclick=function(){$$('button',ops).forEach(function(x){x.classList.remove('ok','no');});
      if(oi===it.a){b.classList.add('ok');fb.className='fb ok';fb.innerHTML='맞았어요. '+it.why;got[id]=1;}else{b.classList.add('no');fb.className='fb no';fb.innerHTML='힌트: '+it.hint;}upd();};ops.appendChild(b);});host.appendChild(box);});});
  var st=document.createElement('div');st.id='study';st.innerHTML='<span id="st-t"></span><button type="button" id="st-g">밑줄: 핵심</button>';document.body.appendChild(st);
  $('#st-g').onclick=function(){glMode=glMode==='core'?'all':glMode==='all'?'off':'core';this.textContent='밑줄: '+{core:'핵심',all:'전체',off:'끄기'}[glMode];mark();};
  var pr=document.createElement('div');pr.id='prog';document.body.appendChild(pr);
  function upd(){var h=document.documentElement,p=h.scrollTop/Math.max(1,h.scrollHeight-h.clientHeight);pr.style.width=(p*100).toFixed(1)+'%';$('#st-t').textContent='읽은 곳 '+Math.round(p*100)+'% · 퀴즈 '+Object.keys(got).length+'/'+nQ;}
  window.addEventListener('scroll',upd,{passive:true});upd();}

/* ── 색: 낮은 곳 남청 → 청록 → 연두 → 노랑 → 빨강 ── */
var STOPS=[[0,[29,59,107]],[.25,[47,143,166]],[.45,[79,195,201]],[.65,[155,226,176]],[.82,[241,182,70]],[1,[240,96,77]]];
function cmap(t,a){t=clamp(t,0,1);for(var i=1;i<STOPS.length;i++){if(t<=STOPS[i][0]){var s0=STOPS[i-1],s1=STOPS[i],u=(t-s0[0])/(s1[0]-s0[0]);var c=s0[1].map(function(v,j){return Math.round(v+(s1[1][j]-v)*u);});return 'rgba('+c[0]+','+c[1]+','+c[2]+','+(a==null?1:a)+')';}}return 'rgb(240,96,77)';}

/* ── 3D 지형 (Canvas 2D, 외부 라이브러리 없음) ──
   좌표: 가로축 x(=w₁), 세로축 y(=w₂), 높이 z(=오차). 화면은 끌어서 돌린다. */
function Surf3D(cv,o){var S=this;S.cv=cv;S.o=o;S.yaw=o.yaw==null?-0.75:o.yaw;S.pitch=o.pitch==null?0.62:o.pitch;S.ov=[];S.dirty=true;S.sel=null;
  S.setF(o.f,o.xr,o.yr,o.zr);
  var drag=null;cv.addEventListener('pointerdown',function(e){drag={x:e.clientX,y:e.clientY,yaw:S.yaw,pitch:S.pitch,moved:false};cv.setPointerCapture(e.pointerId);cv.style.cursor='grabbing';});
  cv.addEventListener('pointermove',function(e){if(!drag)return;var dx=e.clientX-drag.x,dy=e.clientY-drag.y;if(Math.abs(dx)+Math.abs(dy)>3)drag.moved=true;S.yaw=drag.yaw+dx*0.008;S.pitch=clamp(drag.pitch+dy*0.006,0.08,1.5);S.dirty=true;});
  function up(e){if(drag&&!drag.moved&&S.o.onPick){var r=cv.getBoundingClientRect();S.o.onPick(S.pick(e.clientX-r.left,e.clientY-r.top));}drag=null;cv.style.cursor='grab';}
  cv.addEventListener('pointerup',up);cv.addEventListener('pointercancel',function(){drag=null;});
  cv.setAttribute('role','img');cv.tabIndex=0;
  cv.addEventListener('keydown',function(e){var k=e.key,d=0.12;if(k==='ArrowLeft')S.yaw-=d;else if(k==='ArrowRight')S.yaw+=d;else if(k==='ArrowUp')S.pitch=clamp(S.pitch+d,0.08,1.5);else if(k==='ArrowDown')S.pitch=clamp(S.pitch-d,0.08,1.5);else return;e.preventDefault();S.dirty=true;});
  if(o.views!==false&&cv.parentNode){var vb=document.createElement('div');vb.className='vbtns';vb.setAttribute('role','group');vb.setAttribute('aria-label','3D 시점 바꾸기');
    [['비스듬히',-0.75,0.62],['하늘에서',0,1.5],['낮게',-0.9,0.22],['왼쪽으로 돌리기','L'],['오른쪽으로 돌리기','R']].forEach(function(v){var b=document.createElement('button');b.type='button';b.className='bt';b.textContent=v[0];
      b.onclick=function(){if(v[1]==='L')S.yaw-=0.35;else if(v[1]==='R')S.yaw+=0.35;else{S.yaw=v[1];S.pitch=v[2];}S.dirty=true;};vb.appendChild(b);});
    var tip=document.createElement('span');tip.className='glabel';tip.style.alignSelf='center';tip.textContent='· 그림을 누른 뒤 화살표 키로도 돌릴 수 있어요';vb.appendChild(tip);
    var host=cv.parentNode.closest('.twin')||cv.parentNode;if(host.nextElementSibling&&host.nextElementSibling.classList.contains('vbtns-wrap'))host=host.nextElementSibling;var w=document.createElement('div');w.className='vbtns-wrap';w.appendChild(vb);host.insertAdjacentElement('afterend',w);}
  reg(cv,function(dt){if(S.o.onTick)S.o.onTick(dt);if(S.dirty||dt===0){S.draw();S.dirty=false;}});}
Surf3D.prototype.setF=function(f,xr,yr,zr){var S=this,n=S.o.n||30;S.f=f;S.xr=xr||S.xr;S.yr=yr||S.yr;S.n=n;var Z=[],mn=Infinity,mx=-Infinity;
  for(var j=0;j<=n;j++){var row=[];for(var i=0;i<=n;i++){var x=S.xr[0]+(S.xr[1]-S.xr[0])*i/n,y=S.yr[0]+(S.yr[1]-S.yr[0])*j/n,z=f(x,y);if(!isFinite(z))z=NaN;row.push(z);if(isFinite(z)){mn=Math.min(mn,z);mx=Math.max(mx,z);}}Z.push(row);}
  S.Z=Z;S.zr=zr||[mn,mx];if(S.zr[1]-S.zr[0]<1e-9)S.zr=[S.zr[0]-1,S.zr[1]+1];S.dirty=true;};
Surf3D.prototype.nz=function(z){var r=this.zr;return clamp((z-r[0])/(r[1]-r[0]),-0.05,1.15);};
Surf3D.prototype.P=function(x,y,z){var S=this,X=(x-S.xr[0])/(S.xr[1]-S.xr[0])*2-1,Y=(y-S.yr[0])/(S.yr[1]-S.yr[0])*2-1,Zh=(S.nz(z)-0.5)*(S.o.zs||1.1);
  var c=Math.cos(S.yaw),s=Math.sin(S.yaw),rx=X*c-Y*s,ry=X*s+Y*c;var cp=Math.cos(S.pitch),sp=Math.sin(S.pitch);
  /* 화면 y: 높을수록 위, 멀수록 위 · 깊이: 멀고 낮을수록 큼 */
  return [S.cx+rx*S.sc,S.cy+(-Zh*cp-ry*sp)*S.sc,ry*cp-Zh*sp];};
Surf3D.prototype.P0=function(x,y){return this.P(x,y,this.zr[0]-(this.zr[1]-this.zr[0])*0.0);};
Surf3D.prototype.draw=function(){var S=this,R=setup(S.cv),g=R.g,w=R.w,h=R.h;S.w=w;S.h=h;S.cx=w/2;S.cy=h*0.53;S.sc=Math.min(w*0.34,h*0.40)*(S.o.zoom||1);grid24(g,w,h);
  var n=S.n,Z=S.Z,pts=[],i,j;for(j=0;j<=n;j++){var row=[];for(i=0;i<=n;i++){var x=S.xr[0]+(S.xr[1]-S.xr[0])*i/n,y=S.yr[0]+(S.yr[1]-S.yr[0])*j/n;row.push(isFinite(Z[j][i])?S.P(x,y,Math.min(Z[j][i],S.zr[1]+(S.zr[1]-S.zr[0])*.15)):null);}pts.push(row);}
  /* 바닥: 등고선 지도(그림자) */
  var fl=S.o.floor!==false;if(fl){for(j=0;j<n;j++)for(i=0;i<n;i++){var zz=(Z[j][i]+Z[j][i+1]+Z[j+1][i]+Z[j+1][i+1])/4;if(!isFinite(zz))continue;var x0=S.xr[0]+(S.xr[1]-S.xr[0])*i/n,x1=S.xr[0]+(S.xr[1]-S.xr[0])*(i+1)/n,y0=S.yr[0]+(S.yr[1]-S.yr[0])*j/n,y1=S.yr[0]+(S.yr[1]-S.yr[0])*(j+1)/n;
      var a=S.P(x0,y0,S.zr[0]),b=S.P(x1,y0,S.zr[0]),c=S.P(x1,y1,S.zr[0]),d=S.P(x0,y1,S.zr[0]);var lv=S.nz(zz);g.fillStyle=cmap(lv,0.28);g.beginPath();g.moveTo(a[0],a[1]);g.lineTo(b[0],b[1]);g.lineTo(c[0],c[1]);g.lineTo(d[0],d[1]);g.closePath();g.fill();}
    if(S.o.contours!==false){var levels=S.o.levels||12;g.lineWidth=1;for(var L=1;L<levels;L++){var zl=S.zr[0]+(S.zr[1]-S.zr[0])*Math.pow(L/levels,S.o.cpow||1.6);g.strokeStyle=cmap(L/levels,0.55);g.beginPath();
      for(j=0;j<n;j++)for(i=0;i<n;i++){var q=[Z[j][i],Z[j][i+1],Z[j+1][i+1],Z[j+1][i]],P2=[[i,j],[i+1,j],[i+1,j+1],[i,j+1]],seg=[];for(var e=0;e<4;e++){var za=q[e],zb=q[(e+1)%4];if((za-zl)*(zb-zl)<0){var u=(zl-za)/(zb-za),pa=P2[e],pb=P2[(e+1)%4];seg.push([pa[0]+(pb[0]-pa[0])*u,pa[1]+(pb[1]-pa[1])*u]);}}
        if(seg.length>=2){var s0=S.P(S.xr[0]+(S.xr[1]-S.xr[0])*seg[0][0]/n,S.yr[0]+(S.yr[1]-S.yr[0])*seg[0][1]/n,S.zr[0]),s1=S.P(S.xr[0]+(S.xr[1]-S.xr[0])*seg[1][0]/n,S.yr[0]+(S.yr[1]-S.yr[0])*seg[1][1]/n,S.zr[0]);g.moveTo(s0[0],s0[1]);g.lineTo(s1[0],s1[1]);}}g.stroke();}}}
  /* 축 */
  var ax=S.o.axes||['w₁','w₂','오차'],o0=S.P(S.xr[0],S.yr[0],S.zr[0]),ex=S.P(S.xr[1],S.yr[0],S.zr[0]),ey=S.P(S.xr[0],S.yr[1],S.zr[0]),ez=S.P(S.xr[0],S.yr[0],S.zr[1]);
  arrow2(g,o0[0],o0[1],ex[0],ex[1],cssv('--eye'),1.5);arrow2(g,o0[0],o0[1],ey[0],ey[1],cssv('--terrain'),1.5);arrow2(g,o0[0],o0[1],ez[0],ez[1],'rgba(27,29,43,.6)',1.5);
  /* 곡면: 먼 칸부터 */
  if(S.o.surface!==false){var quads=[];for(j=0;j<n;j++)for(i=0;i<n;i++){var A=pts[j][i],B=pts[j][i+1],C=pts[j+1][i+1],D=pts[j+1][i];if(!A||!B||!C||!D)continue;var z4=(Z[j][i]+Z[j][i+1]+Z[j+1][i+1]+Z[j+1][i])/4;quads.push([(A[2]+B[2]+C[2]+D[2])/4,A,B,C,D,z4]);}
    quads.sort(function(a,b){return b[0]-a[0];});var al=S.o.alpha==null?0.86:S.o.alpha;g.lineWidth=0.6;
    quads.forEach(function(q){g.beginPath();g.moveTo(q[1][0],q[1][1]);g.lineTo(q[2][0],q[2][1]);g.lineTo(q[3][0],q[3][1]);g.lineTo(q[4][0],q[4][1]);g.closePath();g.fillStyle=cmap(S.nz(q[5]),al);g.fill();g.strokeStyle='rgba(27,29,43,.22)';g.stroke();});}
  label(g,ex[0]+6,ex[1],ax[0],cssv('--eye'));label(g,ey[0]+6,ey[1],ax[1],cssv('--terrain'));label(g,ez[0]+6,ez[1]-4,ax[2],cssv('--text'));
  /* 덧그림 */
  S.ov.forEach(function(fn){fn(g,S);});
  if(S.o.stamp)stamp(g,w,S.o.stamp);
  if(S.o.aria)S.cv.setAttribute('aria-label',S.o.aria);};
Surf3D.prototype.line3=function(g,pts,col,wd,dash){var S=this;g.strokeStyle=col;g.lineWidth=wd||2;g.setLineDash(dash||[]);g.beginPath();pts.forEach(function(p,k){var q=S.P(p[0],p[1],p[2]);k?g.lineTo(q[0],q[1]):g.moveTo(q[0],q[1]);});g.stroke();g.setLineDash([]);};
Surf3D.prototype.dot3=function(g,x,y,z,col,r,ring){var q=this.P(x,y,z);g.beginPath();g.arc(q[0],q[1],r||5,0,7);g.fillStyle=col;g.fill();if(ring!==false){g.lineWidth=1.8;g.strokeStyle='#ffffff';g.stroke();}return q;};
Surf3D.prototype.arrow3=function(g,a,b,col,wd){var p=this.P(a[0],a[1],a[2]),q=this.P(b[0],b[1],b[2]);arrow2(g,p[0],p[1],q[0],q[1],col,wd||2.4);return q;};
/* 화면 좌표 → 바닥 위 (x,y) 근사: 바닥 격자에서 가장 가까운 점 */
Surf3D.prototype.pick=function(px,py){var S=this,best=null,bd=1e9,n=40;for(var j=0;j<=n;j++)for(var i=0;i<=n;i++){var x=S.xr[0]+(S.xr[1]-S.xr[0])*i/n,y=S.yr[0]+(S.yr[1]-S.yr[0])*j/n,z=S.f(x,y);var q=S.P(x,y,isFinite(z)?Math.min(z,S.zr[1]):S.zr[0]);var d=(q[0]-px)*(q[0]-px)+(q[1]-py)*(q[1]-py);if(d<bd){bd=d;best=[x,y];}}return best;};
Surf3D.prototype.view=function(yaw,pitch){this.yaw=yaw;this.pitch=pitch;this.dirty=true;};

/* ── 2D 선 그래프 ──
   o={xr,yr,logx,logy,series:[{pts:[[x,y]],color,width,dash,dots}],vlines:[{x,color,label,dash}],hlines:[...],xl,yl,stamp,xt:[...],yt:[...]} */
function plot(cv,o){var R=setup(cv),g=R.g,w=R.w,h=R.h,Lm=46,Rm=14,T=20,B=34,W=w-Lm-Rm,H=h-T-B;grid24(g,w,h);
  var tx=function(v){return o.logx?Math.log10(Math.max(v,1e-12)):v;},ty=function(v){return o.logy?Math.log10(Math.max(v,1e-12)):v;};
  var x0=tx(o.xr[0]),x1=tx(o.xr[1]),y0=ty(o.yr[0]),y1=ty(o.yr[1]);
  var X=function(v){return Lm+(tx(v)-x0)/(x1-x0)*W;},Y=function(v){return T+H-(clamp(ty(v),y0-.02*(y1-y0),y1+.02*(y1-y0))-y0)/(y1-y0)*H;};
  g.strokeStyle=cssv('--rule');g.lineWidth=1;g.beginPath();g.moveTo(Lm,T);g.lineTo(Lm,T+H);g.lineTo(Lm+W,T+H);g.stroke();
  g.fillStyle=cssv('--muted');g.font='11.5px '+cssv('--font');g.textAlign='center';(o.xt||[]).forEach(function(t){var px=X(t);g.fillRect(px,T+H,1,4);g.fillText(o.xf?o.xf(t):String(t),px,T+H+16);});
  g.textAlign='right';g.textBaseline='middle';(o.yt||[]).forEach(function(t){var py=Y(t);g.fillRect(Lm-4,py,4,1);g.fillText(o.yf?o.yf(t):String(t),Lm-7,py);});g.textBaseline='alphabetic';
  if(o.xl){g.textAlign='right';g.fillText(o.xl,Lm+W,h-4);} if(o.yl){g.textAlign='left';g.fillText(o.yl,4,12);}
  (o.hlines||[]).forEach(function(l){var py=Y(l.y);g.strokeStyle=l.color;g.setLineDash(l.dash||[4,4]);g.beginPath();g.moveTo(Lm,py);g.lineTo(Lm+W,py);g.stroke();g.setLineDash([]);if(l.label){if(l.left)label(g,Lm+8,py-11,l.label,l.color,'left');else label(g,Lm+W-4,py-11,l.label,l.color,'right');}});
  (o.vlines||[]).forEach(function(l){var px=X(l.x);g.strokeStyle=l.color;g.setLineDash(l.dash||[4,4]);g.beginPath();g.moveTo(px,T);g.lineTo(px,T+H);g.stroke();g.setLineDash([]);if(l.label){if(px>Lm+W*0.72)label(g,px-6,T+10+(l.dy||0),l.label,l.color,'right');else label(g,px+6,T+10+(l.dy||0),l.label,l.color);}});
  (o.series||[]).forEach(function(s){g.strokeStyle=s.color;g.lineWidth=s.width||2;g.setLineDash(s.dash||[]);g.beginPath();var st=false;s.pts.forEach(function(p){if(!isFinite(p[1])){st=false;return;}var px=X(p[0]),py=Y(p[1]);st?g.lineTo(px,py):g.moveTo(px,py);st=true;});g.stroke();g.setLineDash([]);
    if(s.dots)s.pts.forEach(function(p){if(!isFinite(p[1]))return;g.beginPath();g.arc(X(p[0]),Y(p[1]),s.dots,0,7);g.fillStyle=s.color;g.fill();});
    if(s.name){var lp=s.pts[s.pts.length-1];if(lp&&isFinite(lp[1]))label(g,clamp(X(lp[0])-4,Lm+40,Lm+W-4),clamp(Y(lp[1])+(s.ndy||-12),T+8,T+H-8),s.name,s.color,'right');}});
  if(o.stamp)stamp(g,w,o.stamp);if(o.aria)cv.setAttribute('aria-label',o.aria);return {X:X,Y:Y,g:g,w:w,h:h};}

/* ── 대결 (6-2): 결과 보기 전에는 승패를 짐작할 수 없는 표정만 ── */
function Duel(o){var host=$(o.el),pred=null;
  $$('[data-pred]',host).forEach(function(b){b.onclick=function(){pred=b.dataset.pred;$$('[data-pred]',host).forEach(function(x){x.setAttribute('aria-pressed',String(x===b));});};});
  var res=$('.duel-res',host),go=$('[data-go]',host),close=$('[data-close]',host);
  go.onclick=function(){var r=o.run();res.hidden=false;o.show(r,pred);go.hidden=true;close.hidden=false;};
  close.onclick=function(){res.hidden=true;go.hidden=false;close.hidden=true;o.reset&&o.reset();};}

return {$:$,$$:$$,esc:esc,cssv:cssv,reduce:reduce,fmt:fmt,clamp:clamp,spr:spr,say:say,dialogues:dialogues,fillImgs:fillImgs,setMood:setMood,reg:reg,start:start,drawAll:drawAll,setup:setup,grid24:grid24,stamp:stamp,label:label,arrow2:arrow2,btns:btns,ins:ins,Gloss:Gloss,Study:Study,cmap:cmap,Surf3D:Surf3D,plot:plot,Duel:Duel,NAMES:NAMES};
})();
