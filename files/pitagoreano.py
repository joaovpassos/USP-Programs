# Escreva seu programa a seguir
num = int(input('Digite n: ')) #12

a = 1
lista =[]
while a < num/3: #10
    b = a + 1
    while b < num/2:
        c = b + 1
        while c < num/2:
            if a*a + b*b == c*c and a + b + c == num:
                lista.append(a)
                lista.append(b)
                lista.append(c)
            c += 1
        b += 1
    a += 1

if len(lista) == 0:
        print(f'{num} não é pitagoreano')   
else:
    print(f'{num} é pitagoreano ({lista[-3]},{lista[-2]},{lista[-1]})')
