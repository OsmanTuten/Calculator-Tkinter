from tkinter import *


LARGE_FONT_STYLE = ("Arial", 40, "bold")

MEDIUM_FONT_STYLE = ("Arial", 32, "bold")

SMALL_FONT_STYLE = ("Arial", 16)

DIGIT_FONT_STYLE = ("Arial", 24, "bold")

DEFAULT_FONT_STYLE = ("Arial", 20)


RED = "#CD5C5C"

LABEL_COLOR = "#25265E"

LIGHT_GRAY = "#F5F5F5"

WHITE = "#FFFFFF"

OFF_WHITE = "#F8FAFF"

LIGHT_BLUE = "#CCEDFF"

VARIABLE_COLOR = "#b2c8ff"

BLACK = "#000000"



class menu:


    def __init__(self):

        self.root = Tk()

        self.root.geometry("400x667")

        self.root.resizable(0,0)

        self.root.title("Menu")

        self.buttons_frame = self.create_buttons_frame()

        self.buttons = self.create_buttons()

        for x in range(0, 4):

            self.buttons_frame.rowconfigure(x, weight=1)

        self.buttons_frame.columnconfigure(0, weight=1)
        


    def create_buttons_frame(self):

        buttons_frame = Frame(self.root)
        buttons_frame.pack(expand=True, fill="both")

        return buttons_frame


    def create_buttons(self):

        self.use_calculator_button()
        self.use_function_button()
        self.define_function_button()
        self.delete_function_button()


    def use_calculator_button(self):

        button = Button(self.buttons_frame, text="CALCULATOR", bg=WHITE, fg=LABEL_COLOR, font=DIGIT_FONT_STYLE, borderwidth=1, command=self.open_calculator)
        button.grid(row=0, column=0, sticky=NSEW)


    def use_function_button(self):

        button = Button(self.buttons_frame, text="USE FUNCTION", bg=WHITE, fg=LABEL_COLOR, font=DIGIT_FONT_STYLE, borderwidth=1, command=self.open_function_screen)
        button.grid(row=1, column=0, sticky=NSEW)


    def define_function_button(self):

        button = Button(self.buttons_frame, text="DEFINE FUNCTION", bg=WHITE, fg=LABEL_COLOR, font=DIGIT_FONT_STYLE, borderwidth=1, command=self.open_define_function_screen)
        button.grid(row=2, column=0, sticky=NSEW)


    def delete_function_button(self):

        button = Button(self.buttons_frame, text="delete function".upper(), bg=WHITE, fg=LABEL_COLOR, font=DIGIT_FONT_STYLE, borderwidth=1, command=self.open_delete_function_screen)
        button.grid(row=3, column=0, sticky=NSEW)


    def open_calculator(self):

        self.root.destroy()
        open_calc()


    def open_function_screen(self):

        self.root.destroy()
        open_function_screen()


    def open_define_function_screen(self):

        self.root.destroy()
        open_define_function_screen()


    def open_delete_function_screen(self):

        self.root.destroy()
        open_delete_function_screen()


    def run(self):

        self.root.mainloop()


def open_menu():

    menu1 = menu()
    menu1.run()


class calculator:

    def __init__(self):

        self.root = Tk()

        self.root.geometry("400x667")

        self.root.resizable(0,0)

        self.root.title("Calculator")

        self.display_frame = self.create_display_frame()

        self.buttons_frame = self.create_buttons_frame()

        self.total_expression = ""

        self.current_expression = ""

        self.total_label, self.current_label = self.create_display_labels()

        self.DIGITS = {

            7: (0, 1), 8: (0, 2), 9: (0, 3),

            4: (1, 1), 5: (1, 2), 6: (1, 3),

            1: (2, 1), 2: (2, 2), 3: (2, 3)

            }

        self.buttons = self.create_digit_buttons()

        self.operations = {"/": (2, 5, "\u00F7"), "*": (2, 4, "\u00D7"), "-": (3, 4, "-"), "+": (3, 5, "+"), "(": (1, 4, "("), ")": (1, 5, ")")}

        self.create_operator_buttons()

        self.create_special_buttons()

        self.buttons_frame.rowconfigure(0, weight=1)

        for x in range(1, 5):

            self.buttons_frame.rowconfigure(x, weight=1)

            self.buttons_frame.columnconfigure(x, weight=1)

        self.buttons_frame.columnconfigure(5, weight=1)


    def create_display_frame(self):

        display_frame = Frame(self.root, height=221, bg=LIGHT_GRAY)
        display_frame.pack(expand=True, fill="both")

        return display_frame


    def create_buttons_frame(self):

        buttons_frame = Frame(self.root)
        buttons_frame.pack(expand=True, fill="both")

        return buttons_frame


    def create_display_labels(self):

        total_label = Label(self.display_frame, text=self.total_expression, anchor=E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill="both")
        current_label = Label(self.display_frame, text=self.current_expression, anchor=E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        current_label.pack(expand=True, fill="both")

        return total_label, current_label



    def create_digit_buttons(self):

        for digit, coordinate in self.DIGITS.items():
            button = Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGIT_FONT_STYLE, borderwidth=0, command=lambda x = digit: self.add_to_expression(x))
            button.grid(row=coordinate[0], column=coordinate[1], sticky=NSEW)


    def create_operator_buttons(self):

        row = 0

        for operator, symbol in self.operations.items():
            button = Button(self.buttons_frame, text=symbol[2], bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=symbol[0], column=symbol[1], sticky=NSEW)
            row += 1


    def append_operator(self, operator_):

        self.current_expression += operator_
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_current_label()
        self.update_total_label()


    def add_to_expression(self, value):

        self.current_expression += str(value)
        self.update_current_label()


    def update_total_label(self):

        expression = self.total_expression

        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f" {symbol[2]} ")

        self.total_label.config(text=expression)


    def update_current_label(self):

        self.current_label.config(text=self.current_expression[:11])


    def create_special_buttons(self):

        self.create_clear_button()
        self.create_equals_button()
        self.create_power_of_button()
        self.create_menu_button()
        self.create_zero_button()
        self.create_dot_button()


    def create_zero_button(self):

        button = Button(self.buttons_frame, text="0", bg=WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda: self.add_to_expression(0))
        button.grid(row=3, column=1, columnspan=3, sticky=NSEW)


    def create_dot_button(self):

        button = Button(self.buttons_frame, text=".", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda: self.add_to_expression('.'))
        button.grid(row=4, column=3, sticky=NSEW)
    


    def create_power_of_button(self):

        button = Button(self.buttons_frame, text="x\u207F", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.power_of)
        button.grid(row=4, column=2, sticky=NSEW)


    def create_clear_button(self):

        button = Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.clear)
        button.grid(row=4, column=1, sticky=NSEW)


    def create_equals_button(self):

        button = Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=4, columnspan=2, sticky=NSEW)



    def create_menu_button(self):

        button = Button(self.buttons_frame, text="menu", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.open_menu)
        button.grid(row=0, column=4, columnspan=2, sticky=NSEW)


    def clear(self):

        self.current_expression = ""
        self.total_expression = ""
        self.update_total_label()
        self.update_current_label()


    def power_of(self):

        self.current_expression = str(f"{self.current_expression}**")
        self.update_current_label()


    def sqrt(self):

        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_current_label()


    def evaluate(self):

        self.total_expression += self.current_expression
        self.update_total_label()

        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""

        except Exception as e:
            self.current_expression = "Error"

        finally:
            self.update_current_label()

        self.update_current_label()


    def open_menu(self):

        self.root.destroy()
        open_menu()


    def run(self):

        self.root.mainloop()


def open_calc():

    calc = calculator()
    calc.run()


class function_screen:

    def __init__(self):

        self.root = Tk()

        self.root.geometry("600x600")

        self.root.resizable(0,0)

        self.root.title("Function")

        self.display_frame = self.create_display_frame()

        self.variables_frame = self.create_variables_frame()

        self.options = self.get_functions()

        self.functions_dropdown = self.create_functions_dropdown()

        self.variables = ['x','y','z','d','e']

        self.variable_entry_values = self.create_variable_buttons()

        self.result = ""

        self.equation = ""

        self.create_equals_button()

        self.function_label, self.result_label = self.create_display_labels()

        self.create_menu_button()

        for y in range(0, 3):

            self.variables_frame.rowconfigure(y, weight=1)

        for x in range(0, 5):

            self.variables_frame.columnconfigure(x, weight=1)


    def create_display_frame(self):

        display_frame = Frame(self.root, height=50, bg=LIGHT_GRAY)
        display_frame.pack(expand=True, fill="both")

        return display_frame


    def create_variables_frame(self):

        variables_frame = Frame(self.root, height=150, bg=OFF_WHITE)
        variables_frame.pack(expand=True, fill="both")

        return variables_frame


    def create_display_labels(self):

        function_label = Label(self.display_frame, text=self.equation, anchor=E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        function_label.pack(expand=True, fill="both")
        result_label = Label(self.display_frame, text="", anchor=E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        result_label.pack(expand=True, fill="both")

        return function_label, result_label


    def get_functions(self):

        functions_list = []

        with open('functions2.txt', 'r') as file:
            Lines = file.readlines()

            for line in Lines:
                functions_list.append(line)
        
        return functions_list


    def create_functions_dropdown(self):

        selection = StringVar()
        selection.set("Select a function")
        DROP = OptionMenu(self.display_frame, selection, *self.options)
        DROP.config(bg=LIGHT_BLUE)
        DROP.config(fg=LABEL_COLOR)
        DROP.config(font=DEFAULT_FONT_STYLE)
        DROP.config(borderwidth=0)
        DROP.config(anchor=E)
        DROP.pack(expand=True, fill="both")

        return selection


    def create_variable_buttons(self):

        row, col = 0, 0
        variable_buttons = []

        for variable in self.variables:
            msg = Entry(self.variables_frame, bg=VARIABLE_COLOR, fg=LABEL_COLOR, font=DIGIT_FONT_STYLE, borderwidth=0)##########
            msg.grid(row=row, column=col, padx=1, pady=1, sticky=NSEW)
            msg.insert(0, f" {variable}: 0")
            col += 1
            variable_buttons.append(msg)


        return variable_buttons


    def create_equals_button(self):

        equals_button = Button(self.variables_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.evaluate)
        equals_button.grid(row=1, column=0, columnspan=5, padx=1, pady=1, sticky=NSEW)


    def create_menu_button(self):

        button = Button(self.variables_frame, text="menu", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.open_menu)
        button.grid(row=2, column=0, columnspan=5, sticky=NSEW)


    def open_menu(self):

        self.root.destroy()
        open_menu()


    def evaluate(self):

        s = self.functions_dropdown.get()
        x, y, z, d, e = self.variable_entry_values[0].get().split(":")[1], self.variable_entry_values[1].get().split(":")[1], self.variable_entry_values[2].get().split(":")[1], self.variable_entry_values[3].get().split(":")[1], self.variable_entry_values[4].get().split(":")[1]

        with open("functions2.txt", "r") as f:
            Lines = f.readlines()
            index = 0

            for line in Lines:
                if line == s:
                    break
                else:
                    index += 1

        with open("functions1.txt", "r") as f:
            Lines = f.readlines()
            equation = str((Lines[index]).format(x=x,y=y,z=z,d=d,e=e))
            self.equation = str((Lines[index]).format(x=x,y=y,z=z,d=d,e=e))[0:len(equation)-23]
            print("equation:", equation)
            print("self.equation:", self.equation)
            self.result = str(eval(equation))
            self.function_label.config(text=self.equation)
            self.result_label.config(text=self.result)


    def run(self):
        self.root.mainloop()


def open_function_screen():
    function_screen_ = function_screen()
    function_screen_.run()
    

class def_function_screen(calculator):

    def __init__(self):
        super().__init__()

        self.root.title("New Function")

        self.root.geometry("400x750")

        self.buttons_frame.rowconfigure(5, weight=1)

        self.variables = ['x','y','z','d','e']

        self.variable_buttons = self.create_variable_buttons()

        self.create_save_function_button()

        self.function_expression = ""


    def add_to_expression(self, value):

        self.current_expression += str(value)

        if self.current_expression in self.variables:
            self.function_expression += "{" + value + "}"
        else:
            self.function_expression += str(value)

        self.update_current_label()


    def create_variable_buttons(self):

        column = 1

        for variable in self.variables:
            button = Button(self.buttons_frame, text=variable, bg=VARIABLE_COLOR, fg=LABEL_COLOR, font=DIGIT_FONT_STYLE, borderwidth=0, command=lambda x = variable: self.add_to_expression(x))
            button.grid(row=5, column=column, sticky=NSEW)
            column += 1



    def append_operator(self, operator_):

        self.current_expression += operator_
        self.total_expression += self.current_expression
        print("self.current_expression:", self.current_expression)
        if self.current_expression in self.variables:
            self.function_expression += "{" + operator_ + "}"
            
        else:
            self.function_expression += str(operator_)

        print("self.func_expression:", self.function_expression)
        self.current_expression = ""
        self.update_current_label()
        self.update_total_label()

    #################################################################################################################
    #################################################################################################################
    #################################################################################################################
    #################################################################################################################
    
    def power_of(self):

        self.current_expression = str(f"{self.current_expression}**")
        self.total_expression += self.current_expression
        self.function_expression += str("**")
        self.update_current_label()
        print("self.current_expression:", self.current_expression)
        print("self.func_expression:", self.function_expression)
        
        self.current_expression = ""

        self.update_total_label()
        
    def create_save_function_button(self):

        button = Button(self.buttons_frame, text="save", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE , borderwidth=0, command=self.save_function)
        button.grid(row=4, column=4, columnspan=2, sticky=NSEW)


    def save_function(self):

        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_current_label()

        with open("functions1.txt", "a") as f:
            print(self.function_expression)
            f.write(str(self.function_expression) +"      +(({x}+{y}+{z}+{d}+{e})*0) \n")

        with open("functions2.txt", "a") as f:
            print(self.total_expression)
            f.write(str(self.total_expression) +" \n")

        self.function_expression = ""


    def clear(self):

        self.current_expression = ""
        self.total_expression = ""
        self.function_expression = ""
        self.update_total_label()
        self.update_current_label()


def open_define_function_screen():
    def_function_screen_ = def_function_screen()
    def_function_screen_.run()


class delete_function_screen():

    def __init__(self):

        self.root = Tk()

        self.root.geometry("400x400")

        self.root.resizable(0,0)

        self.root.title("Delete Function")

        self.dropdown_frame, self.buttons_frame = self.create_frames()

        self.options = self.get_options()

        self.functions_dropdown = self.create_functions_dropdown()

        self.delete_button = self.create_delete_button()

        self.create_menu_button()

        for x in range(0, 3):

            self.root.rowconfigure(x, weight=1)

        self.root.columnconfigure(0, weight=1)
        

    def create_frames(self):

        self.dropdown_frame = Frame(self.root, bg = LIGHT_GRAY)
        self.dropdown_frame.grid(row=0, column=0, sticky=NSEW)

        self.buttons_frame = Frame(self.root, bg=LIGHT_GRAY)
        self.buttons_frame.grid(row=1, column=0, rowspan=2,  sticky=NSEW)

        return self.dropdown_frame, self.buttons_frame

    
    def create_functions_dropdown(self):
        
        selection = StringVar()
        selection.set("Select a function")
        DROP = OptionMenu(self.dropdown_frame, selection, *self.options)
        DROP.config(bg=LIGHT_BLUE)
        DROP.config(fg=LABEL_COLOR)
        DROP.config(font=DEFAULT_FONT_STYLE)
        DROP.config(borderwidth=0)
        DROP.pack(expand=True, fill="both")

        return selection


    def get_options(self):

        options = []

        with open("functions2.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                options.append(line)

        return options

    def get_selection_index(self):

        selection = self.functions_dropdown.get()
        index = 0

        for option in self.options:
            if option == selection:

                return index

            index += 1


    def delete_function(self):

        index = self.get_selection_index()

        with open("functions1.txt", "r+") as f:
            lines = f.readlines()
            del lines[index] 
            f.seek(0)
            f.truncate()
            f.writelines(lines)

        with open("functions2.txt", "r+") as f:
            lines = f.readlines()
            del lines[index] 
            f.seek(0)
            f.truncate()
            f.writelines(lines)
            
        self.root.destroy()
        open_delete_function_screen()


    def create_delete_button(self):

        button = Button(self.buttons_frame, text='delete'.upper(), bg=RED, fg=WHITE, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.delete_function)
        button.pack(expand=True, fill="both")


    def open_menu(self):

        self.root.destroy()
        open_menu()


    def create_menu_button(self):

        button = Button(self.buttons_frame, text="menu", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.open_menu)
        button.pack(expand=True, fill="both")
    

def open_delete_function_screen():

    menu1 = delete_function_screen()
    
if __name__ == '__main__':
    open_menu()
    




