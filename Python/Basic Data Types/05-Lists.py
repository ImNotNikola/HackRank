if __name__ == '__main__':
    N = int(input())
    L = []

    for n in range(N):
        x = input().split(" ")
        cmd = x[0]
        if cmd == "insert":
            L.insert(int(x[1]), int(x[2]))
        elif cmd == "print":
            print(L)
        elif cmd == "append":
            L.append(int(x[1]))
        elif cmd == "pop":
            L.pop()
        elif cmd == "reverse":
            L = L[::-1]
        elif cmd == "sort":
            L = sorted(L)
        elif cmd == "remove":
            L.remove(int(x[1]))
