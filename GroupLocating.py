import face_recognition as f
from PIL import Image , ImageDraw

img=f.load_image_file("ss.png")
faces=f.face_locations(img)

tmin=faces[0][0]
rmax=faces[0][1]
bmax=faces[0][2]
lmin=faces[0][3]

for face in faces:
    top , right , bottom , left = face
    if(top<tmin):
        tmin=top
    if(right>rmax):
        rmax=right
    if(bottom>bmax):
        bmax=bottom
    if(left<lmin):
        lmin=left

print(len(faces))
pil_img=Image.open("ss.png")
board=ImageDraw.Draw(pil_img)
board.rectangle((lmin-20 , tmin-20 , rmax+20 , bmax+20) , outline=(255 , 0 , 0) , width=5)
pil_img.show()
    