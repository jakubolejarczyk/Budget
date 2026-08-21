from const.color_const import MY_COLOR

def log(message, color):
    prefix = "";
    if color == "dark_grey":
        prefix = "\033[90m"
    print(f"{MY_COLOR} {prefix}{message}\033[0m")