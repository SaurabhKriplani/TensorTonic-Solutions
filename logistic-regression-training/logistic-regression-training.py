import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    m, n = X.shape
    
    w = np.zeros(n)
    b = 0.0

    for i in range(steps):
        z = np.dot(X, w) + b
        p = _sigmoid(z)

        dl_dw = 1/m * np.dot(X.T, (p-y))
        dl_db = 1/m * np.sum(p-y)

        w -= lr*dl_dw
        b -= lr*dl_db

    return w, b