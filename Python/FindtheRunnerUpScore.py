if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    maxv = max(arr)
    l = list(filter(lambda x: x != maxv,arr))
    print(max(l))
