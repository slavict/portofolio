#!/usr/bin/env python3

"""pip install weasyprint"""
import html

import weasyprint
import json

with open('cv_data.json', 'r') as f:
    cv_data = json.load(f)

html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            @page {{ size: A4; margin: 0; }}
            body {{ 
                font-family: 'Segoe UI', Arial, sans-serif; 
                margin: 0; 
                padding: 0; 
                background: linear-gradient(to right, #F3F6F8 30%, #ffffff 30%);
            }}

            .sidebar {{ 
                position: absolute;
                left: 0;
                top: 0;
                width: 30%; 
                padding: 40px 20px; 
                box-sizing: border-box;
                z-index: 2;
            }}

            .main {{ 
                margin-left: 30%;
                width: 70%; 
                padding: 40px; 
                box-sizing: border-box;
            }}

            .profile-img {{ 
                width: 120px; 
                height: 120px; 
                border-radius: 50%; 
                object-fit: cover; 
                margin: 0 auto 20px; 
                border: 4px solid white; 
                display: block; 
            }}

            .sidebar h3 {{ color: #0A66C2; border-bottom: 1px solid #ccc; padding-bottom: 5px; font-size: 16px; margin-top: 25px; }}
            .sidebar p {{ font-size: 12px; line-height: 1.6; color: #333; }}

            .header h1 {{ margin: 0; font-size: 26px; color: #000; }}
            .header h2 {{ margin: 5px 0; font-size: 16px; color: #0A66C2; font-weight: 600; }}
            .section-title {{ color: #0A66C2; border-bottom: 2px solid #0A66C2; margin-top: 25px; margin-bottom: 10px; font-size: 15px; text-transform: uppercase; font-weight: bold; }}

            .exp-item {{ margin-bottom: 18px; }}
            .exp-role {{ font-weight: bold; font-size: 14px; color: #222; }}
            .exp-meta {{ color: #666; font-size: 12px; margin-bottom: 5px; font-style: italic; }}
            .label-text {{ font-size: 12px; font-weight: bold; color: #444; margin-top: 8px; }}
            .desc-text {{ font-size: 11px; line-height: 1.4; margin: 2px 0 2px 10px; }}
        </style>
    </head>
    <body>
        <div class="sidebar">
            <img src="cv_photo.jpg" class="profile-img">
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

            <h3 class="section-title">Summary</h3>
            <p style="font-size: 12px; line-height: 1.5;">{cv_data['summary']}</p>

            <h3 class="section-title">Experience</h3>
            {"".join([f'''
                <div class="exp-item">
                    <span class="exp-role">{e['role']}</span>
                    <div class="exp-meta">{e.get('company') or e.get('organization')} | {e['period']}</div>

                    {f'<div class="label-text">Projects</div>' if e.get('projects') else ''}
                    {"".join([f'<p class="desc-text">• {r}</p>' for r in e.get('projects', [])])}

                    <div class="label-text">Responsibilities</div>
                    {"".join([f'<p class="desc-text">• {r}</p>' for r in e['desc']])}
                </div>
            ''' for e in cv_data['experience']])}

            <h3 class="section-title">Certifications</h3>
            <div class="exp-item">
                {"".join([f'<p class="desc-text">• {r}</p>' for r in cv_data['certifications']])}
            </div>

            <h3 class="section-title">Education</h3>
            <p style="font-size: 12px; line-height: 1.4;">
                    {"".join([f'<strong>• {ed.get("name", " ")}</strong><br>{ed.get("specialisation", " ")}<br>{ed.get("period", " ")}' for ed in cv_data['education']])}
            </p>
        </div>
    </body>
    </html>
    """
weasyprint.HTML(string=html_content, base_url=".").write_pdf("Veaceslav_Turcanu_Modern.pdf")
print("New pdf was created please check Veaceslav_Turcanu_Modern.pdf.")
