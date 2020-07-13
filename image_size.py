from PIL import Image

image = Image.open('1.png')
width, height = image.size
print(f'Исходные размеры картини: высота - {height} px, ширина - {width} px.')
