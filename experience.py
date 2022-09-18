def getExperience(exp):
    exp = str(exp).strip()
    try:
        return int(exp)
    except:
        pass
    try:
        test = exp.split("-")
        x = int(test[0])
        y = int(test[1])
        return (x + y) // 2
    except:
        pass
    try:
        # print(exp)
        if exp.endswith("+"):
            test = exp.replace('+', '')
            return int(test)
    except:
        pass
    return -1


x = "10"
print(getExperience(x))
x = "10-20"
print(getExperience(x))
x = "10+"
print(getExperience(x))
x = "1+0"
print(getExperience(x))
