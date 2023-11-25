import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob('animal_project_txts/*.txt')
pdf = FPDF(orientation='P', unit='mm', format='A4')

for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem
    header_name = filename.capitalize()
    pdf.set_font(family='Times', style='B', size=15)

    pdf.cell(w=30, h=8, txt=header_name, ln=1)
    # pdf.cell(w=30, h=8, txt=, ln=1)

    # Add content
    # df = pd.read_fwf(filepath)
    with open(filepath, 'r') as file:
        content = file.read()
    pdf.set_font(family='Times', size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output(f"PDFs_animals/output.pdf")
