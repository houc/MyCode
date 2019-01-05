def font_color():
    """打印字体颜色"""
    return {"black": "\033[30m",
            "red": "\033[31m",
            "green": "\033[32m",
            "yellow": "\033[33m",
            "blue": "\033[34m",
            "purplish_red": "\033[35m",
            "young_green": "\033[36m",
            "white": "\033[37m",}

def _display_mode():
    """显示效果"""
    return {"thickening": "1",
            "underline": "4"}

def _display_color():
    """显示字体样式"""
    mode = _display_mode()
    return {"thickening_red": "\033[{};31m".format(mode["thickening"]),
            "thickening_white":"\033[{};37m".format(mode["thickening"]),}

RED_BIG = _display_color()["thickening_red"]
WHITE_BIG = _display_color()["thickening_white"]
