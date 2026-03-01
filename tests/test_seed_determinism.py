import numpy as np

from xor_single import make_key


def test_same_seed_produces_same_key() -> None:
    shape = (16, 16, 3)
    key_a = make_key(shape, seed=42)
    key_b = make_key(shape, seed=42)

    assert np.array_equal(key_a, key_b)


def test_different_seed_produces_different_key() -> None:
    shape = (16, 16, 3)
    key_a = make_key(shape, seed=1)
    key_b = make_key(shape, seed=2)

    assert not np.array_equal(key_a, key_b)
