import argparse
from pathlib import Path

import numpy as np
from PIL import Image


def load_rgb(path: Path) -> np.ndarray:
    """Load an image as RGB uint8 array."""
    return np.asarray(Image.open(path).convert("RGB"), dtype=np.uint8)


def save_rgb(arr: np.ndarray, path: Path) -> None:
    """Save an RGB uint8 array as an image."""
    Image.fromarray(arr, mode="RGB").save(path)


def make_key(shape: tuple[int, int, int], seed: int) -> np.ndarray:
    """Generate a deterministic uint8 key for a given shape and seed."""
    rng = np.random.default_rng(seed)
    return rng.integers(0, 256, size=shape, dtype=np.uint8)


def xor_encrypt(img: np.ndarray, key: np.ndarray) -> np.ndarray:
    """Apply XOR encryption/decryption at uint8 pixel level."""
    if img.shape != key.shape:
        raise ValueError(
            f"Image shape {img.shape} and key shape {key.shape} must match."
        )
    return np.bitwise_xor(img, key).astype(np.uint8)


def encrypt_with_seed(img: np.ndarray, seed: int) -> tuple[np.ndarray, np.ndarray]:
    """Encrypt an RGB image with a deterministic key derived from seed."""
    key = make_key(img.shape, seed)
    encrypted = xor_encrypt(img, key)
    return encrypted, key


def decrypt_with_seed(encrypted: np.ndarray, seed: int) -> np.ndarray:
    """Decrypt an RGB image by regenerating the same seed-derived key."""
    key = make_key(encrypted.shape, seed)
    return xor_encrypt(encrypted, key)


def plot_hist(arr: np.ndarray, outpath: Path, title: str) -> None:
    """Plot RGB histogram for a given image array."""
    import matplotlib.pyplot as plt

    flat = arr.reshape(-1, 3)
    plt.figure()
    plt.hist(flat[:, 0], bins=256, range=(0, 255), alpha=0.5, label="R")
    plt.hist(flat[:, 1], bins=256, range=(0, 255), alpha=0.5, label="G")
    plt.hist(flat[:, 2], bins=256, range=(0, 255), alpha=0.5, label="B")
    plt.title(title)
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.legend()
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Seed-based XOR image encryption / decryption"
    )
    parser.add_argument(
        "--input", required=True, help="Input image path (jpg/png/etc.)"
    )
    parser.add_argument("--seed", required=True, type=int, help="Random seed value")
    parser.add_argument("--outdir", required=True, help="Output directory")
    parser.add_argument("--no-hist", action="store_true", help="Do not save histograms")
    args = parser.parse_args()

    in_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    original = load_rgb(in_path)
    encrypted, key = encrypt_with_seed(original, args.seed)
    decrypted = xor_encrypt(encrypted, key)

    key_path = outdir / f"key_seed{args.seed}.png"
    enc_path = outdir / f"encrypted_seed{args.seed}.png"
    dec_path = outdir / f"decrypted_seed{args.seed}.png"

    save_rgb(key, key_path)
    save_rgb(encrypted, enc_path)
    save_rgb(decrypted, dec_path)

    if not args.no_hist:
        hist_original = outdir / "hist_original.png"
        hist_encrypted = outdir / "hist_encrypted.png"
        plot_hist(original, hist_original, "Original Histogram")
        plot_hist(encrypted, hist_encrypted, "Encrypted Histogram")

    print("=== XOR Image Encryption Complete ===")
    print(f"Input:      {in_path}")
    print(f"Seed:       {args.seed}")
    print(f"Key:        {key_path}")
    print(f"Encrypted:  {enc_path}")
    print(f"Decrypted:  {dec_path}")
    if not args.no_hist:
        print(
            f"Histograms: {outdir / 'hist_original.png'} , {outdir / 'hist_encrypted.png'}"
        )


if __name__ == "__main__":
    main()
