import os
import img2pdf


def a4():
    image_list = []

    for x in os.listdir(os.curdir):
        if x.endswith(".png"):
            image_list.append(x)
        if x.endswith(".jpg"):
            image_list.append(x)
        if x.endswith(".jpeg"):
            image_list.append(x)

    for i in image_list:
        splat = i.split('.')
        pdf = splat[0]

        pdf = pdf + ".pdf"

        a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
        layout_fun = img2pdf.get_layout_fun(a4inpt)
        with open(pdf, "wb") as f:
            f.write(img2pdf.convert(i, layout_fun=layout_fun))


a4()
