#1
subjects = ["physics", "calculus", "poetry", "history"]

#2
grades = [98, 97, 85, 88]

#3
gradebook = [
    ["physics", 98],
    ["calculus", 97],
    ["poetry", 85],
    ["history", 88]
]

#4
print(gradebook)

#5
gradebook.append(["computer science", 100])

#6
gradebook.append(["visual arts", 93])

#7
gradebook[-1][1] += 5

#8
gradebook[2].remove(85)
gradebook[2].append("Pass")

#9
print(gradebook)

#10
last_semester_gradebook = [
    ["politics", 80],
    ["latin", 96],
    ["dance", 97],
    ["architecture", 65]
]
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
