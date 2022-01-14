import face_recognition as f

img=f.load_image_file('ss3.jpg')
img_en=f.face_encodings(img)
print("There are" , len(img_en) , "humans in the picture.")
print("The shape of the encoding array ::" , img_en[0].shape)

for i in range(len(img_en)):
    print("Encodings of face" , i+1 , "::\n" , img_en[i])