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
# MODULOS A SEREM UTILIZADOS NO PROGRAMA
import random # para random.choice(lista) na função gere_frase()

#------------------------------------------------------------------
# CONSTANTES

# ponto final, ponto de interrogação, ponto de exclamação
# não consideraremos reticências "..."
PONTUACAO_FINAL = ".?!"

# vírgula, ponto e vírgula, dois pontos, fecha parênteses
# não devem ser precedidos de espaço na frase gerada
PONTUACAO_SEM_ESPACO = ',;:)' + PONTUACAO_FINAL

# travesão, aspas, abre chaves
# devem ser precedidos de espaço na frase gerada
PONTUACAO_COM_ESPACO = '—"('

# todas juntas (reticências foram desconsideradas)
PONTUACAO = PONTUACAO_SEM_ESPACO + PONTUACAO_COM_ESPACO

# usado na função insira espacos
ESPACO = ' '

# semente para o gerador aleatório com o objetivo de reprodutibilidade
SEED = 1234

#------------------------------------------------------------------
#
def main():
    '''(None) -> None

    Para testar as funções juntas. Esta função não será avaliada, entretanto
    ela __não__ deve gerar erro de execução ou sintático. 
    Modifique-a se desejar.
    '''
    # Para efeitos de reprodutibilidade
    random.seed(SEED)

    print('ESCREVENDO "como" MACHADO DE ASSIS!\n')
    print(gere_frase('Quincas', {'.': ['Rubião'], 'Rubião': ['achou'], 'achou': ['um'], 'um': ['rival', 'cão', 'bonito'], 'rival': ['no'], 'no': ['coração'], 'coração': ['de'], 'de': ['Quincas', 'chumbo', 'preto'], 'Quincas': ['Borba'], 'Borba': ['—'], '—': ['um'], 'cão': [',', ','], ',': ['um', 'meio', 'pêlo', 'malhado'], 'bonito': ['cão'], 'meio': ['tamanho'], 'tamanho': [','], 'pêlo': ['cor'], 'cor': ['de'], 'chumbo': [','], 'malhado': ['de'], 'preto': ['.']}))
    # 1 leia nome do arquivo 
    nome = input("Digite o nome do arquivo com o texto: ")

    # 2 leia o corpus
    try:
        with open(nome, "r", encoding="utf-8") as arq:
            texto = arq.read()
    except:
        print(f"main(): Erro na leitura do arquivo '{nome}'")
        return None
    
    # 3 insira espaços antes de pontuações
    texto = insira_espacos(texto)

    # 4 obtenha lista com itens léxicos
    lst_itens = texto.split()
    
    # 5 construa dicionario de sucessores
    dicio = dicio_sucessores(lst_itens)

    # 6 quantidade de frases que devem ser geradas
    n = int(input("Digite o numero de frases que devem ser geradas: "))

    # 7 gere as frase
    for i in range(n):
        # gere i-ésima frase
        print("---")

        # 7.1 pegue palavra inicial da frase a ser gerada
        palavra_inicial = input(f"Digite a palavra inicial da frase {i+1}: ")

        # 7.2 gere uma frase começando com palavra_inicial 
        frase = gere_frase(palavra_inicial, dicio)
        print("Frase gerada:", frase)

    print("\nFIM")

#------------------------------------------------------------------
def insira_espacos(txt):
    '''(str) -> str

    RECEBE uma string `txt`.
    RETORNA a string resultante da inserção de um ESPACO antes e depois de 
    __cada sinal__ em PONTUACAO que estiver em texto.
    '''
    'sorriem, de gestos'
    # modifique o código abaixo para conter a sua solução.
    texto = []
    for i in range(len(txt)):
        if txt[i] in PONTUACAO:
            texto.append(ESPACO)
            texto.append(txt[i])
            texto.append(ESPACO)
        else:
            texto.append(txt[i])
    
    formatado = "".join(texto)
    return formatado
    
#------------------------------------------------------------------
def dicio_sucessores(lst):
    '''(list) -> dict

    RECEBE uma lista `lst`.
    RETORNA um dicionário em que 

        - as __chaves__ são os itens que ocorrem em lst e 
        - o  __valor__ associado a cada chave é a lista dos 
          itens que ocorrem imediatamente após a chave na lista lst.

    Por convenção a lista correspondente ao valor do último item 
    na lst (=lst[-1]) contém o primeiro item da lista (=lst[0]).

    Se a `lst` é a lista vazia a função deve retornar o dicionário vazio.
    '''
    # modifique o código abaixo para conter a sua solução.
    dicio = {}
    j = 0
    for i in lst:
        if i in dicio.keys():
            if j < len(lst) - 1:    
                dicio[i] += [lst[j+1]]
            elif j == len(lst) - 1:
                dicio[i] += [lst[0]]
        else:
            if j < len(lst) - 1:    
                dicio[i] = [lst[j+1]]
            elif j == len(lst) - 1:
                dicio[i] = [lst[0]]
        j += 1
    return dicio

#------------------------------------------------------------------
def gere_frase(p_inicial, dicio):
    '''(str, dict) -> str

    RECEBE uma palavra `p_inicial` e um dicionário `dicio`.

    O dicionário foi criado a partir de um texto com uma ou 
    mais frase; como nos textos de Machado de Assis.

    Cada chave do dicionário é um item (str). O valor no dicionário 
    correspondente a uma chave é uma lista (list) de itens (str). 

    RETORNA uma string representando uma frase.

    A frase retornada deve começar com a string p_inicial e ser gerada 
    segundo o __processo aleatório__ descrito no enunciado.
    
    Os itens na frase devem ser precedidos de um ESPACO, exceto:

        - a palavra inicial e
        - e os sinais de pontuação na string PONTUACAO_SEM_ESPACO.

    Se p_inicial não está no dicionário a função deve retornar a string vazia.
    '''
    # modifique o código abaixo para conter a sua solução.
    i = " "
    cont = 0
    frase = [p_inicial, " "]
    if p_inicial not in dicio:
        return ""
    else:
        while i not in PONTUACAO_FINAL:
            palavra = random.choice(dicio[frase[cont]])
            frase.append(palavra)
            frase.append(" ")
            cont += 2
            if palavra in PONTUACAO_SEM_ESPACO:
                frase[cont-1] = ""
            i = frase[cont]
        oficial = "".join(frase)
        return oficial

#######################################################
###                 FIM                             ###
#######################################################
#
# Não modifique as linhas abaixo
#
# Esse if serve para rodar a main() dentro do Spyder
# e não atrapalhar o corretor automático
# COMENTE as linhas a seguir durante os testes das suas
# funções no Python Shell

if __name__ == '__main__':
    main()