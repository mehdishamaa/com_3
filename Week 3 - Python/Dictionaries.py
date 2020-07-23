def solve(width, height, length, mass):
    if mass >= 20 and (width * height * length) >= 1000000 or (width >= 150 or height >= 150 or length >= 150):
        x = "BH"
        print("REJECTED")
    elif mass >= 20:
        x = "H"
        print("SPECIAL")
    elif (width * height * length) >= 1000000 or (width >= 150 or height >= 150 or length >= 150):
        x = "B"
        print("SPECIAL")
    else:
        x = "S"
        print("STANDARD")



solve(30, 40, 30, 50)




























