# -*- coding: utf-8 -*-
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
