import face_recognition as fc
import os
import cv2
from PIL import Image
import json

KNOWN_FACES_DIR= 'known_faces'
TOLERANCE = 0.6
FRAME_THICKNESS = 3
FONT_THICKNESS = 2

known_faces = []
known_names = []
def load_known():
    for name in os.listdir(KNOWN_FACES_DIR):
        image = fc.load_image_file(f'{KNOWN_FACES_DIR}/{name}')
        encoding = fc.face_encodings(image)[0]
        known_faces.append(encoding)
        known_names.append(name)

def draw_box(cordinates,image,i,name):
    top_left = (cordinates[i][3], cordinates[i][0])
    bottom_right = (cordinates[i][1], cordinates[i][2])
    color = [255, 0, 0]
    cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)
    top_left = (cordinates[i][3], cordinates[i][2])
    bottom_right = (cordinates[i][1], cordinates[i][2] + 22)
    cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
    cv2.putText(image, name, (cordinates[i][3] + 10, cordinates[i][2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                (200, 200, 200), FONT_THICKNESS)

def attandence(list):
    with open(list, 'r') as f:
        attandence_list=json.loads(f.read())


    image= fc.load_image_file('group.webp')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    locations= fc.face_locations(image)
    print(f', found {len(locations)} face(s)')

    photo_face = []
    for i in range (len(locations)):
        cropped = image[locations[i][0]:locations[i][2], locations[i][3]:locations[i][1]]
        photo_face.append(cropped)

    people_on_img=[]
    temp_known_faces=known_faces
    temp_known_names=known_names
    for i in range(len(photo_face)):
        found=False
        img_encoding = fc.face_encodings(photo_face[i])[0]
        for j in range(len(temp_known_faces)):
            result = fc.compare_faces([img_encoding], temp_known_faces[j])
            if result[0]:
                found=True
                name = (known_names[j]).split(".")[0]
                draw_box(locations,image,i,name)
                people_on_img.append(name)
                temp_known_faces.pop(j)
                temp_known_names.pop(j)
                j=j-1
                break
        if not found:
            print("didnt found")
            cv2.imshow("Img", photo_face[i],)
            cv2.waitKey(0)
            name= input("Give him a name")
            im = cv2.cvtColor(photo_face[i], cv2.COLOR_BGR2RGB)
            im1 = Image.fromarray(im)
            im1.save(f"{KNOWN_FACES_DIR}/{name}.jpeg")
            draw_box(locations,image,i,name)
            people_on_img.append(name)

    print(people_on_img)
    print(attandence_list)
    for i in attandence_list["first"]:
        if i not in people_on_img:
            print(f"{i} is missing")
    cv2.imshow("Img", image)
    cv2.waitKey(0)


load_known()
attandence("real_madrid.txt")



