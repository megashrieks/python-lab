class rectangle:
    width = 0
    height = 0
    def __init__(self,w,h):
        self.width = w
        self.height = h
    def getArea(self):
        return self.width * self.height

n = int(input("Enter the number of rectangles : "))
min = 999999
minw = 0
minh = 0

max = -1
maxw = 0
maxh = 0
for i in range(n):
    temp = rectangle(
            int(input("Enter the width of rectangle %d : " % (i+1))),
            int(input("Enter the height of rectangle %d : " % (i+1)))
    )
    temparea = temp.getArea()
    if temparea < min:
        min = temparea
        minw = temp.width
        minh = temp.height
    if temparea > max:
        max = temparea
        maxw = temp.width
        maxh = temp.height

print("dimensions of rectangle with maximum area : ","width : ",maxw,", height : ",maxh)
print("dimensions of rectangle with minimum area : ","width : ",minw,", height : ",minw)
