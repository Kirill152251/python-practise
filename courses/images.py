from PIL import Image

mask = Image.open('/home/kirill/pythonProject/mask.png')
matrix = Image.open('/home/kirill/pythonProject/word_matrix.png')
print(mask.size)
print(matrix.size)
resized_mask = mask.resize((1015, 559))
resized_mask.putalpha(200)
matrix.paste(mask=resized_mask, im=resized_mask)
matrix.show()
