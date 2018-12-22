x = input("which part of the cytoskeleton are you confused about? ")

if x == "microfilament":
    y = input("function or structure? ")
    if y == "function":
        print("Provides support for the cell and is involved with cell movement.")
    elif y == "structure":
        print("Composed of actin arranged in twisted double chain.")
elif x == "microtubule":
    y = input("function or structure? ")
    if y == "function":
        print("Shape and support the cell. They also act as tracks for organelles with motor proteins to move.")
    elif y == "structure":
        print("Composed of tubulin arranged in a straight, hollow tube")
elif x == "int filament":
     y = input("function or structure? ")
    if y == "function":
        print("Reinforce cell shape and anchor some organelles.")
    elif y == "structure":
        print("Permanently positioned supercoiled cables of fibrous proteins")