from PIL import Image

# 加载第一张图片
image1 = Image.open('icon.png')

# 加载第二张图片
image2 = Image.open('1.png')

# 确定两张图片拼接后的总宽度和最大高度
total_width = image1.width + image2.width
max_height = max(image1.height, image2.height)

# 创建一个新的透明背景图片
new_image = Image.new('RGBA', (total_width, max_height), (255, 255, 255, 0))

# 将第一张图片放在新图片的左侧
new_image.paste(image1, (0, 0))

# 将第二张图片放在第一张图片的右侧
new_image.paste(image2, (image1.width, 0))

# 保存拼接后的图片
new_image.save('combined_image.png')

print("Images have been combined and saved as 'combined_image.png'")
