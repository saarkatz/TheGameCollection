import win32api
import win32con
import win32gui


class MetaWindow(type):
    def __new__(cls, name, bases, dct):
        window_class = super().__new__(cls, name, bases, dct)
        cwindow_class = win32gui.WNDCLASS()
        cwindow_class.style = window_class.class_style
        cwindow_class.lpfnWndProc = window_class.message_map
        window_class.class_name = 'EBOW_' + name
        cwindow_class.lpszClassName = window_class.class_name
        win32gui.RegisterClass(cwindow_class)
        return window_class


class Window(metaclass=MetaWindow):
    class_style = win32con.CS_HREDRAW | win32con.CS_VREDRAW

    def __init__(self, title='Window', **kwargs):
        win32gui.InitCommonControls()
        self.hinst = win32api.GetModuleHandle(None)
        self.style = win32con.WS_OVERLAPPEDWINDOW
        self.hwnd = win32gui.CreateWindow(
            self.class_name,  # Class name
            title,  # Title
            self.style,  # Style
            kwargs['x'] if 'x' in kwargs else win32con.CW_USEDEFAULT,  # x
            kwargs['y'] if 'y' in kwargs else win32con.CW_USEDEFAULT,  # y
            kwargs['width'] if 'width' in kwargs else 300,  # width
            kwargs['height'] if 'height' in kwargs else 300,  # height
            0,  # parent
            0,  # menu
            self.hinst,  # hinstance
            None  # Must be None
        )
        win32gui.UpdateWindow(self.hwnd)
        win32gui.ShowWindow(self.hwnd, win32con.SW_SHOW)

    def blit(self, x, y, width, height, source, source_x, source_y):
        hdc = win32gui.GetDC(self.hwnd)
        srcdc = win32gui.CreateCompatibleDC(hdc)
        original = win32gui.SelectObject(srcdc, source)
        win32gui.BitBlt(hdc, x, y, width, height, srcdc, source_x, source_y,
                        13369376)
        win32gui.SelectObject(srcdc, original)
        win32gui.DeleteDC(srcdc)

    @staticmethod
    def on_destroy(hwnd, message, wparam, lparam):
        win32gui.PostQuitMessage(0)
        return True

    message_map = {
        win32con.WM_DESTROY: on_destroy.__func__,
    }


if __name__ == '__main__':
    from ctypes import windll, byref
    from ctypes.wintypes import DWORD
    from time import sleep
    import math
    import random

    imagebuff = (DWORD * (512*512))()
    # bitmap = win32gui.CreateBitmap(512, 512, 1, 8 * 4, None)
    w = Window(width=512, height=512)

    # Blit image
    # for i in range(512):
    #     for j in range(512):
    #         imagebuff[i + 512 * j] = (
    #                                   (i**2 + j**2) % 256  # Blue
    #                                   + (((50 + (20+i)**2 + (10+j)**2) % 256) << 8)  # Green
    #                                   + (((100 + (10+i)**2 + (20+j)**2) % 256) << 16)  # Red
    #                                   )
    # bitmap = windll.gdi32.CreateBitmap(512, 512, 1, 8 * 4,
    #                                    byref(imagebuff))
    # w.blit(0, 0, 512, 512, bitmap, 0, 0)

    bRet, msg = win32gui.GetMessage(w.hwnd, 0, 0)
    k = 0
    while True:
        if bRet == -1:
            print('Error!')
            break
        elif bRet == 0:
            win32gui.SendMessage(791, 0, 0)
        else:
            win32gui.TranslateMessage(msg)
            win32gui.DispatchMessage(msg)
        print(msg)
        print(bRet)

        # Generating a buffer in CPU is slow
        for i in range(512):
            for j in range(512):
                    imagebuff[i + 512 * j] = ((k * 5 + i**2 + j**2) % 256) #
                    # Blue
                                              # + (((k * 7 + i**2 + j**2) % 256)<<8)
                                              # + (((k * 11 + i**2 + j**2) % 256)<<16))
        # imagebuff[k % (512*512)] = random.randint(0,255)
        bitmap = windll.gdi32.CreateBitmap(512, 512, 1, 8 * 4,
                                           byref(imagebuff))
        w.blit(0, 0, 512, 512, bitmap, 0, 0)
        k += 1
        print(k)
        # sleep(0.5)
        bRet, msg = win32gui.PeekMessage(w.hwnd, 0, 0, 1)

    print('done!')
