nums = [0, -1, 4, -3, 2, 0, 5]
N = 3
cont = 0

answ = 0
for num in nums:
    if num > 0 and cont < N:
        answ += num
        cont += 1
print(answ)