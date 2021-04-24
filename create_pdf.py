#-*- coding: utf-8 -*-

import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER, A4, portrait
from reportlab.lib.units import mm, inch

#長形３号
# _sizelongform3 = (120.0*mm, 235*mm)
# _sizelongform3 = (235*mm, 120.0*mm)

def create_pdf(outfile:str, w: float, h: float, grdsz:float):
    # page = canvas.Canvas(outfile, _sizelongform3)
    page = canvas.Canvas(outfile, pagesize=(w*mm, h*mm))
    page.setStrokeColorRGB(0, 0, 0, 0.3)
    grdsz = grdsz*mm
    w,h = page._pagesize
    page.grid([x*grdsz for x in range(int(w//grdsz)+2)], [y*grdsz for y in range(int(h//grdsz)+2)])
    page.save()

def main():
    if len(sys.argv) != 5:
        print('usege:')
        print(' arg1: output file path')
        print(' arg2: width(mm)')
        print(' arg3: height(mm)')
        print(' arg4: grid size(mm)')
        sys.exit()
    p = str(sys.argv[1])
    w = float(sys.argv[2])
    h = float(sys.argv[3])
    g = float(sys.argv[4])
    create_pdf(p, w, h, g)

if __name__ == '__main__':
    main()

