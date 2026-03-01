import argparse
import hashlib
from pathlib import Path

import numpy as np

from xor_single import load_rgb, make_key, plot_hist, save_rgb, xor_encrypt


def _derive_stage_seeds(seeds: list[int]) -> list[int]:
    """Derive deterministic per-stage seeds from the ordered seed sequence."""
    chain = b"xor-image-encryption"
    stage_seeds: list[int] = []

    for index, seed in enumerate(seeds, start=1):
        payload = chain + f"|stage={index}|seed={seed}".encode("utf-8")
        digest = hashlib.sha256(payload).digest()
        stage_seed = int.from_bytes(digest[:8], byteorder="big", signed=False)
        stage_seeds.append(stage_seed)
        chain = digest

    return stage_seeds


def multi_encrypt(img: np.ndarray, seeds: list[int]) -> np.ndarray:
    """Apply cascaded XOR encryption in seed order (order-sensitive keys)."""
    encrypted = img.copy()
    for stage_seed in _derive_stage_seeds(seeds):
        key = make_key(encrypted.shape, stage_seed)
        encrypted = xor_encrypt(encrypted, key)
    return encrypted


def multi_decrypt(img: np.ndarray, seeds: list[int]) -> np.ndarray:
    """Decrypt cascaded XOR encryption by reversing stage order."""
    decrypted = img.copy()
    stage_seeds = _derive_stage_seeds(seeds)
    for stage_seed in reversed(stage_seeds):
        key = make_key(decrypted.shape, stage_seed)
        decrypted = xor_encrypt(decrypted, key)
    return decrypted


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Seed-based XOR image encryption / decryption (multi-seed)"
    )
    parser.add_argument("--input", required=True, help="Input image path (jpg/png)")
    parser.add_argument(
        "--seeds",
        required=True,
        nargs="+",
        type=int,
        help="Seed values (multiple values allowed)",
    )
    parser.add_argument("--outdir", required=True, help="Output directory")
    parser.add_argument("--no-hist", action="store_true", help="Do not save histograms")
    args = parser.parse_args()

    in_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    original = load_rgb(in_path)
    encrypted = original.copy()

    stage_seeds = _derive_stage_seeds(args.seeds)
    for index, (seed, stage_seed) in enumerate(zip(args.seeds, stage_seeds), start=1):
        layer_key = make_key(original.shape, stage_seed)
        save_rgb(layer_key, outdir / f"key_seed{seed}_stage{index}.png")
        encrypted = xor_encrypt(encrypted, layer_key)

    decrypted = multi_decrypt(encrypted, args.seeds)
    seeds_label = "-".join(str(seed) for seed in args.seeds)

    enc_path = outdir / f"multi_encrypted_seeds_{seeds_label}.png"
    dec_path = outdir / f"multi_decrypted_seeds_{seeds_label}.png"

    save_rgb(encrypted, enc_path)
    save_rgb(decrypted, dec_path)

    if not args.no_hist:
        plot_hist(
            original,
            outdir / f"hist_original_seeds_{seeds_label}.png",
            f"Original Histogram (seeds={seeds_label})",
        )
        plot_hist(
            encrypted,
            outdir / f"hist_encrypted_seeds_{seeds_label}.png",
            f"Encrypted Histogram (seeds={seeds_label})",
        )

    print("=== Multi-Seed XOR Image Encryption Complete ===")
    print(f"Input:      {in_path}")
    print(f"Seeds:      {args.seeds}")
    print(f"Encrypted:  {enc_path}")
    print(f"Decrypted:  {dec_path}")


if __name__ == "__main__":
    main()
