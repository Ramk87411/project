
# function with output

def title_case(f_name, l_name):
    if f_name == "" or l_name =="":
        return 
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    # print(f"{formated_f_name} {formated_l_name}")
    return f"{formated_f_name}  {formated_l_name}"


print(title_case("ram", "krishna"))
