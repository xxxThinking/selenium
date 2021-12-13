'''
@File:day03.py
@DateTime:2021/12/12 20:32
@Author:sweet
@Desc: win框运用
'''

# 查找元素
import win32gui
# 元素操作
import win32con

# 1.查找
# 编辑框
# 一级窗口：参数（类名,title）
dialog  = win32gui.FindWindow("#32770","打开")

# 二级：FindWindowEx(子查找函数)参数(一级窗口,不点击就是0,类名,没有名字)
combobox32 = win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)
# 三级:同上一级
combobox = win32gui.FindWindowEx(combobox32,0,"ComboBox",None)
# 四级
edit = win32gui.FindWindowEx(combobox,0,"Edit",None)

# 打开按钮
button = win32gui.FindWindowEx(dialog,0,"Button","打开(&O)")

# 2.操作 往编辑当中,输入文件路径
# 参数(编辑对象,使用方法,无多说明None/点击为1,文件路径)
win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,"filePath") #发送文件路径
win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)  #点击打开按钮