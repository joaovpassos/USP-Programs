# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS OU ATRIBUTOS
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
#------------------------------------------------------------------
# MODULOS UTILIZADOS NO PROGRAMA

# para random.randrange() usada nas funções sorteie_casa_vazia() e sorteie_cidade()
# sorteie_casa_vazia() está totalmente feita e pode ser fonte de inspiração
# sorteie_cidade() está totalmente feita e pode ser fonte de inspiração
import random

# para mt.init_matriz() usada na função sorteie_cidade()
import matriz as mt

#------------------------------------------------------------------
# CONSTANTES
VAZIA    = ' ' # para casa vazia
AZUL     = 'a' # para casa habitada por azul
VERMELHO = 'v' # para casa habitada por vermelho

# valores para teste/debug
DEBUG     = False
SEMENTE   = 10  # para random.seed()
TAMANHO   = 6   # para a dimensão da cidade
PORCENT_A = 40  # porcentagem agentes azuis 
PORCENT_V = 40  # porcentagem agentes vermelhos
DESEJADO  = 3   # número de vizinhos que tornam um agente feliz

######################################################################
def main():
    # inicialização: teste seu programa inicialmente com 
    # DEBUG = True e depois com Debug = False para 
    # usar outros valores
    if DEBUG:
        semente = SEMENTE
        tamanho = TAMANHO
        porc_A  = PORCENT_A
        porc_V  = PORCENT_V
        min_viz_desejado = DESEJADO
    else:        
        print("Bem vindo ao simulador do modelo de segregação de Schelling\n")
        semente = int(input("Digite a semente para o gerador de números pseudo-aleatórios: "))
        tamanho = int(input("Digite o tamanho da matriz cidade: "))
        porc_A = int(input("Digite a porcentagem da população azul: "))
        porc_V = int(input("Digite a porcentagem da população vermelha: "))
        min_viz_desejado = int(input("Digite o número mínimo de vizinhos desejado: "))
    
    # inicialização do gerador de números pseudo-aleatórios    
    random.seed( semente )

    # configuração inicial das moradias na cidade
    mapa = sorteie_cidade( tamanho, porc_A, porc_V )
    print()
    print("Configuração Inicial")
    for lin in range(tamanho):
        print(f"linha {lin:3d} - {mapa[lin]}")

    # simulação do processo    
    fim = False
    iteracao = 0

    while not fim:
        muda_a, muda_v = ache_infelizes( mapa, min_viz_desejado )

        print()
        print(f"{len(muda_a):3d} moradores azuis querem mudar")
        print(f"{len(muda_v):3d} moradores vermelhos querem mudar")
        print(f"Origem dos azuis    : {muda_a}")
        print(f"Origem dos vermelhos: {muda_v}")

        origem = muda_a + muda_v
        destino = atualize_mapa(mapa, origem)

        for i in range(len(origem)):
            print(f"Morador em {origem[i]} se moveu para {destino[i]}")

        iteracao += 1
        print(f"\nEstado do mapa após {iteracao} iterações")
        for lin in range(tamanho):
            print(f"linha {lin:3d} - {mapa[lin]}")

        if len(muda_a) == 0 and len(muda_v) == 0:
            print("Todos os moradores estão felizes e ninguém quer se mudar!")
            fim = True
        else:        
            op = input("\nDigite fim para terminar, ou enter para mais uma iteração: ")
            if op == 'fim':
                fim = True

######################################################################

def conte_vizinhos(M, lin, col):
    ''' (matriz, int, int) -> int
    RECEBE uma matriz M que representa uma cidade e um par [lin, col] que 
           indica uma casa [lin][col] de M. 
    RETORNA o número de casas vizinhas da casa [lin][col] de M em que 
           habitam agentes iguais a M[lin][col].
    '''
    # modifique o código abaixo para conter a sua solução.
    vizinhos = 0
    if (lin-1) >=0 and (col-1) >= 0:
        if M[lin-1][col-1] == M[lin][col]:
            vizinhos += 1
    if (lin-1) >= 0:
        if M[lin-1][col] == M[lin][col]:
            vizinhos += 1
    if (col+1) < len(M) and (lin-1) >= 0:
        if M[lin-1][col+1] == M[lin][col]:
            vizinhos += 1
    if (col-1) >= 0:
        if M[lin][col-1] == M[lin][col]:
            vizinhos += 1
    if (col+1) < len(M):
        if M[lin][col+1] == M[lin][col]:
            vizinhos += 1
    if (lin+1) < len(M[0]) and (col-1) >= 0:
        if M[lin+1][col-1] == M[lin][col]:
            vizinhos += 1
    if (lin+1) < len(M[0]):
        if M[lin+1][col] == M[lin][col]:
            vizinhos += 1
    if (lin+1) < len(M[0]) and (col+1) < len(M):
        if M[lin+1][col+1] == M[lin][col]:
            vizinhos += 1
    return vizinhos

    
######################################################################

def ache_infelizes(M, minviz):
    ''' (matriz, int) -> lista de listas, lista de listas
    RECEBE uma matriz M que representa uma cidade e um inteiro minviz.
    RETORNA duas listas. Cada cada item destas listas é um par 
         [lin, col] que indica uma casa [lin][col] de M habitada por 
         um agente infeliz.
 
    A PRIMEIRA lista contém TODOS os pares [lin, col] tais que o agente que 
         habita a casa [lin][col] é AZUL e está INFELIZ.

    A SEGUNDA lista contém TODOS os pares [lin, col] tais que o agente que 
         habita a casa [lin][col] é VERMELHO e está INFELIZ.

    Um AGENTE está INFELIZ se o número de vizinhos iguais a ele é  
    menor que minviz. 
    '''
    # modifique o código abaixo para conter a sua solução.
    azuis = []
    vermelhos = []
    for i in range(len(M)):
        for j in range(len(M[i])):
            if conte_vizinhos(M,i,j) < minviz:
                if M[i][j] == 'a':
                    azuis += [[i, j]]
                elif M[i][j] == 'v':
                    vermelhos += [[i, j]]

    return azuis, vermelhos
    
######################################################################

def atualize_mapa(M, origem):
    ''' (matriz, list) -> lista de listas
    RECEBE uma matriz M que representa uma cidade e uma lista origem em 
        que cada item é um par [lin, col] que indica uma casa [lin][col]
        de M.
    MODIFICA a matriz M mudando, cada morador de uma casa  
        [lin][col] indicada por um par [lin, col] em origem, para uma 
        casa vazia escolhida de forma aleatória. Para essa escolha 
        aleatoria utilize a função sorteie_casa_vazia() que está totalmente 
        feita mais adiante. 

    Após cada mudança a casa origem fica desocupada/vazia.

    RETORNA uma lista em que cada item é um par [lin, col] que indica 
        uma casa [lin][col] de M. A lista destino deve ser tal que o 
        agente que habitava a casa origem[i] mudou-se para a casa 
        destino[i].

    Estude o enunciado e os exemplos fornecidos no enunciado.
    A função sortei_casa_vazia também pode ser fonte de inspiração.
    '''
    # modifique o código abaixo para conter a sua solução.
    new_positions = []
    for i in origem:
        x = sorteie_casa_vazia(M)
        M[x[0]][x[1]] = M[i[0]][i[1]]
        M[i[0]][i[1]] = VAZIA
        new_positions += [[x[0],x[1]]]
    return new_positions
    
######################################################################
######################################################################
##
##  Utilidades para você usar caso desejar
##
######################################################################

def sorteie_cidade(nlins, pa, pv):
    ''' (int, int, int) -> matriz
    RECEBE inteiros nlins, pa e pv.
    RETORNA uma matriz M que representa uma cidade de dimensão 
        nlins x nlins em que o número (provavelmente) de 

       - moradores azuis é (pa/100)*nlins*nlins, 
       - moradores vermelhos é (pv/100)*nlins*nlins, e
       - casa desabitadas é (1-(pa+pv)/100)*nlins*nlins
    '''
    ncols = nlins # matriz é quadrada
    # 1 inicialmente todas as casas estão desabitadas = VAZIA
    M = mt.init_matriz(nlins, ncols, VAZIA)

    # 2 pecorra a cidade povoando cada  casa com um agente azul ou
    #   um agente vermelho ou deixando desabitada
    for lin in range(nlins):
        for col in range(ncols):
            # faça um sorteio para decidir se a casa [lin][col]
            # será habitada por um agente azul, ou por um agente vermelho
            # ou ficará desabitada
            sorteio = random.randrange(100)
            if  sorteio < pa:     # sorteio em {0,1,...,pa-1}
                M[lin][col] = AZUL
            elif sorteio < pa+pv: # sorteio em {pa,pa+1,...,pa+pv-1}
                M[lin][col] = VERMELHO

    return M

######################################################################

def sorteie_casa_vazia( M ):
    ''' (matriz) -> [int, int]
    RECEBE uma matriz M que representa uma cidade.
    RETORNA um par [lin, col] que indica uma casa vazia [lin][col] 
        de M escohida aleatoriamente.
    '''
    # 1 pegue a dimensão da cidade
    nlins = len(M)
    ncols = nlins # = len(M[0]), nlins == ncols
    
    # 2 crie um lista para armazenar os pares [lin, col] que indicam as
    #   casas [lin][col] de M que estão desabitadas
    casaVazia = []
    
    # 3 pecorra a cidade a procura de casas desabitadas
    for lin in range(nlins):
        for col in range(ncols):
            # a casa esta desabitada, vazia?
            if M[lin][col] == VAZIA:
                # insira o para [lin, col] na nossa lista 
                casaVazia += [ [lin, col] ]
                
    # 4 sorteie uma das casas desabitadas aleatoriamente            
    sorteada = random.randrange( len(casaVazia) )
    
    # retorne a casa sorteda.
    return casaVazia[sorteada]

######################################################################

if __name__ == "__main__":
    main()
