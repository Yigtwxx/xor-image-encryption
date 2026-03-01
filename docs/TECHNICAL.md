# Technical Deep Dive

## Scope

This project implements deterministic XOR masking for RGB images.
It is designed for visual obfuscation, reproducible preprocessing, and educational demonstrations.

## Data model

- Image type: RGB uint8 (`H x W x 3`)
- Key type: RGB uint8 (`H x W x 3`)
- Seed: integer used to initialize NumPy random generator (`np.random.default_rng`)

## Single-seed flow

1. Load image as RGB array.
2. Generate key with same shape using seed.
3. Encrypt with `encrypted = image XOR key`.
4. Decrypt with `decrypted = encrypted XOR key`.

Because XOR is involutive, applying the same key twice restores the original data.

## Multi-seed cascaded flow

Given seeds `s1, s2, ..., sn`:

- A deterministic stage key seed is derived from the ordered seed chain for each stage.
- Encryption: `E = XOR(...XOR(XOR(image, K1'), K2')..., Kn')`
- Decryption: apply stage keys in reverse order: `Kn' ... K2', K1'`

Order matters by design. Using the same seeds in a different order produces different stage
keys and fails to recover the original image.

## Determinism guarantee

For a fixed image shape and seed:

- `make_key(shape, seed)` is deterministic
- encryption output is deterministic
- decryption is deterministic when seed/seed-order is correct

## Complexity

For each XOR pass:

- Time: `O(H * W * 3)`
- Memory: `O(H * W * 3)` for image/key arrays

For multi-seed cascades with `n` seeds:

- Time: `O(n * H * W * 3)`

## Limitations

- This is not a modern cryptographic scheme and should not be used for high-security confidentiality needs.
- Seed secrecy is critical: if seed(s) are exposed, masked image is reversible.
- Histograms are for analysis/teaching and add I/O overhead.

## Public interfaces

### CLI

- `python xor_single.py --input <path> --seed <int> --outdir <dir> [--no-hist]`
- `python xor_multi.py --input <path> --seeds <int> <int> ... --outdir <dir> [--no-hist]`

### Python functions

- `xor_single.make_key(shape, seed)`
- `xor_single.xor_encrypt(img, key)`
- `xor_single.encrypt_with_seed(img, seed)`
- `xor_single.decrypt_with_seed(encrypted, seed)`
- `xor_multi.multi_encrypt(img, seeds)`
- `xor_multi.multi_decrypt(img, seeds)`
