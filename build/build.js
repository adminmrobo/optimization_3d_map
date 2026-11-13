// 페이지 조립: node build/build.js
// p{N}.src.html + common.css + 캐릭터 그림 + labmath.js + common.js (+ deep.json) → 단일 HTML
// 그다음 꼬리표 조립기(ahnboat_lab_explainer/packs/task/onto-retrofit/tools/assembler.html)의 build()와 같은 방식으로
// 지식 색인(#kg)·온톨로지·서지 꾸러미(#export)와 데이터 블록 네 개를 붙인다.
const fs=require('fs'),path=require('path'),vm=require('vm');
const B=__dirname,R=path.join(B,'..');
const rd=f=>fs.readFileSync(path.join(B,f),'utf8');
const css=rd('common.css'),sprites=rd('sprites96.js'),labmath=rd('labmath.js'),common=rd('common.js'),kgx=rd('kgx.js');
const BB=JSON.parse(rd('backbone.json'));
// KGX.toJsonLd를 쓰려고 브라우저 없이 모듈을 띄운다
const ctx={document:{readyState:'loading',addEventListener(){},getElementById(){return null;}},window:{},navigator:{},console};
vm.createContext(ctx);vm.runInContext(kgx+';this.KGX=KGX;',ctx);
const MK={head:['<!-- lab-kg:head -->','<!-- /lab-kg:head -->'],body:['<!-- lab-kg:body -->','<!-- /lab-kg:body -->'],script:['<!-- lab-kg:script -->','<!-- /lab-kg:script -->']};
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const js=o=>JSON.stringify(o).replace(/<\//g,'<\\/');
const sec=(i,t,sub,m)=>'<section class="kgx kgx-sec" id="'+i+'"><div class="kgx-wrap">\n<h2>'+t+'</h2>\n<p class="kgx-sub">'+sub+'</p>\n<div id="'+m+'"></div>\n</div></section>\n';
function attach(H,kg,refs,meta){
  kg=JSON.parse(JSON.stringify(kg));kg.topicLabels={};BB.nodes.forEach(n=>{kg.topicLabels[n.id]=n.label.ko;});
  const ld=ctx.KGX.toJsonLd(kg,meta),t=meta.title||'';
  const head=['<meta name="citation_title" content="'+esc(t)+'">','<meta name="dc.title" content="'+esc(t)+'">','<meta name="dc.date" content="'+esc(meta.date||'')+'">','<meta name="dc.language" content="ko">','<meta name="dc.type" content="InteractiveResource">'];
  (meta.creator||[]).forEach(c=>{if(c.name)head.push('<meta name="citation_author" content="'+esc(c.name)+'">');});
  if(meta.series)head.push('<meta name="dcterms.isPartOf" content="'+esc(meta.series)+'">');
  refs.forEach(r=>{if(r.DOI)head.push('<meta name="dc.source" content="doi:'+esc(r.DOI)+'">');});
  const bh=MK.head[0]+'\n'+head.join('\n')+'\n'+MK.head[1]+'\n';
  const body=MK.body[0]+'\n'+sec('kg','지식 색인 — 이 페이지에서 찾아보기','이 페이지에 나온 개념, 방법, 주장, 비유, 열린 질문을 한곳에 모았다. 검색하고, 항목을 눌러 이웃 관계를 보고, "설명 보러 가기"로 본문에 돌아간다.','kg-mount')+
    sec('export','온톨로지·서지 꾸러미 — 이 페이지의 지식을 가져가기','지식 색인을 출처와 함께 파일로 내려받는다. Zotero(BibTeX·RIS), Protégé(Turtle), Neo4j·Gephi(CSV), 여러 페이지 합치기(kg.json)에 쓴다.','export-mount')+
    '<script type="application/json" id="kg-raw">'+js(kg)+'</'+'script>\n<script type="application/ld+json" id="kg-ld">'+js(ld)+'</'+'script>\n'+
    '<script type="application/json" id="refs-csl">'+js(refs)+'</'+'script>\n<script type="application/json" id="page-meta">'+js(meta)+'</'+'script>\n'+MK.body[1]+'\n';
  const sc=MK.script[0]+'\n<script>\n'+kgx+'\n</'+'script>\n'+MK.script[1]+'\n';
  H=H.replace('</head>',bh+'</head>');
  let i=H.lastIndexOf('<footer'),j=H.lastIndexOf('</body>'),p=(i>=0&&i<j)?i:j;H=H.slice(0,p)+body+H.slice(p);
  j=H.lastIndexOf('</body>');H=H.slice(0,j)+sc+H.slice(j);return H;}
const pages=[['p0.src.html','index.html','0'],['p1.src.html','1_math_map.html','1'],['p2.src.html','2_experiment_lab.html','2']];
for(const [src,out,n] of pages){
  if(!fs.existsSync(path.join(B,src)))continue;
  let H=rd(src).replace('<!--@@CSS@@-->','<style>\n'+css+'\n</style>')
    .replace('/*@@SPRITES@@*/',()=>n==='0'?rd('sprites_index.js'):sprites).replace('/*@@LABMATH@@*/',()=>labmath).replace('/*@@COMMON@@*/',()=>common)
    .replace('/*@@DEEP@@*/',()=>fs.existsSync(path.join(B,'deep.json'))?rd('deep.json'):'null');
  const kf=path.join(B,'kg_'+n+'.json');
  if(fs.existsSync(kf))H=attach(H,JSON.parse(fs.readFileSync(kf,'utf8')),JSON.parse(rd('refs_'+n+'.json')),JSON.parse(rd('meta_'+n+'.json')));
  fs.writeFileSync(path.join(R,out),H);console.log(out,(Buffer.byteLength(H)/1024).toFixed(0)+' KB');}
