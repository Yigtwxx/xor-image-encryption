# XOR Image Encryption for Vision Pipelines

Deterministic, seed-based XOR masking for RGB images.
Built for fast dataset obfuscation, computer vision preprocessing, and reproducible experiments.

[![CI](https://github.com/Yigtwxx/xor-image-encryption/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/Yigtwxx/xor-image-encryption/actions/workflows/python-app.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Why this project

- Reproducible masking: the same seed always generates the same key.
- Lightweight: pure Python + NumPy + Pillow.
- Reversible: applying XOR with the same key restores the original image.
- Practical for ML workflows where visual obfuscation is needed before sharing data.

## What it is / What it is not

- What it is: a deterministic XOR masking tool for images.
- What it is not: a replacement for modern cryptographic standards like AES or ChaCha20.

## 60-second quickstart

### 1) Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Single-seed encryption + roundtrip

```bash
python xor_single.py --input bugsbunny.jpg --seed 42 --outdir outputs
```

### 3) Multi-seed cascaded encryption + roundtrip

```bash
python xor_multi.py --input bugsbunny.jpg --seeds 11 22 33 --outdir outputs
```

## Demo and sample outputs

- Demo animation: [assets/demo.gif](assets/demo.gif)
- Encrypted sample: [outputs/encrypted_seed42.png](outputs/encrypted_seed42.png)
- Decrypted sample: [outputs/decrypted_seed42.png](outputs/decrypted_seed42.png)
- Histogram (encrypted): [outputs/hist_encrypted.png](outputs/hist_encrypted.png)

## Technical docs

- Deep dive: [docs/TECHNICAL.md](docs/TECHNICAL.md)
- Security policy: [SECURITY.md](SECURITY.md)
- Contribution guide: [CONTRIBUTING.md](CONTRIBUTING.md)
- Code of conduct: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- GitHub operations checklist: [docs/GITHUB_OPERATION_CHECKLIST.md](docs/GITHUB_OPERATION_CHECKLIST.md)
- Release notes draft: [docs/RELEASE_NOTES_v0.1.0.md](docs/RELEASE_NOTES_v0.1.0.md)

## Recommended GitHub metadata

Use this in the repo "About" field:

`Seed-based XOR image encryption for deterministic dataset masking and computer vision preprocessing.`

Recommended topics:

`image-encryption`, `xor`, `computer-vision`, `dataset-anonymization`, `python`, `numpy`, `pillow`, `image-processing`, `reproducibility`, `cryptography-education`

## Roadmap

- CLI polish
- Batch dataset encryption
- Reproducible benchmark suite

See: [ROADMAP.md](ROADMAP.md)

## Call to action

If this project is useful:

- Star the repository
- Watch for updates
- Open a Discussion with your use case or benchmark
