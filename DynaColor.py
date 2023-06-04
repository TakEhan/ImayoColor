import datetime
import time
import tkinter

def DynaColor():
    return hex(int(time.mktime(datetime.datetime.now().timetuple()))//(16*16))

def ShowColor(Hcolor):
    canvas.create_rectangle(100,100,200,200,fill='#'+Hcolor.replace('0x',''))


if __name__ == '__main__':
    print(DynaColor())
    window=tkinter.Tk()
    canvas=tkinter.Canvas(window,width=300,height=300)
    canvas.pack()
    ShowColor(DynaColor())
    window.mainloop()