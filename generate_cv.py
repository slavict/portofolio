#!/usr/bin/env python3

"""
pip install weasyprint
"""
import argparse
import json
import os
import sys
import weasyprint


def main():
    p = argparse.ArgumentParser(
        description="CV PDF & HTML Generator (Multi-page Support)",
    )
    p.add_argument(
        "-o",
        "--output",
        default="Veaceslav_Turcanu_Modern.pdf",
        help="Output PDF path (default: Veaceslav_Turcanu_Modern.pdf)",
    )
    p.add_argument(
        "--html-output",
        default="Veaceslav_Turcanu_Modern.html",
        help="Output HTML path (default: Veaceslav_Turcanu_Modern.html)",
    )
    p.add_argument(
        "-i",
        "--input",
        default="cv_python_dev_data.json",
        help="Input job CV data file path json format (default: cv_python_dev_data.json)",
    )
    args = p.parse_args()

    if not os.path.exists(args.input):
        print(f"Input CV data file '{args.input}' does not exist.")
        p.print_help()
        sys.exit(1)

    with open(args.input, "r", encoding="utf-8") as f:
        cv_data = json.load(f)

    html_content = f"""<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <title>{cv_data['name']} - CV</title>
    <style>
        @page {{ 
            size: A4; 
            margin: 0; 
        }}

        body {{ 
            font-family: 'Segoe UI', Arial, sans-serif; 
            margin: 0; 
            padding: 0; 
            background: #ffffff;
            -webkit-print-color-adjust: exact;
            color-adjust: exact;
        }}

        /* Containerul principal flexibil care permite separarea pe pagini */
        .cv-container {{
            display: flex;
            min-height: 297mm;
            width: 100%;
        }}

        /* Fundalul asimetric generat prin pseudo-element pentru a se extinde pe toate paginile */
        body::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 30%;
            height: 100%;
            background-color: #F3F6F8;
            z-index: -1;
        }}

        /* Stiluri specifice pentru vizualizarea pe ecran (Browser) */
        @media screen {{
            body {{
                background: #525659;
                padding: 20px 0;
            }}
            body::before {{
                display: none; /* Dezactivat pe ecran pentru a folosi containerul fix */
            }}
            .page-container {{
                width: 210mm;
                margin: 0 auto;
                background: linear-gradient(to right, #F3F6F8 30%, #ffffff 30%);
                box-shadow: 0 0 10px rgba(0,0,0,0.5);
                box-sizing: border-box;
            }}
        }}

        .sidebar {{ 
            width: 30%; 
            padding: 40px 20px; 
            box-sizing: border-box;
        }}

        .main {{ 
            width: 70%; 
            padding: 40px; 
            box-sizing: border-box;
        }}

        /* Managementul paginilor (Page Breaks) */
        .exp-item, .section-block {{
            page-break-inside: avoid;
            break-inside: avoid; /* Previne tăierea unui bloc de experiență la jumătate */
        }}

        .section-title {{ 
            color: #0A66C2; 
            border-bottom: 2px solid #0A66C2; 
            margin-top: 25px; 
            margin-bottom: 10px; 
            font-size: 15px; 
            text-transform: uppercase; 
            font-weight: bold;
            page-break-after: avoid;
            break-after: avoid; /* Titlul nu va rămâne singur la final de pagină */
        }}

        /* Elemente Profil & Elemente Vizuale */
        .profile-img {{ 
            width: 120px; 
            height: 120px; 
            border-radius: 50%; 
            object-fit: cover; 
            margin: 0 auto 20px; 
            border: 4px solid white; 
            display: block; 
        }}

        .sidebar h3 {{ 
            color: #0A66C2; 
            border-bottom: 1px solid #ccc; 
            padding-bottom: 5px; 
            font-size: 16px; 
            margin-top: 25px; 
        }}

        .sidebar p {{ 
            font-size: 12px; 
            line-height: 1.6; 
            color: #333; 
        }}

        .header h1 {{ 
            margin: 0; 
            font-size: 26px; 
            color: #000; 
        }}

        .header h2 {{ 
            margin: 5px 0; 
            font-size: 16px; 
            color: #0A66C2; 
            font-weight: 600; 
        }}

        .exp-role {{ 
            font-weight: bold; 
            font-size: 14px; 
            color: #222; 
        }}

        .exp-meta {{ 
            color: #666; 
            font-size: 12px; 
            margin-bottom: 5px; 
            font-style: italic; 
        }}

        .label-text {{ 
            font-size: 12px; 
            font-weight: bold; 
            color: #444; 
            margin-top: 8px; 
        }}

        .desc-text {{ 
            font-size: 11px; 
            line-height: 1.4; 
            margin: 2px 0 2px 10px; 
        }}
    </style>
</head>
<body>
    <div class="page-container">
        <div class="cv-container">
            <div class="sidebar">
                <img src="cv_photo.jpg" class="profile-img" alt="Profile Photo">
                <h3>Contact</h3>
                <p>📍 {cv_data['location']}<br>📧 {cv_data['email']}<br>📱 {cv_data['phone']}</p>
                <h3>Core Skills</h3>
                <p>{"<br>".join([f"• {s}" for s in cv_data['skills']])}</p>
                <h3>Languages</h3>
                <p>{"<br>".join([f"• {s}" for s in cv_data['languages']])}</p>
            </div>

            <div class="main">
                <div class="header">
                    <h1>{cv_data['name']}</h1>
                    <h2>{cv_data['headline']}</h2>
                </div>

                <div class="section-block">
                    <h3 class="section-title">Summary</h3>
                    <p style="font-size: 12px; line-height: 1.5; margin: 0;">{cv_data['summary']}</p>
                </div>

                <h3 class="section-title">Experience</h3>
                {"".join([f'''
                    <div class="exp-item">
                        <span class="exp-role">{e['role']}</span>
                        <div class="exp-meta">{e.get('company') or e.get('organization') or ''} | {e['period']}</div>

                        {f'<div class="label-text">Projects</div>' if e.get('projects') else ''}
                        {"".join([f'<p class="desc-text">• {r}</p>' for r in e.get('projects', [])])}

                        <div class="label-text">Responsibilities</div>
                        {"".join([f'<p class="desc-text">• {r}</p>' for r in e['desc']])}
                    </div>
                ''' for e in cv_data['experience']])}

                <div class="section-block">
                    <h3 class="section-title">Certifications</h3>
                    <div class="exp-item">
                        {"".join([f'<p class="desc-text">• {r}</p>' for r in cv_data['certifications']])}
                    </div>
                </div>

                <div class="section-block">
                    <h3 class="section-title">Education</h3>
                    <p style="font-size: 12px; line-height: 1.4; margin: 0;">
                        {"".join([f'<strong>• {ed.get("name", " ")}</strong><br>{ed.get("specialisation", " ")}<br>{ed.get("period", " ")}<br>' for ed in cv_data['education']])}
                    </p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

    # Salvarea fișierului HTML
    with open(args.html_output, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"New HTML file was created please check {args.html_output}.")

    # Generarea fișierului PDF
    weasyprint.HTML(string=html_content, base_url=".").write_pdf(args.output)
    print(f"New PDF was created please check {args.output}.")


if "__main__" == __name__:
    main()
