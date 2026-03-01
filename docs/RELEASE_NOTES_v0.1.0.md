# v0.1.0 Release Notes (Draft)

## Highlights

- Deterministic single-seed XOR masking for RGB images
- Cascaded multi-seed XOR masking with order-sensitive decryption
- New technical documentation and contribution guides
- CI pipeline across Python 3.10, 3.11, and 3.12
- Test coverage for roundtrip and determinism guarantees

## Security note

This project is designed for lightweight reversible masking, not as a replacement for modern encryption standards (AES/ChaCha20).

## Example usage

```bash
python xor_single.py --input bugsbunny.jpg --seed 42 --outdir outputs
python xor_multi.py --input bugsbunny.jpg --seeds 11 22 33 --outdir outputs
```
