n = int(input())
arr = list(map(int, input().split()))
for i in range(len(arr)):
  if i % 2 == 0:
      print(arr[i])


n = int(input())
arr = list(map(int, input().split()))
for i in arr:
  if i % 2 == 0:
      print(i)


n = int(input())
arr = list(map(int, input().split()))
pos = 0
for i in arr:
  if i > 0:
      pos += 1
print(pos)


n = int(input())
arr = list(map(int, input().split()))
res = 0
for i in range(1, len(arr)):
  if arr[i - 1] < arr[i]:
      res += 1
print(res)


n = int(input())
arr = list(map(int, input().split()))
res = False
for i in range(1, len(arr)):
  if arr[i - 1] > 0 and arr[i] > 0 or arr[i - 1] < 0 and arr[i] < 0:
      res = True
      break
print("YES" if res else "NO")


n = int(input())
arr = list(map(int, input().split()))
res = 0
for i in range(1, len(arr) - 1):
  if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
      res += 1
print(res)


n = int(input())
arr = list(map(int, input().split()))
for i in range(len(arr) - 1, -1, -1):
  print(arr[i])