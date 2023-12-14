import pyautogui
import time
# マウスを指定した座標に移動する
pyautogui.moveTo(100, 100, duration=1)
# マウスを現在の位置から指定した相対座標に移動する
pyautogui.move(50, 50, duration=1)
# マウスの左クリックを行う
pyautogui.click()
# マウスの右クリックを行う
pyautogui.rightClick()
# マウスのダブルクリックを行う
pyautogui.doubleClick()
# マウスのドラッグを行う
pyautogui.drag(100, 0, duration=1)
# マウスのスクロールを行う
pyautogui.scroll(10)
# マウスの現在位置を取得する
x, y = pyautogui.position()
print(f"マウスの現在位置: ({x}, {y})")
# マウスの移動速度を設定する
pyautogui.PAUSE = 1
# マウスの自動操作を行う
pyautogui.moveTo(500, 500, duration=1)
pyautogui.click()
pyautogui.typewrite("Hello, World!", interval=0.2)
