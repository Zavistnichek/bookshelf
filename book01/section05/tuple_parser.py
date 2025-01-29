import ast


def parse_element(element):
    element = element.strip()
    if not element:
        return None
    if element.isdigit():
        return int(element)
    try:
        return float(element)
    except ValueError:
        if element.lower() == "true":
            return True
        elif element.lower() == "false":
            return False
        try:
            return ast.literal_eval(element)
        except (ValueError, SyntaxError):
            pass
    return element
