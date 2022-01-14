import face_recognition as f

ma=f.load_image_file("me.jpg")
m1=f.load_image_file("me1.jpg")
m2=f.load_image_file("me2.jpg")
m3=f.load_image_file("me3.jpg")

ma_en=f.face_encodings(ma)[0]
m1_en=f.face_encodings(m1)[0]
m2_en=f.face_encodings(m2)[0]
m3_en=f.face_encodings(m3)[0]

faces=[m1_en , m2_en , m3_en]
dist=f.face_distance(faces , ma_en)

print("The distance between ma to m1 , m2 , m3 resp. ::")
print(dist)


