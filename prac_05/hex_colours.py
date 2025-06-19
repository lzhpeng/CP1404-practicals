COLORS = {
    "ALICEBLUE": "#F0F8FF",
    "ANTIQUEWHITE": "#FAEBD7",
    "AQUA": "#00FFFF",
    "AQUAMARINE": "#7FFFD4",
    "AZURE": "#F0FFFF",
    "BEIGE": "#F5F5DC",
    "BISQUE": "#FFE4C4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#FFEBCD",
    "BLUE": "#0000FF"
}

while True:
    color_name = input("Enter a color name (or press Enter to quit): ").strip()
    if color_name == "":
        break
    color_key = color_name.replace(" ", "").upper()
    if color_key in COLORS:
        print(f"The hexadecimal code for {color_name} is {COLORS[color_key]}")
    else:
        print("Invalid color name. Please try again.") 