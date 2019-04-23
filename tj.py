
def parserT2J(text, t_json):
    for key, value in t_json.items():
        text = text.replace(f"{{ {key} }}", value)
    return text