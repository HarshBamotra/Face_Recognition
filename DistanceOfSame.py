import face_recognition as f

m1=f.load_image_file("me.jpg")
m2=f.load_image_file("me1.jpg")
m3=f.load_image_file("me2.jpg")

m1_en=f.face_encodings(m1)[0]
m2_en=f.face_encodings(m2)[0]
m3_en=f.face_encodings(m3)[0]

dis1=f.face_distance([m1_en] , m2_en)
dis2=f.face_distance([m2_en] , m3_en)
dis3=f.face_distance([m3_en] , m1_en)

print("Distance between 1 and 2 ::" , dis1)
print("Distance between 2 and 3 ::" , dis2)
print("Distance between 3 and 1 ::" , dis3)



