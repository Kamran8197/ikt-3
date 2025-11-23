# 1.
for _ in range(4):
    print('* ' * 4)

#2

# 3. 3x5 düzbucaqlı
rows, cols = 3, 5
for _ in range(rows):
    print('* ' * cols)

#4

# 5. İstifadəçinin ədədinin vurma cədvəli (1-10)
n = int(input("Ədəd daxil et: "))
for i in range(1, 11):
    print(f"{n} x {i:2} = {n*i}")


#9 

rows = int(input("Sətir sayı: "))
cols = int(input("Sütun sayı: "))
for _ in range(rows):
    print('# ' * cols)

#11

rows = 5
for i in range(1, rows+1):
    print(' ' * (rows - i) + '* ' * i)
