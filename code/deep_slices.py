"""2편 ③·④ 실험: 가중치가 수천 개인 신경망의 오차 지형을 '단면'으로 본다.

우리가 새로 짠 코드다(영상의 hyper.py를 옮긴 것이 아니다). 같은 아이디어만 빌렸다.
  - 신경망: 입력 4 → 64 → 64 → 1, 모든 층 tanh, 목표는 sin(첫 입력)
  - 데이터: 표준정규 입력 5,000개 → 훈련 4,000 / 검증 1,000
  - (A) 학습률 세 가지로 20 에포크, 배치 32
  - (B) 학습이 끝난 가중치 둘레의 2차원 단면(무작위 방향 두 개, 층별 크기 맞춤) 31×31
  - (C) 잡음 섞인 훈련 40개로 1,500 에포크 → 훈련·검증 오차가 갈라지는 곳
실행: python3 code/deep_slices.py  → build/deep.json
"""
import json, numpy as np, pathlib

SEED = 2026
L = [4, 64, 64, 1]

def init(rng):
    return [rng.normal(0, .2, (a, b)) for a, b in zip(L, L[1:])]

def forward(W, X):
    hs = [X]
    for w in W:
        hs.append(np.tanh(hs[-1] @ w))
    return hs

def mse(W, X, y):
    return float(np.mean((forward(W, X)[-1] - y) ** 2))

def step(W, X, y, lr):
    hs = forward(W, X)
    d = 2 * (hs[-1] - y) / len(X)            # ∂(평균제곱)/∂출력
    for k in range(len(W) - 1, -1, -1):
        d = d * (1 - hs[k + 1] ** 2)          # tanh의 기울기
        g = hs[k].T @ d
        d = d @ W[k].T
        W[k] = W[k] - lr * g
    return W

def train(X, y, Xv, yv, lr, batch, epochs, seed, every=1):
    rng = np.random.default_rng(seed)
    W = init(rng)
    W0 = [w.copy() for w in W]
    log = [(0, mse(W, X, y), mse(W, Xv, yv))]
    for ep in range(1, epochs + 1):
        order = rng.permutation(len(X))
        for i in range(0, len(X), batch):
            j = order[i:i + batch]
            W = step(W, X[j], y[j], lr)
            if not np.isfinite(W[0]).all():
                break
        if ep % every == 0 or ep == epochs or ep < 30:
            log.append((ep, mse(W, X, y), mse(W, Xv, yv)))
    return W0, W, log

rng = np.random.default_rng(SEED)
X = rng.normal(size=(5000, 4))
y = np.sin(X[:, :1])
Xt, Xv, yt, yv = X[:4000], X[4000:], y[:4000], y[4000:]
var = float(np.var(yv))
out = {"seed": SEED, "layers": L, "varTarget": round(var, 4), "lr": {}}

# (A) 학습률 세 가지
finals = {}
for lr in [1e-5, 0.1, 10.0]:
    W0, W, log = train(Xt, yt, Xv, yv, lr, 32, 20, SEED + 1)
    out["lr"][str(lr)] = [[e, round(a, 5), round(b, 5)] for e, a, b in log]
    finals[lr] = (W0, W)
    print(f"lr {lr:g}: 시작 검증 {log[0][2]:.4f} → 끝 {log[-1][2]:.4f}  (분산 대비 {log[-1][2]/var:.3%})")

# (B) 단면: 학습 끝(lr 0.1) 가중치 θ* 둘레, 방향 d1, d2는 층마다 θ*와 같은 크기로 맞춘다
W0, Ws = finals[0.1]
r2 = np.random.default_rng(SEED + 7)
def rand_dir():
    d = [r2.normal(size=w.shape) for w in Ws]
    return [di * (np.linalg.norm(w) / np.linalg.norm(di)) for di, w in zip(d, Ws)]
d1, d2 = rand_dir(), rand_dir()
n = 31; span = np.linspace(-1, 1, n)
grid = [[round(mse([w + a * u + b * v for w, u, v in zip(Ws, d1, d2)], Xv, yv), 4) for a in span] for b in span]
out["slice2d"] = {"n": n, "range": [-1, 1], "z": grid,
                  "center": round(mse(Ws, Xv, yv), 5)}
# 출발점 → 도착점 직선 단면
line = []
for t in np.linspace(-0.25, 1.25, 61):
    Wt = [a + t * (b - a) for a, b in zip(W0, Ws)]
    line.append([round(float(t), 3), round(mse(Wt, Xv, yv), 5)])
out["line"] = line
nparam = sum(w.size for w in Ws)
out["nparam"] = int(nparam)
print("가중치 수", nparam, "단면 가운데", out["slice2d"]["center"], "단면 최댓값", max(max(r) for r in grid))

# (C) 잡음 섞인 훈련 40개, 1,500 에포크 (배치 8, 학습률 0.1)
r3 = np.random.default_rng(SEED + 11)
Xs = r3.normal(size=(40, 4)); ys = np.sin(Xs[:, :1]) + r3.normal(0, 0.3, (40, 1))
_, _, log = train(Xs, ys, Xv, yv, 0.1, 8, 1500, SEED + 13, every=5)
out["overfit"] = [[e, round(a, 5), round(b, 5)] for e, a, b in log]
best = min(log, key=lambda t: t[2])
out["overfitBest"] = [best[0], round(best[1], 5), round(best[2], 5)]
print("과적합: 검증 최저 에포크", best[0], "검증", round(best[2], 4), "/ 1500 에포크 훈련", round(log[-1][1], 4), "검증", round(log[-1][2], 4))

pathlib.Path(__file__).resolve().parent.parent.joinpath("build", "deep.json").write_text(json.dumps(out, separators=(",", ":")))
