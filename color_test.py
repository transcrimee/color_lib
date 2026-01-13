
from color_lib import color
from color_lib import style
import keyboard

     
print(color.rgb_text(255,105,180, "This is custom pink text"))
print(style.bold_style("This is custom bold text"))
print(color.rgb_text(255,105,180, style.bold_style("This is custom pink&bold text")))

print(color.rgb_text(100, 255, 100, "This is custom green text"))
print(style.bold_style( "This is custom bold text"))
print(style.italic_style( "This is custom bold text"))
print(style.bold_italic_style( "This is custom bold text"))
print("------- now for less important ones -------")
print(style.dim_style( "This is custom bold text"))
print(style.underline_style( "This is custom bold text"))
print(style.blinking_style( "This is custom bold text"))
print(style.invert_style( "This is custom bold text"))
print(style.strikethrough_style( "This is custom bold text"))
keyboard.wait('esc')