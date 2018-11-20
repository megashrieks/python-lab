file = open("data.txt")
lines = 0
string = ""
for line in file:
    string += line
    lines += 1
words = len(string.split())
chars = len(string) - words
print("lines :",lines,"\nwords : ",words,"\nchars :",chars)
