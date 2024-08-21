

def calculate(type):
    with open("data.txt", "r") as file:
        lines = file.readlines()

    numbers = [int(i) for i in lines[0].split()]
    if type == "add":
        return sum(numbers)
    elif type == "multiply":
        out = 1
        for i in range(len(numbers)):
            out = out * numbers[i]
        return out
    elif type == "minus":
        out = numbers[0]
        for i in range(len(numbers)-1):
            out = out - numbers[i]
        return out
    elif type == "divide":
        out = numbers[0]
        for i in range(len(numbers)-1):
            if numbers[i] != 0:
                out = out / numbers[i]
            else:
                return "Division by zero"
        return out
    else:
        return "Invalid type"

print(calculate("divide"))