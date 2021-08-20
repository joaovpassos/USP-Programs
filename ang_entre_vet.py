from math import acos, pi

#PERGUNTAR AS COORDENADAS DO VETOR U

valido = False
while valido == False:
    i = 0
    u = input('Digite as coordenadas do vetor 1: ')
    for caracter in u:
        if (caracter != ',') and (not caracter.isnumeric()) and (caracter != '-') and (caracter != '.'):
            i += 1
    if i == 0:
        valido = True

#PERGUNTAR AS COORDENADAS DO VETOR V

valido = False
while valido == False:
    i = 0
    v = input('Digite as coordenadas do vetor 2: ')
    for caracter in v:
        if (caracter != ',') and (not caracter.isnumeric()) and (caracter != '-') and (caracter != '.'):
            i += 1
    if i == 0:
        valido = True

lista_u = []
lista_v = []

#INSERIR AS COORDENADAS NAS LISTAS

for coord in u.split(','):
    lista_u.append(float(coord))
for coord in v.split(','):
    lista_v.append(float(coord))

#CÁLCULO DO PRODUTO ESCALAR

prod_escalar = 0
i = 0
while i < len(lista_u):
    mult = (lista_u[i] * lista_v[i])
    i +=1
    prod_escalar += mult

#CÁLCULO DAS NORMAS DOS VETORES

soma_quad = 0
for coord in lista_u:
    soma_quad += coord**2
nu = soma_quad**(1/2)

soma_quad = 0
for coord in lista_v:
    soma_quad += coord**2
nv = soma_quad**(1/2)

#CÁLCULO DO ÂNGULO ENTRE OS VETORES

cos = prod_escalar/(nu*nv)
cos_print = round(prod_escalar/(nu*nv),2)
graus = acos(cos) * 180 / pi

#VERIFICAR SE OS VETORES SÃO LI OU LD

if graus == 0 or graus == 180:
    li_ld = "L.D."
else:
    li_ld = "L.I."

#PRODUTO VETORIAL

if len(lista_u) == 3 and len(lista_v) == 3:
    coord_prod_vet = [
        lista_u[1] * lista_v[2] - lista_u[2] * lista_v[1],
        -(lista_u[0] * lista_v[2] - lista_u[2] * lista_v[0]),
        lista_u[0] * lista_v[1] - lista_u[1] * lista_v[0]
    ]
else:
    coord_prod_vet = "Não existe"

#MÓDULO DA SOMA DOS VETORES

resultante = (nu**(2) + nv**(2) + 2*nu*nv*cos)**(1/2)

#COORDENADAS DA SOMA DOS VETORES

i = 0
lista_coord_res = []
while i < len(lista_u):
    lista_coord_res.append(lista_u[i] + lista_v[i])
    i += 1

#PRINTS

print(f'\nO cosseno do ângulo entre os vetores é: {cos_print}')
print(f'A norma do primeiro vetor é: {nu:.2f}')
print(f'A norma do segundo vetor é: {nv:.2f}')
print(f'O módulo da soma dos vetores é: {resultante:.2f}')
print(f'As coordenadas do vetor resultante é: {lista_coord_res}')
print(f'O produto escalar entre os vetores é: {prod_escalar}')
print(f'A medida do ângulo entre os vetores é: {graus:.2f}º')
print(f'O conjunto dos vetores é {li_ld}')
print(f'Produto vetorial entre os dois vetores: {coord_prod_vet}\n')