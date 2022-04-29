#Autor: Eduardo Bouhid Neto
#Data: 23/5/21

#Bibliotecas
import turtle

#Decl.Globais

# 1. Recebe um valor em metros e retorna uma tupla
# na forma (decímetros, centímetros, milímetros)
def tuplaDCM(Lmetros):
    dm = Lmetros*10
    cm = Lmetros*100
    mm = Lmetros*1000

    return (dm,cm,mm)
 # 2. Recebe por parâmetro um inteiro representando
 # um ano, retorna um valor booleano que indica se
 #esse ano é bissexto ou não
def isBissexto(ano):
    if ano % 400 == 0:
        return True
    elif ano % 4 == 0 and ano % 100 != 0:
            return True
    
    return False

# 3. Lê um número de lados e um tamanho de lado,
# e plota um polígono regular com essas características
# na tela.
def polRegular(tartaruga, nlados, dimLado):
    

    tela = turtle.Screen()
    for i in range(nlados):
        tartaruga.forward(dimLado)
        tartaruga.left(360/nlados)

# 4. Lê uma lista de cores e um tamanho de lado,
# e desenha um polígono com um lado de cada cor
# da lista (len(lista) = nLados)
def polRegularColorido(tartaruga, dimLado, listaCor):
    #Lendo as cores
    
    #Inicializando parâmetros turtle
    tela = turtle.Screen()

    #Plotando a figura
    for i in range(len(listaCor) - 1):
        tartaruga.color(listaCor[i])
        tartaruga.forward(dimLado)
        tartaruga.left(360/(len(listaCor) - 1))

# 5. Conta a quantidade de numerais em uma string
# passada como parâmetro
def contaNums(texto):
    nums = 0
    for char in texto:
        if char.isnumeric():
            nums += 1

    return nums

# 6. Verifica se uma lista (seq_gene) está contida em
# outra (seq_ref). Ambas listas são parâmetros.
def isContido(seq_gene, seq_ref):
    for i in range(0, len(seq_ref)): #Elementos de seq_ref, pra comparar
        iguaisConsecutivos = 0
        for j in range(0, len(seq_gene)): #Varrendo os elementos de seq_gene, pra comparar
            if i+j < len(seq_ref):
                if seq_gene[j] == seq_ref[i+j]:
                    iguaisConsecutivos += 1
        if iguaisConsecutivos == len(seq_gene):
            return True
    
    return False

# 7. Imprime na tela um "y", cuja altura é parâmetro da função
def ipsilon(height):
    espacosMeio = height - 1
    espacosEsquerda = 0
    limiteV = height//2 if height%2 == 0 else (height//2) + 1
    #Primeira parte, que parece um 'v'
    for i in range(limiteV):
        if i != limiteV - 1:
            print(espacosEsquerda*' '+ '*' + espacosMeio*' ' + '*')
        else:
            print((height//2)*' ' + '*')
        espacosEsquerda += 1
        espacosMeio -= 2 #Precisamos compensar o espaço adicional à esquerda

    #Segunda parte, que parece uma '/'
    espacos = height//2 - 1 #
    for i in range(height-(height//2)-1):
        print(' '*espacos + '*')
        espacos -= 1

# 8. Recebe uma matriz e retorna se ela é simétrica ou não
def isSimetrica(matriz):
    #Criando a matriz transposta
    transposta = []
    nColunas = len(matriz[0])
    for j in range(nColunas):
        linhaTransposta = []
        for linha in matriz:
            linhaTransposta.append(linha[j])
        transposta.append(linhaTransposta)
    
    #Comparando com a matriz original
    diferencas = 0
    if len(transposta) != len(matriz):
        resp = False
    else:
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if matriz[i][j] != transposta[i][j]:
                    diferencas += 1
        resp = True if diferencas == 0 else False
    return resp

# 9. Recebe duas matrizes como parâmetros e retorna o produto delas
# -1 = produto impossível
def prodMatriz(m1, m2):
    nColunas_m1 = len(m1[0])
    nColunas_m2 = len(m2[0])
    nLinhas_m1 = len(m1)
    nLinhas_m2 = len(m2)

    #Caso as dimensões tornem o produto impossível
    if nColunas_m1 != nLinhas_m2:
        return -1
    produto = []

    #Calculando o produto
    for i in range(nLinhas_m1):
        linhaProd = []
        for j in range(nColunas_m2):
            soma = 0
            a = 0
            b = 0
            while a < nColunas_m1 and b < nLinhas_m2:
                soma += m1[i][a] * m2[b][j]
                a += 1
                b += 1
            linhaProd.append(soma)
        produto.append(linhaProd)
    
    return produto


# 10. Recebe um nome de arquivo, um texto e um número. Insere o texto na linha
# indicada, dentro do arquivo.
def insereNaLinha(filename, texto, linha):
    try:
        data = open("%s" %filename, 'r')
        listaLinhas = data.readlines()
        data.close()
        listaLinhas.insert(linha-1, texto)
        data = open("%s" %filename, 'w')
        data.writelines(listaLinhas)
        data.close()
    except:
        print("Arquivo inexistente!")


#Função Main(), realiza a chamada de todas as anteriores
def main():
    #1 - Conversão de valor em metros para dm,cm,mm
    print("\n1 - Conversão de valor em metros para dm,cm,mm")
    mts = float(input("Informe um valor em metros: "))
    (dm, cm, mm) = tuplaDCM(mts)
    print("%d m = %d dm | %d cm | %d mm" %(mts, dm, cm, mm))

    #2 - Verificação se um ano é bissexto
    print("\n2 - Verificação se um ano é bissexto")
    ano = int(input("Informe um ano: "))
    msg = "Eh bissexto" if isBissexto(ano) else "Nao eh bissexto"
    print("%d " %ano + msg)

    #3 - Geração de polígono regular
    cleiton = turtle.Turtle()
    nlados = int(input("Informe o numero de lados: "))
    dimLado = float(input("Informe o tamanho do lado do poligono: "))
    print("\n3 - Geração de polígono regular")
    polRegular(cleiton, nlados, dimLado)

    #4 - Geração de polígono regular colorido
    gerson = turtle.Turtle()
    print("\n4 - Geração de polígono regular colorido")
    dimLado = int(input("Tamanho do lado do polígono colorido: "))
    listaCor = []
    cor = input("Informe a cor do primeiro lado: ")
    listaCor.append(cor)
    while cor != '0':
        cor = input("Informe a cor do proximo lado (0 p/encerrar): ")
        listaCor.append(cor)
    polRegularColorido(gerson, dimLado, listaCor)

    #5 - Contando a quantidade de numerais em uma string
    print("\n5 - Contando a quantidade de numerais em uma string")
    texto = input("Digite um texto: ")
    print("O texto tem %d numerais." %contaNums(texto))

    #6 - Verificação se uma lista está contida em outra
    print("\n6 - Verificação se uma lista está contida em outra")
    seq_gene = []
    seq_ref = []
    node = 0
    while node != 'a':
        node = input("Informe o termo do gene ('a' encerra a leitura): ")
        if node != 'a':
            seq_gene.append(node)
    
    node = 0

    while node != 'a':
        node = input("Informe o termo da referência ('a' encerra a leitura): ")
        if node != 'a':
            seq_ref.append(node)
    
    msg = "está contido na referência" if isContido(seq_gene, seq_ref) else "não está contido na referência."
    print("O gene digitado " + msg)

    #7 - Imprime um "Y" na tela, com a altura especificada
    print("\n7 - Imprime um 'Y' na tela, com a altura especificada")

    dimY = int(input("Qual tamanho de Y você deseja?: "))
    ipsilon(dimY)

    #8 - Verifica se uma matriz é simétrica ou não
    print("\n8 - Verifica se uma matriz é simétrica ou não")
    m1 = [[3,5,6],[5,2,4],[6,4,8]] #Simétrica
    m2 = [[0,2,6],[4,9,2],[3,5,7]] #Ñ-simétrica

    msg = "é simétrica." if isSimetrica(m1) else "não é simétrica."
    print("m1 " + msg)
    msg = "é simétrica." if isSimetrica(m2) else "não é simétrica."
    print("m2 " + msg)

    #9 - Produto de 2 matrizes
    print("\n9 - Produto de 2 matrizes")

    #Produto 3x3 - 3x3: 
    m1 = [[3,5,6],[5,2,4],[6,4,8]]
    m2 = [[0,2,6],[4,9,2],[3,5,7]] 
    prod = prodMatriz(m1, m2)
    
    print("m1 = ", m1)
    print("m2 = ", m2)
    print("O produto de m1 com m2 é: ")
    if prod != -1:
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                print("%d " %prod[i][j], end = "")
            print()
    else:
        print("Produto impossível! (Dimensões inválidas)")
    
    #Produto 2x3 - 3x3:
    m1 = [[3,5,6],[5,2,4]]
    m2 = [[0,2,6],[4,9,2],[3,5,7]] 
    prod = prodMatriz(m1, m2)
    
    print("\nm1 = ", m1)
    print("m2 = ", m2)
    print("O produto de m1 com m2 é: ")
    if prod != -1:
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                print("%d " %prod[i][j], end = "")
            print()
    else:
        print("Produto impossível! (Dimensões inválidas)")

    #Produto 3x2 - 3x3 (inválido):
    m1 = [[3,5],[5,2], [4,2]]
    m2 = [[0,2,6],[4,9,2],[3,5,7]] 
    prod = prodMatriz(m1, m2)
    print("\nm1 = ", m1)
    print("m2 = ", m2)
    
    print("O produto de m1 com m2 é: ")
    if prod != -1:
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                print("%d " %prod[i][j], end = "")
            print()
    else:
        print("Produto impossível! (Dimensões inválidas)")
    
    
    #10 - Modifica um arquivo texto, inserindo uma linha com o texto desejado
    print("\n10 - Modifica um arquivo texto, inserindo uma linha com o texto desejado")
    filename = input("Informe o nome do arquivo (com extensão): ")
    txtappend = input("Digite a linha que deseja inserir: ")
    linepos = int(input("Em qual linha deseja fazer a alteração?: "))
    txtappend += '\n'
    insereNaLinha(filename, txtappend, linepos)

#Testbench
main()