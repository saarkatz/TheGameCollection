# The Environment
*[Graphics Device Interface](https://docs.microsoft.com/en-us/windows/win32/gdi/windows-gdi)
or GDI enables applications to use
graphics and formatted text on both the video display and the printer.
Window-based applications do not access the graphics hardware directly.
Instead, GDI interacts with device drivers on behalf of applications.*

## Introduction
In this section we will discuss the way by which the Windows operating
system allows for the creation and manipulation of windows. \
We will than use a windows window as the target of our graphic
procedure.

## The architecture of a window
[Windows](https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-wndclassa)
in Windows are classes that define properties such as
style, name, parent process, menu name and more. \
These classes need not be a class in object oriented sense but rather
are structures defined and
[registered](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-registerclassa)
once with the system, after which
they can be
[instantiated](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createwindowa)
using an API call. \
To use drawing operations on the window we need to create a
[Device Context](https://docs.microsoft.com/en-us/windows/win32/gdi/device-contexts)
or DC which contains the  various objects used for these operations. \
Generally speaking, the DC is the access point to the graphical hardware
of the window.

DCs are used for every graphical device in the windows operating system
including displays, printers, plotters etc.

DCs include various methods of drawing some of which are pen, brush,
shape drawing and direct pixel blit-ing.
