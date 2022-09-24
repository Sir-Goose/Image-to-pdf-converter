import os

import img2pdf
from PIL import Image


def one():
    img_path = 'document-1.png'
    pdf_path = 'createdpf.pdf'

    image = Image.open(img_path)
    pdf_bytes = img2pdf.convert(image.filename)

    file = open(pdf_path, 'wb')
    file.write(pdf_bytes)
    image.close()
    file.close()

def a4():
    image_list = []

    for x in os.listdir(os.curdir):
        if x.endswith(".png"):
            image_list.append(x)
        if x.endswith(".jpg"):
            image_list.append(x)
        if x.endswith(".jpeg"):
            image_list.append(x)

    length = len(image_list)


    i = 0
    while i < length:

        splat = image_list[i].split('.')
        pdf = splat[0]

        pdf = pdf + ".pdf"

        a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
        layout_fun = img2pdf.get_layout_fun(a4inpt)
        with open(pdf, "wb") as f:
            f.write(img2pdf.convert(image_list[i], layout_fun=layout_fun))
        i += 1

a4()




