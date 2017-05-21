def is_number(number):
    try:
        float(number);
        return True;
    except ValueError:
        pass;
    try:
        import unicodedata;
        unicodedata.numeric(number);
        return True;
    except (TypeError , ValueError):
        pass;
    return False;

print(is_number(1));
print(is_number("1"));
print(is_number("da"));