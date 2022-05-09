import face_recognition as fc
import cv2


img = cv2.imread("ronaldo.webp")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding= fc.face_encodings(rgb_img)[0]
img2= cv2.imread("messi.jpg")
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2= fc.face_encodings(rgb_img2)[0]
result = fc.compare_faces([img_encoding],img_encoding2)
print(result[0])
"""
 = cv2.imread("messi.jpg")
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2= face_recognition.face_encodings(rgb_img2)[0]

result = face_recognition.compare_faces([img_encoding],img_encoding2)
print(result)

cv2.imshow("Img", img)
cv2.imshow("Img2", img2)
image = fc.load_image_file("group.webp")
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

face_loc= fc.batch_face_locations(image)
print(face_loc)
cv2.waitKey(0)
"""


"""
face_locations = fc.face_locations(image)
for i in range (len(face_locations)):
    print(face_locations[i][0])
    cv2.imshow("photo",image)
cv2.waitKey(0)
"""
