class student:
    def __init__(self, number, height, weight):
        self.height = height
        self.weight = weight
        self.number = number


student_list = []
num = int(input())
for i in range(num):
    h, w = map(int, input().split())
    student_list.append(student(i+1, h, w))

student_list.sort(key=lambda x: (-x.height, -x.weight, x.number))

for i in range(num):
    print(student_list[i].height,
          student_list[i].weight, student_list[i].number)
