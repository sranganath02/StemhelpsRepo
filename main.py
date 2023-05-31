#This is the first comment
variable = 2
print(str(variable) + " is my favorite number")

# for(int i = 0; i < 3; i+=2) {
# print("whatever")
# }
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
weirdArr = [1, "apple", True]
for i in range(len(arr)):
    print(arr[i])
print("===============")


print(arr[2:8:2])

print("===============")
#arr [starting point: ending point: how much you skip]
#ascending
print(arr[1::2])

print("===============")
#decending
#arr [starting point: ending point: how much you skip]
print(arr[::-2])
print("===============")
#strings startin
print("This is a string")
print('This is a character')
#"" means string but '' means character
#using for loops print every character in a new line with the string : "This is a string"
testString  = "     This is a string     "
for i in range(len(testString)):
    if (testString[i] != "s") and (testString[i] != "i"):
        print(testString[i])
print("===============")
print("Without the extra spaces")
for i in range(1, len(testString) - 1):
    if (testString[i] == " ") and ((testString[i - 1] == " ") or (testString[i + 1] == " ")):
        continue
    print(testString[i])
print("===============")
#easier way to do This
banana = testString.strip(" ")
for i in range(len(banana)):
    print(banana[i])
print("===============")
print(banana)
print(banana.split(" "))
print("===============")
print(False and True or False and False)
print("===============")
print(True == "23")
apple = "apple"
banana = "banana"
cherry = "cherry"
lunchbox = []
lunchbox.append(apple)
lunchbox.append(cherry)
lunchbox.remove(lunchbox[0])
print(lunchbox)
print("===============")
#dictionaries
#dictionary has keys and values. nameOfDictionary[key]  = value
backpack = ["apple", "apple","apple", "apple", "apple","apple", "banana", "banana", "banana", "banana", "cherry", "cherry","cherry", "cherry","cherry","cherry", "cherry"]
dict = {"lunchbox": ["apple", "banana", "cheese"], "bitches": "none"}
dict["lunchbox"].append(cherry)
print(dict["lunchbox"][:])
print("===============")


dictbackpack = {}
for i in range(len(backpack)):
    if (backpack[i] not in dictbackpack):
        dictbackpack[backpack[i]] = 1
    else:
        dictbackpack[backpack[i]] +=1
print(dictbackpack)
print("===============")
print(str(dictbackpack["apple"]) + " is the number of apples")


# for i in range(len(weirdArr)):
#     print(weirdArr[i])
