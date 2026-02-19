cases = ["35"," wrfwergr    ","    qwerty        ","61.94"]
def convert_string(string):
    if string.isdigit():
        return float(string)
    else:
        return None
def clean_string(text):
    return text.strip().lower()

convert_string()


#print([convert_string(i) for i in cases])
#print([clean_string(i) for i in cases])