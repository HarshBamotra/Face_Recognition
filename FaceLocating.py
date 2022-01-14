import face_recognition as f
from PIL import Image , ImageDraw

img=f.load_image_file('ss.png')
faces=f.face_locations(img , model="CNN")
pil_img=Image.open('ss.png')
board=ImageDraw.Draw(pil_img)
print("There are" , len(faces) , "people in the picture." )
for face in faces:
    top , right , bottom , left = face
    board.rectangle((left , top , right , bottom) , outline=(255 , 0 , 0) , width=5)
pil_img.show()