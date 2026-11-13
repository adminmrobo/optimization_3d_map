# 좌표축 위의 그릇 — 3D 지도로 본 모델 최적화

가중치를 좌표축으로, 오차를 높이로 세운 3D 지도 위에서 모델 최적화를 보는 연구실 해설입니다. 연구실 스킬 ai-lab-explainer v1.14("낮의 연구실", 흰 배경)를 따릅니다. 박사·조수 하루·초파리 연구원·주판봇과 인턴 시아·모아가 진행합니다.

- 사이트: https://adminmrobo.github.io/optimization_3d_map/
- 글 · 안상선 ((주)M-Robo 대표) · [저자 소개](https://adminmrobo.github.io/who_am_i/who_am_i.html)

| 편 | 파일 | 내용 | 대결 |
|---|---|---|---|
| 목차 | `index.html` | 두 편으로 가는 첫 화면 | — |
| 1편 수학 편 | `1_math_map.html` | ① 단면과 한 걸음 ② 그래디언트와 법선(깃대와 그림자) ③ 헤시안·고유값·보폭 한계 ④ 안장점(감자칩) ⑤ 야코비안과 역전파 | 기울기 0이면 바닥인가? → 초파리 승 (F) |
| 2편 실험실 편 | `2_experiment_lab.html` | ① 배치 크기(공 세 개 경주) ② 학습률 한계 ③ 가중치 4,416개 신경망의 단면 ④ 에포크와 과적합 | 작은 배치냐, 풀배치냐 → 조건부 (C) |

세 페이지 모두 흰 배경의 단일 HTML 파일입니다(외부 요청은 글꼴 하나). 3D는 Canvas 2D로 직접 그렸고, 끌거나 시점 버튼·화살표 키로 돌릴 수 있습니다. 페이지 끝에 지식 색인(`#kg`)과 온톨로지·서지 꾸러미(`#export`)가 있습니다.

## 바탕 자료와 저작권

- matharium 인포그래픽 3장(곡면 감자칩의 기하, 벡터 미분 연산자, 그래디언트·야코비안·헤시안), matheorems 영상(그래프 곡면의 야코비안과 법선), Machine Learning from Scratch 39편·43편(Facebook 릴스) — 사용자가 제공한 자료입니다. 원본 그림·영상·코드는 이 저장소에 넣지 않았고, 3D와 그래프는 모두 새로 그렸습니다.
- 39편·43편 설명글의 숫자는 영상 속 코드를 옮겨 실행해 그대로 재현되는 것을 확인했습니다(2편 정리의 검증 상자). 페이지의 실험은 같은 아이디어로 새로 짠 코드라 숫자가 조금 다릅니다.
- 논문: Dauphin 외(2014), Li 외(2018), Rumelhart·Hinton·Williams(1986), Goodfellow·Bengio·Courville(2016), Goyal 외(2017), He 외(2016), Ioffe·Szegedy(2015), Polyak(1964), Kingma·Ba(2015).
- 사용자 제공 자료(인포그래픽·영상)의 원 게시물 주소·게시일은 아직 받지 못해 "미확인"으로 적었습니다.
- 캐릭터 이름·설정·그림은 저작권자 안상선의 허락 없이 사용할 수 없습니다.

## 폴더

```
.
├─ index.html · 1_math_map.html · 2_experiment_lab.html   완성 페이지 (build/에서 만듦)
├─ build/
│  ├─ p0/p1/p2.src.html   페이지 원본
│  ├─ common.css · common.js   공용 디자인·모듈 (3D 지형 Surf3D, 그래프, 용어 말풍선, 퀴즈, 대결)
│  ├─ labmath.js           계산 모듈 (시드 고정 데이터, 미니배치 경사하강, 헤시안, 안장 대결)
│  ├─ deep.json            2편 ③·④ 신경망 실험 결과 (code/deep_slices.py가 만듦)
│  ├─ kg_defs.py           지식 그래프·참고문헌·페이지 서지 정의 → kg_N / refs_N / meta_N.json
│  ├─ kgx.js · backbone.json   지식 색인·꾸러미 모듈과 AI 영역 뼈대 (ahnboat_lab_explainer onto-retrofit에서 가져옴)
│  ├─ sprites96.js · sprites_index.js   캐릭터 팩에서 고른 표정 그림
│  ├─ make_guide.js        퀴즈 정답표 다시 뽑기 (node build/make_guide.js)
│  └─ build.js             조립: node build/build.js
├─ code/
│  ├─ check_numbers.js     페이지 기대 수치 다시 계산 (node code/check_numbers.js)
│  └─ deep_slices.py       신경망 단면·학습률·과적합 실험 (python3 code/deep_slices.py, numpy)
├─ COVER_PROMPTS_optimization_3d_map.md   표지 세 장의 Genspark 지시문 (밝은 낮 연구실)
├─ LECTURE_GUIDE.md                       강의자용 가이드 (2차시 흐름·발문·퀴즈 정답표)
├─ IMG_spec_optimization_3d_map.md        이미지 제작 명세서
├─ cover_manifest.json                    표지 현황판 연결
└─ KG_registry_additions.json             시리즈 등록부에 새로 더할 ID
```

다시 만들기: `python3 code/deep_slices.py && python3 build/kg_defs.py && node build/build.js`

## 주요 수치 (설명용 모형, 시드 고정)

| 실험 | 값 |
|---|---|
| 뉴런 하나 그릇의 바닥 (w, b), 오차 | (2.00, 1.01), 1.037 |
| 헤시안 고유값 · 학습률 한계 2/λmax | 1.99 · 5.99 · 0.334 |
| 카드 1,000장 본 뒤 오차: 풀배치 / 배치 10 | 8.020 / 1.068 |
| 100걸음 뒤 오차: 풀배치 / 배치 100 / 배치 10 | 1.037 / 1.039 / 1.068 |
| 안장 대결 멈춘 곳 오차: 초파리 / 주판봇 | 0.000 / 1.000 |
| 신경망(4·64·64·1, 가중치 4,416개) 20 에포크 검증 오차: η 0.00001 / 0.1 / 10 | 0.261 / 0.0083 / 0.393 |
| 과적합(훈련 40개): 검증 최저 에포크 · 1,500 에포크 뒤 훈련 / 검증 | 5 · 0.0002 / 0.243 |

## 표지

세 페이지 모두 표지 그림이 들어가 있습니다(`img/`, WebP 1600·960). 원본 PNG는 `img/src/`에 있고, 지시문은 `COVER_PROMPTS_optimization_3d_map.md`입니다.

## 고친 내역

- v1.3 (2026-11-14): 표지 그림 세 장 반영(목차·1편·2편).
- v1.2 (2026-11-14): 연구실 스킬 v1.14 적용 — 8-2 색 토큰(흰 배경·-soft 채움·캐릭터 색), 단추 규칙, 캔버스 격자·도장 색, 지식 색인 모듈 v1.14 판, 표지 지시문을 v1.14 시즌 구절로.
- v1.1 (2026-11-14): 페르소나 감사 반영 — 흰 배경, 퀴즈 정답 위치 분산, 3D 시점 버튼·화살표 키, 야코비안 점 슬라이더, 안장 대결의 비켜 서기를 음의 고유벡터 방향으로 일반화, 생성 AI 상자 출처 보강, 2편 숫자 요약에 걸음 수 표기, 입문자 순서 안내·한 줄 직관, 단면 크기 맞춤 방식 주석, 모바일 카드 격자, 실무 상자(모멘텀·Adam·학습률 일정), 강의자용 가이드, 대체 표지 배지 숨김.
