import face_recognition as fr
from PIL import Image

photo_harsh=fr.load_image_file('ss.png' , 'RGB')         #loading image in RGB
photo_harsh_BW=fr.load_image_file('ss.png' , 'L')        #loading image in B&W
print("Harsh photo RGB::" , photo_harsh.shape)
print("Harsh photo BW::" , photo_harsh_BW.shape)

pil_photo=Image.fromarray(photo_harsh)
pil_photo_BW=Image.fromarray(photo_harsh_BW)

pil_photo_BW.show()
pil_photo.show()
