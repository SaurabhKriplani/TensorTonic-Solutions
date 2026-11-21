import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:

    if len(seqs) == 0:
        return np.empty((0, max_len if max_len is not None else 0), dtype=int)

    seqs = [list(seq) for seq in seqs]

    if max_len is None:
        max_len = max(len(seq) for seq in seqs)

    for i in range(len(seqs)):
        if len(seqs[i]) < max_len:
            seqs[i].extend([pad_value] * (max_len - len(seqs[i])))
        else:
            del seqs[i][max_len:]

    return np.array(seqs, dtype=int)