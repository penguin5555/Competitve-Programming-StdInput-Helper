def stdInput(type): # assists in getting inputs in different ways and returns the data needed
    if type == "TC": # test case count
        return int(input())
    if type == "SI": # spaced integers
        return [int(i) for i in input().split()]
    if type == "SS": # spaced strings
        return [i for i in input().split()]
    if type == "TCSI": # needs test case count, spaced integers
        fin = []
        for _ in range(stdInput("TC")):
            x = [int(i) for i in input().split()]
            fin.append(x)
        return fin
    if type == "TCSS": # needs test case count, spaced strings, gives string of each line
        fin = []
        for _ in range(stdInput("TC")):
            x = [i for i in input().split()]
            fin.append(x)
        return fin
    if type == "S": # single string
        return input()
    if type == "I": # single integer
        return int(input())

# example: T = stdInput("TC")
