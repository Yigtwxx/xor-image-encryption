# xor-image-encryption
A simple image encryption and decryption tool using XOR with seed-based key generation. Supports RGB pixel-level encryption, histogram analysis, and multi-seed operations.

<p align="center"> <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" /> <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge" /> <img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" /> <img src="https://img.shields.io/badge/Security-XOR%20Encryption-orange?style=for-the-badge" /> </p>

Seed-based, reversible, RGB-level XOR encryption for fast and lightweight image security.
Designed for dataset anonymization, research pipelines, demos, and educational cryptography.

🌟 Key Capabilities
✅ Seed-Based Key Generation

Deterministic masks derived from integer seeds

Guarantees reversible encryption

Ideal for reproducible datasets

✅ RGB Channel XOR Engine

8-bit XOR for each RGB channel

Ultra-fast CPU performance

Fully reversible with the same seed

✅ Multi-Layer Encryption (xor_multi.py)

Cascaded multiple-seed encryption

Higher diffusion and entropy

Still perfectly reversible

✅ Single-Layer Encryption (xor_single.py)

Clean and simple one-pass XOR engine

Great for small demos or fast obfuscation

✅ Organized Output Directory

All encrypted and decrypted files stored in /outputs
