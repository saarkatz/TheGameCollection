import sys
from ctypes import windll, Structure, WINFUNCTYPE, \
    c_long, c_int, c_uint, c_char_p, byref, WinError

kernel32 = windll.kernel32
user32 = windll.user32
gdi32 = windll.gdi32

WNDPROC = WINFUNCTYPE(c_long, c_int, c_uint, c_int, c_int)


class MyWNDCLASS(Structure):
    __fields__ = [
        ('lpfnWndProc', WNDPROC),
        ('hInstance',  c_int),
        ('lpszClassName', c_char_p),
    ]

WM_PAINT = 15
WM_DESTROY = 2
def WndProc(hwnd, message, wParam, lParam):
    if message == WM_PAINT:
        return 0
    elif message == WM_DESTROY:
        return 0
    return user32.DefWindowProcA(c_int(hwnd), c_int(message), c_int(wParam), c_int(lParam))

wndclass = MyWNDCLASS()
wndclass.lpfnWndProc = WNDPROC(WndProc)
wndclass.hInstance = kernel32.GetModuleHandleA(c_int(0))
wndclass.lpszClassName = b'MyWindowClassTHG'

if not user32.RegisterClassA(byref(wndclass)):
    raise WinError()

hwnd = user32.CreateWindowEx(
    0,                              #// Optional window styles.
    b'MyWindowClassTHG',                     #// Window class
    b"Learn to Program Windows",    #// Window text
    13565952,            #// Window style

    #// Size and position
    -2147483648, -2147483648, -2147483648, -2147483648,

    0,       #// Parent window
    0,       #// Menu
    kernel32.GetModuleHandleA(c_int(0)),  #// Instance handle
    0        #// Additional application data
    )

user32.ShowWindow(c_int(hwnd), c_int(1))
