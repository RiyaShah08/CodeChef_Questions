n = int(input())
for c in range(n):
    a, b = map(int, input().split())
    c = a % b
    print(c)