# day = input("Enter the day:")
# if day == "Friday":
#     print("Today is friday")
# else:
#     print("Today is not friday")

    
# weather = input("Enter the weather:")
# if weather == "rainy":
#     print("It is rainy day")
# elif weather == "sunny":
#     print("It is sunny day")
# else:
#     print("It is cold day")
 
    
# marks = int(input("Enter the marks:"))
# if marks > 75:
    #  print("Pass")
# elif marks <= 75:
    # print ("average")
# elif marks < 50:
    # print("good")
# else:
    # print("fail")


    
# if-else task


# Question1
# name = input("Enter the name:")
# age = int(input("Enter the age:"))
# height = float(input("Enter the height:"))

# if age >= 21:
#     print("Is adult")
# else:
#      print("Is minor")


# question2
# numbers = [1,2,3,4,5]
# for i in range(5):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)

# even_numbers = []
# odd_numbers = []

# for n in numbers:
#     if n % 2 == 0:
#         even_numbers.append(n)
#     else:
#         odd_numbers.append(n)

# print("All numbers:", numbers)
# print("Even numbers:", even_numbers)
# print("Odd numbers:", odd_numbers)


# question3
# marks = (70, 55, 48, 90, 60)

# average = sum(marks) / len(marks)

# print("Average:", average)


# if average >= 50:
#     print("Pass")
# else:
#     print("Fail")
 
    
# question4
# ch = input("Enter a single character: ")

# if len(ch) != 1:
#     print("Please enter exactly one character.")
# else:
#     if ch.isdigit():
#         print("Digit")
#     elif ch.lower() in 'aeiou':
#         print("Vowel")
#     elif ch.isalpha():
#         print("Consonant")
#     else:
#         print("Neither vowel, consonant, nor digit")
 
        
# question5
# print("Enter 10 numbers:")
# numbers = []

# for i in range(10):
#     n = int(input(f"Number {i+1}: "))
#     numbers.append(n)

# unique_numbers = set(numbers)

# print("Unique numbers:")
# for num in unique_numbers:
#     print(num)


# question10
# numbers = (10, 25, 30, 35, 40, 18, 50, 67)
# print("Numbers greater than 30 are :")
# for num in numbers:
#     if num >30:
#         print(num)
     
        
# question11
# users = {
#     "riya" : "1507",
#     "krishna" : "1811"
# } 
# username = input("Enter username:")
# password = input("Enter the password:")

# if username in users and users[username]==password :
#     print("Login Valid")
# else:
#     print("Login Invalid")
 
    
# question12 
# cities_temp = {
#     "Baroda": 42.5,
#     "Mumbai": 33.2,
#     "Delhi": 41.0,
#     "Kolkata": 36.8,
#     "Jaipur": 40.5,
#     "Chennai": 38.3
# }

# print("Cities with temperature greater than 40°C:")

# for city, temp in cities_temp.items():
#     if temp > 40:
#        print(city, "-", temp)


# question14
# chars = ['a', 'b', 'e', 'k', 'o']

# vowels = 0
# consonants = 0

# for ch in chars:
    # if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        # vowels += 1
    # else:
        # consonants += 1

# print("Vowels:", vowels)
# print("Consonants:", consonants)


# question18
# students = {
#     "Riya": 78,
#     "Krishna": 67,
#     "Neha": 47,
#     "Prachi": 69,
#     "khushi": 55
# }

# for name, marks in students.items():
#     if marks >= 50:
#         print(name, "Passed")
#     else:
#         print(name,"Failed")  
 
        
# question20
# numbers = [10, 25, 5, 40, 15, 60, 30]

# smallest = min(numbers)
# largest = max(numbers)
# average = sum(numbers) / len(numbers)

# result = {
#     "smallest": smallest,
#     "largest": largest,
#     "average": average
# }  
# print(result)


# question19
# books = [
#     "Maths",
#     "Cloud Computing",
#     "Python Basics",
#     "Data Science",
#     "Cloud Computing",
#     "Maths"
# ]
# book_count = {}

# for book in books:
#     if book in book_count:
#         book_count[book] += 1
#     else:
#         book_count[book] = 1
        
# print("Book frequency:")
# print(book_count)


# question16
# numbers = []

# for i in range(10):
    # num = int(input(f"Enter number {i+1}: "))
    # numbers.append(num)

# unique_numbers = list(set(numbers))

# even_numbers = []

# for num in unique_numbers:
    # if num % 2 == 0:
        # even_numbers.append(num)

# odd_numbers = []

# for num in unique_numbers:
    # if num % 2 != 0:
        # odd_numbers.append(num)

# print("Original List:", numbers)
# print("List without duplicates:", unique_numbers)
# print("Even Numbers:", even_numbers)
# print("Odd Numbers:", odd_numbers)


# question15
# name = input("Enter student name: ")

# marks = []

# for i in range(5):
#     mark = int(input(f"Enter marks for subject {i+1}: "))
#     marks.append(mark)

# total = sum(marks)
# average = total / 5

# if average >= 90:
#     grade = "A"
# elif average >= 75:
#     grade = "B"
# elif average >= 60:
#     grade = "C"
# elif average >= 40:
#     grade = "D"
# else:
#     grade = "F"

# student = {
#     "name": name,
#     "marks": marks,
#     "total": total,
#     "average": average,
#     "grade": grade
# }
# print(student)


# question21
# numbers = (10, 15, 8, 7, 20, 13, 4, 9)

# result = {
#     "even": 0,
#     "odd": 0
# }

# for num in numbers:
#     if num % 2== 0:
#         result["even"] += 1
#     else:
#         result["odd"] += 1
        
# print("Tuple:", numbers)
# print("Dictionary:", result)


# question13 
# numbers = []

# print("Enter 10 numbers:")
# for i in range(10):
#     n = float(input(f"Enter number {i + 1}: "))
#     numbers.append(n)

# positive_count = 0
# negative_count = 0
# zero_count = 0

# for n in numbers:
#     if n > 0:
#         positive_count += 1
#     elif n < 0:
#         negative_count += 1
#     else:
#         zero_count += 1
        
# print("Numbers:", numbers)
# print("Positive numbers:", positive_count)
# print("Negative numbers:", negative_count)
# print("Zeros:", zero_count)


# question9
# items = []

# for i in range(5):
#     item = input(f"Enter item {i + 1}: ")
#     items.append(item)


# unique_items = set(items)

# print("You entered:", items)
# print("Unique items:", unique_items)
# print("Number of unique items:", len(unique_items))


# question8
# student = {
#     "name": "Riya",
#     "marks": [85, 92, 78, 88, 90]  # list of marks
# }

# total = sum(student["marks"])

# average = total / len(student["marks"])

# if average >= 90:
#     grade = "A+"
# elif average >= 80:
#     grade = "A"
# elif average >= 70:
#     grade = "B"
# elif average >= 60:
#     grade = "C"
# elif average >= 50:
#     grade = "D"
# else:
#     grade = "F"

# print("Name:", student["name"])
# print("Marks:", student["marks"])
# print("Total:", total)
# print("Average:", average)
# print("Grade:", grade)


# question7
# b1 = input("Value 1 (True/False): ")
# b2 = input("Value 2 (True/False): ")
# b3 = input("Value 3 (True/False): ")

# val1 = (b1.strip().lower() == "true")
# val2 = (b2.strip().lower() == "true")
# val3 = (b3.strip().lower() == "true")

# bool_tuple = (val1, val2, val3)

# true_count = 0

# if bool_tuple[0] == True:
#     true_count += 1
# if bool_tuple[1] == True:
#     true_count += 1
# if bool_tuple[2] == True:
#     true_count += 1

# print("Tuple:", bool_tuple)
# print("Number of True values:", true_count)


# question6
# prices = []
# print("Enter 5 prices:")
# for i in range(5):
#     p = float(input(f"Price {i+1}: "))
#     prices.append(p)

# highest = prices[0]

# if prices[1] > highest:
#     highest = prices[1]

# if prices[2] > highest:
#     highest = prices[2]

# if prices[3] > highest:
#     highest = prices[3]

# if prices[4] > highest:
#     highest = prices[4]

# print("Highest price:", highest)


# Student Result management system

name = input("Enter the student: ")

marks_list = []

for i in range(5):
    mark = float(input(f"Enter mark for subject {i+1}: "))

    if mark > 100:
        print("Not valid")
        continue     

    marks_list.append(mark)

marks_tuple = tuple(marks_list)

total = sum(marks_tuple)
average = total / len(marks_tuple)

if average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

print("\nStudent Result")
print("Marks:", marks_tuple)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)

