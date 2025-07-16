import pandas as pd

def run_stress_test(df, tarif_persen):
    df.columns = [col.strip() for col in df.columns]

    tarif_decimal = tarif_persen / 100

    df['Penurunan_Ekspor_%'] = df['Elastisitas_Harga'] * tarif_decimal * 100

    df['Nilai_Ekspor_Hilang_USD'] = (df['Penurunan_Ekspor_%'] / 100) * df['Ekspor_AS_2024_USD_miliar']

    df['Estimasi_PHK'] = (df['Ketergantungan_AS_%'] / 100) * (df['Penurunan_Ekspor_%'] / 100) * df['Tenaga_Kerja']

    
    df['Penurunan_Ekspor_%'] = df['Penurunan_Ekspor_%'].round(2)
    df['Nilai_Ekspor_Hilang_USD'] = df['Nilai_Ekspor_Hilang_USD'].round(2)
    df['Estimasi_PHK'] = df['Estimasi_PHK'].round().astype(int)

    df_sorted = df.sort_values(by='Nilai_Ekspor_Hilang_USD', ascending=False)

    return df_sorted[['Sektor', 'Penurunan_Ekspor_%', 'Nilai_Ekspor_Hilang_USD', 'Estimasi_PHK']]
