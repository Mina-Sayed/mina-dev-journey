# Mina's Dev Journey

A standalone playable pixel-art portfolio for **Mina Sayed — Senior Full Stack Engineer**.

## Play

After the release branch is merged, open:

- https://raw.githack.com/Mina-Sayed/mina-dev-journey/main/index.html

## Features

- Four career worlds: Datum Solution, Exacall, TDRA and 2P Perfect Presentation
- Keyboard and mobile touch controls
- Mini-game missions with sequential progression
- Quick Portfolio mode
- Local save with safe fallback when storage is unavailable
- English and Arabic interface toggle
- No external runtime dependencies: the game is one self-contained `index.html`

## Verified locally

The browser QA covers:

- Menu boot
- Quick Portfolio
- Canvas game boot
- Datum mission opening and completion
- Exacall unlock progression
- Mobile controls and responsive width
- Browser page errors

Run the test with Python Playwright:

```bash
python -m pip install playwright
python -m playwright install chromium
python tests/browser-qa.py
```
