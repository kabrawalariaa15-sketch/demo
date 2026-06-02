# for loop practice

# name = "kabrawala"
# for kabrawala in name:
#    print(kabrawala) 
  
# name = "kabrawala riya"
# for kabrawala  in name:
    # print(kabrawala) 
    
# fruit = ['apple', 'orange', 'banana', 'mango']
# for k in fruit:
    # print(k)
    
# for i in range(50):
    # print(i)
   
# for i in range(0,100):
    # print(i)
    
# for i in range(0,50,2):
    # print(i)
    
# for i in range(50,0,-1):
    # print(i)
    
# for i in range(0,50,3):
    # print(i)

# for i in range(50):
    #  if i == 25:
        #  break
    #  print(i)
     
# for i in range(50):
    # if i == 25:
        # continue
    # print(i)
    
# while loop practice

# i = 0
# while i in range(50):
#     print(i)
#     i += 1
    
# i = 0
# while i in range(50):
#     print(i)
#     i += 2

# i = 0
# while i in range(50):
#     if i == 20:
#         break
#     print(i)
#     i += 1
        
# i = 0
# while i in range(50):
#     i += 1
#     if i == 5:
#         continue
#     print(i)


# loop question
# Q1
# numbers = [10, 20, 30, 40, 50]
# total = 0
# for i in numbers:
#     total = total + i
# print("Sum =", total)

#  Q2
# numbers = [10, 15, 20, 25, 30, 35, 40]
# for i in numbers:
#     if i % 2 == 0:
#         print(i)

# Q3
# numbers = [10, 15, 20, 25, 30, 35, 40]
# for i in numbers:
    # if i % 2 != 0:
        # print(i)

#  Q4
# numbers = [20, 55, 10, 75, 40, 90, 30]
# count = 0
# for i in numbers:
#     if i > 50:
#         count = count + 1
# print("Count =", count)

# Q5
# numbers = [25, 80, 15, 95, 40, 60]
# maximum = numbers[0]
#  for i in numbers:
    # if i > maximum:
        # maximum = i
# print("Maximum number =", maximum)

#  Q6
# numbers = [25, 80, 15, 95, 40, 60]
# minimum = numbers[0]
# for i in numbers:
    # if i < minimum:
        # minimum = i
# print("Minimum number =", minimum)

# Q7
# numbers = [10, -5, 20, -8, 15, -3, 0]
# positive = 0
# negative = 0
# for i in numbers:
#     if i > 0:
#         positive = positive + 1
#     elif i < 0:
#         negative = negative + 1
# print("Positive numbers =", positive)
# print("Negative numbers =", negative)

# Q8
# numbers = (10, 20, 30, 40, 50)
# for i in numbers:
    # print(i)

#  Q9
# numbers = (10, 25, 15, 30, 5, 40, 18)
# count = for i in numbers:
#     if i < 20:
#         count = count + 1
# print("count =", count)

#  Q10
# numbers = (10, 20, 30, 40, 50)
# total = 0
# for i in numbers:
#     total = total + i
# print("Sum =", total)

#  Q11
# text = input("Enter a string: ")
# count = 0
# for i in text:
#     if i in "aeiouAEIOU":
#         count = count + 1
# print("Number of vowels =", count)

#  Q12
# text = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# consonants = 0
# for i in text:
#     if i.isalpha():  # check only letters
#         if i not in vowels:
#             consonants = consonants + 1
# print("Number of consonants =", consonants)

# Q13
# text = input("Enter a string: ")
# for i in text:
    # print(i)

#  Q14
# text = input("Enter a string: ")
# count = 0
# for i in text:
    # if i.isupper():
        # count = count + 1
# print("Number of uppercase letters =", count)

# Q15
# text = input("Enter a string: ")
# count = 0
# for i in text:
    # if i.islower():
        # count = count + 1
# print("Number of lowercase letters =", count)

#  Q16
# numbers = {1, 2, 3, 2, 4, 1, 5}
# print("Unique elements are:")
# for i in numbers:
    # print(i)

#  Q17
# numbers = {45, 120, 67, 150, 99, 200, 80}
# count = 0
# for i in numbers:
    # if i > 100:
        # count += 1
# print("Count of numbers greater than 100:", count)

# q18
# student = {
#     "name": "Riya",
#     "age": 20,
#     "course": "MCA"
# }
# print("Dictionary Keys:")
# for key in student.keys():
#     print(key)

# Q19
# student = {
#     "name": "Riya",
#     "age": 20,
#     "course": "MCA"
# }
# print("Dictionary Values:")
# for value in student.values():
#     print(value)

# Q20
# marks = int(input("Enter marks: "))
# if marks >= 35:
    # print("Pass")
# else:
    # print("Fail")

# Q21
# numbers = [10, 15, 22, 7, 8, 13, 24]
# even_count = 0
# odd_count = 0
# for i in numbers:
    # if i % 2 == 0:
        # even_count += 1
    # else:
        # odd_count += 1
# print("Even numbers count:", even_count)
# print("Odd numbers count:", odd_count)

#Q22
# numbers = [10, 20, 30, 40, 50]
# total = sum(numbers)
# count = len(numbers)
# average = total / count
# print("Average is:", average)

#Q23
# numbers = [10, -5, 20, -8, 0, 15, -3]
# positive = []
# negative = []
# for i in numbers:
    # if i >= 0:
        # positive.append(i)
    # else:
        # negative.append(i)
# print("Positive numbers list:", positive)
# print("Negative numbers list:", negative)

# Q24
# numbers = [10, 12, 25, 33, 40, 55, 67]
# count = 0
# for i in numbers:
    # if i % 5 == 0:
        # count += 1
# print("Count of numbers divisible by 5:", count)

# Q25
# text = input("Enter a string: ")
# reverse_text = ""
# for i in text:
    # reverse_text = i + reverse_text
# print("Reversed string:", reverse_text)

#Q26
# text = input("Enter a string: ")
# freq = {}
# for char in text:
    # if char in freq:
        # freq[char] += 1
    # else:
        # freq[char] = 1
# print("Character frequency:")
# for key, value in freq.items():
    # print(key, ":", value)

#  Q28
# list1 = [5, 10, 15, 20]
# list2 = [25, 30, 35, 40]
# merged_list = list1 + list2
# print("Merged list elements:")
# for i in merged_list:
    # print(i)
    
# Q27
# number = [110, 1, 88, 25, 69]
# unique_number = list(set(number))
# unique_number.sort(reverse=True)
# if len(unique_number) >=2:
    # second_largest = unique_number
    # print("Second largest number is:",second_largest)
# else:
    # print("Second largest number not found")

# Q29
# count = 0
# for i in range
# for i in range(10, 51):
    # count += 1
# print("Count of numbers between 10 and 50 is:", count)

# Q30
# numbers = [1, 2, 3, 2, 4, 5, 1, 6]
# unique_numbers = list(set(numbers))
# print("List after removing duplicates:")
# print(unique_numbers)

# Q31
# numbers = [2.5, 3.7, 1.2, 4.6, 5.0]
# total = sum(numbers)
# print("Sum of float numbers is:", total)


#Q32
# words = ["apple", "banana", "orange", "grapes"]
# vowels = "aeiou"
# count = 0
# for word in words:
#     for ch in word.lower():
#         if ch in vowels:
#             count += 1
# print("Total vowels:", count)

# Q33
# students = {
#     "Riya": 78,
#     "Krishna": 45,
#     "Neha": 67,
#     "Durva": 32,
#     "Priya": 88
# }
# print("Passed Students:")
# for name, marks in students.items():
#     if marks >= 50:
#         print(name, ":", marks)

#Q34
# products = {
    # "Shoes": 2000,
    # "Bag": 1500,
    # "Watch": 3000
# }
# discount = 10   # 10% discount
# for product, price in products.items():
    # new_price = price - (price * discount / 100)
    # print(product, "Discounted Price:", new_price)


#Q35
# marks = {
    # "Riya": 85,
    # "Krishna": 72,
    # "Sonal": 90,
    # "Neha": 65
# }
# highest = max(marks.values())
# print("Highest value in dictionary is:", highest)

#Q36
# marks = {
    # "riya": 85,
    # "krishna" : 72,
    # "Sonal" : 90,
    # "Neha" : 65
# }
# lowest = min(marks.values())
# print("Lowest value in dictionary is:", lowest)

#Q37
# numbers = [2, 4, 6, 8, 10]
# result = 1
# for num in numbers:
    # result = result *num
# print("Multiplication of all numbers is:",result)
#  
#  38
# students = [ 
    # ("Riya", 85),
    # ("krishna", 78),
    # ("Neha", 92)
# ]
# for item in students:
    # print(item)
    
# Q39
# tuples_list = [
    # (1, 2, 3),
    # ("a", "b"),
    # (10,),
    # (4, 5, 6, 7)
# ]
# for t in tuples_list:
    # print(t, "has", len(t), "elements")

# Q40
# numbers = [1, 2, 2, 3, 4, 4, 5, 6, 1]
# unique_values = set(numbers)
# print("Unique values:", unique_values)

# Q41
# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 11, 13]
# count = 0
# for num in numbers:
#     if num > 1:
#         is_prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             count += 1
# print("Number of prime numbers in list:", count)

# Q42
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# common_elements = []
# for item in list1:
    # if item in list2:
        # common_elements.append(item)
# print("Common elements:", common_elements)


# Q43
# text = "Python1234"
# digits = 0
# letters = 0
# for ch in text:
    # if ch.isdigit():
        # digits += 1
    # elif ch.isalpha():
        # letters += 1
# print("Digits:", digits)
# print("Letters:", letters)


#Q44
# num = 5  # you can change the number
# for i in range(1, 11):
    # print(num, "x", i, "=", num * i)


#Q45
# sentence = "My name is Riya Kabrawala"
# words = sentence.split()
# print("Number of words:", len(words))


#Q46
# students = [
    # {"name": "Riya", "marks": 85},
    # {"name": "krishna", "marks": 70},
    # {"name": "Neha", "marks": 90},
    # {"name": "kriti", "marks": 60}
# ]
# total = 0
# for student in students:
    # total += student["marks"]
# average = total / len(students)
# print("Average marks:", average)


#Q47
# students = [
    # {"name": "Riya", "marks": 85},
    # {"name": "krishna", "marks": 70},
    # {"name": "Neha", "marks": 90},
    # {"name": "kriti", "marks": 90}
# ]
# highest_marks = max(student["marks"] for student in students)
# print("Topper Student(s):")
# for student in students:
    # if student["marks"] == highest_marks:
        # print(student["name"], "-", student["marks"])

# #Q48
# students = [
#     {"name": "Riya", "marks": 85},
#     {"name": "krishna", "marks": 40},
#     {"name": "Neha", "marks": 55},
#     {"name": "kriti", "marks": 30},
#     {"name": "durva", "marks": 70}
# ]
# pass_count = 0
# fail_count = 0
# for student in students:
#     if student["marks"] >= 50:
#         pass_count += 1
#     else:
#         fail_count += 1
# print("Passed students:", pass_count)
# print("Failed students:", fail_count)


#Q49
# nested_list = [
#     [1, 2, 3],
#     [4, 5],
#     [6, 7, 8, 9]
# ]

# for sublist in nested_list:
#     for element in sublist:
#         print(element)

#Q50
# students = {
#     "student1": {"name": "Riya", "marks": 85},
#     "student2": {"name": "krishna", "marks": 70},
#     "student3": {"name": "Neha", "marks": 90}
# }

# for student_id, details in students.items():
#     for value in details.values():
#         print(value)

#Q51
# nested_list = [
    # [1, 2, 3],
    # [4, 5, 6, 7],
    # [8, 9]
# ]
# even_count = 0
# odd_count = 0
# for sublist in nested_list:
    # for num in sublist:
        # if num % 2 == 0:
            # even_count += 1
        # else:
            # odd_count += 1
# print("Even numbers:", even_count)
# print("Odd numbers:", odd_count)


#Q52
# nested_list = [
    # [1, 2, 3],
    # [4, 5, 6],
    # [7, 8, 9]
# ]
# total_sum = 0 
# for sublist in nested_list:
    # for num in sublist:
        # total_sum += num
# print("Sum of all elements:", total_sum)


#Q53
# marks = 76  
# if marks >= 80:
#     grade = "A"
# elif marks >= 60:
#     grade = "B"
# elif marks >= 40:
#     grade = "C"
# else:
#     grade = "Fail"
# print("Marks:", marks)
# print("Grade:", grade)

#Q54
# text = input("Enter a string: ")

# uppercase = 0
# lowercase = 0
# digits = 0
# symbols = 0

# for ch in text:
#     if ch.isupper():
#         uppercase += 1
#     elif ch.islower():
#         lowercase += 1
#     elif ch.isdigit():
#         digits += 1
#     else:
#         symbols += 1

# print("Uppercase letters:", uppercase)
# print("Lowercase letters:", lowercase)
# print("Digits:", digits)
# print("Symbols:", symbols)


#Q55
# numbers = [10, 7, 13, 20, 17, 9, 5, 22, 11]

# print("Prime numbers:")

# for num in numbers:
#     if num > 1:
#         is_prime = True

#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break

#         if is_prime:
#             print(num)


#Q56
# products = {
#     "Laptop": 50000,
#     "Mobile": 20000,
#     "Headphones": 2000
# }

# tax_rate = 0.10  # 10% tax

# for item, price in products.items():
#     tax = price * tax_rate
#     final_price = price + tax

#     print("Product:", item)
#     print("Original Price:", price)
#     print("Tax:", tax)
#     print("Final Price:", final_price)
#     print()


#Q57
# numbers = [10, 20, 30, 20, 40, 10, 50, 30]

# duplicates = []

# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] == numbers[j]:
#             if numbers[i] not in duplicates:
#                 duplicates.append(numbers[i])

# print("Duplicate elements:", duplicates)


#Q58
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# print("Common elements:")

# for item in set1:
#     if item in set2:
#         print(item)


#Q59
# names = ["Amit", "Riya", "Om", "Neha", "Isha", "Umesh", "Karan"]

# vowels = "AEIOUaeiou"

# print("Names starting with a vowel:")

# for name in names:
#     if name[0] in vowels:
#         print(name)


#Q60
# numbers = [121, 123, 454, 789, 111, 202]

# print("Palindrome numbers:")

# for num in numbers:
#     if str(num) == str(num)[::-1]:
#         print(num)


#Q61
# numbers = [10, -5, 0, 8, -3, 7, 12, 0, -9]

# positive = 0
# negative = 0
# even = 0
# odd = 0
# zero = 0

# for num in numbers:
#     if num > 0:
#         positive += 1
#     elif num < 0:
#         negative += 1
#     else:
#         zero += 1

#     if num != 0:
#         if num % 2 == 0:
#             even += 1
#         else:
#             odd += 1

# print("Positive numbers:", positive)
# print("Negative numbers:", negative)
# print("Even numbers:", even)
# print("Odd numbers:", odd)
# print("Zero count:", zero)


#Q62
# name = input("Enter student name: ")

# marks = []

# for i in range(1, 6):
#     mark = float(input(f"Enter marks of Subject {i}: "))
#     marks.append(mark)

# marks_tuple = tuple(marks)

# total = sum(marks_tuple)
# average = total / len(marks_tuple)

# if average >= 90:
#     grade = "A"
# elif average >= 75:
#     grade = "B"
# elif average >= 50:
#     grade = "C"
# else:
#     grade = "Fail"

# student = {
#     "Name": name,
#     "Marks": marks_tuple,
#     "Total": total,
#     "Average": average,
#     "Grade": grade
# }

# print("\n----- Student Report -----")
# for key, value in student.items():
#     print(key, ":", value)



subjects = ("Maths", "Science", "English", "Computer", "Gujarati")

students = [
    {
        "name": "Riya",
        "marks": [85, 90, 88, 92, 80]
    },
    {
        "name": "krishna",
        "marks": [70, 75, 68, 72, 78]
    },
    {
        "name": "neha",
        "marks": [95, 98, 97, 96, 99]
    }
]
passed_students = set()

def calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    return sum(marks) / len(marks)

def check_result(avg):
    if avg >= 40:
        return "Pass"
    else:
        return "Fail"

def find_topper(students):
    topper_name = ""
    highest_avg = 0
    for student in students:
            avg = calculate_average(student["marks"])

            if avg > highest_avg:
                highest_avg = avg
                topper_name = student["name"]
    return topper_name

print("STUDENT REPORT")

for student in students:
    total = calculate_total(student["marks"])
    avg = calculate_average(student["marks"])
    result = check_result(avg)

    if result == "Pass":
        passed_students.add(student["name"])

    print("\nName:", student["name"])
    print("Marks:", student["marks"])
    print("Total:", total)
    print("Average:", round(avg, 2))
    print("Result:", result)

topper = find_topper(students)

print("\nSUMMARY")
print("Passed Students:", passed_students)
print("Topper:", topper)


# #PROJECT 2 
board = [" " for i in range(9)]

winning_conditions = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
)


played_positions = set()


def print_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("")
    print(board[3], "|", board[4], "|", board[5])
    print("")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(board, player):
    for condition in winning_conditions:
        a, b, c = condition

        if board[a] == board[b] == board[c] == player:
            return True

    return False



def check_draw(board):
    if " " not in board:
        return True
    return False



def switch_player(player):
    if player == "X":
        return "O"
    else:
        return "X"



current_player = "X"

print("TIC TAC TOE")
print("Positions:")
print("1 | 2 | 3")
print("4 | 5 | 6")
print("7 | 8 | 9")

for turn in range(9):

    print_board(board)

    move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1

    
    if move < 0 or move > 8:
        print("Invalid Position!")
        continue

    if move in played_positions:
        print("Position Already Taken!")
        continue

    
    board[move] = current_player
    played_positions.add(move)

    
    if check_winner(board, current_player):
        print_board(board)
        print(f"Player {current_player} Wins!")
        break

    
    if check_draw(board):
        print_board(board)
        print("Game Draw!")
        break

    
    current_player = switch_player(current_player)


print("Game Over")
