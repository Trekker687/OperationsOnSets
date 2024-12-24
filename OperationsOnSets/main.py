set1 = {""}
set1.remove("")
for i in range(0,4):
    num = int(input("Enter a number: "))
    set1.add(num)
print("set of integers: ", set1)


set2 = {""}
set2.remove("")
for i in range(0,3):
    num = int(input("Enter a number: "))
    string = input("Enter a string: ")
    set2.add(string)
    set2.add(num)
print("set of mixed datatypes : " ,set2)

set3 = {""}
set3.remove("")
for i in range(0,2):
    num = int(input("Enter a number: "))
    dupli = int(input("Enter the duplicate of the number: "))
    set3.add(dupli)
    set3.add(num)
print("set of numbers with duplicates removed: ", set3)

set4 = {""}
set4.remove("")
for i in range(0,6):
    num = int(input("Enter a number: "))
    set4.add(num)
print("set of integers: ", set4)
removenum = int(input("Enter a number to remove from the set"))
for r in range(len(set4)):
    if removenum == set4[r]:
        set4.remove(set4[r])
        print("New set : ", set4)
        break
    else:
        i == i+1
