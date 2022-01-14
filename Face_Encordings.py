import face_recognition as f

img=f.load_image_file('jw.jpg')
img_en=f.face_encodings(img)[0]

img1=f.load_image_file('me.jpg')
img1_en=f.face_encodings(img1)[0]

dis1=f.face_distance([img_en] , img1_en)

print("Distance ::" , dis1)