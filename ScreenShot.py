# 需要安装(pip安装)的第三方包：keyboard，pillow,baidu-aip

import keyboard  #控制键盘事件
import time
from PIL import ImageGrab

from ShowContent import ShowService

def screenShot():
    # 完成截图-->F1-->ctrl+c
    if keyboard.wait(hotkey='f1')==None:
        if keyboard.wait(hotkey='ctrl+c')==None:
            time.sleep(0.01)
            # 读取剪切板内的图片
            img=ImageGrab.grabclipboard()
            #保存
            img.save('cutImg.png')


while(True):
    screenShot()

    modelShow=ShowService()
    text= modelShow.showPicText('cutImg.png')
    print(text)
            
