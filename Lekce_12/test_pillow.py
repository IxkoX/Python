from PIL import Image
import os

image = Image.open(r"C:\Users\frant\OneDrive\Obrázky\Uložené obrázky\V__08D0(2).jpeg")

new_image = image.resize((500, 500))
new_image = new_image.rotate(90)
new_image = new_image.convert('L') 

image.close()

#new_image.show()

image_dir = "C:/Users/frant/Downloads/Test_image"

for name in os.listdir(image_dir):
    if name.endswith(('.png','.jpeg','jpg')):
        image_path = os.path.join(image_dir, name)
        
        print(image_path)
        # print(os.path.isfile(image_path))
        image = Image.open(image_path)
        print(image.size)
        image.close()
        if image.size[0] > 1000:
            os.remove(image_path)







