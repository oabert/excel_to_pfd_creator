import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob('Text+Files/*.txt')
pdf = FPDF(orientation='P', unit='mm', format='A4')

for filepath in filepaths:
    # df = pd.read_fwf(filepath)
    pdf.add_page()
    filename = Path(filepath).stem
    header_name = filename.capitalize()
    pdf.set_font(family='Times', style='B', size=15)

    pdf.cell(w=30, h=8, txt=header_name, ln=1)
    # pdf.cell(w=30, h=8, txt=, ln=1)


pdf.output(f"PDFs_animals/output.pdf")
