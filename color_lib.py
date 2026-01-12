class color:
    @staticmethod
    def rgb_text(r, g, b, text):
        return f"\033[38;2;{r};{g};{b}m{text}\033[0m"
class style:
    @staticmethod
    def text_style(b, text):
     return f"\033[1;{b}m{text}\033[0m"
        
print(color.rgb_text(100, 255, 100, "This is custom green text"))
print(style.text_style(1, "This is custom bold text"))
