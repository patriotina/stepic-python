i = 0

def midMark(stud):
    s = stud.strip().split(';')
    md = (int(s[1]) + int(s[2]) + int(s[3])) / 3
    marks[0] = marks[0] + int(s[1])
    marks[1] = marks[1] + int(s[2])
    marks[2] = marks[2] + int(s[3])

    print(md)

marks = [0, 0, 0]
with open('students.txt') as f:
    for line in f:
        midMark(line)
        i += 1

print(marks[0]/i, marks[1]/i, marks[2]/i)