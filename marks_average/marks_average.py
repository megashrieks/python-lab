file = open(input("Enter filename :"))
for line in file:
    total = 0
    linestr = line.split()
    for i in range(1,len(linestr)):
        total += int(linestr[i])
    print("Student :%s\ntotal : %d\naverage : %f\n"%(linestr[0],total,total/(len(linestr)-1)))
