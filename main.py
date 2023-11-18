import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob('invoices/*.xlsx')

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_num, invoice_date = filename.split('-')
    pdf.set_font(family='Times', style='B', size=15)
    pdf.set_text_color(100, 100, 100)
    # Header
    pdf.cell(w=50, h=10, txt=f"Invoice num. {invoice_num}", ln=1)
    pdf.cell(w=50, h=10, txt=f"Date {invoice_date}")

    pdf.output(f"PDFs/{filename}.pdf")


