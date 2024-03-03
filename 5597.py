import sys

student = list(range(1, 31))
for i in range(28):
    student.remove(int(sys.stdin.readline().strip()))
print(student[0])
print(student[1])