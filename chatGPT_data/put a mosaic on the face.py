import cv2
# 顔検出器の読み込み
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# 画像の読み込み
image = cv2.imread('input.jpg')
# グレースケールに変換
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 顔の検出
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
# 顔にモザイクをかける
for (x, y, w, h) in faces:
    # 顔の領域を切り出す
    face = image[y:y+h, x:x+w]
    
    # 顔の領域を縮小してモザイク効果を作る
    small_face = cv2.resize(face, (10, 10))
    mosaic_face = cv2.resize(small_face, (w, h), interpolation=cv2.INTER_NEAREST)
    
    # 元の画像にモザイクをかける
    image[y:y+h, x:x+w] = mosaic_face
# モザイクをかけた画像を保存
cv2.imwrite('output.jpg', image)
