import face_recognition as fr
from PIL import Image

photo=fr.load_image_file("ss.png" , "RGB")     #loading the image in RGB
pil_gp=Image.fromarray(photo)                   #converting the numpy array into picture
pil_gp.show()                                   #showing the picture

l=fr.face_locations(photo , model='HOG')        #locating the faces 
print("There are" , len(l) , "peoples.")        #printing the number of faces as len of list

print("Top" , "\t\t" , "Right" , "\t\t" , "Bottom" , "\t" , "Left")
for face in l:
    top , right , bottom , left = face          #extracting top , right , bottom , left form the tuple
    print(top , "\t\t" , right , "\t\t" , bottom , '\t\t' , left)
    f=photo[top:bottom , left:right]            #slicing the numpy array and extracting the faces as array
    pil_photo=Image.fromarray(f)                #converting the arrays into pictures
    pil_photo.show()                            #finally showing each picture one by one
