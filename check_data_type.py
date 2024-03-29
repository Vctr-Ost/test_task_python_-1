def check_type(value):
    try:
        float_value = float(value)
        int_value = int(float_value)
        if int_value == float_value:
            return "int"
        else:
            return "float"
    except ValueError:
        return "str"