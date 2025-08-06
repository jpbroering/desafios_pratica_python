a,b,c = [int(num) for num in input().split()]

maior_ab = (a+b+abs(a-b))/2

maior_ab = (maior_ab+c+abs(maior_ab-c))/2

print(f"{int(maior_ab)} eh o maior")