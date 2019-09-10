
import pywin
import os
#import Pywin32
import win32gui
import win32api

print("hello world")

#两种运行某个程序的方法
def runApp():
    os.system(r'C:\Users\lzx\Desktop\s41586-019-1119-1.pdf')

def RunApp():
    #最后一个参数表示窗口属性， 0 不显示 1 正常显示 2最小化 3 最大化
    res = win32api.ShellExecute(0, 'open', r'C:\Users\lzx\Desktop\s41586-019-1119-1.pdf', '', '', 3)


def findAppHandle():
    appName = r'C:\Users\lzx\Desktop\s41586-019-1119-1.pdf'
    hwnd = win32gui.FindWindow(None, appName)
    print(hwnd)

#RunApp()
#runApp()
findAppHandle()


#import PyGetWindow
import pyautogui
print(pyautogui.size())


#绝对移动
pyautogui.moveTo(100, 100, duration=1)

#相对移动
pyautogui.moveRel(0, 50, duration=1)

#获取当前鼠标位置
print(pyautogui.position())

#控制鼠标点击 ，鼠标会自动移动到所设置的位置去点击
pyautogui.click(100, 100, duration=1)

#控制鼠标拖动， 绝对拖动
pyautogui.dragTo(1000, 1000, duration=1)

#相对拖动
pyautogui.dragRel(100, 0, duration=1)

#滚动屏幕
pyautogui.scroll(200)


#自动输入字符串
pyautogui.typewrite("hello world")

#传递键名
pyautogui.typewrite(["a","left", "ctrlleft"])

#按下组合键
pyautogui.hotkey("ctrlleft","a")



