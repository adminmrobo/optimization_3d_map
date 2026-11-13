# 표지 지시문 — 좌표축 위의 그릇 (목차 · 1편 · 2편)

세 장 모두 지금은 대체 표지(코드로 그린 등고선 + 캐릭터 그림)로 나갑니다. 연구실 스킬 v1.14의 "낮의 연구실" 기준(시즌 구절, 장소 표, 표지 조립 순서)을 따릅니다. 밤·어둠·네온 불빛 같은 말은 넣지 않습니다. 그림을 받으면 ai-lab-explainer 18-15 절차로 `data-img="cover_index"`, `cover_01`, `cover_02` 자리에 넣고 `cover_manifest.json`의 `status`를 고칩니다.

**참고 이미지 (세 장 모두 함께 올리기):** 네 캐릭터 기본 그림 — GitHub `adminmrobo/fruitfly-lab-expressions`의 박사·조수·초파리 연구원·주판봇 기본 표정(E13), 목차 표지는 인턴 시아·모아(E13)도.

---

## 0. 목차 — `cover_index`

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_index · L (16:9, 1920 이상) |
| 장소 (앵커) | B 연구실 — 낮의 연구실 전경(큰 창, 흰 벽), 바닥 전체에 은은하게 빛나는 등고선 지도 |
| 주제 은유 | 연구실 바닥에서 솟아오른 반투명 그릇 모양 지형(격자 무늬), 바닥 가운데에 작은 초록 빛점 |
| 네 캐릭터 포즈 | 박사: 가운데 뒤에서 지형을 손바닥으로 가리킴 / 조수: 오른쪽 옆에서 클립보드를 들고 지형을 내려다봄 / 초파리: 왼쪽에서 오른쪽을 보며 지형 가장자리에 쪼그려 앉아 관찰 / 주판봇: 오른쪽에서 왼쪽을 보며 주판을 들고 있음 · 인턴 시아·모아는 뒤쪽 양옆에 작게 |
| 대체 글 (alt) | 연구실 바닥에 솟은 빛나는 그릇 모양 오차 지형을 연구실 식구들이 둘러싸고 바라보는 장면 |
| 앞 표지와 다른 점 | 시리즈 첫 표지 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 캐릭터(박사, 조수, 초파리 연구원, 주판봇, 인턴 둘)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a wide bright daytime laboratory with large windows; the whole floor glows softly with concentric contour lines like a topographic map.
All four characters together:
chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, standing at the center back and presenting the terrain with an open palm;
girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, standing at the right side holding a clipboard and looking down at the terrain;
anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, crouching at the edge of the terrain and observing closely;
boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left.
Two small maid interns in the background: one calm girl with long straight jet-black hair, no headdress, charcoal-black maid dress with large gray bow; one gentle girl with long ash-beige wavy hair, white frilled maid headband, camel cardigan, holding a pink teacup.
Visual metaphor of the topic: a translucent bowl-shaped terrain with a glowing grid rising from the floor, one small green light at the lowest point of the bowl.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the bowl-shaped terrain.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때:** `Same characters, same art style and composition. Change only: {고칠 점}. Still no text.`

---

## 1. 1편 수학 편 — `cover_01`

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_01 · L (16:9, 1920 이상) |
| 장소 (앵커) | D 생활 — 낮의 연구실 탁자 위 커다란 지형 모형(산과 지도), 연보라 시험관 받침을 한쪽에 둬 시리즈 표식 유지 |
| 주제 은유 | 말안장(감자칩) 모양의 빛나는 곡면 모형 위에 꽂힌 작은 흰 깃대 하나, 깃대의 초록 그림자가 내리막 쪽으로 뻗음 |
| 네 캐릭터 포즈 | 박사: 가운데 뒤에서 깃대를 가리킴 / 조수: 오른쪽에서 곡면을 칼로 자른 단면 판(빛나는 곡선)을 들어 보임 / 초파리: 왼쪽에서 오른쪽을 보며 안장 가운데 평평한 곳을 손가락으로 짚고 의심하는 표정 / 주판봇: 오른쪽에서 왼쪽을 보며 주판을 들고 자신만만 |
| 대체 글 (alt) | 말안장 모양의 지형 모형에 꽂힌 깃대와 그림자를 연구실 식구 넷이 살펴보는 장면 |
| 앞 표지와 다른 점 | 목차는 그릇 지형·바닥 등고선, 1편은 탁자 위 안장 모형·깃대·단면 판 |

**영어 프롬프트 (Genspark 안내 문구는 목차와 같음)**
```
Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a wide bright daytime laboratory with large windows; a large table in the middle holds a glowing terrain model.
All four characters together:
chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the center back pointing at a small white flagpole;
girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, on the right holding up a thin glowing cross-section plate shaped like a curve;
anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, touching the flat center of the saddle with one finger, doubtful look;
boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, confident.
Visual metaphor of the topic: a saddle-shaped (curved potato crisp shaped) glowing surface model with a fine grid; a small white flagpole stands perpendicular to the surface and its soft green shadow stretches downhill.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the flagpole and the saddle.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

---

## 2. 2편 실험실 편 — `cover_02`

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_02 · L (16:9, 1920 이상) |
| 장소 (앵커) | B 연구실 — 낮의 연구실 실험대, 벽의 화이트보드는 비워 둠(글자 없음) |
| 주제 은유 | 실험대 위 큰 그릇 모형 안으로 빛나는 공 세 개(빨강·분홍·초록)가 서로 다른 궤적으로 굴러 내려감, 옆에 작은 카드 더미 |
| 네 캐릭터 포즈 | 박사: 가운데 뒤에서 팔짱 끼고 지켜봄 / 조수: 오른쪽에서 초시계를 들고 공을 굴릴 준비 / 초파리: 왼쪽에서 오른쪽을 보며 카드 몇 장만 손에 쥐고 작은 초록 공을 가리킴 / 주판봇: 오른쪽에서 왼쪽을 보며 카드 더미 전체를 팔에 안고 빨간 공 쪽을 봄 · 인턴 시아는 신호 깃발, 모아는 응원 |
| 대체 글 (alt) | 실험대 위 그릇 모형에 공 세 개가 굴러 내려가고 연구실 식구들이 결과를 기다리는 장면 |
| 앞 표지와 다른 점 | 목차는 바닥 지형, 1편은 안장 모형·깃대, 2편은 실험대·공 세 개·카드 더미 |

**영어 프롬프트**
```
Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a wide bright daytime laboratory with large windows; an experiment bench in front with a large bowl-shaped terrain model; a blank whiteboard on the back wall (nothing written on it).
All four characters together:
chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the center back with arms folded, watching;
girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, on the right holding a stopwatch, ready to start;
anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, holding only a few small blank cards and pointing at a small green ball;
boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left, hugging a tall stack of blank cards and looking at a red ball.
Two small maid interns at the sides: a calm girl with long straight jet-black hair holding a small signal flag; a gentle girl with ash-beige wavy hair and white frilled headband cheering with a fist.
Visual metaphor of the topic: three glowing balls (red, pink, green) rolling down into the bowl along three different paths, the green one zigzagging, the red one smooth.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the bowl and the three balls.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```
