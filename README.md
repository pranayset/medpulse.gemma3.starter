# MedPulse Gemma 3 — Starter Project

A privacy-first educational starter for experimenting with synthetic discharge-summary rewriting using Gemma 3 and optional LoRA fine-tuning.

> **Important:** This is a learning/demo project, not a medical device. Do not use it for diagnosis, treatment decisions, or real patient care. Use only synthetic, non-identifiable examples. Model outputs can be inaccurate and must not be treated as clinical advice.

## Project structure

```text
medpulse-gemma3-starter/
├── config/                  # Safe, non-secret configuration
├── data/
│   ├── sample/              # Tiny synthetic demo data only
│   └── private/             # Ignored; keep private datasets here locally only
├── notebooks/
│   └── medpulse3.ipynb      # Main starter notebook
├── src/medpulse/            # Reusable project code
├── tests/                   # Lightweight validation tests
├── .gitignore
├── requirements.txt
└── README.md
```

## Privacy and repository safety

Never commit real patient information, private datasets, credentials, Hugging Face tokens, private keys, trained LoRA adapters, model weights, checkpoints, or runtime caches. The included `.gitignore` blocks common sensitive paths and file types, but **`.gitignore` is not a substitute for reviewing staged files**.

- Use synthetic data only in the public repository.
- Store Hugging Face tokens in Colab Secrets or environment variables; never paste tokens into notebooks.
- Keep local-only files in `data/private/`, `outputs/`, or `checkpoints/`.
- Before pushing, run `git status --ignored` and `git diff --cached --name-only`.
- If a secret was committed, revoke/rotate it immediately. Removing it in a later commit does not erase it from Git history.

## Quick start (Windows PowerShell)

```powershell
Expand-Archive .\medpulse-gemma3-starter.zip -DestinationPath .
Set-Location .\medpulse-gemma3-starter

py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m pytest
```

If PowerShell blocks activation, use this for the current terminal only:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Notebook

Open `notebooks/medpulse3.ipynb` in Jupyter or upload it to Google Colab. The first cells validate the environment and load the synthetic sample. Model loading and generation are optional and require an authorized Hugging Face account if the chosen model is gated. Do not store access tokens in notebook cells.

## Publish to GitHub

Create an **empty** GitHub repository (for example `medpulse-gemma3-starter`) without adding a README, then from this folder:

```powershell
git init
git branch -M main
git add .
git status --short
git diff --cached --name-only
git diff --cached --stat
```

Inspect the staged file list. If anything private or large appears, stop and unstage it before proceeding. Then:

```powershell
git commit -m "Add privacy-first MedPulse Gemma 3 starter"
git remote add origin https://github.com/YOUR-USERNAME/medpulse-gemma3-starter.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. Authenticate using Git Credential Manager or the browser prompt; never put a password or token directly in the remote URL.

## Included synthetic data

`data/sample/synthetic_discharge_examples.jsonl` contains fictional, non-identifiable demo records. It is not clinical guidance and should not be used as ground truth.

## License

MIT license for the starter scaffolding; check the licenses and terms of any model, dataset, or dependency you separately use.
