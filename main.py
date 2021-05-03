import numpy as np
import pyautogui
import cv2
import datetime
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

codec = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

recordingTime = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
filename = f'{recordingTime}.mp4'
fps = 20.0

output = cv2.VideoWriter(filename, codec, fps,(width,height))

# Window
cv2.namedWindow('Recording', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Recording', 480, 270)

while 1:
    img = pyautogui.screenshot()
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    output.write(img)
    cv2.imshow('Recording', img)
    if cv2.waitKey(10) == ord('q'):
        break

output.release()
cv2.destroyAllWindows()
