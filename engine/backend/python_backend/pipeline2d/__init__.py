"""
The Pipeline 2D contains a definition and implementation of a pipeline steps
for rendering a two dimensional scene.
The Pipeline also defines the primitives (i.e. Data structures) on which it
operates.
"""

from ctypes import windll, byref
from ctypes.wintypes import DWORD

user32 = windll.user32
gdi32 = windll.gdi32

arrtype = DWORD * (512*512)
arr = arrtype()

bmap = gdi32.CreateBitmap(512, 512, 1, 4*8, byref(arr))
window = user32.GetActiveWindow()
hdc = user32.GetDC(window)
src = gdi32.CreateCompatibleDC(hdc)
gdi32.SelectObject(src, bmap)
gdi32.BitBlt(hdc, 10, 10, 512, 512, src, 0, 0, 13369376)
gdi32.DeleteDC(src)