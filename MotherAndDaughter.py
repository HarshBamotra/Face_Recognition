import face_recognition as f

daughters=[]
mothers=[]
daughters_en=[]
mothers_en=[]

for i in range(1 , 4):
    path_m="mothers/mother_{}.jpg"
    path_d="daughters/daughter_{}.jpg"
    mothers.append(f.load_image_file(path_m.format(i))
    daughters.append(f.load_image_file(path_d.format(i))
    mothers_en.append(f.face_encodings(mothers[i][0]))
    daughters_en.append(f.face_encodings(daughters[i][0]))

for i in range(1 , 4):
    print("Distance :: Daughter" , i , "mothers 0 , 1 , 2 , 3 ::")
    print(f.face_distance(mothers_en , daughters_en[i])

    