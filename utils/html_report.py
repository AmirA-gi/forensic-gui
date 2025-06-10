import os

def generate_html_report(results, output_path='html/report.html'):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Forensic Tracer</title>
    <style>
        body {
            font-family: sans-serif;
            background-color: #fff;
            margin: 20px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        h2 {
            margin-top: 40px;
            color: #444;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin-top: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        th, td {
            border: 1px solid #ccc;
            padding: 6px 12px;
            text-align: left;
            font-size: 13px;
        }
        th {
            background-color: #eaeaea;
            color: #000;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        .section {
            margin-bottom: 50px;
        }
    </style>
</head>
<body>
    <h1>Forensic Tracer</h1>
"""

    for section, content in results.items():
        html += f'<div class="section">\n<h2>{section.upper()}</h2>\n<table>\n<thead>\n<tr><th>Ключ</th><th>Значение</th></tr>\n</thead>\n<tbody>\n'

        if isinstance(content, dict):
            for key, value in content.items():
                html += f"<tr><td>{key}</td><td>{value}</td></tr>\n"

        elif isinstance(content, list):
            for idx, item in enumerate(content, start=1):
                html += f"<tr><td>{idx}</td><td>{item}</td></tr>\n"

        else:
            html += f"<tr><td>Результат</td><td>{content}</td></tr>\n"

        html += "</tbody>\n</table>\n</div>\n"

    html += "</body>\n</html>"

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
