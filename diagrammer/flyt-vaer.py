grader=int(input("Hvor mange grader er det ute? "))

if grader < 10:
    print("Ta på jakke")
    type=input("Regner det? ")
    if type.lower()=="ja":
        print("Ta med paraply")
else:
    print("Kos deg i det varme været")



I=0
while i<20:
    I+=2
    print(I)