"""두 편의 지식 그래프(kg_N.json)·참고문헌(refs_N.json)·페이지 서지(meta_N.json)를 만든다.
형식은 ahnboat_lab_explainer/packs/task/onto-retrofit/templates 와 본편 O1·O2를 따른다.
실행: python3 build/kg_defs.py  → 그다음 node build/build.js"""
import json, pathlib
B = pathlib.Path(__file__).resolve().parent
TODAY = "2026-11-14"
BASE = "https://adminmrobo.github.io/optimization_3d_map/"

# ── 참고문헌 (CSL-JSON) ─────────────────────────────────────
def ref(id_, type_, title, authors, year=None, container=None, extra=None, role="background", supports=(), locs=(), verified=None, checked="", note=""):
    r = {"id": id_, "type": type_, "title": title, "author": authors}
    if year: r["issued"] = {"date-parts": [[year]]}
    if container: r["container-title"] = container
    r.update(extra or {})
    r["accessed"] = {"date-parts": [[2026, 11, 14]]}
    r["lab"] = {"work": "lab:work/" + id_, "role": role, "supports": list(supports), "locs": list(locs),
                "verified": verified or {}, "checkedBy": checked}
    if note: r["lab"]["note"] = note
    return r

USERSRC = "사용자 제공 자료(이미지·영상)에서 옮김. 원 게시물 주소·게시일은 받지 못함"
REFS = {
 "matharium_crisp": lambda s: ref("matharium_crisp", "graphic", "The geometry of a curved crisp", [{"literal": "matharium"}], role="primary", supports=s,
        verified={"title": True, "author": True, "year": False, "url": False}, checked=USERSRC, note="그림은 페이지에 넣지 않고 새로 그림"),
 "matharium_vecops": lambda s: ref("matharium_vecops", "graphic", "The Vector Differential Operators", [{"literal": "matharium"}], role="primary", supports=s,
        verified={"title": True, "author": True, "year": False, "url": False}, checked=USERSRC),
 "matharium_del": lambda s: ref("matharium_del", "graphic", "The Del Operator", [{"literal": "matharium"}], role="primary", supports=s,
        verified={"title": True, "author": True, "year": False, "url": False}, checked=USERSRC, note="그림은 페이지에 넣지 않고 표로 다시 씀"),
 "knott1911life": lambda s: ref("knott1911life", "book", "Life and Scientific Work of Peter Guthrie Tait", [{"family": "Knott", "given": "Cargill Gilston"}],
        1911, None, {"publisher": "Cambridge University Press"}, supports=s, locs=[{"claim": "lab:claim/nabla-name-1870", "loc": "p. 145"}],
        verified={"title": True, "author": True, "year": True, "pages": False}, checked="웹 검색 2026-11-16 (Wikipedia 'Nabla symbol' 각주, Neumaier 'History of Nabla')"),
 "matharium_gjh": lambda s: ref("matharium_gjh", "graphic", "Gradient, Jacobian and Hessian", [{"literal": "matharium"}], role="primary", supports=s,
        verified={"title": True, "author": True, "year": False, "url": False}, checked=USERSRC),
 "matheorems_graph": lambda s: ref("matheorems_graph", "motion_picture", "그래프 곡면 z = f(u, v)의 야코비안과 법선 (z = sin u cos v)", [{"literal": "matheorems"}], role="primary", supports=s,
        verified={"title": False, "author": True, "year": False, "url": False}, checked=USERSRC, note="제목은 영상 내용을 보고 붙인 설명 제목"),
 "mlfs39": lambda s: ref("mlfs39", "motion_picture", "Machine Learning from Scratch, part 39: mini batch gradient descent", [{"literal": "Machine Learning from Scratch"}], role="data", supports=s,
        extra={"medium": "Facebook 릴스"}, verified={"title": True, "author": False, "year": False, "url": False}, checked=USERSRC + ". 영상 속 코드를 옮겨 실행해 설명글 숫자 재현 확인(2026-11-14)"),
 "mlfs43": lambda s: ref("mlfs43", "motion_picture", "Machine Learning from Scratch, part 43: hyperparameters", [{"literal": "Machine Learning from Scratch"}], role="data", supports=s,
        extra={"medium": "Facebook 릴스"}, verified={"title": True, "author": False, "year": False, "url": False}, checked=USERSRC + ". 영상 속 코드를 옮겨 실행해 설명글 숫자 재현 확인(2026-11-14)"),
 "dauphin2014identifying": lambda s: ref("dauphin2014identifying", "paper-conference", "Identifying and attacking the saddle point problem in high-dimensional non-convex optimization",
        [{"family": "Dauphin", "given": "Yann N."}, {"family": "Pascanu", "given": "Razvan"}, {"family": "Gulcehre", "given": "Caglar"}, {"family": "Cho", "given": "Kyunghyun"}, {"family": "Ganguli", "given": "Surya"}, {"family": "Bengio", "given": "Yoshua"}],
        2014, "Advances in Neural Information Processing Systems 27", {"page": "2933-2941", "URL": "https://arxiv.org/abs/1406.2572"}, supports=s, locs=[{"claim": "lab:claim/saddles-proliferate-high-dim", "loc": "초록, 2장"}],
        verified={"title": True, "author": True, "year": True, "container": True, "pages": True, "doi": False}, checked="웹 검색 2026-11-14 (NeurIPS 논문 페이지, arXiv 1406.2572, mlanthology)"),
 "goodfellow2016deep": lambda s: ref("goodfellow2016deep", "book", "Deep Learning", [{"family": "Goodfellow", "given": "Ian"}, {"family": "Bengio", "given": "Yoshua"}, {"family": "Courville", "given": "Aaron"}],
        2016, None, {"publisher": "MIT Press", "URL": "https://www.deeplearningbook.org/"}, supports=s, locs=[{"claim": "lab:claim/lr-limit-quadratic", "loc": "4장 수치 계산 (4.3)"}],
        verified={"title": True, "author": True, "year": True, "publisher": True, "pages": False}, checked="제작자 지식 — 장·절 위치는 원문 대조 안 함"),
 "rumelhart1986learning": lambda s: ref("rumelhart1986learning", "article-journal", "Learning representations by back-propagating errors",
        [{"family": "Rumelhart", "given": "David E."}, {"family": "Hinton", "given": "Geoffrey E."}, {"family": "Williams", "given": "Ronald J."}],
        1986, "Nature", {"volume": "323", "page": "533-536", "DOI": "10.1038/323533a0"}, supports=s,
        verified={"title": True, "author": True, "year": True, "container": True, "pages": True, "doi": True}, checked="웹 검색 2026-11-14 (nature.com 인용 정보, ADS)"),
 "li2018visualizing": lambda s: ref("li2018visualizing", "paper-conference", "Visualizing the Loss Landscape of Neural Nets",
        [{"family": "Li", "given": "Hao"}, {"family": "Xu", "given": "Zheng"}, {"family": "Taylor", "given": "Gavin"}, {"family": "Studer", "given": "Christoph"}, {"family": "Goldstein", "given": "Tom"}],
        2018, "Advances in Neural Information Processing Systems 31", {"URL": "https://arxiv.org/abs/1712.09913"}, supports=s, locs=[{"claim": "lab:claim/random-direction-slices", "loc": "3장 (무작위 방향 단면, 필터 정규화)"}],
        verified={"title": True, "author": True, "year": True, "container": True, "pages": False, "doi": False}, checked="웹 검색 2026-11-14 (NeurIPS 논문 페이지, arXiv 1712.09913)"),
 "goyal2017accurate": lambda s: ref("goyal2017accurate", "article", "Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour",
        [{"family": "Goyal", "given": "Priya"}, {"family": "Dollár", "given": "Piotr"}, {"family": "Girshick", "given": "Ross"}, {"family": "Noordhuis", "given": "Pieter"}, {"family": "Wesolowski", "given": "Lukasz"}, {"family": "Kyrola", "given": "Aapo"}, {"family": "Tulloch", "given": "Andrew"}, {"family": "Jia", "given": "Yangqing"}, {"family": "He", "given": "Kaiming"}],
        2017, "arXiv", {"number": "1706.02677", "URL": "https://arxiv.org/abs/1706.02677"}, supports=s,
        verified={"title": True, "author": True, "year": True, "container": True, "pages": False, "doi": False}, checked="제작자 지식 — 원문 대조 안 함"),
 "he2016deep": lambda s: ref("he2016deep", "paper-conference", "Deep Residual Learning for Image Recognition",
        [{"family": "He", "given": "Kaiming"}, {"family": "Zhang", "given": "Xiangyu"}, {"family": "Ren", "given": "Shaoqing"}, {"family": "Sun", "given": "Jian"}],
        2016, "Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)", {"page": "770-778"}, supports=s,
        verified={"title": True, "author": True, "year": True, "container": True, "pages": False, "doi": False}, checked="제작자 지식 — 원문 대조 안 함"),
 "ioffe2015batch": lambda s: ref("ioffe2015batch", "paper-conference", "Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift",
        [{"family": "Ioffe", "given": "Sergey"}, {"family": "Szegedy", "given": "Christian"}], 2015, "Proceedings of the 32nd International Conference on Machine Learning (ICML)", None, supports=s,
        verified={"title": True, "author": True, "year": True, "container": True, "pages": False, "doi": False}, checked="제작자 지식 — 원문 대조 안 함"),
 "polyak1964some": lambda s: ref("polyak1964some", "article-journal", "Some methods of speeding up the convergence of iteration methods",
        [{"family": "Polyak", "given": "Boris T."}], 1964, "USSR Computational Mathematics and Mathematical Physics", {"volume": "4", "issue": "5"}, supports=s,
        verified={"title": True, "author": True, "year": True, "container": True, "pages": False, "doi": False}, checked="제작자 지식 — 원문 대조 안 함"),
 "kingma2015adam": lambda s: ref("kingma2015adam", "paper-conference", "Adam: A Method for Stochastic Optimization",
        [{"family": "Kingma", "given": "Diederik P."}, {"family": "Ba", "given": "Jimmy"}], 2015, "International Conference on Learning Representations (ICLR)", {"URL": "https://arxiv.org/abs/1412.6980"}, supports=s,
        verified={"title": True, "author": True, "year": True, "container": True, "pages": False, "doi": False}, checked="제작자 지식 — 원문 대조 안 함"),
 "song2019generative": lambda s: ref("song2019generative", "paper-conference", "Generative Modeling by Estimating Gradients of the Data Distribution",
        [{"family": "Song", "given": "Yang"}, {"family": "Ermon", "given": "Stefano"}], 2019, "Advances in Neural Information Processing Systems 32", {"page": "11895-11907", "URL": "https://arxiv.org/abs/1907.05600"}, supports=s,
        locs=[{"claim": "lab:claim/score-is-gradient", "loc": "초록, 2장"}],
        verified={"title": True, "author": True, "year": True, "container": True, "pages": True, "doi": False}, checked="웹 검색 2026-11-16 (arXiv 1907.05600, NeurIPS 2019 논문 페이지, 저자 저장소 BibTeX)"),
 "gonzalez2018digital": lambda s: ref("gonzalez2018digital", "book", "Digital Image Processing (4th ed.)", [{"family": "Gonzalez", "given": "Rafael C."}, {"family": "Woods", "given": "Richard E."}],
        2018, None, {"publisher": "Pearson", "ISBN": "978-0-13-335672-4"}, supports=s, locs=[{"claim": "lab:claim/laplacian-filter-edges", "loc": "3장 공간 필터링 (3.6 샤프닝 필터)"}],
        verified={"title": True, "author": True, "year": True, "publisher": True, "pages": False}, checked="웹 검색 2026-11-16 (Pearson·MathWorks 도서 페이지) — 절 번호는 원문 대조 안 함"),
}

# ── 그래프 도우미 ──────────────────────────────────────────
class G:
    def __init__(s, page): s.page, s.nodes, s.edges, s.ids = page, [], [], set()
    def n(s, id_, type_, ko, en, anchor, level=2, definition=None, family="optimization", conf="high", cov="explained", source=None, alt=None):
        if id_ in s.ids: return id_
        d = {"id": id_, "type": type_, "label": {"ko": ko, "en": en}, "page": s.page, "anchor": anchor, "level": level,
             "status": "known", "confidence": conf, "coverage": cov, "family": family, "domain": ["ai"], "match": []}
        if definition: d["definition"] = {"ko": definition}
        if source: d["source"] = source
        if alt: d["altLabel"] = {"ko": alt}
        s.nodes.append(d); s.ids.add(id_); return id_
    def e(s, a, p, b, anchor, conf="high"): s.edges.append({"s": a, "p": "lab:" + p, "o": b, "anchor": anchor, "confidence": conf})
    def work(s, rid, ko, en): return s.n("lab:work/" + rid, "Work", ko, en, "#top", 1, family="optimization")
    def dump(s, n):
        (B / f"kg_{n}.json").write_text(json.dumps({"version": "1.3", "page": s.page, "nodes": s.nodes, "edges": s.edges}, ensure_ascii=False, indent=1))

T_CALC, T_GD, T_BP, T_LOSS, T_SGD = "lab:topic/calculus-optimization-math", "lab:topic/gradient-descent", "lab:topic/backpropagation", "lab:topic/loss-function", "lab:topic/sgd-minibatch"

# ══════════════ 1편 ══════════════
g = G("1_math_map")
axis = g.n("lab:concept/parameter-axis", "Concept", "좌표축(가중치 축)", "Parameter axis", "#map", 1, "가중치 하나가 지도의 축 하나. 가중치가 n개면 축이 n개인 지도.")
land = g.n("lab:concept/loss-landscape", "Concept", "오차 지형", "Loss landscape", "#map", 1, "가중치마다 잰 오차를 높이로 세운 땅.", alt=["손실 지형"])
cut = g.n("lab:concept/loss-slice", "Concept", "단면", "Loss-landscape slice", "#s1", 1, "다른 축을 한 값에 묶고 남은 축으로만 본 지형.")
gd = g.n("lab:method/gradient-descent", "Method", "경사하강", "Gradient descent", "#s1", 1, "기울기의 반대 방향으로 조금씩 걸어 오차를 줄이는 방법.")
lr = g.n("lab:concept/learning-rate", "Concept", "학습률", "Learning rate", "#s1", 1, "한 걸음의 크기. 새 가중치 = 옛 가중치 − 학습률 × 기울기.")
grad = g.n("lab:concept/gradient", "Concept", "그래디언트", "Gradient", "#s2", 2, "편미분을 모은 벡터. 가장 가파른 오르막 방향을 가리킨다.", alt=["기울기", "∇f"])
nrm = g.n("lab:concept/surface-normal", "Concept", "법선", "Surface normal", "#s2", 2, "곡면과 직각인 방향. 그래프 곡면에서는 n = (−∂f/∂u, −∂f/∂v, 1).")
tan = g.n("lab:concept/tangent-vector", "Concept", "접선 벡터", "Tangent vector", "#s2", 2, "곡면 위 격자선을 따라가는 방향. t_u = (1, 0, ∂f/∂u).")
curl0 = g.n("lab:concept/curl-free-gradient", "Concept", "그래디언트의 회전은 0", "Curl of a gradient is zero", "#s2", 3, "그래디언트로 만든 벡터장은 소용돌이가 없다. 내리막 흐름은 제자리를 돌지 않는다.")
hes = g.n("lab:concept/hessian", "Concept", "헤시안", "Hessian matrix", "#s3", 3, "2차 편미분을 모은 정사각 표. 방향마다의 굽음을 적는다.")
eig = g.n("lab:concept/curvature-eigenvalue", "Concept", "고유값(굽음)", "Curvature eigenvalue", "#s3", 3, "헤시안을 어느 방향으로 봐도 변하지 않는 굽음 숫자.")
lap = g.n("lab:concept/laplacian", "Concept", "라플라시안", "Laplacian", "#s3", 3, "2차 편미분의 합 = 헤시안 고유값의 합 = ∇·∇f.")
delop = g.n("lab:concept/del-operator", "Concept", "나블라(∇) 연산자", "Del (nabla) operator", "#del-op", 2, "칸마다 편미분이 든 벡터 (∂/∂x, ∂/∂y, ∂/∂z). 붙는 방식에 따라 그래디언트·발산·회전·라플라시안이 된다.", alt=["델", "del", "∇"])
divg = g.n("lab:concept/divergence", "Concept", "발산", "Divergence", "#del-op", 2, "∇·F. 한 점에서 나가는 양과 들어오는 양의 차. 양수면 샘, 음수면 빨아들이는 곳.")
g.e(delop, "relatedTo", grad, "#del-op"); g.e(delop, "relatedTo", divg, "#del-op"); g.e(delop, "relatedTo", lap, "#del-op"); g.e(delop, "relatedTo", curl0, "#del-op"); g.e(lap, "relatedTo", divg, "#del-op")
lim = g.n("lab:concept/step-size-limit", "Concept", "보폭 한계 2/λmax", "Step-size stability limit", "#s3", 3, "2차 근사에서 경사하강이 줄어드는 학습률의 상한.")
cond = g.n("lab:concept/ill-conditioning", "Concept", "길쭉함(조건수)", "Ill-conditioning", "#s3", 3, "가장 큰 굽음과 가장 작은 굽음의 비. 크면 지그재그로 느리게 내려간다.")
sad = g.n("lab:concept/saddle-point", "Concept", "안장점", "Saddle point", "#s4", 3, "기울기가 0이지만 한 방향으로는 최저, 다른 방향으로는 최고인 곳.")
hyp = g.n("lab:concept/hyperbolic-paraboloid", "Concept", "쌍곡포물면", "Hyperbolic paraboloid", "#s4", 2, "z = x²/a² − y²/b². 한 방향은 위로, 다른 방향은 아래로 휜 곡면.")
rul = g.n("lab:concept/doubly-ruled-surface", "Concept", "이중 선직면", "Doubly ruled surface", "#s4", 3, "곧은 선 두 무리로 다 덮이는 곡면.")
jac = g.n("lab:concept/jacobian", "Concept", "야코비안", "Jacobian matrix", "#s5", 3, "벡터 함수의 1차 편미분 표. 작은 원이 어떤 타원이 되는지 알려 준다.")
chain = g.n("lab:concept/chain-rule", "Concept", "연쇄 법칙", "Chain rule", "#s5", 3, "이어 붙인 함수의 미분은 각 미분의 곱(야코비안의 곱).")
bp = g.n("lab:method/backpropagation", "Method", "역전파", "Backpropagation", "#s5", 3, "오차의 기울기에 층마다의 야코비안을 뒤에서부터 곱해 모든 가중치의 기울기를 구하는 계산.")
neuron = g.n("lab:method/single-neuron-regression", "Method", "뉴런 하나 (w, b)", "Single linear neuron", "#map", 1, "예측 = w·x + b. 가중치가 둘뿐이라 오차 지형 전체를 3D로 그릴 수 있다.")
# 한계 사슬
L1 = g.n("lab:limitation/one-axis-at-a-time", "Limitation", "축 하나씩만 움직임", "Moves one axis at a time", "#s1", 2)
L2 = g.n("lab:limitation/gradient-no-step-size", "Limitation", "기울기만으로는 보폭을 모름", "Gradient gives no step size", "#s2", 2)
L3 = g.n("lab:limitation/quadratic-local", "Limitation", "2차 근사는 그 점 둘레에서만 맞음", "Quadratic model is local", "#s3", 3)
L4 = g.n("lab:limitation/single-map-only", "Limitation", "층을 지나는 변화는 모름", "Ignores layer-to-layer mapping", "#s4", 3)
L5 = g.n("lab:limitation/linear-approx", "Limitation", "야코비안은 작은 범위의 직선 근사", "Jacobian is a local linear approximation", "#s5", 3)
# 사다리 칸 = 방법 (K1·K2): 칸마다 한계 → 다음 칸이 해결
M1 = g.n("lab:method/slice-descent", "Method", "① 단면 위 한 걸음", "Step on a 1D slice", "#s1", 1, "다른 축을 묶어 둔 단면 곡선의 기울기로 한 축만 옮긴다.")
M3 = g.n("lab:method/curvature-step-limit", "Method", "③ 굽음으로 보폭 한계 정하기", "Curvature-based step limit", "#s3", 3, "헤시안의 가장 큰 고유값으로 학습률의 상한 2/λmax를 정한다.")
M4 = g.n("lab:method/second-order-critical-test", "Method", "④ 헤시안 부호로 임계점 판별", "Second-order critical-point test", "#s4", 3, "기울기 0인 곳에서 고유값 부호로 바닥·봉우리·안장을 가린다.")
LAD = [M1, gd, M3, M4, bp]
for (a, b), L, anc in zip(zip(LAD, LAD[1:]), [L1, L2, L3, L4], ["#s1", "#s2", "#s3", "#s4"]):
    g.e(a, "hasLimitation", L, anc); g.e(L, "addressedBy", b, anc); g.e(a, "prerequisiteOf", b, "#sum")
g.e(bp, "hasLimitation", L5, "#s5")
g.e(cut, "prerequisiteOf", M1, "#s1"); g.e(hes, "prerequisiteOf", M3, "#s3"); g.e(eig, "prerequisiteOf", M4, "#s4"); g.e(jac, "prerequisiteOf", bp, "#s5")
g.e(gd, "relatedTo", grad, "#s2")
# 개념 관계
g.e(axis, "partOf", land, "#map"); g.e(land, "broader", T_LOSS, "#map"); g.e(cut, "partOf", land, "#s1")
g.e(gd, "broader", T_GD, "#s1"); g.e(lr, "partOf", gd, "#s1"); g.e(grad, "prerequisiteOf", gd, "#s2")
g.e(tan, "prerequisiteOf", nrm, "#s2"); g.e(nrm, "relatedTo", grad, "#s2"); g.e(curl0, "partOf", grad, "#s2")
g.e(eig, "partOf", hes, "#s3"); g.e(lap, "derivedFrom", hes, "#s3"); g.e(lim, "derivedFrom", eig, "#s3"); g.e(lim, "relatedTo", lr, "#s3"); g.e(cond, "derivedFrom", eig, "#s3")
g.e(hyp, "relatedTo", sad, "#s4"); g.e(rul, "partOf", hyp, "#s4"); g.e(sad, "evaluatedBy", eig, "#s4")
g.e(chain, "partOf", bp, "#s5"); g.e(jac, "prerequisiteOf", chain, "#s5"); g.e(bp, "broader", T_BP, "#s5")
for c in (grad, hes, lap, jac, eig): g.e(c, "broader", T_CALC, "#sum")
g.e(neuron, "demonstratedBy", "lab:sim/p1-bowl-map", "#map") if False else None
# 비유
A = [("lab:analogy/hill-slice", "산을 칼로 자른 단면", "Hill cross-section", "#s1", cut),
     ("lab:analogy/flagpole-shadow", "비탈에 꽂은 깃대의 그림자", "Flagpole shadow on a slope", "#s2", nrm),
     ("lab:analogy/elongated-bowl", "길쭉한 그릇", "Elongated bowl", "#s3", cond),
     ("lab:analogy/stacked-crisp", "통에 포개 담는 곡면 감자칩", "Stacked curved crisp", "#s4", hyp),
     ("lab:analogy/rubber-sheet", "당겨진 고무판의 모눈", "Stretched rubber sheet", "#s5", jac)]
for i, ko, en, anc, tgt in A: g.n(i, "Analogy", ko, en, anc, 1); g.e(i, "analogyOf", tgt, anc)
# 시뮬레이션
S = [("lab:sim/p1-bowl-map", "오차 지도 (뉴런 하나의 그릇)", "Bowl map of a single neuron", "#map", land),
     ("lab:sim/p1-slice-walk", "단면 위 1차원 경사하강", "1D descent on a slice", "#s1", cut),
     ("lab:sim/p1-flagpole", "접선·법선·바닥 그림자", "Tangents, normal and shadow", "#s2", nrm),
     ("lab:sim/p1-curvature", "고유값으로 만든 땅과 공 굴리기", "Curvature playground", "#s3", hes),
     ("lab:sim/p1-saddle", "쌍곡포물면 단면과 곧은 선", "Saddle sections and rulings", "#s4", hyp),
     ("lab:sim/p1-rubber", "원이 타원이 되는 고무판", "Circle-to-ellipse warp", "#s5", jac)]
for i, ko, en, anc, tgt in S: g.n(i, "Simulation", ko, en, anc, 2); g.e(tgt, "demonstratedBy", i, anc)
g.e(neuron, "demonstratedBy", "lab:sim/p1-bowl-map", "#map")
# 대결
m_fly = g.n("lab:method/curvature-check-escape", "Method", "굽음 확인 후 비켜 서기", "Curvature check and escape", "#duel", 3, "기울기가 0에 가까우면 헤시안 고유값을 보고, 음수 방향이 있으면 그쪽으로 한 발 비켜 선다.")
m_robo = g.n("lab:method/gradient-only-stop", "Method", "기울기 0이면 멈추기", "Stop at zero gradient", "#duel", 2, "기울기만 보고, 0이 되면 바닥이라고 보고 멈춘다.")
met = g.n("lab:metric/final-loss", "Metric", "멈춘 곳의 오차", "Final loss", "#duel", 1)
g.e(m_fly, "contrastsWith", m_robo, "#duel"); g.e(m_fly, "evaluatedBy", met, "#duel"); g.e(m_robo, "evaluatedBy", met, "#duel"); g.e(m_fly, "relatedTo", sad, "#duel")
g.n("lab:sim/p1-duel", "Simulation", "안장점 대결", "Saddle duel", "#duel", 3); g.e(m_fly, "demonstratedBy", "lab:sim/p1-duel", "#duel")
# 질문
q1 = g.n("lab:question/p1-blindfold", "Question", "눈을 가린 채 기울기와 굽음만으로 바닥을 찾을 수 있을까?", "Can a blindfolded walker find the bottom from slope and curvature?", "#top", 1)
q2 = g.n("lab:question/p1-zero-gradient", "Question", "기울기 0이면 바닥인가?", "Is zero gradient a minimum?", "#duel", 2)
g.e(land, "raises", q1, "#top"); g.e(sad, "raises", q2, "#duel")
# 주장과 문헌
W = {k: g.work(k, ko, en) for k, ko, en in [
    ("matharium_crisp", "matharium — The geometry of a curved crisp", "matharium — The geometry of a curved crisp"),
    ("matharium_vecops", "matharium — The Vector Differential Operators", "matharium — The Vector Differential Operators"),
    ("matharium_del", "matharium — The Del Operator", "matharium — The Del Operator"),
    ("knott1911life", "Knott 1911 Life of P. G. Tait", "Knott 1911 Life and Scientific Work of P. G. Tait"),
    ("matharium_gjh", "matharium — Gradient, Jacobian and Hessian", "matharium — Gradient, Jacobian and Hessian"),
    ("matheorems_graph", "matheorems — 그래프 곡면의 야코비안과 법선", "matheorems — Jacobian and normal of a graph surface"),
    ("mlfs39", "ML from Scratch 39 — 미니배치", "ML from Scratch 39 — mini batch"),
    ("mlfs43", "ML from Scratch 43 — 하이퍼파라미터", "ML from Scratch 43 — hyperparameters"),
    ("dauphin2014identifying", "Dauphin 외 2014", "Dauphin et al. 2014"),
    ("goodfellow2016deep", "Goodfellow 외 2016 Deep Learning", "Goodfellow et al. 2016 Deep Learning"),
    ("rumelhart1986learning", "Rumelhart·Hinton·Williams 1986", "Rumelhart, Hinton & Williams 1986"),
    ("goyal2017accurate", "Goyal 외 2017", "Goyal et al. 2017"), ("he2016deep", "He 외 2016 ResNet", "He et al. 2016 ResNet"), ("ioffe2015batch", "Ioffe·Szegedy 2015", "Ioffe & Szegedy 2015")]}
C = [("lab:claim/lr-warmup", "학습 초기에 학습률을 천천히 올리는 워밍업이 큰 배치 학습의 초기 불안정을 줄인다", "Gradual warmup stabilizes early large-batch training", "#s3", lr, "goyal2017accurate", "2.2절"),
     ("lab:claim/residual-connections", "잔차 연결이 매우 깊은 신경망의 학습을 가능하게 한다", "Residual connections ease training of very deep nets", "#s5", bp, "he2016deep", "본문"),
     ("lab:claim/batch-normalization", "정규화 층이 깊은 신경망 학습을 빠르고 안정되게 한다", "Normalization layers speed up and stabilize training", "#s5", bp, "ioffe2015batch", "본문"),
     ("lab:claim/normal-is-neg-gradient-lift", "그래프 곡면의 법선은 (−∂f/∂u, −∂f/∂v, 1)이다", "Normal of a graph surface is (−f_u, −f_v, 1)", "#s2", nrm, "matheorems_graph", "영상 수식"),
     ("lab:claim/curl-grad-zero", "그래디언트의 회전과 회전의 발산은 늘 0이다", "Curl of gradient and divergence of curl vanish", "#s2", curl0, "matharium_vecops", "How they connect"),
     ("lab:claim/laplacian-examples", "∇²(x² + y²) = 4, ∇²(x² − y²) = 0", "Laplacian examples", "#s3", lap, "matharium_vecops", "Laplacian 칸"),
     ("lab:claim/del-four-operations", "∇ 하나가 붙는 방식에 따라 그래디언트·발산·회전·라플라시안을 만든다", "One del operator yields gradient, divergence, curl and Laplacian", "#del-op", delop, "matharium_del", "본문 전체"),
     ("lab:claim/nabla-name-1870", "나블라라는 이름은 1870년 W. R. 스미스가 하프 모양을 보고 테이트에게 제안했다", "The name nabla was suggested to Tait by W. R. Smith in 1870", "#del-op", delop, "knott1911life", "p. 145"),
     ("lab:claim/crisp-doubly-ruled", "쌍곡포물면은 곧은 선 두 무리를 품는다", "A hyperbolic paraboloid is doubly ruled", "#s4", rul, "matharium_crisp", "아래 문구"),
     ("lab:claim/hessian-classifies", "헤시안 고유값이 임계점을 분류한다", "Hessian eigenvalues classify critical points", "#s3", hes, "matharium_gjh", "Hessian 칸"),
     ("lab:claim/saddles-proliferate-high-dim", "고차원 비볼록 지형에서는 나쁜 국소 최소보다 안장점이 문제를 일으킨다", "Saddle points, not local minima, proliferate in high dimensions", "#s4", sad, "dauphin2014identifying", "초록, 2장"),
     ("lab:claim/lr-limit-quadratic", "2차 함수에서 경사하강은 학습률이 2/λmax보다 작을 때 줄어든다", "GD converges on a quadratic iff lr < 2/λmax", "#s3", lim, "goodfellow2016deep", "4장"),
     ("lab:claim/backprop-1986", "역전파는 층마다의 기울기를 뒤에서부터 전해 가중치를 고친다", "Backpropagation adjusts weights by propagating error gradients", "#s5", bp, "rumelhart1986learning", "본문"),
     ("lab:claim/one-neuron-bowl", "뉴런 하나(w, b)의 평균제곱오차는 그릇 모양 2차 곡면이다", "MSE of a single linear neuron is a quadratic bowl", "#map", neuron, "mlfs39", "영상 설명")]
for cid, ko, en, anc, tgt, wk, loc in C:
    g.n(cid, "Claim", ko, en, anc, 2, source=[{"ref": wk, "loc": loc}]); g.e(cid, "supports", tgt, anc); g.e(cid, "assertedIn", W[wk], anc)
g.e(W["mlfs43"], "relatedTo", lr, "#s1")
# 퀴즈
Q = [("s1", 1, gd), ("s1", 2, lim), ("s2", 1, nrm), ("s2", 2, grad), ("s3", 1, lim), ("s3", 2, sad), ("s4", 1, lap), ("s4", 2, rul), ("s5", 1, jac), ("s5", 2, chain), ("duel", 1, sad)]
QL = {"s1": "단면 위 한 걸음", "s2": "법선과 그래디언트", "s3": "굽음과 보폭", "s4": "안장과 라플라시안", "s5": "야코비안과 연쇄", "duel": "대결 안장점"}
for sec, k, tgt in Q:
    qid = f"lab:quiz/p1-{sec}-{k}"; g.n(qid, "QuizItem", f"{QL[sec]} 문제 {k}", f"Quiz {sec}-{k}", "#" + sec, 2); g.e(qid, "assesses", tgt, "#" + sec)
g.dump(1)
used1 = {"goyal2017accurate": [lr], "he2016deep": [bp], "ioffe2015batch": [bp], "matharium_crisp": [rul, hyp], "matharium_vecops": [curl0, lap], "matharium_del": [delop, divg, lap], "knott1911life": [delop], "matharium_gjh": [hes, jac, grad], "matheorems_graph": [nrm, tan],
         "mlfs39": [neuron], "mlfs43": [lr], "dauphin2014identifying": [sad], "goodfellow2016deep": [lim], "rumelhart1986learning": [bp]}
(B / "refs_1.json").write_text(json.dumps([REFS[k](v) for k, v in used1.items()], ensure_ascii=False, indent=1))

# ══════════════ 2편 ══════════════
g = G("2_experiment_lab")
hp = g.n("lab:concept/hyperparameter", "Concept", "하이퍼파라미터", "Hyperparameter", "#map", 1, "학습 전에 사람이 정하는 숫자. 기울기로 고쳐지지 않는다.")
lr = g.n("lab:concept/learning-rate", "Concept", "학습률", "Learning rate", "#s2", 1, "한 걸음의 크기. 새 가중치 = 옛 가중치 − 학습률 × 기울기.")
bs = g.n("lab:concept/batch-size", "Concept", "배치 크기", "Batch size", "#s1", 1, "한 걸음에 기울기를 잴 때 쓰는 데이터 개수.")
ep = g.n("lab:concept/epoch", "Concept", "에포크", "Epoch", "#s4", 1, "데이터 전체를 한 바퀴 다 보는 것.")
dw = g.n("lab:concept/depth-width", "Concept", "깊이·너비", "Depth and width", "#map", 1, "층의 수와 층마다의 뉴런 수.")
mb = g.n("lab:method/minibatch-sgd", "Method", "미니배치 경사하강", "Mini-batch gradient descent", "#s1", 2, "걸음마다 일부 데이터로만 기울기를 재어 걷는 방법.")
fb = g.n("lab:method/full-batch-gd", "Method", "풀배치 경사하강", "Full-batch gradient descent", "#s1", 2, "걸음마다 데이터 전부로 정확한 기울기를 재는 방법.")
gd = g.n("lab:method/gradient-descent", "Method", "경사하강", "Gradient descent", "#s1", 1, "기울기의 반대 방향으로 조금씩 걸어 오차를 줄이는 방법.")
div = g.n("lab:concept/divergence-of-training", "Concept", "발산", "Training divergence", "#s2", 2, "걸음마다 오차가 커져 숫자가 끝없이 불어나는 것.")
lim = g.n("lab:concept/step-size-limit", "Concept", "보폭 한계 2/λmax", "Step-size stability limit", "#s2", 3, "2차 근사에서 경사하강이 줄어드는 학습률의 상한.")
hes = g.n("lab:concept/hessian", "Concept", "헤시안", "Hessian matrix", "#s2", 3, "2차 편미분을 모은 정사각 표. 방향마다의 굽음을 적는다.")
sl = g.n("lab:concept/loss-slice", "Concept", "단면", "Loss-landscape slice", "#s3", 2, "다른 축은 고정하고 고른 방향으로만 자른 지형.")
rd = g.n("lab:method/random-direction-slice", "Method", "무작위 방향 2차원 단면", "Random-direction 2D slice", "#s3", 3, "학습이 끝난 점을 가운데 두고 무작위 방향 두 개로 평면을 잘라 오차를 그린다. 방향 길이는 층별 가중치 크기에 맞춘다.")
land = g.n("lab:concept/loss-landscape", "Concept", "오차 지형", "Loss landscape", "#s3", 1, "가중치마다 잰 오차를 높이로 세운 땅.")
of = g.n("lab:concept/overfitting", "Concept", "과적합", "Overfitting", "#s4", 2, "훈련 데이터에만 지나치게 맞춰 처음 보는 데이터에서 오차가 커지는 것.")
es = g.n("lab:method/early-stopping", "Method", "조기 종료", "Early stopping", "#s4", 2, "검증 오차가 더 나아지지 않을 때 학습을 멈추는 방법.")
val = g.n("lab:concept/validation-set", "Concept", "검증 데이터", "Validation set", "#s4", 1, "학습에 쓰지 않고 떼어 둔 데이터. 설정과 멈출 시점을 고르는 데 쓴다.")
test = g.n("lab:concept/test-set", "Concept", "시험 데이터", "Test set", "#s4", 1, "고르는 데도 쓰지 않고 마지막 채점에만 쓰는 데이터.")
m1 = g.n("lab:metric/full-data-loss", "Metric", "전체 데이터 오차", "Full-data loss", "#s1", 1)
m2 = g.n("lab:metric/validation-loss", "Metric", "검증 오차", "Validation loss", "#s3", 1)
L1 = g.n("lab:limitation/fixed-learning-rate", "Limitation", "학습률을 묶어 둠", "Learning rate held fixed", "#s1", 2)
L2 = g.n("lab:limitation/two-weights-only", "Limitation", "가중치 두 개일 때만 한계를 계산할 수 있음", "Limit computable only for tiny models", "#s2", 2)
L3 = g.n("lab:limitation/plenty-of-data", "Limitation", "데이터가 넉넉할 때만 본 모습", "Seen only with ample data", "#s3", 2)
L4 = g.n("lab:limitation/single-seed-run", "Limitation", "데이터 40개·시드 하나의 한 번 실험", "Single small run", "#s4", 2)
sweep = g.n("lab:method/learning-rate-sweep", "Method", "② 학습률 고르기", "Learning-rate sweep", "#s2", 2, "학습률을 여러 값으로 돌려 보고 오차로 고른다. 굽음이 정한 한계를 넘지 않는다.")
LAD = [mb, sweep, rd, es]
for (a, b), L, anc in zip(zip(LAD, LAD[1:]), [L1, L2, L3], ["#s1", "#s2", "#s3"]):
    g.e(a, "hasLimitation", L, anc); g.e(L, "addressedBy", b, anc); g.e(a, "prerequisiteOf", b, "#sum")
g.e(es, "hasLimitation", L4, "#s4")
g.e(bs, "partOf", mb, "#s1"); g.e(lr, "partOf", sweep, "#s2"); g.e(sl, "partOf", rd, "#s3"); g.e(ep, "partOf", es, "#s4")
for c in (lr, bs, ep, dw): g.e(c, "partOf", hp, "#map")
g.e(mb, "broader", T_SGD, "#s1"); g.e(fb, "broader", T_GD, "#s1"); g.e(mb, "broader", gd, "#s1"); g.e(fb, "broader", gd, "#s1"); g.e(gd, "broader", T_GD, "#s1")
g.e(mb, "contrastsWith", fb, "#s1"); g.e(mb, "evaluatedBy", m1, "#s1"); g.e(fb, "evaluatedBy", m1, "#s1")
g.e(lim, "derivedFrom", hes, "#s2"); g.e(div, "relatedTo", lim, "#s2"); g.e(lr, "hasLimitation", div, "#s2")
g.e(sl, "partOf", land, "#s3"); g.e(rd, "solves", sl, "#s3"); g.e(land, "broader", T_LOSS, "#s3"); g.e(rd, "evaluatedBy", m2, "#s3")
g.e(of, "evaluatedBy", m2, "#s4"); g.e(es, "addressedBy", of, "#s4") if False else g.e(of, "addressedBy", es, "#s4"); g.e(es, "evaluatedOn", val, "#s4"); g.e(val, "relatedTo", test, "#s4"); g.e(ep, "relatedTo", of, "#s4")
A = [("lab:analogy/flashcard-batches", "문제 카드 묶음", "Flashcard batches", "#s1", mb),
     ("lab:analogy/lab-safety-range", "실험 조건의 안전 범위", "Safe operating range", "#s2", lim),
     ("lab:analogy/tissue-section", "시료의 얇은 절편", "Thin tissue section", "#s3", sl),
     ("lab:analogy/sealed-exam", "봉인된 모의고사", "Sealed practice exam", "#s4", val),
     ("lab:analogy/experiment-condition-table", "실험 조건표", "Experiment condition sheet", "#map", hp)]
for i, ko, en, anc, tgt in A: g.n(i, "Analogy", ko, en, anc, 1); g.e(i, "analogyOf", tgt, anc)
S = [("lab:sim/p2-batch-race", "같은 그릇 공 세 개 경주", "Three-ball batch race", "#s1", mb),
     ("lab:sim/p2-lr-limit", "학습률과 보폭 한계", "Learning-rate limit", "#s2", lim),
     ("lab:sim/p2-deep-slice", "4,416차원 신경망의 단면", "Slice of a 4,416-D landscape", "#s3", rd),
     ("lab:sim/p2-overfit", "훈련·검증 오차 곡선", "Train vs validation curves", "#s4", of),
     ("lab:sim/p2-duel", "배치 대결 (조건부)", "Batch duel (conditional)", "#duel", bs)]
for i, ko, en, anc, tgt in S: g.n(i, "Simulation", ko, en, anc, 2); g.e(tgt, "demonstratedBy", i, anc)
q1 = g.n("lab:question/p2-cheapest-path", "Question", "같은 그릇에서 공을 어떻게 굴려야 가장 싸고 빠르게 바닥에 닿을까?", "How to reach the bottom cheapest and fastest?", "#top", 1)
q2 = g.n("lab:question/p2-batch-duel", "Question", "작은 배치냐, 풀배치냐 — 무엇을 같게 두고 견주나?", "Small batch or full batch — equal steps or equal compute?", "#duel", 2)
g.e(hp, "raises", q1, "#top"); g.e(bs, "raises", q2, "#duel")
W = {k: g.work(k, ko, en) for k, ko, en in [
    ("mlfs39", "ML from Scratch 39 — 미니배치", "ML from Scratch 39 — mini batch"),
    ("mlfs43", "ML from Scratch 43 — 하이퍼파라미터", "ML from Scratch 43 — hyperparameters"),
    ("li2018visualizing", "Li 외 2018", "Li et al. 2018"),
    ("goodfellow2016deep", "Goodfellow 외 2016 Deep Learning", "Goodfellow et al. 2016 Deep Learning"),
    ("matharium_gjh", "matharium — Gradient, Jacobian and Hessian", "matharium — Gradient, Jacobian and Hessian"),
    ("goyal2017accurate", "Goyal 외 2017", "Goyal et al. 2017"), ("polyak1964some", "Polyak 1964", "Polyak 1964"), ("kingma2015adam", "Kingma·Ba 2015 Adam", "Kingma & Ba 2015 Adam")]}
mom = g.n("lab:method/momentum", "Method", "모멘텀", "Momentum", "#sum", 2, "지난 걸음의 방향을 이어 받아 걷는 경사하강 변형.")
adam = g.n("lab:method/adam", "Method", "Adam", "Adam optimizer", "#sum", 2, "가중치마다 기울기 크기를 따로 기억해 보폭을 맞추는 최적화 방법.")
sch = g.n("lab:method/learning-rate-schedule", "Method", "학습률 일정(워밍업·감소)", "Learning-rate schedule", "#sum", 2, "학습 중에 학습률을 바꾸는 방법. 처음엔 올리고 나중엔 줄인다.")
for m_ in (mom, adam, sch): g.e(m_, "relatedTo", sweep, "#sum"); g.e(m_, "broader", T_GD, "#sum")
C = [("lab:claim/linear-scaling-warmup", "배치를 키우면 학습률도 비례해 키우고 워밍업을 함께 쓰면 큰 배치로도 정확도를 지킬 수 있다", "Linear scaling rule with warmup for large minibatches", "#sum", sch, "goyal2017accurate", "2장"),
     ("lab:claim/momentum-accelerates", "모멘텀은 반복법의 수렴을 빠르게 한다", "Momentum accelerates convergence", "#sum", mom, "polyak1964some", "본문"),
     ("lab:claim/adam-adaptive", "Adam은 기울기의 1·2차 모멘트 추정으로 매개변수마다 보폭을 맞춘다", "Adam adapts per-parameter step sizes", "#sum", adam, "kingma2015adam", "1·2장"),
     ("lab:claim/mlfs39-numbers-reproduced", "39편 설명글의 숫자(7.869, 0.993, 0.956, 오르막 41걸음)가 영상 코드로 그대로 재현된다", "Part 39 numbers reproduce", "#sum", mb, "mlfs39", "설명글, 영상 코드 minibatch.py"),
     ("lab:claim/mlfs43-numbers-reproduced", "43편의 학습률 0.1 검증 오차(목표 분산의 약 2%)가 영상 코드로 재현된다", "Part 43 number reproduces", "#sum", lr, "mlfs43", "설명글, 영상 코드 hyper.py"),
     ("lab:claim/random-direction-slices", "고차원 오차 지형은 무작위 방향으로 자른 1·2차원 단면으로 본다", "High-D landscapes are viewed through random-direction slices", "#s3", rd, "li2018visualizing", "3장"),
     ("lab:claim/lr-limit-quadratic", "2차 함수에서 경사하강은 학습률이 2/λmax보다 작을 때 줄어든다", "GD converges on a quadratic iff lr < 2/λmax", "#s2", lim, "goodfellow2016deep", "4장"),
     ("lab:claim/early-stopping-validation", "검증 오차로 멈출 시점을 고르고 최종 성능은 따로 둔 데이터로 잰다", "Early stopping uses validation; report on held-out test", "#s4", es, "goodfellow2016deep", "7장(조기 종료)"),
     ("lab:claim/hessian-curvature", "헤시안은 기울기가 바뀌는 정도, 곧 굽음을 적는다", "Hessian captures how the gradient changes", "#s2", hes, "matharium_gjh", "Hessian 칸")]
for cid, ko, en, anc, tgt, wk, loc in C:
    g.n(cid, "Claim", ko, en, anc, 2, source=[{"ref": wk, "loc": loc}]); g.e(cid, "supports", tgt, anc); g.e(cid, "assertedIn", W[wk], anc)
Q = [("s1", 1, ep), ("s1", 2, mb), ("s2", 1, lim), ("s2", 2, lr), ("s3", 1, sl), ("s3", 2, rd), ("s4", 1, of), ("s4", 2, test), ("duel", 1, bs)]
QL = {"s1": "배치와 에포크", "s2": "학습률 한계", "s3": "단면", "s4": "과적합과 시험 데이터", "duel": "조건부 대결"}
for sec, k, tgt in Q:
    qid = f"lab:quiz/p2-{sec}-{k}"; g.n(qid, "QuizItem", f"{QL[sec]} 문제 {k}", f"Quiz {sec}-{k}", "#" + sec, 2); g.e(qid, "assesses", tgt, "#" + sec)
g.dump(2)
used2 = {"goyal2017accurate": [sch], "polyak1964some": [mom], "kingma2015adam": [adam], "mlfs39": [mb], "mlfs43": [lr], "li2018visualizing": [rd], "goodfellow2016deep": [lim, es], "matharium_gjh": [hes]}
(B / "refs_2.json").write_text(json.dumps([REFS[k](v) for k, v in used2.items()], ensure_ascii=False, indent=1))

# ── 페이지 서지 ──
def meta(n, title, about, based, slug):
    return {"title": title, "series": "좌표축 위의 그릇 — 3D 지도로 본 모델 최적화", "number": str(n),
            "creator": [{"name": "안상선", "role": "author", "affiliation": "(주)M-Robo"}], "contributor": [{"name": "AI 보조 제작", "role": "assistant"}],
            "date": TODAY, "version": "1.3", "language": ["ko"], "license": "", "url": BASE + slug, "about": about, "basedOn": based,
            "educationalLevel": "입문~중급", "learningResourceType": "interactive explainer", "registry": "KG_00_registry 0.2",
            "suggestedCitation": f"안상선 (2026). {title}. 좌표축 위의 그릇 — 3D 지도로 본 모델 최적화 {n}, v1.3."}
(B / "meta_1.json").write_text(json.dumps(meta(1, "좌표축 위의 그릇 ① 수학 편 — 기울기·굽음·휨으로 읽는 3D 오차 지도",
    ["lab:concept/loss-landscape", "lab:concept/gradient", "lab:concept/hessian", "lab:concept/saddle-point", "lab:concept/jacobian"], list(used1), "1_math_map.html"), ensure_ascii=False, indent=1))
(B / "meta_2.json").write_text(json.dumps(meta(2, "좌표축 위의 그릇 ② 실험실 편 — 배치·학습률·에포크를 3D 지도 위에서 고르기",
    ["lab:concept/hyperparameter", "lab:method/minibatch-sgd", "lab:concept/learning-rate", "lab:concept/loss-slice", "lab:concept/overfitting"], list(used2), "2_experiment_lab.html"), ensure_ascii=False, indent=1))

# ══════════════ 3편 ══════════════
g = G("3_arrow_field")
sfield = g.n("lab:concept/scalar-field", "Concept", "숫자 밭(스칼라장)", "Scalar field", "#map", 1, "공간의 점마다 숫자 하나가 붙은 것. 온도, 농도, 오차.", alt=["스칼라장"])
vfield = g.n("lab:concept/vector-field", "Concept", "화살표 밭(벡터장)", "Vector field", "#map", 1, "공간의 점마다 화살표 하나가 붙은 것. 바람, 물 흐름.", alt=["벡터장"])
axes3 = g.n("lab:concept/cartesian-3d", "Concept", "x·y·z 세 축 공간", "3D Cartesian space", "#map", 1, "앞뒤·좌우·위아래 세 방향이 모두 공간 축인 좌표계. 점의 주소는 (x, y, z).")
delop = g.n("lab:concept/del-operator", "Concept", "나블라(∇) 연산자", "Del (nabla) operator", "#map", 1, "(∂/∂x, ∂/∂y, ∂/∂z). 세 방향으로 조금씩 재는 도구 묶음.", alt=["델", "del", "∇"])
pdv = g.n("lab:concept/partial-derivative", "Concept", "편미분", "Partial derivative", "#s1", 1, "다른 좌표는 고정하고 한 좌표만 움직였을 때의 변화율.")
grad = g.n("lab:concept/gradient", "Concept", "그래디언트", "Gradient", "#s2", 1, "편미분 셋을 묶은 화살표. 가장 가파른 오르막, 등위면과 직각.", alt=["기울기", "∇f"])
lvl = g.n("lab:concept/level-surface", "Concept", "등위면(같은 값 껍질)", "Level surface", "#s2", 1, "값이 같은 점들을 이은 면. 2차원에서는 등고선.")
divg = g.n("lab:concept/divergence", "Concept", "발산", "Divergence", "#s3", 1, "∇·F. 작은 상자에서 (나간 양 − 들어온 양) ÷ 부피.")
curl = g.n("lab:concept/curl", "Concept", "회전", "Curl", "#s4", 2, "∇×F. 작은 바람개비가 가장 빨리 도는 축과 세기(빠르기의 두 배).")
rhr = g.n("lab:concept/right-hand-rule", "Concept", "오른손 법칙", "Right-hand rule", "#s4", 1, "네 손가락을 도는 쪽으로 감으면 엄지가 회전 화살표 방향.")
lap = g.n("lab:concept/laplacian", "Concept", "라플라시안", "Laplacian", "#s5", 2, "∇·∇f. 6 × (이웃 여섯 평균 − 가운데) ÷ h². 양수 움푹, 음수 볼록.")
heat = g.n("lab:concept/heat-equation", "Concept", "열방정식", "Heat equation", "#s5", 2, "∂T/∂t = k∇²T. 이웃 평균보다 낮은 곳은 데워진다.")
curl0 = g.n("lab:concept/curl-free-gradient", "Concept", "그래디언트의 회전은 0", "Curl of a gradient is zero", "#sum", 2, "그래디언트로 만든 화살표 밭은 소용돌이가 없다.")
divcurl0 = g.n("lab:concept/div-of-curl-zero", "Concept", "회전의 발산은 0", "Divergence of a curl is zero", "#sum", 2, "회전 화살표로 만든 밭에는 샘도 구멍도 없다.")
gd = g.n("lab:method/gradient-descent", "Method", "경사하강", "Gradient descent", "#s2", 1, "−∇f 쪽으로 조금씩 걸어 값을 줄이는 방법.")
m_fd = g.n("lab:method/finite-difference", "Method", "이웃 점 찍어 보기(차분)", "Finite difference", "#s1", 1, "한 좌표를 ±h 움직인 두 점의 값 차이 ÷ 2h로 편미분을 잰다.")
m_box = g.n("lab:method/flux-box", "Method", "그물 상자 출입 세기", "Flux through a small box", "#s3", 1, "여섯 면의 출입을 더해 부피로 나눠 발산을 잰다.")
m_pad = g.n("lab:method/paddle-wheel", "Method", "바람개비 고리 셈(순환)", "Paddle-wheel circulation", "#s4", 2, "축에 수직인 작은 고리를 따라 물살을 더해 넓이로 나눈 값 = 회전의 그 축 성분.")
m_nb6 = g.n("lab:method/six-neighbour-stencil", "Method", "이웃 여섯 평균 비교", "Six-neighbour stencil", "#s5", 2, "∇²f ≈ 6 × (이웃 평균 − 가운데) ÷ h².")
m_look = g.n("lab:method/judge-by-look", "Method", "겉모양으로 판단", "Judge rotation by arrow shape", "#duel", 1, "화살표가 원을 그리면 돈다고 본다.")
m_calc = g.n("lab:method/judge-by-curl", "Method", "회전을 계산해 판단", "Judge rotation by computed curl", "#duel", 2, "∂Fy/∂x − ∂Fx/∂y를 이웃 점으로 재서 0이 아니면 돈다고 본다.")
met = g.n("lab:metric/correct-calls", "Metric", "네 곳 중 맞힌 수", "Correct calls out of four", "#duel", 1)
A = {k: g.n("lab:analogy/" + k, "Analogy", ko, en, anc, 1) for k, ko, en, anc in [
    ("thermometer-probe", "온도계를 한 방향으로만 옮기기", "Moving a thermometer along one axis", "#s1"),
    ("warmth-compass", "따뜻해지는 쪽 나침반", "Compass toward warmth", "#s2"),
    ("mesh-box-dye", "그물 상자와 물감", "Mesh box and dye", "#s3"),
    ("stream-paddle", "개울의 바람개비", "Paddle wheel in a stream", "#s4"),
    ("six-neighbours", "이웃 여섯 집 온도 비교", "Comparing with six neighbours", "#s5")]}
for a, t in zip(A.values(), [pdv, grad, divg, curl, lap]): g.e(a, "analogyOf", t, g.nodes[[n["id"] for n in g.nodes].index(a)]["anchor"])
L = {k: g.n("lab:limitation/" + k, "Limitation", ko, en, anc, 2) for k, ko, en, anc in [
    ("partials-axis-only", "편미분은 축 방향 셋만 봄", "Partials see only the three axes", "#s1"),
    ("gradient-scalar-only", "그래디언트는 숫자 밭에만", "Gradient applies to scalar fields only", "#s2"),
    ("divergence-misses-swirl", "발산은 소용돌이를 못 봄", "Divergence misses swirl", "#s3"),
    ("paddle-infinitesimal", "아주 작은 바람개비 가정", "Assumes an infinitesimal paddle", "#s4"),
    ("stencil-step-size", "h가 크면 근사가 어긋남", "Large h breaks the approximation", "#s5")]}
for a, l, b, anc in [(pdv, "partials-axis-only", grad, "#s1"), (grad, "gradient-scalar-only", divg, "#s2"), (divg, "divergence-misses-swirl", curl, "#s3")]:
    g.e(a, "hasLimitation", L[l], anc); g.e(L[l], "addressedBy", b, anc)
g.e(curl, "hasLimitation", L["paddle-infinitesimal"], "#s4"); g.e(lap, "hasLimitation", L["stencil-step-size"], "#s5")
for a, b in [(axes3, pdv), (pdv, grad), (grad, divg), (divg, curl), (grad, lap), (divg, lap)]: g.e(a, "prerequisiteOf", b, "#sum")
for c in (grad, divg, curl, lap): g.e(c, "derivedFrom", delop, "#map")
g.e(grad, "evaluatedOn", sfield, "#map"); g.e(divg, "evaluatedOn", vfield, "#map"); g.e(curl, "evaluatedOn", vfield, "#map"); g.e(lap, "evaluatedOn", sfield, "#map")
g.e(sfield, "partOf", axes3, "#map"); g.e(vfield, "partOf", axes3, "#map"); g.e(lvl, "relatedTo", grad, "#s2"); g.e(gd, "derivedFrom", grad, "#s2"); g.e(rhr, "partOf", curl, "#s4"); g.e(heat, "derivedFrom", lap, "#s5")
g.e(curl0, "relatedTo", grad, "#sum"); g.e(curl0, "relatedTo", curl, "#sum"); g.e(divcurl0, "relatedTo", divg, "#sum"); g.e(divcurl0, "relatedTo", curl, "#sum")
g.e(m_fd, "solves", pdv, "#s1"); g.e(m_box, "demonstratedBy", "lab:sim/p3-flux-box", "#s3"); g.e(m_pad, "demonstratedBy", "lab:sim/p3-paddle", "#s4"); g.e(m_nb6, "demonstratedBy", "lab:sim/p3-neighbours", "#s5")
for sid, ko, en, anc, tgt in [("p3-axes", "세 축 상자와 점의 주소", "3D box and point address", "#map", axes3), ("p3-thermometer", "온도계 실험", "Thermometer probe", "#s1", pdv), ("p3-compass", "나침반 실험(등위면과 그래디언트)", "Level surface and gradient", "#s2", grad),
                              ("p3-flux-box", "그물 상자 실험", "Flux box and dye", "#s3", divg), ("p3-paddle", "바람개비 실험", "Paddle wheel", "#s4", curl), ("p3-neighbours", "이웃 여섯 집 실험", "Six-neighbour stencil", "#s5", lap), ("p3-duel", "바람개비 대결", "Paddle duel", "#duel", curl)]:
    g.n("lab:sim/" + sid, "Simulation", ko, en, anc, 2); g.e(tgt, "demonstratedBy", "lab:sim/" + sid, anc)
g.e(m_box, "relatedTo", divg, "#s3"); g.e(m_pad, "relatedTo", curl, "#s4"); g.e(m_nb6, "relatedTo", lap, "#s5")
g.e(m_calc, "contrastsWith", m_look, "#duel"); g.e(m_calc, "evaluatedBy", met, "#duel"); g.e(m_look, "evaluatedBy", met, "#duel"); g.e(m_calc, "relatedTo", curl, "#duel")
q1 = g.n("lab:question/p3-one-symbol", "Question", "기호 ∇ 하나가 어떻게 오르막·샘·소용돌이·움푹함을 모두 잴까?", "How does one symbol measure slope, source, swirl and dip?", "#top", 1)
q2 = g.n("lab:question/p3-look-vs-curl", "Question", "화살표 겉모양으로 바람개비가 도는지 알 수 있나?", "Can arrow shape tell whether a paddle spins?", "#duel", 2)
g.e(delop, "raises", q1, "#top"); g.e(curl, "raises", q2, "#duel")
W = {k: g.work(k, ko, en) for k, ko, en in [
    ("matharium_del", "matharium — The Del Operator", "matharium — The Del Operator"),
    ("matharium_vecops", "matharium — The Vector Differential Operators", "matharium — The Vector Differential Operators"),
    ("knott1911life", "Knott 1911 Life of P. G. Tait", "Knott 1911 Life and Scientific Work of P. G. Tait"),
    ("song2019generative", "Song·Ermon 2019", "Song & Ermon 2019"),
    ("gonzalez2018digital", "Gonzalez·Woods 2018 Digital Image Processing", "Gonzalez & Woods 2018 Digital Image Processing")]}
C = [("lab:claim/del-four-operations", "∇ 하나가 붙는 방식에 따라 그래디언트·발산·회전·라플라시안을 만든다", "One del operator yields gradient, divergence, curl and Laplacian", "#map", delop, "matharium_del", "본문 전체"),
     ("lab:claim/curl-grad-zero", "그래디언트의 회전과 회전의 발산은 늘 0이다", "Curl of gradient and divergence of curl vanish", "#sum", curl0, "matharium_vecops", "How they connect"),
     ("lab:claim/nabla-name-1870", "나블라라는 이름은 1870년 W. R. 스미스가 하프 모양을 보고 테이트에게 제안했다", "The name nabla was suggested to Tait by W. R. Smith in 1870", "#map", delop, "knott1911life", "p. 145"),
     ("lab:claim/score-is-gradient", "점수 기반 생성 모델은 데이터 분포의 그래디언트(점수)를 추정해 그 방향으로 표본을 옮긴다", "Score-based models estimate and follow gradients of the data distribution", "#s2", grad, "song2019generative", "초록, 2장"),
     ("lab:claim/laplacian-filter-edges", "라플라시안 필터는 밝기가 급히 바뀌는 경계를 드러낸다", "The Laplacian filter highlights intensity edges", "#s5", lap, "gonzalez2018digital", "3장")]
for cid, ko, en, anc, tgt, wk, loc in C:
    g.n(cid, "Claim", ko, en, anc, 2, source=[{"ref": wk, "loc": loc}]); g.e(cid, "supports", tgt, anc); g.e(cid, "assertedIn", W[wk], anc)
for c in (pdv, grad, divg, curl, lap, delop): g.e(c, "broader", T_CALC, "#sum")
g.e(gd, "broader", T_GD, "#s2")
Q = [("s1", 1, pdv), ("s1", 2, pdv), ("s2", 1, lvl), ("s2", 2, gd), ("s3", 1, divg), ("s3", 2, divg), ("s4", 1, curl), ("s4", 2, curl0), ("s5", 1, lap), ("s5", 2, lap), ("duel", 1, curl)]
QL = {"s1": "편미분", "s2": "그래디언트", "s3": "발산", "s4": "회전", "s5": "라플라시안", "duel": "대결 바람개비"}
for sec, k, tgt in Q:
    qid = f"lab:quiz/p3-{sec}-{k}"; g.n(qid, "QuizItem", f"{QL[sec]} 문제 {k}", f"Quiz {sec}-{k}", "#" + sec, 2); g.e(qid, "assesses", tgt, "#" + sec)
g.dump(3)
used3 = {"matharium_del": [delop, grad, divg, curl, lap], "matharium_vecops": [curl0, divcurl0], "knott1911life": [delop], "song2019generative": [grad], "gonzalez2018digital": [lap]}
(B / "refs_3.json").write_text(json.dumps([REFS[k](v) for k, v in used3.items()], ensure_ascii=False, indent=1))
m3 = meta(3, "좌표축 위의 그릇 ③ 화살표 밭 편 — x·y·z 세 축 공간에서 읽는 ∇(나블라)",
    ["lab:concept/del-operator", "lab:concept/gradient", "lab:concept/divergence", "lab:concept/curl", "lab:concept/laplacian"], list(used3), "3_arrow_field.html")
m3.update({"date": "2026-11-16", "version": "1.0", "educationalLevel": "입문", "suggestedCitation": "안상선 (2026). 좌표축 위의 그릇 ③ 화살표 밭 편 — x·y·z 세 축 공간에서 읽는 ∇(나블라). 좌표축 위의 그릇 — 3D 지도로 본 모델 최적화 3, v1.0."})
(B / "meta_3.json").write_text(json.dumps(m3, ensure_ascii=False, indent=1))

# ══════════════ 목차 ══════════════
g = G("index")
land = g.n("lab:concept/loss-landscape", "Concept", "오차 지형", "Loss landscape", "#top", 1, "가중치마다 잰 오차를 높이로 세운 땅.")
axis = g.n("lab:concept/parameter-axis", "Concept", "좌표축(가중치 축)", "Parameter axis", "#top", 1, "가중치 하나가 지도의 축 하나.")
gd = g.n("lab:method/gradient-descent", "Method", "경사하강", "Gradient descent", "#chapters", 1, "기울기의 반대 방향으로 조금씩 걸어 오차를 줄이는 방법.")
hp = g.n("lab:concept/hyperparameter", "Concept", "하이퍼파라미터", "Hyperparameter", "#chapters", 1, "학습 전에 사람이 정하는 숫자.")
p1 = g.n("lab:section/series-part-1", "Section", "1편 수학 편", "Part 1: mathematics", "#chapters", 1)
p2 = g.n("lab:section/series-part-2", "Section", "2편 실험실 편", "Part 2: experiments", "#chapters", 1)
p3 = g.n("lab:section/series-part-3", "Section", "3편 화살표 밭 편", "Part 3: vector fields and del", "#chapters", 1)
delop0 = g.n("lab:concept/del-operator", "Concept", "나블라(∇) 연산자", "Del (nabla) operator", "#chapters", 1, "(∂/∂x, ∂/∂y, ∂/∂z). 그래디언트·발산·회전·라플라시안을 만드는 도구 묶음.")
g.e(delop0, "explainedIn", p3, "#chapters"); g.e(p1, "relatedTo", p3, "#chapters"); g.e(delop0, "broader", T_CALC, "#chapters")
q = g.n("lab:question/series", "Question", "학습을 오차 지도 위의 걷기로 볼 수 있을까?", "Can learning be read as walking on a loss map?", "#top", 1)
w = g.work("goodfellow2016deep", "Goodfellow 외 2016 Deep Learning", "Goodfellow et al. 2016 Deep Learning")
c = g.n("lab:claim/gd-on-loss", "Claim", "경사하강은 오차 함수의 기울기 반대 방향으로 가중치를 고친다", "Gradient descent moves weights against the loss gradient", "#top", 1, source=[{"ref": "goodfellow2016deep", "loc": "4.3"}])
g.e(axis, "partOf", land, "#top"); g.e(land, "explainedIn", p1, "#chapters"); g.e(hp, "explainedIn", p2, "#chapters"); g.e(gd, "explainedIn", p1, "#chapters")
g.e(p1, "prerequisiteOf", p2, "#chapters"); g.e(land, "raises", q, "#top"); g.e(c, "supports", gd, "#top"); g.e(c, "assertedIn", w, "#top"); g.e(gd, "broader", T_GD, "#top"); g.e(land, "broader", T_LOSS, "#top"); g.e(hp, "relatedTo", gd, "#chapters")
g.dump(0)
(B / "refs_0.json").write_text(json.dumps([REFS["goodfellow2016deep"](["lab:method/gradient-descent"])], ensure_ascii=False, indent=1))
m0 = meta(0, "좌표축 위의 그릇 — 3D 지도로 본 모델 최적화 (목차)", ["lab:concept/loss-landscape", "lab:method/gradient-descent", "lab:concept/hyperparameter"], ["goodfellow2016deep"], "")
(B / "meta_0.json").write_text(json.dumps(m0, ensure_ascii=False, indent=1))

for n in (0, 1, 2, 3):
    k = json.loads((B / f"kg_{n}.json").read_text()); ids = {x["id"] for x in k["nodes"]}
    deg = {i: 0 for i in ids}; rel = 0; bad = []
    for e in k["edges"]:
        if e["p"] == "lab:relatedTo": rel += 1
        for x in (e["s"], e["o"]):
            if x in deg: deg[x] += 1
            elif not x.startswith("lab:topic/"): bad.append(x)
    iso = [i for i, d in deg.items() if d == 0]
    print(f"page {n}: nodes {len(ids)} edges {len(k['edges'])} relatedTo {rel/len(k['edges']):.0%} isolated {iso} dangling {bad}")
