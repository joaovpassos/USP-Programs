x = float(input("Digite x: "))
y = float(input("Digite y: "))

if 0 <= x <= 8 and 0 <= y <= 8:
    if (0 <= x < 1 or 7 < x <= 8) and (0 <= y < 2): #pescoço
        print("branco")
    elif 3.5 <= x <= 4.5 and 3.5 <= y <= 4.5: #nariz
        print("branco")
    elif (1 <= x <= 3 or 5 <= x <= 7) and (7.25 <= y <= 7.75): #sobrancelha
        print("branco")
    elif (((x-2)**2 + (y-6)**2 <= 1**2) and not ((x-2)**2 + (y-6)**2 <= 0.5**2)): #olho esquerdo
        print("branco")
    elif (((x-6)**2 + (y-6)**2 <= 1**2) and not ((x-6)**2 + (y-6)**2 <= 0.5**2)): #olho direito
        print("branco")
    elif 3 < x < 5 and 1.5 < y < 2.5: #boca
        print("branco")
    elif ((x-3)**2 + (y-2)**2 < 0.5**2): #boca esquerda
        print("branco")
    elif ((x-5)**2 + (y-2)**2 < 0.5**2): #boca direita
        print("branco")
    else:
        print("azul")
else:
    print("branco")
