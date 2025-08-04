nums = [4, 5, 4, 2, 5]

answ = []
for num in nums:
    if num not in answ:
        answ.append(num)
    else:
        continue
print(answ)