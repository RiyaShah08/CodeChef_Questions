no = 0
n, k = map(int, input().split())
for i in range(n):
	x = int(input())
	if x % k == 0:
		no += 1
print(no)