# CV / Portfolio

Personal resume for **Veaceslav Țurcanu** — Python Backend Engineer (Linux & IoT).

## Contents

- **`index.html`** — Web CV (open in a browser or serve locally)
- **`Veaceslav_Turcanu_Modern.pdf`** — Printable PDF export
- **`cv_data.json`** — Structured CV data (experience, skills, education)
- **`generate_cv.py`** — Regenerates the PDF from `cv_data.json` (requires [WeasyPrint](https://weasyprint.org/))
- **`cv_photo.jpg`** — Profile photo used in HTML and PDF

## Quick start

View the site:

```bash
python3 -m http.server 8080
```

Then open [http://localhost:8080](http://localhost:8080).

Regenerate the PDF after editing `cv_data.json`:

```bash
pip install weasyprint
python3 generate_cv.py
```
