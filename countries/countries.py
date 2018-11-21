names = []
capitals = []
populations = []
max = -1

def putCountry(name, capital, population):
    global max
    if name in names:
        print("Country already exists")
    else:
        names.append(name)
        capitals.append(capital)
        populations.append(population)
        print("Country inserted successfully")
        if max is -1:
            max = 0
        elif populations[max] < population:
            max = len(populations) - 1
option = -1
while option is not 4:
    print("Enter option : ")
    print("1. Insert Country")
    print("2. Get Country Information")
    print("3. Get Max Population")
    print("4. Exit")
    option = int(input())
    if option is 1:
        putCountry(
                input("Enter country name : "),
                input("Enter country capital : "),
                input("Enter country population : ")
                )
    elif option is 2:
        name = input("Enter the country name to fetch the information : ")
        if name not in names:
            print("Country doesn't exist")
        else:
            index = names.index(name)
            print("Capital : ",capitals[index])
            print("Population : ",populations[index])
    elif option is 3:
        if max is -1:
            print("Enter atleast 1 country")
        else:
            print("The country with the highest population is : ",names[max])
