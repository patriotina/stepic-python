i = True
sum = 0
sqs = 0
while i:
    s = int(input())
    sum += s
    sqs += s*s
    if sum == 0:
        print(sqs)
        break
