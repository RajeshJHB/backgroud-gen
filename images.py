from PIL import Image, ImageFilter

img = Image.open('pics/rr.jpeg')
#filtered_img = img.filter(ImageFilter.BLUR)
#filtered_img = img.convert('L')
#filtered_img.save("Grey.png",'png')
#crooked_img = filtered_img.rotate(90)
#filtered_img.show()
#crooked_img.show()
#resize_img = filtered_img.resize((300,300))  # must be a tuple
#box = (100,100,300,300)
#region = img.crop(box)
#region.save("Cropped.png",'png')
img.thumbnail((400,200))
img.save('thumbnail.jpg')
print(img.size)