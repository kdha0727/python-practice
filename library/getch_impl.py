import os
import sys


class GetCh(object):
    """
    Gets a single character bytes object from standard input.
    Does not echo to the screen.
    """

    if os.name == 'nt':
        @staticmethod
        def impl():
            import msvcrt
            return msvcrt.getch()

    else:
        @staticmethod
        def impl():
            import sys
            import tty
            import termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

    __call__ = impl


# try to make GetCh class as Singleton

def singleton_constructor(cls, *_, **__):
    global getch
    if getch is not None:
        return getch
    getch = object.__new__(cls)
    return getch


getch = None
GetCh.__new__ = singleton_constructor
module = type(sys)(__name__)
module.GetCh = GetCh
module.getch = GetCh()
sys.modules[__name__] = module
