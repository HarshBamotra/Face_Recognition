from PIL import Image , ImageFilter

pil_img=Image.open('ss.png')
pil_img.show()
pil_imag=pil_img.filter(ImageFilter.EMBOSS())
pil_imag.show()