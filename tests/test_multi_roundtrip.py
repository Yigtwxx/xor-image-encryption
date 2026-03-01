import numpy as np

from xor_multi import multi_decrypt, multi_encrypt


def _random_rgb(seed: int = 321) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return rng.integers(0, 256, size=(20, 30, 3), dtype=np.uint8)


def test_multi_seed_roundtrip_restores_original() -> None:
    image = _random_rgb()
    seeds = [11, 22, 33]

    encrypted = multi_encrypt(image, seeds)
    decrypted = multi_decrypt(encrypted, seeds)

    assert np.array_equal(decrypted, image)


def test_multi_seed_order_is_sensitive() -> None:
    image = _random_rgb(seed=567)
    seeds = [7, 14, 21]

    encrypted = multi_encrypt(image, seeds)
    wrong_order_decrypted = multi_decrypt(encrypted, list(reversed(seeds)))

    assert not np.array_equal(wrong_order_decrypted, image)
