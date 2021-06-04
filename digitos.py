# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------
     
'''
    Nome: Joao Victor Passos Goncalves
    NUSP: 12557716

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''

# escreva seu programa a seguir
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