from flask import Flask, render_template, request, send_file
import pandas as pd
import os
from stress_test import run_stress_test

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
RESULT_FILE = 'static/result.csv'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('static', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    tarif_input = float(request.form['tarif'])
    file = request.files['file']

    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        df = pd.read_csv(filepath) if filepath.endswith('.csv') else pd.read_excel(filepath)
        result_df = run_stress_test(df, tarif_input)
        result_df.to_csv(RESULT_FILE, index=False)

        table_html = result_df.to_html(classes='table table-striped', index=False)
        chart_data = {
            'sektor': result_df['Sektor'].tolist(),
            'penurunan_ekspor': result_df['Penurunan_Ekspor_%'].tolist(),
            'nilai_hilang': result_df['Nilai_Ekspor_Hilang_USD'].tolist(),
            'phk': result_df['Estimasi_PHK'].tolist(),
        }
        return render_template('index.html', table_html=table_html, chart_data=chart_data)

    return 'No file uploaded.', 400

@app.route('/download')
def download():
    return send_file(RESULT_FILE, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
