num = int(input())
student_list = []


def setting(data):
    return data[1]


for i in range(num):
    name, score = input().split()
    print(name)
    print(score)
    student_list.append((name, int(score)))

# student_list.sort(key=setting)
student_list.sort(key=lambda student: student[1])

for student in student_list:
    print(student[0], end=' ')
