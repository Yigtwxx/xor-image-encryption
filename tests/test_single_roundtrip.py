import numpy as np

from xor_single import decrypt_with_seed, encrypt_with_seed, xor_encrypt


def _random_rgb(seed: int = 123) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return rng.integers(0, 256, size=(32, 24, 3), dtype=np.uint8)


def test_single_seed_roundtrip_restores_original() -> None:
    image = _random_rgb()
    encrypted, key = encrypt_with_seed(image, seed=42)
    decrypted = xor_encrypt(encrypted, key)

    assert np.array_equal(decrypted, image)


def test_decrypt_with_seed_restores_original() -> None:
    image = _random_rgb(seed=999)
    encrypted, _ = encrypt_with_seed(image, seed=2025)
    decrypted = decrypt_with_seed(encrypted, seed=2025)

    assert np.array_equal(decrypted, image)
