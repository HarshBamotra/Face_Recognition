import face_recognition as f

img=f.load_image_file("single/e.jpg")
img1=f.load_image_file("single/k.jpg")

img_en=f.face_encodings(img)[0]
img1_en=f.face_encodings(img1)[0]

result=f.compare_faces([img_en] , img1_en , tolerance=0.5)
if(result[0]):
    print("Same person")
else:
    print("Not same")