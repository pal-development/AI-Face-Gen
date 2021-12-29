import requests

file_format = "pal_face_generation-%s.jpg"

amount = int(input("How many faces do you want to generate?: "))
for count in range(amount):
    img_data = requests.get("https://thispersondoesnotexist.com/image").content
    with open(file_format % (str(count)), 'wb') as handler:
        handler.write(img_data)
    print(f"Generated {str(count)} Faces!")
    count = count + 1
