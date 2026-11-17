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
 "mltut_math_behind_ai": lambda s: ref("mltut_math_behind_ai", "graphic", "Mathematics Behind AI", [{"literal": "ML Tut"}], role="background", supports=s,
        verified={"title": True, "author": True, "year": False, "url": False}, checked=USERSRC, note="계산 순서와 예시 숫자만 참고, 그림은 새로 그림"),
 "ahn_battery_factory": lambda s: ref("ahn_battery_factory", "webpage", "배터리 불량 분류기·수명 회귀 공장 편", [{"family": "안", "given": "상선"}], 2026, None, {"URL": "https://adminmrobo.github.io/how_to_make_ai_model_factory_version/classifier.html"}, role="background", supports=s,
        verified={"title": True, "author": True, "year": True, "url": True}, checked="2026-11-16"),
 "matharium_crisp": lambda s: ref("matharium_crisp", "graphic", "The geometry of a curved crisp", [{"literal": "matharium"}], role="primary", supports=s,
        verified={"title": True, "author": True, "year": False, "url": False}, checked=USERSRC, note="그림은 페이지에 넣지 않고 새로 그림"),
 "matheorems_coords": lambda s: ref("matheorems_coords", "graphic", "Gradient in Different Coordinate Systems", [{"literal": "@matheorems"}], role="primary", supports=s,
        verified={"title": True, "author": True, "year": False, "url": False}, checked=USERSRC),
 "matharium_vecops": lambda s: ref("matharium_vecops", "graphic", "The Vector Differential Operators", [{"literal": "matharium"}], role="primary", supports=s,
        verified={"title": True, "author": True, "year": False, "url": False}, checked=USERSRC),
 "matharium_del": lambda s: ref("matharium_del", "graphic", "The Del Operator", [{"literal": "matharium"}], role="primary", supports=s,
        verified={"title": True, "author": True, "year": False, "url": False}, checked=USERSRC, note="그림은 페이지에 넣지 않고 표로 다시 씀"),
 "knott1911life": lambda s: ref("knott1911life", "book", "Life and Scientific Work of Peter Guthrie Tait", [{"family": "Knott", "given": "Cargill Gilston"}],
        1911, None, {"publisher": "Cambridge University Press"}, supports=s, locs=[{"claim": "lab:claim/nabla-name-1870", "loc": "p. 145"}],
        verified={"title": True, "author": True, "year": True, "pages": False}, checked="웹 검색 2026-11-16 (Wikipedia 'Nabla symbol' 각주, Neumaier 'History of Nabla')"),
 "matharium_lagrange": lambda s: ref("matharium_lagrange", "graphic", "Lagrange Multipliers", [{"literal": "matharium"}], role="primary", supports=s,
        verified={"title": True, "author": True, "year": False, "url": False}, checked=USERSRC),
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
 "sciencesnow_gjh": lambda s: ref("sciencesnow_gjh", "graphic", "Gradient vs Jacobian vs Hessian", [{"literal": "Sciences Now"}], role="primary", supports=s,
        verified={"title": True, "author": True, "year": False, "url": False}, checked=USERSRC, note="그림은 페이지에 넣지 않고 표로 다시 씀"),
 "matharium_hessian": lambda s: ref("matharium_hessian", "graphic", "Hessian Matrix", [{"literal": "matharium"}], role="primary", supports=s,
        verified={"title": True, "author": True, "year": False, "url": False}, checked=USERSRC, note="인물 초상과 그림은 넣지 않음. 아래 고유값 그림의 알 모양은 그래프가 아니라 오해 소지가 있어 따르지 않음"),
 "wiki_hessian": lambda s: ref("wiki_hessian", "webpage", "Hessian matrix", [{"literal": "Wikipedia"}], container="Wikipedia", supports=s,
        extra={"URL": "https://en.wikipedia.org/wiki/Hessian_matrix"}, verified={"title": True, "url": True}, checked="웹 검색 2026-11-16 (MacTutor·Encyclopedia.com 교차 확인: 헤세 1811–1874, 이름은 실베스터)"),
 "nocedal2006numerical": lambda s: ref("nocedal2006numerical", "book", "Numerical Optimization", [{"family": "Nocedal", "given": "Jorge"}, {"family": "Wright", "given": "Stephen J."}],
        2006, None, {"publisher": "Springer", "edition": "2"}, supports=s, verified={"title": True, "author": True, "year": True}, checked="서지 정보 확인 2026-11-16"),
 "baydin2018automatic": lambda s: ref("baydin2018automatic", "article-journal", "Automatic Differentiation in Machine Learning: a Survey",
        [{"family": "Baydin", "given": "Atılım Güneş"}, {"family": "Pearlmutter", "given": "Barak A."}, {"family": "Radul", "given": "Alexey Andreyevich"}, {"family": "Siskind", "given": "Jeffrey Mark"}],
        2018, "Journal of Machine Learning Research", {"volume": "18", "issue": "153", "page": "1-43"}, supports=s, verified={"title": True, "author": True, "year": True}, checked="서지 정보 확인 2026-11-16"),
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
 "leibniz1684nova": lambda s: ref("leibniz1684nova", "article-journal", "Nova Methodus pro Maximis et Minimis", [{"family": "Leibniz", "given": "Gottfried Wilhelm"}], 1684, "Acta Eruditorum", {"volume": "3", "page": "467-473"}, supports=s,
        verified={"title": True, "author": True, "year": True, "pages": True}, checked="웹 검색 2026-11-16 (Wikipedia 'Nova Methodus pro Maximis et Minimis', Il Giardino di Archimede)"),
 "archimede_newton_leibniz": lambda s: ref("archimede_newton_leibniz", "webpage", "Newton and Leibniz: the birth of calculus", [{"literal": "Il Giardino di Archimede"}], None, None, {"URL": "https://archimede.dimai.unifi.it/archimede/archimede_NEW_inglese/mostra_calcolo/pannelli/3.html"}, supports=s,
        verified={"title": True, "author": True, "year": False, "url": True}, checked="웹 검색 2026-11-16"),
 "wiki_calculus_controversy": lambda s: ref("wiki_calculus_controversy", "webpage", "Leibniz–Newton calculus controversy", [{"literal": "Wikipedia"}], None, None, {"URL": "https://en.wikipedia.org/wiki/Leibniz%E2%80%93Newton_calculus_controversy"}, supports=s,
        verified={"title": True, "author": True, "year": False, "url": True}, checked="웹 검색 2026-11-16"),
 "het_neoclassicals": lambda s: ref("het_neoclassicals", "webpage", "The Neoclassicals — Introduction", [{"family": "Fonseca", "given": "Gonçalo L."}], None, "History of Economic Thought website", {"URL": "https://www.hetwebsite.net/het/essays/margrev/ncintro.htm"}, supports=s,
        verified={"title": True, "author": True, "year": False, "url": True}, checked="웹 검색 2026-11-16"),
 "bussotti2003genesis": lambda s: ref("bussotti2003genesis", "article-journal", "On the Genesis of the Lagrange Multipliers", [{"family": "Bussotti", "given": "P."}], 2003, "Journal of Optimization Theory and Applications", {"volume": "117", "issue": "3", "page": "453-459"}, supports=s,
        verified={"title": True, "author": True, "year": True, "pages": True}, checked="웹 검색 2026-11-16 (Harvard Knill 게시 PDF 첫 쪽)"),
 "lemarechal2012cauchy": lambda s: ref("lemarechal2012cauchy", "article-journal", "Cauchy and the Gradient Method", [{"family": "Lemaréchal", "given": "Claude"}], 2012, "Documenta Mathematica, Extra Volume ISMP", {"page": "251-254"}, supports=s,
        verified={"title": True, "author": True, "year": True, "pages": True}, checked="웹 검색 2026-11-16 (EMS Press 장 파일)"),
 "het_euler": lambda s: ref("het_euler", "webpage", "Euler's Theorem", [{"family": "Fonseca", "given": "Gonçalo L."}], None, "History of Economic Thought website", {"URL": "https://www.hetwebsite.net/het/essays/math/euler.htm"}, supports=s,
        verified={"title": True, "author": True, "year": False, "url": True}, checked="웹 검색 2026-11-16 (+ Britannica 'Philip Henry Wicksteed', Flux 1894 서평)"),
 "hoerl1970ridge": lambda s: ref("hoerl1970ridge", "article-journal", "Ridge Regression: Biased Estimation for Nonorthogonal Problems", [{"family": "Hoerl", "given": "Arthur E."}, {"family": "Kennard", "given": "Robert W."}], 1970, "Technometrics", {"volume": "12", "issue": "1", "page": "55-67", "DOI": "10.1080/00401706.1970.10488634"}, supports=s,
        verified={"title": True, "author": True, "year": True, "pages": True, "doi": True}, checked="웹 검색 2026-11-16 (MaRDI, CMU 사본)"),
 "cement_world": lambda s: ref("cement_world", "webpage", "시멘트 제조업 World", [{"literal": "adminmrobo"}], 2026, None, {"URL": "https://adminmrobo.github.io/smart_factory_world/cement/"}, role="background", supports=s,
        verified={"title": True, "author": True, "year": True, "url": True}, checked="2026-11-16 페이지 확인"),
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
    ("matharium_lagrange", "matharium — Lagrange Multipliers", "matharium — Lagrange Multipliers"),
    ("sciencesnow_gjh", "Sciences Now — Gradient vs Jacobian vs Hessian", "Sciences Now — Gradient vs Jacobian vs Hessian"),
    ("matharium_hessian", "matharium — Hessian Matrix", "matharium — Hessian Matrix"),
    ("wiki_hessian", "Wikipedia — Hessian matrix", "Wikipedia — Hessian matrix"),
    ("nocedal2006numerical", "Nocedal·Wright 2006 Numerical Optimization", "Nocedal & Wright 2006 Numerical Optimization"),
    ("baydin2018automatic", "Baydin 외 2018 자동미분 개관", "Baydin et al. 2018 AD survey"),
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
     ("lab:claim/hessian-symmetric", "2차 편미분이 연속이면 헤시안은 대칭이다(클레로·슈바르츠)", "The Hessian is symmetric when second partials are continuous", "#s3", hes, "sciencesnow_gjh", "Important Notes"),
     ("lab:claim/hessian-is-jacobian-of-gradient", "헤시안은 그래디언트의 야코비안이다", "The Hessian is the Jacobian of the gradient", "#gjh", hes, "wiki_hessian", "Relation to Jacobian"),
     ("lab:claim/hessian-name-sylvester", "헤시안은 헤세(1811–1874)의 이름을 따 실베스터가 붙인 이름이다", "Sylvester named the Hessian after Otto Hesse", "#s3", hes, "wiki_hessian", "도입부"),
     ("lab:claim/newton-one-step-quadratic", "2차 함수에서 뉴턴 걸음 θ − H⁻¹∇f는 한 번에 기울기 0인 점에 닿고, 큰 모델에서는 헤시안 근사(L-BFGS)를 쓴다", "Newton's step reaches the stationary point of a quadratic in one step; large problems use quasi-Newton approximations", "#s3", hes, "nocedal2006numerical", "3·6·7장"),
     ("lab:claim/reverse-mode-vjp", "역방향 자동미분은 벡터-야코비안 곱(VJP)을, 순방향은 야코비안-벡터 곱(JVP)을 구한다", "Reverse mode computes VJPs, forward mode computes JVPs", "#s5", bp, "baydin2018automatic", "3절"),
     ("lab:claim/hessian-definiteness-examples", "x² + y², x² − y², −(x² + y²)의 헤시안은 각각 양의 정부호(바닥)·부정부호(안장)·음의 정부호(봉우리)다", "Hessians of x²+y², x²−y², −(x²+y²) are positive definite, indefinite, negative definite", "#s3", hes, "matharium_hessian", "Geometry in two variables"),
     ("lab:claim/hessian-classifies", "헤시안 고유값이 임계점을 분류한다", "Hessian eigenvalues classify critical points", "#s3", hes, "matharium_gjh", "Hessian 칸"),
     ("lab:claim/saddles-proliferate-high-dim", "고차원 비볼록 지형에서는 나쁜 국소 최소보다 안장점이 문제를 일으킨다", "Saddle points, not local minima, proliferate in high dimensions", "#s4", sad, "dauphin2014identifying", "초록, 2장"),
     ("lab:claim/lr-limit-quadratic", "2차 함수에서 경사하강은 학습률이 2/λmax보다 작을 때 줄어든다", "GD converges on a quadratic iff lr < 2/λmax", "#s3", lim, "goodfellow2016deep", "4장"),
     ("lab:claim/backprop-1986", "역전파는 층마다의 기울기를 뒤에서부터 전해 가중치를 고친다", "Backpropagation adjusts weights by propagating error gradients", "#s5", bp, "rumelhart1986learning", "본문"),
     ("lab:claim/one-neuron-bowl", "뉴런 하나(w, b)의 평균제곱오차는 그릇 모양 2차 곡면이다", "MSE of a single linear neuron is a quadratic bowl", "#map", neuron, "mlfs39", "영상 설명")]
for cid, ko, en, anc, tgt, wk, loc in C:
    g.n(cid, "Claim", ko, en, anc, 2, source=[{"ref": wk, "loc": loc}]); g.e(cid, "supports", tgt, anc); g.e(cid, "assertedIn", W[wk], anc)
g.e(W["mlfs43"], "relatedTo", lr, "#s1")
# ── ⑥ 라그랑주 승수 ──
lgn = g.n("lab:concept/lagrangian", "Concept", "라그랑지안", "Lagrangian", "#s6", 2, "ℒ(x, λ) = f(x) − λg(x). 모든 변수와 λ로 편미분해 0으로 놓으면 ∇f = λ∇g와 g = 0.", alt=["ℒ"])
lmu = g.n("lab:concept/lagrange-multiplier", "Concept", "라그랑주 승수", "Lagrange multiplier", "#s6", 2, "제약 위 최적점에서 ∇f = λ∇g를 맞추는 배수.", alt=["λ"])
shp = g.n("lab:concept/shadow-price", "Concept", "그림자 가격", "Shadow price", "#s6-shadow", 2, "제약 한 단위의 값어치. λ = df*/dc.", alt=["잠재가격"])
cop = g.n("lab:concept/constrained-optimization", "Concept", "제약 있는 최적화", "Constrained optimization", "#s6", 2, "g(x) = 0을 지키면서 f(x)를 가장 크게 또는 작게 하는 문제.")
tng = g.n("lab:analogy/ridge-trail-touch", "Analogy", "둘레길에 스치는 등고선", "Contour touching the trail", "#s6", 1)
g.e(tng, "analogyOf", lmu, "#s6"); g.e(lgn, "partOf", cop, "#s6"); g.e(lmu, "partOf", lgn, "#s6"); g.e(lmu, "relatedTo", grad, "#s6"); g.e(grad, "prerequisiteOf", lmu, "#s6"); g.e(shp, "relatedTo", lmu, "#s6-shadow")
L6a = g.n("lab:limitation/lagrange-candidates-only", "Limitation", "∇f = λ∇g는 후보만 찾는다", "Tangency gives candidates only", "#s6", 2)
L6b = g.n("lab:limitation/lagrange-needs-grad-g", "Limitation", "후보 점에서 ∇g ≠ 0이어야 한다", "Needs a nonzero constraint gradient", "#s6", 2)
g.e(lmu, "hasLimitation", L6a, "#s6"); g.e(lmu, "hasLimitation", L6b, "#s6")
for sid, ko, en, anc, tgt in [("lab:sim/p1-lagrange-fence", "곡면 위 울타리와 ∇f·∇g", "Constraint curve on a surface with ∇f and ∇g", "#s6", lmu), ("lab:sim/p1-shadow-price", "울타리를 넓히면 — 그림자 가격", "Relaxing the constraint: shadow price", "#s6-shadow", shp)]:
    g.n(sid, "Simulation", ko, en, anc, 2); g.e(tgt, "demonstratedBy", sid, anc)
for cid, ko, en, anc, tgt in [("lab:claim/lagrange-tangency", "제약 위 최적점에서는 f의 등위선이 제약 곡선에 접하므로 ∇f = λ∇g이고, g = 0과 합쳐 n + 1개 식이 된다", "At a constrained optimum ∇f = λ∇g, giving n + 1 equations with g = 0", "#s6", lmu),
                              ("lab:claim/lagrange-circle-example", "원 x² + y² = 1 위에서 x + y의 최댓값은 (1/√2, 1/√2)에서 √2이다", "Max of x + y on the unit circle is √2 at (1/√2, 1/√2)", "#s6", lmu),
                              ("lab:claim/lambda-shadow-price", "λ는 제약을 풀 때 최적값이 바뀌는 빠르기로, 경제학에서 그림자 가격이라 부른다", "λ is the rate of change of the optimum as the constraint relaxes — the shadow price", "#s6-shadow", shp)]:
    g.n(cid, "Claim", ko, en, anc, 2, source=[{"ref": "matharium_lagrange", "loc": "인포그래픽 본문"}]); g.e(cid, "supports", tgt, anc); g.e(cid, "assertedIn", W["matharium_lagrange"], anc)
# 퀴즈
Q = [("s1", 1, gd), ("s1", 2, lim), ("s2", 1, nrm), ("s2", 2, grad), ("s3", 1, lim), ("s3", 2, sad), ("s3", 3, hes), ("s4", 1, lap), ("s4", 2, rul), ("s5", 1, jac), ("s5", 2, chain), ("s6", 1, lmu), ("s6", 2, shp), ("duel", 1, sad)]
QL = {"s1": "단면 위 한 걸음", "s2": "법선과 그래디언트", "s3": "굽음과 보폭", "s4": "안장과 라플라시안", "s5": "야코비안과 연쇄", "s6": "라그랑주 승수", "duel": "대결 안장점"}
for sec, k, tgt in Q:
    qid = f"lab:quiz/p1-{sec}-{k}"; g.n(qid, "QuizItem", f"{QL[sec]} 문제 {k}", f"Quiz {sec}-{k}", "#" + sec, 2); g.e(qid, "assesses", tgt, "#" + sec)
g.dump(1)
used1 = {"goyal2017accurate": [lr], "he2016deep": [bp], "ioffe2015batch": [bp], "matharium_crisp": [rul, hyp], "matharium_vecops": [curl0, lap], "matharium_del": [delop, divg, lap], "knott1911life": [delop], "matharium_gjh": [hes, jac, grad], "matharium_lagrange": [lmu, shp, lgn], "sciencesnow_gjh": [hes, jac, grad], "matharium_hessian": [hes], "wiki_hessian": [hes], "nocedal2006numerical": [hes], "baydin2018automatic": [bp], "matheorems_graph": [nrm, tan],
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
    ["lab:concept/loss-landscape", "lab:concept/gradient", "lab:concept/hessian", "lab:concept/saddle-point", "lab:concept/jacobian", "lab:concept/lagrange-multiplier"], list(used1), "1_math_map.html"), ensure_ascii=False, indent=1))
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
    ("matheorems_coords", "@matheorems — Gradient in Different Coordinate Systems", "@matheorems — Gradient in Different Coordinate Systems"),
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
# ── ⑥ 헬게이트: 원통·구면 좌표의 ∇ ──
cyl = g.n("lab:concept/cylindrical-coordinates", "Concept", "원통좌표", "Cylindrical coordinates", "#s6", 3, "(r, θ, z) — 바닥 거리, 방위각, 높이.")
sph = g.n("lab:concept/spherical-coordinates", "Concept", "구면좌표", "Spherical coordinates", "#s6", 3, "(r, θ, φ) — 원점 거리, 극각, 방위각. 책에 따라 θ·φ를 바꿔 씀.")
scf = g.n("lab:concept/scale-factor", "Concept", "배율(스케일 인자)", "Scale factor", "#s6", 3, "좌표 1만큼이 실제 거리 몇인가. 원통 (1, r, 1), 구면 (1, r, r sin θ).")
inv = g.n("lab:concept/gradient-invariance", "Concept", "좌표에 따라 변하지 않는 그래디언트", "Coordinate-invariant gradient", "#s6", 3, "가장 가파른 오르막은 하나 — 좌표계는 성분과 단위벡터만 바꾼다.")
g.e(grad, "prerequisiteOf", inv, "#s6"); g.e(cyl, "relatedTo", scf, "#s6"); g.e(sph, "relatedTo", scf, "#s6"); g.e(scf, "partOf", inv, "#s6")
g.n("lab:analogy/globe-degree", "Analogy", "적도와 극지방의 경도 1도", "One degree of longitude at the equator vs near the pole", "#s6", 2); g.e("lab:analogy/globe-degree", "analogyOf", scf, "#s6")
L6 = g.n("lab:limitation/coordinate-singularity", "Limitation", "r = 0, sin θ = 0에서 정의되지 않음", "Undefined at r = 0 and sin θ = 0", "#s6", 3); g.e(scf, "hasLimitation", L6, "#s6")
for sid, ko, en, anc, tgt in [("lab:sim/p3-coord-gradient", "같은 화살표, 다른 자 — 좌표계별 ∇V", "Same arrow, different rulers", "#s6", inv), ("lab:sim/p3-arc-length", "같은 각도, 다른 거리 — r·Δθ", "Same angle, different arc length", "#s6", scf)]:
    g.n(sid, "Simulation", ko, en, anc, 3); g.e(tgt, "demonstratedBy", sid, anc)
for cid, ko, en, tgt in [("lab:claim/grad-cylindrical", "원통좌표에서 ∇V = r̂ ∂V/∂r + θ̂ (1/r) ∂V/∂θ + ẑ ∂V/∂z", "Gradient in cylindrical coordinates", cyl),
                         ("lab:claim/grad-spherical", "구면좌표에서 ∇V = r̂ ∂V/∂r + θ̂ (1/r) ∂V/∂θ + φ̂ (1/(r sin θ)) ∂V/∂φ", "Gradient in spherical coordinates", sph)]:
    g.n(cid, "Claim", ko, en, "#s6", 3, source=[{"ref": "matheorems_coords", "loc": "인포그래픽 본문"}]); g.e(cid, "supports", tgt, "#s6"); g.e(cid, "assertedIn", W["matheorems_coords"], "#s6")
g.e(scf, "relatedTo", "lab:topic/feature-scaling", "#s6") if False else None
for c in (cyl, sph, scf, inv): g.e(c, "broader", T_CALC, "#s6")
Q = [("s6", 1, scf), ("s6", 2, inv), ("s1", 1, pdv), ("s1", 2, pdv), ("s2", 1, lvl), ("s2", 2, gd), ("s3", 1, divg), ("s3", 2, divg), ("s4", 1, curl), ("s4", 2, curl0), ("s5", 1, lap), ("s5", 2, lap), ("duel", 1, curl)]
QL = {"s1": "편미분", "s2": "그래디언트", "s3": "발산", "s4": "회전", "s5": "라플라시안", "s6": "헬게이트 좌표계", "duel": "대결 바람개비"}
for sec, k, tgt in Q:
    qid = f"lab:quiz/p3-{sec}-{k}"; g.n(qid, "QuizItem", f"{QL[sec]} 문제 {k}", f"Quiz {sec}-{k}", "#" + sec, 2); g.e(qid, "assesses", tgt, "#" + sec)
g.dump(3)
used3 = {"matharium_del": [delop, grad, divg, curl, lap], "matharium_vecops": [curl0, divcurl0], "knott1911life": [delop], "song2019generative": [grad], "gonzalez2018digital": [lap], "matheorems_coords": [cyl, sph, scf]}
(B / "refs_3.json").write_text(json.dumps([REFS[k](v) for k, v in used3.items()], ensure_ascii=False, indent=1))
m3 = meta(3, "좌표축 위의 그릇 ③ 화살표 밭 편 — x·y·z 세 축 공간에서 읽는 ∇(나블라)",
    ["lab:concept/del-operator", "lab:concept/gradient", "lab:concept/divergence", "lab:concept/curl", "lab:concept/laplacian", "lab:concept/scale-factor"], list(used3), "3_arrow_field.html")
m3.update({"date": "2026-11-18", "version": "1.2", "educationalLevel": "입문", "suggestedCitation": "안상선 (2026). 좌표축 위의 그릇 ③ 화살표 밭 편 — x·y·z 세 축 공간에서 읽는 ∇(나블라). 좌표축 위의 그릇 — 3D 지도로 본 모델 최적화 3, v1.1."})
(B / "meta_3.json").write_text(json.dumps(m3, ensure_ascii=False, indent=1))

# ══════════════ 최적화 첫걸음 ① ══════════════
FS = "최적화 첫걸음"
g = G("first_step_1")
slope = g.n("lab:concept/slope", "Concept", "기울기", "Slope", "#s0", 1, "올라간 양 ÷ 옆으로 간 거리.")
deriv = g.n("lab:concept/derivative", "Concept", "미분(도함수)", "Derivative", "#s11", 1, "간격을 0에 가깝게 줄였을 때의 기울기 = 접선의 기울기.", alt=["미분계수", "도함수"])
secant = g.n("lab:concept/secant-line", "Concept", "할선", "Secant line", "#s11", 1, "곡선 위 두 점을 이은 직선.")
tangent = g.n("lab:concept/tangent-line", "Concept", "접선", "Tangent line", "#s11", 1, "곡선에 한 점에서 닿는 직선.")
limit = g.n("lab:concept/limit", "Concept", "극한", "Limit", "#s22", 1, "한없이 가까워질 때 다가가는 끝값.")
marg = g.n("lab:concept/marginal", "Concept", "한계(marginal)", "Marginal", "#s12", 1, "하나 더 했을 때 늘어나는 양. 경제학에서 미분의 다른 이름.")
mc = g.n("lab:concept/marginal-cost", "Concept", "한계비용(MC)", "Marginal cost", "#s12", 1, "한 단위 더 만들 때 늘어나는 비용 = 총비용의 미분.")
mr = g.n("lab:concept/marginal-revenue", "Concept", "한계수입(MR)", "Marginal revenue", "#s32", 1, "한 단위 더 팔 때 늘어나는 수입. 완전경쟁이면 가격.")
stat = g.n("lab:concept/stationary-point", "Concept", "기울기 0인 점", "Stationary point", "#s13", 1, "꼭대기·바닥(·안장)의 후보.")
pdv = g.n("lab:concept/partial-derivative", "Concept", "편미분", "Partial derivative", "#s14", 1, "나머지는 고정하고 하나만 움직였을 때의 기울기.")
tdiff = g.n("lab:concept/total-differential", "Concept", "전미분", "Total differential", "#s14", 1, "모두 조금씩 움직였을 때의 변화 = 편미분 × 움직인 양의 합.")
mu = g.n("lab:concept/marginal-utility", "Concept", "한계효용", "Marginal utility", "#s23", 1, "하나 더 쓸 때 늘어나는 만족.")
mrev = g.n("lab:concept/marginal-revolution", "Concept", "한계혁명", "Marginal revolution", "#s23", 2, "1871–74년 제번스·멩거·왈라스가 한계효용으로 값어치를 설명한 일.")
fcvc = g.n("lab:concept/fixed-variable-cost", "Concept", "고정비·가변비", "Fixed and variable cost", "#s31", 1, "생산량과 무관한 비용과 생산량 따라 느는 비용.")
mrmc = g.n("lab:concept/mr-equals-mc", "Concept", "MR = MC", "MR equals MC", "#s32", 1, "이윤 최대의 1계 조건. MC가 MR을 아래에서 뚫고 올라가는 교점.")
shut = g.n("lab:concept/shutdown-point", "Concept", "조업중단점", "Shutdown point", "#s33", 1, "평균가변비용의 최저점. 가격이 이 밑이면 단기에도 문을 닫는다.")
beven = g.n("lab:concept/break-even-point", "Concept", "손익분기점", "Break-even point", "#s33", 1, "평균총비용의 최저점. 이윤 0.")
pc = g.n("lab:concept/perfect-competition", "Concept", "완전경쟁", "Perfect competition", "#c3", 1, "누구도 가격을 정하지 못하는 시장. MR = P.")
m_flip = g.n("lab:method/never-shut", "Method", "MR = MC, 문은 늘 연다", "MR = MC without shutdown", "#duel", 1, "판수는 MR = MC로 고르되, 가격이 조업중단점 밑이어도 문을 연다.")
m_mrmc = g.n("lab:method/mr-mc-rule", "Method", "MR = MC에서 멈추기 + 조업중단", "MR = MC rule with shutdown", "#duel", 1)
met = g.n("lab:metric/profit-sum", "Metric", "세 날 이윤 합", "Sum of profits over three days", "#duel", 1)
A = {k: g.n("lab:analogy/" + k, "Analogy", ko, en, anc, 1) for k, ko, en, anc in [
    ("speedometer", "속도계", "Speedometer", "#s11"), ("one-more-batch", "한 판 더", "One more batch", "#s12"),
    ("hilltop", "산꼭대기의 평평한 발밑", "Flat ground at the hilltop", "#s13"), ("field-area", "밭 넓이의 띠와 귀퉁이", "Strips and corner of a field", "#s14"),
    ("glass-of-water", "물 한 잔 더", "One more glass of water", "#s23"), ("rent-anyway", "닫아도 나가는 임대료", "Rent paid even when closed", "#s33")]}
for a, t in zip(A.values(), [deriv, mc, stat, tdiff, mu, shut]): g.e(a, "analogyOf", t, g.nodes[[n["id"] for n in g.nodes].index(a)]["anchor"])
L = {k: g.n("lab:limitation/" + k, "Limitation", ko, en, anc, 2) for k, ko, en, anc in [
    ("smooth-only", "매끄러운 곡선에서만 미분", "Differentiable only where smooth", "#s11"), ("discrete-vs-marginal", "한 판 더 ≠ 미분", "One more unit is not exactly the derivative", "#s12"),
    ("stationary-not-optimum", "기울기 0은 후보일 뿐", "Zero slope is only a candidate", "#s13"), ("short-run-only", "조업중단점은 단기 개념", "Shutdown is a short-run idea", "#s33"),
    ("price-taker", "완전경쟁 가정 (MR = P)", "Assumes price-taking (MR = P)", "#c3")]}
g.e(deriv, "hasLimitation", L["smooth-only"], "#s11"); g.e(mc, "hasLimitation", L["discrete-vs-marginal"], "#s12"); g.e(stat, "hasLimitation", L["stationary-not-optimum"], "#s13")
g.e(L["stationary-not-optimum"], "addressedBy", mrmc, "#s32"); g.e(shut, "hasLimitation", L["short-run-only"], "#s33"); g.e(mrmc, "hasLimitation", L["price-taker"], "#c3")
for a, b in [(slope, deriv), (deriv, marg), (deriv, stat), (deriv, pdv), (pdv, tdiff), (marg, mrmc), (stat, mrmc), (fcvc, shut), (mrmc, shut), (limit, deriv)]: g.e(a, "prerequisiteOf", b, "#sum")
g.e(secant, "partOf", deriv, "#s11"); g.e(tangent, "partOf", deriv, "#s11"); g.e(mc, "derivedFrom", marg, "#s12"); g.e(mr, "derivedFrom", marg, "#s32"); g.e(mu, "derivedFrom", marg, "#s23")
g.e(mrev, "relatedTo", mu, "#s23"); g.e(beven, "contrastsWith", shut, "#s33"); g.e(pc, "relatedTo", mr, "#c3"); g.e(mrmc, "relatedTo", mc, "#s32")
for sid, ko, en, anc, tgt in [("fs1-slope", "기울기 삼각형", "Slope triangle", "#s0", slope), ("fs1-secant", "할선을 접선으로", "Secant to tangent", "#s11", deriv), ("fs1-onemore", "한 판 더의 비용", "Cost of one more batch", "#s12", mc),
                              ("fs1-hill", "이윤 곡선의 기울기 0", "Zero slope on the profit curve", "#s13", stat), ("fs1-area", "밭 넓이의 전미분", "Total differential of area", "#s14", tdiff), ("fs1-limit", "h를 줄이는 표", "Shrinking h table", "#s22", limit),
                              ("fs1-mrmc", "MC와 가격의 교점", "MC meets price", "#s32", mrmc), ("fs1-shutdown", "문을 열까 닫을까", "Open or shut", "#s33", shut), ("fs1-duel", "빵 공장 대결", "Bakery duel", "#duel", shut)]:
    g.n("lab:sim/" + sid, "Simulation", ko, en, anc, 1); g.e(tgt, "demonstratedBy", "lab:sim/" + sid, anc)
g.e(m_mrmc, "contrastsWith", m_flip, "#duel"); g.e(m_mrmc, "evaluatedBy", met, "#duel"); g.e(m_flip, "evaluatedBy", met, "#duel"); g.e(m_mrmc, "relatedTo", mrmc, "#duel")
q1 = g.n("lab:question/fs-why", "Question", "미분은 왜 쓰나요?", "Why do we use derivatives?", "#prologue", 1)
q2 = g.n("lab:question/fs-when", "Question", "미분은 언제부터 있었어요?", "Since when has the derivative existed?", "#prologue", 1)
q3 = g.n("lab:question/fs-what", "Question", "미분으로 뭘 할 수 있어요?", "What can we do with derivatives?", "#prologue", 1)
g.e(deriv, "raises", q1, "#prologue"); g.e(limit, "raises", q2, "#prologue"); g.e(mrmc, "raises", q3, "#prologue")
W1 = {k: g.work(k, ko, en) for k, ko, en in [("leibniz1684nova", "라이프니츠 1684", "Leibniz 1684"), ("archimede_newton_leibniz", "아르키메데스 정원: 뉴턴과 라이프니츠", "Garden of Archimedes: Newton and Leibniz"),
    ("wiki_calculus_controversy", "미적분 우선권 논쟁", "Leibniz–Newton calculus controversy"), ("het_neoclassicals", "HET: 신고전학파 소개", "HET: The Neoclassicals"),
    ("bussotti2003genesis", "Bussotti 2003", "Bussotti 2003"), ("lemarechal2012cauchy", "Lemaréchal 2012", "Lemaréchal 2012"), ("het_euler", "HET: 오일러 정리", "HET: Euler's Theorem"),
    ("hoerl1970ridge", "Hoerl·Kennard 1970", "Hoerl & Kennard 1970"), ("rumelhart1986learning", "Rumelhart·Hinton·Williams 1986", "Rumelhart, Hinton & Williams 1986")]}
C1 = [("lab:claim/leibniz-first-publication", "1684년 라이프니츠의 논문이 미분을 다룬 첫 출판물이다", "Leibniz 1684 is the first publication on calculus", "#s21", deriv, "leibniz1684nova", "Acta Eruditorum 3"),
      ("lab:claim/newton-fluxions-1665", "뉴턴은 1665–66년에 유율법을 세웠고 1687년에 처음 출판했다", "Newton developed fluxions in 1665–66, first published 1687", "#s21", deriv, "archimede_newton_leibniz", "패널 3"),
      ("lab:claim/independent-invention", "두 사람이 따로 만들었다는 견해가 널리 받아들여진다", "Independent invention is widely accepted", "#s21", deriv, "wiki_calculus_controversy", "Hall 1980 인용"),
      ("lab:claim/marginal-revolution-1871", "제번스·멩거(1871)와 왈라스(1874)가 한계효용으로 값어치를 설명했다", "Jevons, Menger (1871) and Walras (1874) founded marginal utility theory", "#s23", mrev, "het_neoclassicals", "Introduction")]
for cid, ko, en, anc, tgt, wk, loc in C1:
    g.n(cid, "Claim", ko, en, anc, 2, source=[{"ref": wk, "loc": loc}]); g.e(cid, "supports", tgt, anc); g.e(cid, "assertedIn", W1[wk], anc)
for wk in ("bussotti2003genesis", "lemarechal2012cauchy", "het_euler", "hoerl1970ridge", "rumelhart1986learning"): g.e(W1[wk], "relatedTo", limit, "#s21")
for c in (deriv, pdv, tdiff, stat, limit): g.e(c, "broader", T_CALC, "#sum")
Q1 = [("s0", 1, slope), ("c1", 1, deriv), ("c1", 2, stat), ("c1", 3, pdv), ("c2", 1, deriv), ("c2", 2, mrev), ("c3", 1, mrmc), ("c3", 2, shut), ("duel", 1, shut)]
for sec, k, tgt in Q1:
    qid = f"lab:quiz/fs1-{sec}-{k}"; g.n(qid, "QuizItem", f"{sec} 문제 {k}", f"Quiz {sec}-{k}", "#" + sec, 1); g.e(qid, "assesses", tgt, "#" + sec)
g.dump(4)
used4 = {"leibniz1684nova": [deriv], "archimede_newton_leibniz": [deriv], "wiki_calculus_controversy": [deriv], "het_neoclassicals": [mrev], "bussotti2003genesis": [limit], "lemarechal2012cauchy": [limit], "het_euler": [limit], "hoerl1970ridge": [limit], "rumelhart1986learning": [limit]}
(B / "refs_4.json").write_text(json.dumps([REFS[k](v) for k, v in used4.items()], ensure_ascii=False, indent=1))
m4 = meta(4, "최적화 첫걸음 ① 혹시… 미분 좋아하세요? — 왜, 언제부터, 어디에", [deriv, marg, stat, mrmc, shut], list(used4), "first_step_1.html")
m4.update({"series": FS, "date": "2026-11-18", "version": "1.4", "educationalLevel": "입문", "suggestedCitation": "안상선 (2026). 최적화 첫걸음 ① 혹시… 미분 좋아하세요? — 왜, 언제부터, 어디에. 최적화 첫걸음 1, v1.4."})
(B / "meta_4.json").write_text(json.dumps(m4, ensure_ascii=False, indent=1))

# ══════════════ 최적화 첫걸음 ② ══════════════
g = G("first_step_2")
mp = g.n("lab:concept/marginal-product", "Concept", "한계생산", "Marginal product", "#s41", 1, "한 단위 더 투입할 때의 생산 증가 = 생산함수의 편미분.")
pdv = g.n("lab:concept/partial-derivative", "Concept", "편미분", "Partial derivative", "#s41", 1, "나머지는 고정하고 하나만 움직였을 때의 기울기.")
vmp = g.n("lab:concept/vmp-equals-wage", "Concept", "P × MP_L = w", "Value of marginal product equals wage", "#s41", 1, "한 명 더의 매출 = 임금에서 고용을 멈춘다.")
lag = g.n("lab:concept/lagrangian", "Concept", "라그랑지안", "Lagrangian", "#s42", 2, "목표 − λ × (제약). 편미분을 모두 0으로 놓아 푼다.")
lam = g.n("lab:concept/lagrange-multiplier", "Concept", "라그랑주 승수 λ", "Lagrange multiplier", "#s42", 2, "제약을 1단위 풀 때 목표가 바뀌는 양. 비용 최소화에서는 한계비용.")
iso = g.n("lab:concept/isoquant", "Concept", "등량선·등비용선", "Isoquant and isocost", "#s42", 1, "같은 생산량 곡선과 같은 비용 직선. 접하는 점이 가장 싼 조합.")
mc = g.n("lab:concept/marginal-cost", "Concept", "한계비용(MC)", "Marginal cost", "#s42", 1, "한 단위 더 만들 때 늘어나는 비용.")
crs = g.n("lab:concept/constant-returns", "Concept", "규모에 대한 수익 불변", "Constant returns to scale", "#s43", 1, "모든 투입을 t배 하면 생산도 t배.")
euler = g.n("lab:concept/euler-theorem", "Concept", "오일러 정리(생산물 소진)", "Euler's theorem (product exhaustion)", "#s43", 2, "1차 동차함수면 Q = MP_L·L + MP_K·K.")
ode = g.n("lab:concept/differential-equation", "Concept", "미분방정식", "Differential equation", "#s44", 2, "지금 상태가 변화 속도를 정하는 식.")
eulm = g.n("lab:method/euler-method", "Method", "오일러 방법(계단 풀이)", "Euler method", "#s44", 2, "짧은 Δt마다 기울기 × Δt만큼 이동해 미분방정식을 푼다.")
gd = g.n("lab:method/gradient-descent", "Method", "경사하강", "Gradient descent", "#s51", 1, "w ← w − 학습률 × 기울기.")
lr = g.n("lab:concept/learning-rate", "Concept", "학습률", "Learning rate", "#s51", 1, "경사하강의 보폭.")
chainr = g.n("lab:concept/chain-rule", "Concept", "연쇄법칙", "Chain rule", "#s52", 1, "이어진 함수의 미분 = 고리마다 미분의 곱.")
bp = g.n("lab:method/backpropagation", "Method", "역전파", "Backpropagation", "#s52", 2, "연쇄법칙의 곱을 손실에서부터 거꾸로 계산.")
nonlin = g.n("lab:concept/nonlinearity", "Concept", "비선형성", "Nonlinearity", "#s53", 1, "∂²y/∂x² ≠ 0. 제곱항으로 잡는다.")
inter = g.n("lab:concept/interaction", "Concept", "상호작용", "Interaction", "#s53", 1, "∂²y/∂x₁∂x₂ ≠ 0. 교차항으로 잡는다.")
fe = g.n("lab:concept/feature-engineering", "Concept", "특성공학", "Feature engineering", "#s53", 1, "모형에 넣을 입력(특성)을 만들고 고르는 일.")
reg = g.n("lab:concept/regularization", "Concept", "규제항(벌점)", "Regularization penalty", "#s54", 2, "가중치 크기에 매기는 벌점 λ|w|². 볼록 손실에서는 울타리 제약과 같은 답.")
m_sq = g.n("lab:method/square-terms", "Method", "제곱항 추가", "Add squared terms", "#duel", 1, "1, x₁, x₂, x₁², x₂².")
m_cross = g.n("lab:method/cross-term", "Method", "교차항 추가", "Add cross term", "#duel", 1, "1, x₁, x₂, x₁², x₁·x₂.")
met = g.n("lab:metric/validation-mse", "Metric", "검증 평균제곱오차", "Validation MSE", "#duel", 1)
A = {k: g.n("lab:analogy/" + k, "Analogy", ko, en, anc, 1) for k, ko, en, anc in [
    ("one-more-worker", "사람 한 명 더", "One more worker", "#s41"), ("cheapest-16t", "16톤을 가장 싸게", "16 tonnes at least cost", "#s42"), ("split-revenue", "매출 나눠 주기", "Splitting the revenue", "#s43"),
    ("cooling-coffee", "식는 커피", "Cooling coffee", "#s44"), ("foggy-mountain", "안개 낀 산 내려가기", "Descending a foggy mountain", "#s51"), ("flour-to-sales", "밀가루 값에서 매출까지", "From flour price to sales", "#s52"),
    ("fertilizer-water", "비료와 물", "Fertilizer and water", "#s53"), ("fence", "가중치 울타리", "A fence around the weights", "#s54")]}
for a, t in zip(A.values(), [vmp, lag, euler, ode, gd, chainr, inter, reg]): g.e(a, "analogyOf", t, g.nodes[[n["id"] for n in g.nodes].index(a)]["anchor"])
L = {k: g.n("lab:limitation/" + k, "Limitation", ko, en, anc, 2) for k, ko, en, anc in [
    ("short-run-capital", "단기(기계 고정)", "Short run with fixed capital", "#s41"), ("equality-constraint", "등식 제약만 (부등식은 KKT)", "Equality constraints only", "#s42"),
    ("crs-long-run", "규모수익불변·장기 경쟁", "Constant returns and long-run competition", "#s43"), ("convex-bowl", "그릇 모양 손실", "Bowl-shaped loss", "#s51"), ("convex-only", "볼록일 때만 같은 답", "Equivalent only when convex", "#s54")]}
g.e(vmp, "hasLimitation", L["short-run-capital"], "#s41"); g.e(L["short-run-capital"], "addressedBy", lag, "#s42"); g.e(lag, "hasLimitation", L["equality-constraint"], "#s42")
g.e(euler, "hasLimitation", L["crs-long-run"], "#s43"); g.e(gd, "hasLimitation", L["convex-bowl"], "#s51"); g.e(reg, "hasLimitation", L["convex-only"], "#s54")
for a, b in [(pdv, mp), (mp, vmp), (vmp, lag), (lag, lam), (crs, euler), (ode, gd), (gd, bp), (chainr, bp), (pdv, nonlin), (pdv, inter), (lag, reg)]: g.e(a, "prerequisiteOf", b, "#sum")
g.e(lam, "relatedTo", mc, "#s42"); g.e(iso, "partOf", lag, "#s42"); g.e(eulm, "solves", ode, "#s44"); g.e(gd, "relatedTo", eulm, "#s44"); g.e(lr, "partOf", gd, "#s51")
g.e(nonlin, "contrastsWith", inter, "#s53"); g.e(nonlin, "partOf", fe, "#s53"); g.e(inter, "partOf", fe, "#s53"); g.e(reg, "relatedTo", lag, "#s54")
for sid, ko, en, anc, tgt in [("fs2-hire", "사람 한 명 더 실험", "Hiring experiment", "#s41", vmp), ("fs2-isoquant", "등량선과 비용 직선", "Isoquant and isocost", "#s42", lag), ("fs2-euler", "매출 나누기 막대", "Revenue split bars", "#s43", euler),
                              ("fs2-ode", "커피·경사하강 계단 풀이", "Euler steps for coffee and descent", "#s44", ode), ("fs2-gd", "학습률 실험", "Learning-rate experiment", "#s51", gd), ("fs2-chain", "연쇄 세 고리", "Three-link chain", "#s52", chainr),
                              ("fs2-features", "특성과 두 번 미분", "Features and second derivatives", "#s53", inter), ("fs2-ridge", "울타리와 벌점", "Fence and penalty", "#s54", reg), ("fs2-duel", "제곱항 vs 교차항 대결", "Square vs cross-term duel", "#duel", inter)]:
    g.n("lab:sim/" + sid, "Simulation", ko, en, anc, 1); g.e(tgt, "demonstratedBy", "lab:sim/" + sid, anc)
g.e(m_cross, "contrastsWith", m_sq, "#duel"); g.e(m_cross, "evaluatedBy", met, "#duel"); g.e(m_sq, "evaluatedBy", met, "#duel"); g.e(m_cross, "relatedTo", inter, "#duel"); g.e(m_sq, "relatedTo", nonlin, "#duel")
q = g.n("lab:question/fs-how-much", "Question", "얼마만큼 생산하면 될까요?", "How much should we produce?", "#top", 1)
q2 = g.n("lab:question/fs-time-cost", "Question", "시간과 비용이 들어간 공정은 어떻게 최적화할까?", "How to optimize a process with time and cost?", "#epi", 2)
g.e(vmp, "raises", q, "#top"); g.e(ode, "raises", q2, "#epi")
W2 = {k: g.work(k, ko, en) for k, ko, en in [("bussotti2003genesis", "Bussotti 2003", "Bussotti 2003"), ("het_euler", "HET: 오일러 정리", "HET: Euler's Theorem"), ("lemarechal2012cauchy", "Lemaréchal 2012", "Lemaréchal 2012"),
    ("rumelhart1986learning", "Rumelhart·Hinton·Williams 1986", "Rumelhart, Hinton & Williams 1986"), ("hoerl1970ridge", "Hoerl·Kennard 1970", "Hoerl & Kennard 1970"), ("cement_world", "시멘트 제조업 World", "Cement manufacturing World")]}
C2 = [("lab:claim/lagrange-1788", "라그랑주 승수법은 1788년 『해석역학』에서 정식화됐다", "Lagrange multipliers were formulated in Mécanique analytique (1788)", "#s42", lag, "bussotti2003genesis", "본문 2절"),
      ("lab:claim/wicksteed-flux-1894", "윅스티드(1894)의 생산물 소진 주장을 플럭스가 오일러 정리로 짚었다", "Flux identified Wicksteed's product exhaustion with Euler's theorem (1894)", "#s43", euler, "het_euler", "본문"),
      ("lab:claim/cauchy-1847", "경사하강은 1847년 코시의 학술원 보고에서 처음 나왔다", "Gradient descent first appeared in Cauchy's 1847 note", "#s51", gd, "lemarechal2012cauchy", "p. 251"),
      ("lab:claim/backprop-1986", "역전파는 연쇄법칙으로 층마다의 기울기를 뒤에서부터 전한다", "Backpropagation propagates gradients backward via the chain rule", "#s52", bp, "rumelhart1986learning", "본문"),
      ("lab:claim/ridge-1970", "능형 회귀는 가중치 크기에 벌점을 더해 큰 계수를 누른다", "Ridge regression penalizes coefficient size", "#s54", reg, "hoerl1970ridge", "2절")]
for cid, ko, en, anc, tgt, wk, loc in C2:
    g.n(cid, "Claim", ko, en, anc, 2, source=[{"ref": wk, "loc": loc}]); g.e(cid, "supports", tgt, anc); g.e(cid, "assertedIn", W2[wk], anc)
g.e(W2["cement_world"], "relatedTo", ode, "#epi")
for c in (pdv, lag, lam, euler, ode, chainr): g.e(c, "broader", T_CALC, "#sum")
g.e(gd, "broader", T_GD, "#s51"); g.e(bp, "broader", T_BP, "#s52"); g.e(fe, "broader", "lab:topic/feature-engineering", "#s53"); g.e(reg, "broader", "lab:topic/weight-decay", "#s54")
Q2 = [("c4", 1, vmp), ("c4", 2, lam), ("c4", 3, euler), ("c5", 1, lr), ("c5", 2, chainr), ("c5", 3, inter), ("duel", 1, inter)]
for sec, k, tgt in Q2:
    qid = f"lab:quiz/fs2-{sec}-{k}"; g.n(qid, "QuizItem", f"{sec} 문제 {k}", f"Quiz {sec}-{k}", "#" + sec, 1); g.e(qid, "assesses", tgt, "#" + sec)
g.dump(5)
used5 = {"bussotti2003genesis": [lag], "het_euler": [euler], "lemarechal2012cauchy": [gd], "rumelhart1986learning": [bp], "hoerl1970ridge": [reg], "cement_world": [ode]}
(B / "refs_5.json").write_text(json.dumps([REFS[k](v) for k, v in used5.items()], ensure_ascii=False, indent=1))
m5 = meta(5, "최적화 첫걸음 ② 공장에서 인공지능까지", [vmp, lag, euler, gd, inter], list(used5), "first_step_2.html")
m5.update({"series": FS, "date": "2026-11-16", "version": "1.3", "educationalLevel": "입문", "suggestedCitation": "안상선 (2026). 최적화 첫걸음 ② 공장에서 인공지능까지. 최적화 첫걸음 2, v1.3."})
(B / "meta_5.json").write_text(json.dumps(m5, ensure_ascii=False, indent=1))


# ══════════════ 최적화 첫걸음 ⓪ ══════════════
g = G("first_step_0")
# ── 0 서론: 모델은 한 번에 만들어지지 않는다 ──
nrn = g.n("lab:concept/artificial-neuron", "Concept", "인공 뉴런", "Artificial neuron", "#s01", 1, "입력 × 가중치의 합에 편향을 더하고 활성화 함수를 거친 값.")
sigm = g.n("lab:concept/sigmoid", "Concept", "시그모이드", "Sigmoid", "#s01", 1, "어떤 수든 0과 1 사이로 접는 S자 함수.")
itr = g.n("lab:concept/iterative-training", "Concept", "반복 학습(한 걸음씩 고치기)", "Iterative training", "#s02", 1, "오차의 기울기 반대쪽으로 가중치를 조금씩 고치는 일을 여러 번 되풀이한다.")
gd0 = g.n("lab:method/gradient-descent", "Method", "경사하강", "Gradient descent", "#s02", 1, "기울기의 반대 방향으로 조금씩 걸어 오차를 줄이는 방법.")
tvs = g.n("lab:concept/train-validation-split", "Concept", "훈련·검증 나누기", "Train/validation split", "#s03", 1, "손에 쥔 데이터를 배우는 몫과 점검하는 몫으로 나눈다. 시험 몫은 끝까지 봉인.")
rec = g.n("lab:concept/recall", "Concept", "재현율", "Recall", "#s03", 1, "진짜 불량 가운데 모델이 잡아낸 비율.")
ovf = g.n("lab:concept/overfitting", "Concept", "과적합(외우기)", "Overfitting", "#s03", 1, "훈련 오차는 계속 줄지만 처음 보는 데이터에서는 나빠지는 상태.")
piv = g.n("lab:method/re-tuning", "Method", "되돌아가 다시 정비하기(피봇팅)", "Going back and re-tuning (pivoting)", "#s04", 1, "데이터가 바뀌면 그대로 쓰기·처음부터 다시 배우기·이어서 고치기(미세조정) 가운데 고른다.")
shift = g.n("lab:concept/distribution-shift", "Concept", "분포 이동", "Distribution shift", "#s04", 1, "재료·공정이 바뀌어 새 데이터가 훈련 때와 다르게 생긴 상황.")
L0 = g.n("lab:limitation/train-loss-only", "Limitation", "훈련 오차만 보고 고르기", "Choosing by training loss only", "#s03", 2)
g.e(nrn, "relatedTo", sigm, "#s01"); g.e(itr, "relatedTo", gd0, "#s02"); g.e(itr, "prerequisiteOf", tvs, "#s03")
g.e(ovf, "relatedTo", tvs, "#s03"); g.e(rec, "partOf", tvs, "#s03"); g.e(gd0, "hasLimitation", L0, "#s03"); g.e(L0, "addressedBy", tvs, "#s03")
g.e(shift, "relatedTo", piv, "#s04"); g.e(itr, "prerequisiteOf", piv, "#s04")
for sid, ko, en, anc, tgt in [("fs0-neuron", "뉴런 하나 계산", "One neuron calculator", "#s01", nrn), ("fs0-train", "반복 학습 대시보드", "Iterative training dashboard", "#s02", itr),
                              ("fs0-scorecard", "여러 측면 성적표", "Multi-metric scorecard", "#s03", ovf), ("fs0-pivot", "공장 B에서 다시 정비", "Re-tuning for factory B", "#s04", piv)]:
    g.n("lab:sim/" + sid, "Simulation", ko, en, anc, 1); g.e(tgt, "demonstratedBy", "lab:sim/" + sid, anc)
q0 = g.n("lab:question/fs-intro", "Question", "고칠 방향은 누가 알려 주나?", "Who tells the model which way to adjust?", "#c0", 1)
g.e(itr, "raises", q0, "#c0"); g.e(gd0, "relatedTo", q0, "#c0")
nxt = g.n("lab:section/first-step-1", "Section", "다음 편: 혹시… 미분 좋아하세요?", "Next: Do you like derivatives?", "#sum", 1)
g.e(q0, "explainedIn", nxt, "#sum")
g.e(gd0, "broader", T_GD, "#s02"); g.e(tvs, "broader", "lab:topic/data-splitting", "#s03"); g.e(rec, "broader", "lab:topic/precision-recall", "#s03")
g.e(ovf, "broader", "lab:topic/generalization", "#s03"); g.e(piv, "broader", "lab:topic/transfer-learning", "#s04"); g.e(shift, "broader", "lab:topic/distribution-shift", "#s04")
g.e(nrn, "broader", "lab:topic/perceptron", "#s01"); g.e(sigm, "broader", "lab:topic/activation-function", "#s01")
W0 = {k: g.work(k, ko, en) for k, ko, en in [("mltut_math_behind_ai", "ML Tut: Mathematics Behind AI", "ML Tut: Mathematics Behind AI"), ("ahn_battery_factory", "배터리 불량 분류기 공장 편", "Battery defect classifier factory")]}
g.e(W0["mltut_math_behind_ai"], "relatedTo", nrn, "#s01"); g.e(W0["ahn_battery_factory"], "relatedTo", tvs, "#s03"); g.e(W0["ahn_battery_factory"], "relatedTo", piv, "#s04")
for k, tgt in [(1, itr), (2, tvs), (3, piv)]:
    qid = f"lab:quiz/fs0-c0-{k}"; g.n(qid, "QuizItem", f"c0 문제 {k}", f"Quiz c0-{k}", "#c0", 1); g.e(qid, "assesses", tgt, "#c0")
g.dump(6)
used6 = {"mltut_math_behind_ai": [nrn], "ahn_battery_factory": [tvs, piv]}
(B / "refs_6.json").write_text(json.dumps([REFS[k](v) for k, v in used6.items()], ensure_ascii=False, indent=1))
m6 = meta(6, "최적화 첫걸음 ⓪ 인공지능 모델에서의 최적화 — 모델은 한 번에 만들어지지 않는다", [itr, tvs, piv], list(used6), "first_step_0.html")
m6.update({"series": FS, "number": "0", "date": "2026-11-18", "version": "1.0", "educationalLevel": "입문", "suggestedCitation": "안상선 (2026). 최적화 첫걸음 ⓪ 인공지능 모델에서의 최적화 — 모델은 한 번에 만들어지지 않는다. 최적화 첫걸음 0, v1.0."})
(B / "meta_6.json").write_text(json.dumps(m6, ensure_ascii=False, indent=1))

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
g.e(delop0, "explainedIn", p3, "#chapters");
fs0 = g.n("lab:section/first-step-0", "Section", "최적화 첫걸음 ⓪ — 인공지능 모델에서의 최적화", "First step to optimization 0: optimization in AI models", "#firststep", 1)
fs1 = g.n("lab:section/first-step-1", "Section", "최적화 첫걸음 ① — 혹시… 미분 좋아하세요?", "First step to optimization 1: do you like derivatives?", "#firststep", 1)
fs2 = g.n("lab:section/first-step-2", "Section", "최적화 첫걸음 ② — 공장에서 인공지능까지", "First step to optimization 2: from factories to AI", "#firststep", 1)
der0 = g.n("lab:concept/derivative", "Concept", "미분", "Derivative", "#firststep", 1, "아주 짧은 순간의 기울기.")
g.e(der0, "explainedIn", fs1, "#firststep"); g.e(fs0, "prerequisiteOf", fs1, "#firststep"); g.e(fs1, "prerequisiteOf", fs2, "#firststep"); g.e(fs2, "prerequisiteOf", p1, "#firststep"); g.e(der0, "broader", T_CALC, "#firststep"); g.e(p1, "relatedTo", p3, "#chapters"); g.e(delop0, "broader", T_CALC, "#chapters")
q = g.n("lab:question/series", "Question", "학습을 오차 지도 위의 걷기로 볼 수 있을까?", "Can learning be read as walking on a loss map?", "#top", 1)
w = g.work("goodfellow2016deep", "Goodfellow 외 2016 Deep Learning", "Goodfellow et al. 2016 Deep Learning")
c = g.n("lab:claim/gd-on-loss", "Claim", "경사하강은 오차 함수의 기울기 반대 방향으로 가중치를 고친다", "Gradient descent moves weights against the loss gradient", "#top", 1, source=[{"ref": "goodfellow2016deep", "loc": "4.3"}])
g.e(axis, "partOf", land, "#top"); g.e(land, "explainedIn", p1, "#chapters"); g.e(hp, "explainedIn", p2, "#chapters"); g.e(gd, "explainedIn", p1, "#chapters")
g.e(p1, "prerequisiteOf", p2, "#chapters"); g.e(land, "raises", q, "#top"); g.e(c, "supports", gd, "#top"); g.e(c, "assertedIn", w, "#top"); g.e(gd, "broader", T_GD, "#top"); g.e(land, "broader", T_LOSS, "#top"); g.e(hp, "relatedTo", gd, "#chapters")
g.dump(0)
(B / "refs_0.json").write_text(json.dumps([REFS["goodfellow2016deep"](["lab:method/gradient-descent"])], ensure_ascii=False, indent=1))
m0 = meta(0, "좌표축 위의 그릇 — 3D 지도로 본 모델 최적화 (목차)", ["lab:concept/loss-landscape", "lab:method/gradient-descent", "lab:concept/hyperparameter"], ["goodfellow2016deep"], "")
(B / "meta_0.json").write_text(json.dumps(m0, ensure_ascii=False, indent=1))

for n in (0, 1, 2, 3, 4, 5, 6):
    k = json.loads((B / f"kg_{n}.json").read_text()); ids = {x["id"] for x in k["nodes"]}
    deg = {i: 0 for i in ids}; rel = 0; bad = []
    for e in k["edges"]:
        if e["p"] == "lab:relatedTo": rel += 1
        for x in (e["s"], e["o"]):
            if x in deg: deg[x] += 1
            elif not x.startswith("lab:topic/"): bad.append(x)
    iso = [i for i, d in deg.items() if d == 0]
    print(f"page {n}: nodes {len(ids)} edges {len(k['edges'])} relatedTo {rel/len(k['edges']):.0%} isolated {iso} dangling {bad}")
