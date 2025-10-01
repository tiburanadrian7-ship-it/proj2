def processcount(string):
    chars = {}
    for char in string:
        lowerchar = char.lower()
        if lowerchar in chars:
            chars[lowerchar][0] += 1
        else:
            chars[lowerchar] = [1, char] 

    for processcount, char in chars.values():
        print(f"{char}={processcount}", end=", ")
    print()

string = input("Enter string: ")
str1, str2 = [s.strip() for s in string.split(",")]

processcount(str1)
processcount(str2)