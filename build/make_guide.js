// 강의자용 가이드의 퀴즈 정답표 부분을 페이지 원본에서 뽑는다: node build/make_guide.js > build/answer_key.md
const fs=require('fs');const out=[];
for(const [f,name] of [['build/p1.src.html','1편 수학 편'],['build/p2.src.html','2편 실험실 편']]){
  const s=fs.readFileSync(f,'utf8');const i=s.indexOf('U.Study({quiz:');const j=s.indexOf('\n}});',i);
  const Q=eval('('+s.slice(i+'U.Study({quiz:'.length,j+2)+')');let qn=0;out.push(`### ${name}\n\n| 칸 | 문제 | 정답(화면 위치) | 왜 |\n|---|---|---|---|`);
  for(const k of Object.keys(Q))for(const it of Q[k]){const n=it.o.length,tgt=(qn++*2+1)%n;
    const strip=x=>x.replace(/<[^>]+>/g,'').replace(/\|/g,'/');out.push(`| ${k} | ${strip(it.q)} | ${'①②③④'[tgt]} ${strip(it.o[it.a])} | ${strip(it.why)} |`);}
  out.push('');}
process.stdout.write(out.join('\n'));
