# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
# ------------------------------------------------------------------

"""
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

"""

#----------------------------------------------------    
def primo(n):
    '''(int) -> bool

       RECEBE um número inteiro n.
       RETORNA True se n é primo e False em caso contrário.
    '''
    # remova o print() e escreva suas função a seguir 
    primo = True
    if n <= 1:
        primo = False
        return False
    count = 2
    while count <= n/2 and primo:
        if n % count == 0:
            primo = False
        count += 1
    return primo
      

#----------------------------------------------------        
def goldbach(n):
    '''(int) -> bool, int, int 

       RECEBE um número inteiro n.
       RETORNA True, p, q se n é soma de dois números primos p e q.
       Se n não é soma de dois números primos a função retorna False, 1, 1.
    '''
    # remova o print() e escreva suas função a seguir 
    var = False
    p = 2
    while p <= n/2:
        if primo(p):
            q = n - p
            if primo(q):
                var = True
                x = p
                y = q
        p += 1

    if var == True:
        return True, x, y
    else:
        return False, 1, 1
          

#----------------------------------------------------    
def exponencial(n0, e, p, d):
    '''(int, int, float, int) -> int 

       RECEBE 

         * o número n0 de indivíduos infectados em um dia 0;
         * o número diário médio e de indivíduos com quem alguém 
           infectado é exposto;
         * a probabilidade p de uma exposição resultar em uma infecção;
         * um inteiro d,  d >=  0. 

      RETORNA o número total de indivíduos infectados até o dia d 
      determinado por (n0, e, p).
    '''
    # remova o print() e escreva suas função a seguir 
    total = int((1 + e * p)**d * n0)
    return total
    
#--------------------------------------------------
def logistica(n0, e, p, n, d):
    '''(int, int, float, int, int) -> int
 
       RECEBE 

         * o número n0 de indivíduos infectados em um dia 0;
         * o número diário médio e de indivíduos com quem alguém 
           infectado é exposto;
         * a probabilidade p de uma exposição resultar em uma infecção;
         * o número n de indivíduos na população; e
         * um inteiro d, d >= 0. 

       RETORNA o número total de indivíduos infectados até o dia d 
       determinado por (n0, e, p, n).

    '''
    # remova o print() e escreva suas função a seguir 
    i = 0
    x = n0
    while i < d:
      n1 = (1 + e * p * (1 - (x/n))) * x
      x = n1
      i += 1
    return int(x)
