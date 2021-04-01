# Ascending Descending Order Sorter
#made by Soham
# Give in a list of numbers 
# And have them arranged in ascending or descending order
numList = []
length = int(input("Enter length of list of numbers: "))
i = 0
# This gets all of the numbers in the list
type = input("Enter the type (Ascending/Descending: ")
type = type.upper()
while i < length:
    number = int(input("Enter one number: "))
    numList.append(number)
    number = 0
    i = i + 1
i= 0
OrderedList = []
while i < len(numList):
    OrderedList.append("")
    i = i + 1
if type == "A":
    i = 0
    while i < length:
        OrderedList[i] = min(numList)
        del numList[numList.index(min(numList))]
        i = i + 1
elif type == "D":
    i = 0
    while i < length:
        OrderedList[i] = max(numList)
        del numList[numList.index(max(numList))]
        i = i + 1
OrderedList = str(OrderedList)
OrderedList = OrderedList.replace("[", "")
OrderedList = OrderedList.replace("]", "")
OrderedList = OrderedList.replace("'", "")
print(OrderedList)