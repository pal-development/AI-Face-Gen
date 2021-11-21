import requests

amount = int(input("How many faces do you want to generate?: "))
count = 1
for i in range(amount):
    print(f"Generated {str(count)} Faces!")
    img_data = requests.get("https://thispersondoesnotexist.com/image").content
    with open(f'pal_face_generation-{str(count)}.jpg', 'wb') as handler:
        handler.write(img_data)
    count = count + 1
