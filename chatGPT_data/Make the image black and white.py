from PIL import Image
def convert_to_grayscale(image_path):
    # 画像を開く
    image = Image.open(image_path)
    # 画像を白黒に変換する
    grayscale_image = image.convert('L')
    # 変換した画像を保存する
    grayscale_image.save('grayscale_image.jpg')
# 画像のパスを指定して白黒に変換する
image_path = 'image.jpg'
convert_to_grayscale(image_path)
