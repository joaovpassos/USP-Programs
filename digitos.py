number = int(input("Digite n: ")) #EXEMPLO: 125
soma = 0
x = 0
n = number
while n > 0: #TAMANHO DO NÚMERO
    n //= 10
    x += 1
#dV1
tamanho = x
n = number
while n > 0:
    digit = n % 10
    mult = digit * tamanho
    soma += mult
    tamanho -= 1
    n //= 10
dv1 = soma % 11
if dv1 == 10:
    dv1 = 0
#dV2
tamanho = x - 1
soma2 = 0
n = number 
while n > 0:
    digit2 = n % 10
    mult2 = digit2 * tamanho
    soma2 += mult2
    tamanho -= 1
    n //= 10
dv2 = (soma2 + (dv1*x)) % 11
if dv2 == 10:
    dv2 = 0
print(f'DVs = {dv1} {dv2}')
