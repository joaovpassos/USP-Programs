
# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
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
#####################################################################
# MÓDULOS A SEREM UTILIZADOS NO PROGRAMA
# random.shuffle(lst) embaralha os elementos da lista lst.
import random 

#####################################################################
def main():
    '''
    Essa função auxilia no teste das funções pedidas para o EP08.
    Se desejar, escreva mais testes.

    Atenção: a tabulação das linhas foi removida e deve ser consertada 
    antes que a função possa ser utilizada.
    '''
    print("INÍCIO DOS TESTES")

    # testes da função circular()
    print("Função circular()")
    amigos1 = [1,2,3,4,0]
    amigos2 = [1,2,0,4,3]
    print(f"circular({amigos1}) = {circular(amigos1)}")
    print(f"circular({amigos2}) = {circular(amigos2)}")

    # testes da função experimento()
    print("Função experimento()")
    semente = int(input("Digite o valor da semente do gerador de números pseudo-aleatórios: "))
    random.seed(semente)
    MINN  = int(input("Qual o número mínimo de pessoas: "))
    MAXN  = int(input("Qual o número máximo de pessoas: "))
    passo = int(input("Qual o passo: "))
    T     = int(input("Qual o número de tentativas em cada experimento: "))
    SHOW  = input("Você quer ver as listas que são circulares [s/n]: ")

    debug = False
    if SHOW == 'S' or SHOW == 's':
        debug = True

    N = MINN
    while N <= MAXN:
        pN = experimento(N, T, debug)
        print(f"p({N}) = {pN}")
        N = N + passo

    print("TESTES ENCERRADOS")    

    ###################################################################
def sorteie_amigos( N ):
    ''' (int) -> list
    RECEBE um inteiro N > 0.
    RETORNA uma lista de tamanho N, contendo os números de 0 a N em 
        ordem aleatória.

    ATENÇÃO: a tabulação das linhas foi removida e a ordem de algumas 
    linhas alterada. Ela deve ser consertada antes possa ser utilizada.
    '''
    i = 0
    amigos = []
    while i < N:
        amigos += [i]
        i += 1
    random.shuffle(amigos)
    return amigos    

######################################################################
def circular(amigo_de):
    ''' (list) -> bool 
    RECEBE uma lista amigo_de (de "amigos secretos")
    RETORNA True se a lista for circular e False em caso contrário.
    '''
    # modifique o código abaixo para conter a sua solução.
    ver = []
    x = 0
    for i in range(len(amigo_de)):
        y = amigo_de[x]
        x = y
        ver += [y]

    if x == 0 and ver.count(0) == 1:
        return True
    else:
        return False

###################################################################
def experimento(N, T, debug=False):
    ''' (int, int) -> float
    RECEBE um inteiro N > 0, um inteiro T > 0 e um booleano debug.
    RETORNA a probabilidade de uma lista de "amigo secretos" com
        N participantes ser circular.

    Esta probabilidade deve ser calculada a partir de T sorteios 
    de listas de tamanho N, e calculando a frequência das listas 
    circulares.

    Se a opção debug é True a função deve imprimir todas as 
    listas sortedas que forem circulares, como mostrado no
    enunciado.
    '''
    # modifique o código abaixo para conter a sua solução.
    s = 0
    for _ in range(T):
        p = sorteie_amigos(N)
        if circular(p):
            if debug:
                print(f'{s+1} : {p}')
            s += 1
    prob = s/T
    return prob

#=====================================================================
# Não modifique as linhas abaixo
# Esse if serve para executar a main() dentro do Spyder
# e não atrapalhar o avaliador
if __name__ == '__main__':
    main()
