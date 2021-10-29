import face_recognition as f
from PIL import Image , ImageDraw , ImageFont

img=f.load_image_file('ss2.jpg')
faces=f.face_locations(img)
pil_gimg=Image.fromarray(img)
board=ImageDraw.Draw(pil_gimg)
fnt=ImageFont.truetype("Myfont-Regular.ttf" , 20)

for face in faces:
    top , right , bottom , left = face
    image=img[top:bottom , left:right]
    #pil_img=Image.fromarray(image)
    #pil_img.show()
    #name=input("Enter the name of the person ::")
    board.rectangle((left , top , right , bottom) , outline=(255 , 0 , 0) , width=5)
    board.text((left , bottom) , name , font=fnt , fill=(0 , 0 , 255))
pil_gimg.show()
