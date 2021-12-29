import requests

amount = int(input("How many faces do you want to generate?: "))
for count in range(amount):
    img_data = requests.get("https://thispersondoesnotexist.com/image").content
    with open(f'pal_face_generation-{str(count)}.jpg', 'wb') as handler:
        handler.write(img_data)
    print(f"Generated {str(count)} Faces!")
    count = count + 1
