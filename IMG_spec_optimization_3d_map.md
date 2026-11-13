# 이미지 제작 명세서 — 좌표축 위의 그릇 (목차 · 1편 · 2편)

## 1. 그림체와 고정 외형
캐릭터 팩 `CHAR_lab4` 1.4 (fruitfly-lab-expressions @ 86d04ac). 18-3 그림체, 18-4 고정 외형을 그대로 따른다. 주판봇은 v2.

## 2. 필요한 그림 전체

| 키 | 판 | 쓰는 곳 | 상태 |
|---|---|---|---|
| `cover_index` | L | index.html 맨 위 | 새로 그림 — `COVER_PROMPTS_optimization_3d_map.md` 0번 |
| `cover_01` | L | 1_math_map.html 맨 위 | 새로 그림 — 같은 파일 1번 |
| `cover_02` | L | 2_experiment_lab.html 맨 위 | 새로 그림 — 같은 파일 2번 |
| 말풍선·등장인물·대결 머리 표정 41종 | A~D | 세 페이지 | 기본 팩에 있음 (새로 그리지 않음) |

페이지에 쓰는 표정 키: `doc_front` `doc_think` `doc_magic` `doc_judge` `doc_board` · `asst_smile` `asst_report` `asst_firm` `asst_spark` `asst_shock` `asst_proud` · `fly_point` `fly_magnify` `fly_arms` `fly_coffee` `fly_clip` `fly_type` · `robo_smile` `robo_coin` `robo_calc` `robo_happy` `robo_sigh` `robo_blush` `robo_wow` `robo_meh` · `sia_explain` `sia_signal` `sia_smile` `sia_doze` `sia_guide` `sia_think` · `moa_tea` `moa_cheer` `moa_report` `moa_smile` `moa_sparkle` `moa_ok` · `x1_hint` `x2_hint` `x3_hint`

## 3. 새로 그릴 그림
표지 세 장뿐이다. 프롬프트·포즈·alt는 `COVER_PROMPTS_optimization_3d_map.md`.

3D 지도·그래프·단면은 모두 페이지 코드(Canvas 2D)가 그리므로 그림 파일이 필요 없다. 그림 안에 개념 효과(기울기 화살표, 등고선)를 그려 넣지 않는다.

## 4. 일관성 지침
- 세 표지의 장소·소품이 겹치지 않게: 목차 = 바닥 지형, 1편 = 탁자 위 안장 모형과 깃대, 2편 = 실험대·공 세 개·카드 더미.
- 생물 앵커가 아닌 시리즈라 현미경·초파리 해부 소품을 넣지 않는다.
- 대결 결과를 암시하지 않는다(1편: 초파리 승, 2편: 조건부 — 표지는 둘 다 결과 전 장면).

## 5. 넘겨받은 뒤 처리 (18-15)
1. 16:9·1600 이상·글자 없음·캐릭터 외형 확인 → 2. 안전 영역 → 3. WebP 1600×900(220 KB 이하) → 4. 각 페이지 `.cover .frame` 안에 `<img class="art" ...>`를 넣고 대체 표지 배지(`.badge`)를 지움 → 5. 390·768·1280 폭 확인 → 6. `cover_manifest.json` 상태를 `ok`로.

## 6. 매니페스트
`cover_manifest.json` (저장소 맨 위).
