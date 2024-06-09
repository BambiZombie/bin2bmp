from PIL import Image

# 创建图像对象
width = 400  # 图像宽度
height = 300  # 图像高度
image = Image.new("RGBA", (width, height))

# 设置图像尺寸和颜色模式
image_size = image.size
image_mode = image.mode

# 创建像素数组
pixels = []

# 从二进制文件读取字节数组
with open("test.bin", "rb") as f:
    byte_array = f.read()

if len(byte_array) % 3 != 0:
    byte_array += bytes([0x90] * (3 - len(byte_array) % 3))

# 将字节数组转换为像素值
for i in range(0, len(byte_array), 3):
    r = byte_array[i]
    g = byte_array[i+1]
    b = byte_array[i+2]
    pixels.append((r, g, b, 0))  # 添加Alpha通道值为0

if len(pixels) < width * height:
    pixels.extend([(0x90, 0x90, 0x90, 0)] * (width * height - len(pixels)))  # 添加Alpha通道值为0的像素

# 设置像素值
image.putdata(pixels)

image.save("out.bmp")
