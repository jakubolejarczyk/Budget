from const import ColorConst

class ColorUtil:
    @staticmethod
    def set_color(color_type):
        color = ColorConst.COLOR_WHITE
        match color_type:
            case "white":
                color = ColorConst.COLOR_WHITE
            case "cyan":
                color = ColorConst.COLOR_CYAN
            case "dark_gray":
                color = ColorConst.COLOR_DARK_GRAY
            case _:
                color = ColorConst.COLOR_WHITE
        print(color, end = "")

    @staticmethod
    def reset_color():
        print(ColorConst.COLOR_END, end = "")