def three_args(var1, var2, var3):
    if var1 == None and var2 is not None and var3 is not None:
        print(f"Переданы аргументы: var2={var2}, var3={var3}")
    elif var1 is not None and var2 == None and var3 is not None:
        print(f"Переданы аргументы: var2={var2}, var3={var3}")
    elif var1 is not None and var2 is not None and var3 == None:
        print(f"Переданы аргументы:  var1={var1}, var2={var2}")
    else:
        print("More than one argument is none")
three_args(None, 3, 4)


