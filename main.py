import turtle
more_data = input("insert data names and put space between to separate variables:")
word = ""
variable_holder = []
for i in range(len(more_data)):
    letter = more_data[i]
    if letter == " ":
        exec("temp_data_holder = [word]")
        variable_holder += temp_data_holder
        word = ""
    else:
        word += letter
exec("temp_data_holder = [word]")
variable_holder += temp_data_holder
print(variable_holder)
checker_string = input("are you sure(yes to continue or no to exit and retry):")
if checker_string == "no":
    exit()
function_holder: list = []
for i in range(len(variable_holder)):
    current_value = variable_holder[i]
    print("!İNPUT FUNCTİONS ONE BY ONE! !FUNCTİONS CAN ONLY RETURN ONE OBJECT!")
    print("now you will insert function for your variables and the syntax you must follow for the functions is:"
          "f(-local variables-,-global variables-,module names-)=-code-")  # function reader yap
    function_holder = input(f"insert function for variable({i}):")
    print(function_holder)
    checker_string = input("are you sure(yes to continue or no to exit and retry):")
    if checker_string == "no":
        function_holder.pop(i)
        i -= 1
function_dict_holder = []
i = 0
for var_name in variable_holder:
    func_data = function_holder[i]
    dict_assembler = {var_name: func_data}
    function_dict_holder += dict_assembler
    i += 1

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.title("aargf/pargf reader")  # passive raster graphics file (pargf) and active raster graphics file (aargf)
pen = turtle.Pen
while True:
    screen.exitonclick()
    # yukarıda input aldığımız ekstra datayı kullan
