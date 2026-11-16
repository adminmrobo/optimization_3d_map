# Genspark 그림 지시문 — 최적화 첫걸음 ("혹시… 미분 좋아하세요?")

> **받음 (2026-11-16):** 표지 2장·프롤로그 3컷·카드 썸네일 1장을 반영했습니다. 저장소 `img/fs_cover_01·02(.webp, _960)`, `img/fs_prologue_1~3(.webp, _600)`, `img/fs_thumb.webp`. 말풍선 대사는 HTML 글자로 얹었습니다. 같은 그림이 캐릭터 저장소 fruitfly-lab-expressions의 `images/scenes/optimization_first_step/`에도 있습니다.

## 공통 규칙

- **참고 이미지:** fruitfly-lab-expressions의 캐릭터 그림만 첨부합니다. 장면마다 표정 E번호를 고릅니다(specs/README.md).
- **화풍:** 시리즈와 같은 밝은 낮 연구실 화풍을 씁니다.
- **패러디 범위:** "OO 좋아하세요?" 패러디는 **대사 형식과 상반신 + 말풍선 구도만** 빌립니다. 원작 만화 장면은 Genspark에 참고 이미지로 넣지 않습니다. 원작 인물의 외모·교복·리본도 쓰지 않습니다. 하루·시아·모아는 각자의 원래 모습 그대로 그립니다.
- **말풍선:** 그림 생성기는 한글 글자를 잘 그리지 못하므로 말풍선은 **비워 두게** 합니다. 대사("혹시… 미분 좋아하세요?" 등)는 HTML에서 글자로 얹습니다.
- **파일:** 표지는 L(16:9, 1920 이상), 프롤로그 컷은 4:3입니다. 받은 그림은 optimization_3d_map 저장소의 img/에 webp로 넣습니다. 지금 페이지에는 그림판 표지와 연구실 식구 기본 그림으로 꾸민 프롤로그 세 컷이 임시로 들어 있습니다(그림을 받으면 `.panel3` 안의 img를 바꿈).

| 키 | 쓰는 곳 | 판 |
|---|---|---|
| fs_cover_01 | 최적화 첫걸음 ① 표지 (first_step_1.html) | 16:9 |
| fs_cover_02 | 최적화 첫걸음 ② 표지 (first_step_2.html) | 16:9 |
| fs_prologue_1~3 | 프롤로그 세 컷 (하루·시아·모아) | 4:3 |
| card | ahnboat.xyz SPECIAL 카드 띠 그림 (확률 분포 도감 옆) | 16:9로 만들어 띠 비율로 자름 |

---

## 1. fs_cover_01 — 최적화 첫걸음 ① 표지

| 항목 | 내용 |
|---|---|
| 장면 | 낮의 연구실 칠판 앞. 하루가 수줍게 웃으며 고개를 살짝 기울여 묻는 상반신, 양옆에 빈 말풍선 두 개 |
| 주제 은유 | 칠판에 그려진 언덕 모양 곡선과 그 꼭대기에 닿은 수평 접선(빛나는 선), 곡선 위를 미끄러지는 작은 접선 자 |
| 뒤쪽 | 시아(왼쪽 뒤, 손을 들고 다음 질문 대기), 모아(오른쪽 뒤, 노트를 안고 반짝이는 눈) |
| 대체 글 | 칠판의 언덕 곡선 앞에서 하루가 미분을 좋아하느냐고 묻는 장면 |

**영어 프롬프트**
```
Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Bright daytime laboratory mood, soft natural sunlight, clean white walls, light lavender, mint and pink accents.
Scene: in front of a large chalkboard in a bright laboratory, a bust shot in the style of a manga panel with two EMPTY speech bubbles on the left and right (no text inside).
Main character: girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, smiling shyly with a light blush, head slightly tilted, as if asking a gentle question.
Behind her on the left: a calm girl intern with long straight jet-black hair, charcoal-black maid dress with large gray bow, raising one hand, waiting to ask next.
Behind her on the right: a gentle girl intern with long ash-beige wavy hair, white frilled maid headband, camel cardigan, hugging a notebook with sparkling eyes.
Visual metaphor: on the chalkboard a smooth hill-shaped curve with a glowing horizontal tangent line touching its top, and a small ruler-shaped tangent sliding along the curve.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain and bright.
Mood: shy, warm, curious — the moment right before a question.
No text, no letters, no numbers, no logos, no school uniform, no ribbon bow tie, no weapons, no real brands.
```

---

## 2. fs_cover_02 — 최적화 첫걸음 ② 표지

| 항목 | 내용 |
|---|---|
| 장면 | 낮의 작은 공장 모형(디오라마) 위. 작업자 인형들(노동), 기계 몇 대(자본), 출구에서 나오는 상자(제품) |
| 주제 은유 | 동전 두 줄기(임금·이자)가 작업자와 기계로 흘러감, 공장 위 공중에 두 곡선(오르는 곡선과 내려오는 곡선)이 만나는 빛나는 점 |
| 네 캐릭터 | 박사: 가운데 뒤에서 공장을 내려다봄 / 모아: 앞쪽에서 손을 들고 "얼마나 만들까요?" 표정(빈 말풍선) / 초파리: 왼쪽에서 오른쪽을 보며 두 곡선이 만나는 점을 가리킴 / 주판봇: 오른쪽에서 왼쪽을 보며 주판을 들고 상자 더미를 끝없이 쌓으려 함 |
| 대체 글 | 작은 공장 모형 위에서 연구실 식구들이 얼마나 생산할지 따져 보는 장면 |

**영어 프롬프트**
```
Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Bright daytime laboratory mood, soft natural sunlight, clean white walls, light lavender, mint and pink accents.
Scene: on a large lab table stands a small factory diorama: tiny worker figures, a few small machines, and product boxes coming out of the exit; two thin streams of gold coins flow toward the workers and the machines.
Floating above the factory: two glowing curves, one rising and one falling, crossing at a bright point.
Characters:
chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the center back looking down at the factory;
a gentle girl intern with long ash-beige wavy hair, white frilled maid headband, camel cardigan, in front raising her hand with a curious face, an EMPTY speech bubble beside her;
anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, pointing at the crossing point of the two curves;
boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left, holding an abacus and stacking product boxes too high.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain and bright; light falls on the factory and the crossing point.
Mood: curious, friendly rivalry.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no real brands.
```

---

## 3. fs_prologue_1~3 — 프롤로그 세 컷 (4:3)

세 컷은 구도를 같게 맞춥니다. 상반신, 양옆에 빈 말풍선, 배경은 옅은 스크린톤 느낌의 연구실입니다. 인물만 바꿔 연달아 묻는 느낌을 냅니다.

| 키 | 인물 | 표정·동작 | HTML에서 얹을 대사 |
|---|---|---|---|
| fs_prologue_1 | 하루 | 수줍은 미소, 고개 기울임 | "혹시…" / "미분 좋아하세요?" |
| fs_prologue_2 | 시아 | 차분하게 손가락 하나를 듦 | "그럼…" / "미분은 언제부터 있었어요?" |
| fs_prologue_3 | 모아 | 노트를 안고 반짝이는 눈 | "그걸로…" / "뭘 할 수 있어요?" |

**영어 프롬프트 (fs_prologue_1 — 인물 줄만 바꿔 2·3에 씀)**
```
Square-ish 4:3 illustration in the style of a single manga panel, matching the attached reference images exactly.
Bust shot, centered, with two EMPTY speech bubbles on the left and right (no text inside).
Light screentone-style background of a bright laboratory, soft daylight.
Character: girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, smiling shyly with a light blush, head slightly tilted.
No text, no letters, no numbers, no logos, no school uniform, no ribbon bow tie.
```
- fs_prologue_2 인물 줄: `calm girl intern, long straight jet-black hair, charcoal-black maid dress with large gray bow, raising one finger thoughtfully.`
- fs_prologue_3 인물 줄: `gentle girl intern, long ash-beige wavy hair, white frilled maid headband, camel cardigan, hugging a notebook with sparkling eyes.`

---

## 4. card — ahnboat.xyz SPECIAL 카드 띠 그림

옆 카드(확률 분포 도감·머신러닝 도감·신경망 도감)와 같은 모양으로 맞춥니다. 단색 띠 배경, 왼쪽 위 테두리 제목 상자, 오른쪽에 캐릭터와 소품을 둡니다. 띠 색은 분홍(하루 색)입니다. 제목 상자는 **비워 두고** "최적화 첫걸음" 글자는 다른 카드와 같은 방식으로 얹습니다.

```
Wide banner illustration for a website card, 16:9 (will be cropped to a short horizontal strip), matching the attached reference images exactly (16-bit RPG pixel art).
Flat solid dusty-pink background with subtle horizontal pixel stripes.
Top-left: an EMPTY rounded title box with a thick white outline (no text inside), leaving room for a title.
Right side: a girl researcher with long pink hair in two round buns and a navy streak, white lab coat over lavender hoodie, smiling shyly, holding up a small glowing ruler that touches the top of a hill-shaped curve drawn on a small easel board as a horizontal tangent line.
Keep the characters and props in the right 45% of the image; keep the lower-left area plain.
No text, no letters, no numbers, no logos.
```
