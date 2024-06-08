from PIL import Image

# 打开 BMP 图像
image = Image.open("out.bmp")

# 获取图像的像素数据
pixels = list(image.getdata())

# 将像素数据转换为字节数组
byte_array = bytearray()
for r, g, b in pixels:
    byte_array.append(r)
    byte_array.append(g)
    byte_array.append(b)

# 将字节数组写入新的二进制文件
with open("recovered.bin", "wb") as f:
    f.write(byte_array)

print("二进制文件已成功还原为 recovered.bin")