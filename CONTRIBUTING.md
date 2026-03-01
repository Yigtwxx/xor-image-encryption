# Contributing

Thanks for contributing to `xor-image-encryption`.

## Development setup

```bash
git clone https://github.com/Yigtwxx/xor-image-encryption.git
cd xor-image-encryption
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install pytest flake8
```

## Run checks

```bash
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --max-line-length=120 --statistics
pytest -q
```

## Contribution workflow

1. Fork and create a feature branch.
2. Keep changes focused and small.
3. Add/adjust tests for behavior changes.
4. Update docs when command/output behavior changes.
5. Open a PR using the template.

## Commit guidance

- Use clear, imperative messages.
- Reference issue IDs when relevant.

## Reporting bugs and requesting features

- Use GitHub issue templates.
- For security concerns, follow `SECURITY.md`.

## Code style

- Python code should be readable and minimal.
- Keep public CLI arguments backward compatible unless versioned otherwise.
