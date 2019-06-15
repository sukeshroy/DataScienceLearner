import PIL.Image
import PIL.ImageDraw
import face_recognition

# load the image and convert it into numpy array
image =face_recognition.load_image_file("images/sample_image.jpg")

#find all the faces in the image
face_locations = face_recognition.face_locations(image)
no_of_faces = len(face_locations)
print(no_of_faces)

#draw the rectangular image on the face

pil_image = PIL.Image.fromarray(image)

for face_location in face_locations:
    top,right,bottom,left =face_location
    draw_shape = PIL.ImageDraw.Draw(pil_image)
    draw_shape.rectangle([left, top, right, bottom],outline="red")

#displat the image
pil_image.save("images/output_image.jpg")
pil_image.show()