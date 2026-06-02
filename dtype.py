# practice
# p1 = ['riya','sonal','krishna','prachi']
# p1.append("juhi")
# print(p1)

# p1.pop()
# print(p1)

# # p1.clear()
# # print(p1)

# p1.sort()
# print(p1)

# p1.reverse()
# print(p1)

# p1.insert(2,'tithi')
# print(p1)

# p2 = p1.count('prachi')
# print(p2)

# p2 = p1.index("tithi")
# print(p2)

# print(len(p1))


# a1 = ['15','18','7','11','27','12','6']
# a1.append(21)
# print(a1)

# r1 = ['11','12','13','14']
# r1.pop()
# print(r1)

# k1 = ['apple','banana','grapes']
# k1.clear()
# print(k1)

# s1 = ['rose','lily','sunflower','tulip']
# s1.sort()
# print(s1)

# b1 = ['15','80','25','67']
# b1.reverse()
# print(b1)

# c1 = ['7','18','45','50','48']
# c1.insert(1,'27')
# print(c1)

# d1 = ['2','4','6','8','10']
# d2 = d1.index('6')
# print(d2)

# e1 = ['55','67','70','55','45','55','60']
# e2 = e1.count('55')
# print(e2)

# f1 = ['kabrawala','shah','desai','patel']
# print(len(f1))



# g1 = ('7','14','21','18','45','60','14')
# g2 = g1.count('14')
# print(g2)

# s1 = ('prachi','tithi','shakshi','nishra')
# s2 = s1.index('nishra')
# print(s2)


# q1list = ['5','10',',15']
# q1tuple = tuple[q1list]
# print(q1tuple)

# q1list = ['riya','nishra','dhriti']
# q1tuple = tuple(q1list)
# print(q1tuple)


# list tasks
# color = ['white','pink','blue','yellow','green','brown']

# color.append('black')
# print(color)

# color.remove('yellow')
# print(color)

# print(len(color))

# color = ['white','blue','pink','orange','blue']
# print("first element:",color[0])
# print("last element:",color[4])

# color = ['white','blue','pink','orange','blue']
# color[2] = 5
# print(color)

# color2 = ['white','blue','pink','orange',]
# color2.sort()
# print(color2)

# color = ['white','blue','pink','orange','blue']
# color1 = color.count('blue')
# print(color1)

# numbers = [10, 25, 8, 67, 87]
# maximum = max(numbers)
# print("Maximum number is:", maximum)

# # color.reverse()
# # print(color)


# tuple tasks
# fruit = ('apple','orange','pineapple','kiwi','cherry','apple')

# fruit = ('apple','orange','pineapple','kiwi','cherry','apple')
# print("first element:",fruit[0])
# print("last element:",fruit[5])

# print(len(fruit))



# fruit = list[fruit]
# print(fruit)

# color = tuple(color)
# print(color)

# w = ('apple','kiwi','orange','mango','cherry','grapes','mango')
# w1 = w.count('mango')
# print(w1)

# tuple1 = (5, 7, 9)
# tuple2 = (15, 18)
# sum = tuple1 + tuple2
# print(sum)


# w = ('apple','kiwi','orange','mango','cherry','grapes','mango')
# print(w[-1])
# print(w)


# set task

# numbers = {'15','18','23','45','50','67'}
# numbers.add("77")
# print(numbers)

# numbers = {'5','95','15','45','80','30'}
# numbers.remove("45")
# print(numbers)

# set = {20, 40, 60, 80,100}
# if 20 in set:
    # print("value exists")
# else:
    # print("not found")

# set1 = {10, 20, 30}
# set2 = {30, 40, 50}
# result = set1.union(set2)
# print(result)

# set = {'riya','prachi','krishna'}
# list = list[set]
# print(list)

# set = {'kabrawala','shah','pate','singh'}
# set.clear()
# print(set)

# a = {'5','10','15','20','45'}
# b = {'15','20','25'}
# diff = (a-b)
# print(diff)

# a = {'16','24','45'}
# b = {'64','75',94,'45'}
# result = (a&b)
# print(result)

# set = {10, 100, 50}
# set.update([20, 60, 90])
# print(set)


# dictionary task
# a1 = {
    # 'name' : 'krishna',
    # 'city': 'pune',
    # 'age': 20
# }
# print(a1)

# a1.update({'name1': 'riya'})
# print(a1)

# q1 = {
    # 'name' : 'sonal',
    # 'city' : 'mumbai' 
# }
# q1.pop('city')
# print(q1)

# k1 = {
    # 'name' : 'riya',
    # 'city' : 'pune',
    # 'color' : 'white',
    # 'flower' : 'sunflower'
# }
# print(k1.keys())
# print(k1.values())

# r1 = {
#     "name" : "riya",
#     "marks" : 82,
#     "course": "maths"
# }
# r1["marks"] = 75
# print(r1)

# student = {
#     "name": "riya",
#     "city" : "pune",
#     "age" : 20
# }
# if "city" in student:
#     print("key exists")
# else:
#     print("not found")
    
# student = {
#     "name": "riya",
#     "city" : "pune",
#     "age" : 20
# }
# print(len(student))

# student = {
#     "name": "riya",
#     "city" : "pune",
#     "age" : 20
# }
# print(student.keys())

# dict1 = {
#      "a" : 10,
#      "b" : 20
# }
# dict2 = {
#     "c" : 30,
#     "d" : 40
# }
# merged_dict = dict1 | dict2
# print(merged_dict)



# task3
tuple = (10, 20, 30, 20, 40)
list_data = list(tuple)

set_data = set(list_data)

final_list = list(list_data)

print("tuple:",tuple)
print("list:",list_data)
print("set:",set_data)
print("Final list:",final_list)

# task2
list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined_list = (list1+list2)

combined_tuple = tuple(combined_list)

combined_set = set(combined_tuple)

data = {
    "list" : combined_list,
    "tuple" : combined_tuple,
    "set" : combined_set
}
print("combined list:",combined_list)
print("Tuple:", combined_tuple)
print("set:", combined_set)
print("Dictionary:", data)


# task1
student1 = "riya"
student2 = "krishna"
student3 = "prachi"

marks = (44, 45, 42)

subjects = {"maths", "science", "english"}

data = {
    "students" : [student1, student2, student3],
    "marks" : marks,
    "subjects" : subjects
}

second_student = data["students"][1]
first_marks = data["marks"][0]
one_subject = data["subjects"]

print("second student:", second_student)
print("first mark:", first_marks)
print("one subject:", one_subject)
