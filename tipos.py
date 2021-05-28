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
s = input("Digite uma string s: ")
i = int(input("Digite um inteiro i: "))
x = float(input("Digite um float x: "))
print(f"s = '{s}' ({type(s)})")    #s = '10' (<class 'str'>)
print(f"i = {i} ({type(i)})")
print(f"x = {x} ({type(x)})")
print(f"s + s = '{s}' + '{s}' = '{s+s}' ({type(s+s)})")
print(f"i + i = {i} + {i} = {i+i} ({type(i+i)})")
print(f"x + x = {x} + {x} = {x+x} ({type(x+x)})")
print(f"i * s = {i} * '{s}' = '{i*s}' ({type(i*s)})")
print(f"i * i = {i} * {i} = {i*i} ({type(i*i)})")
print(f"i * x = {i} * {x} = {i*x} ({type(i*x)})")
print(f"x / i = {x} / {i} = {x/i} ({type(x/i)})")
print(f"i / i = {i} / {i} = {i/i} ({type(i/i)})")
print(f"i // i = {i} // {i} = {i//i} ({type(i//i)})")
print(f"i / 2 * 3 = {i} / 2 * 3 = {i/2*3} ({type(i/2*3)})")
print(f"i // 2 * 3 = {i} // 2 * 3 = {i//2*3} ({type(i//2*3)})")
print(f"i % 3 = {i} % 3 = {i%3} ({type(i%3)})")