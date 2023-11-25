import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob('invoices/*.xlsx')

for filepath in filepaths:
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_num, invoice_date = filename.split('-')
    pdf.set_font(family='Times', style='B', size=15)
    pdf.set_text_color(80, 80, 80)

    # Doc header
    pdf.cell(w=50, h=10, txt=f"Invoice num. {invoice_num}", ln=1)
    pdf.cell(w=50, h=10, txt=f"Date {invoice_date}", ln=1)

    # Read Excel table
    df = pd.read_excel(filepath, sheet_name='Sheet 1')

    # Add table header
    columns_t = df.columns
    columns_t = [item.replace('_', " ").capitalize() for item in columns_t]
    pdf.set_font(family='Times', style='B', size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=35, h=8, txt=columns_t[0], border=1)
    pdf.cell(w=65, h=8, txt=columns_t[1], border=1)
    pdf.cell(w=35, h=8, txt=columns_t[2], border=1)
    pdf.cell(w=30, h=8, txt=columns_t[3], border=1)

    pdf.cell(w=30, h=8, txt=columns_t[4], border=1, ln=1)

    # Add rows
    for index, row in df.iterrows():
        pdf.set_font(family='Times', size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=35, h=8, txt=str(row['product_id']), border=1)
        pdf.cell(w=65, h=8, txt=str(row['product_name']), border=1)
        pdf.cell(w=35, h=8, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['price_per_unit']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['total_price']), border=1, ln=1)

    # Cal total sum
    total = df['total_price'].sum()

    pdf.set_font(family='Times', style='B', size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=35, h=8, txt='', border=1)
    pdf.cell(w=65, h=8, txt='', border=1)
    pdf.cell(w=35, h=8, txt='', border=1)
    pdf.cell(w=30, h=8, txt='', border=1)
    pdf.cell(w=30, h=8, txt=str(total), border=1, ln=1)

    # Summary
    pdf.set_font(family='Times', style='B', size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=f"The total due amount is {total} Euro", ln=1)

    # Logo
    pdf.set_font(family='Times', style='B', size=12)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=23, h=8, txt=f"YYokStore")
    pdf.image('icons8-store-64.png', w=6)

    pdf.output(f"PDFs/{filename}.pdf")


