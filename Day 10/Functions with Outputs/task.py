def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "no firstname or a lastname found"
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}"

result = format_name("HENK", "truus")
print(result)