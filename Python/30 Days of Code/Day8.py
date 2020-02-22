n = int(input())
d = dict()

for i in range(0,n):
    name, number = input().split()
    d[name] = number

for j in range(0,n):
    name = input()
    if name in d:
        print("{}={}".format(name, d[name]))
    else:
        print("Not found")
