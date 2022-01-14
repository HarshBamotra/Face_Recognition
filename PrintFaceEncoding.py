import face_recognition as f

img=f.load_image_file('me.jpg')
img_en=f.face_encodings(img)[0]
print("The shape of the encoding array ::" , img_en.shape)
print("Encodings ::" , img_en)