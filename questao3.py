def retiraspa (entrada):
    return entrada[1:-1]

def media (entrada):
    return entrada[0]/entrada[1]

def ler_arquivo(file):
    file.readline()
    file_formatdado = []
    for linha in file:
        file_formatdado.append(linha.replace('"', '').replace('\n', '').split(";"))

    return file_formatdado

anoInicial = input("Digite o ano Inicial: ")
anoFinal = input("Digite o ano Final: ")
anoInicialBC = anoInicial

if len(anoInicial) == 0 or len(anoFinal) == 0:
    print("Anos não informados")
    exit()

livros = []
anos = []

#Verificando se é na ordem crescente ou decrescente;
if int(anoInicial) <= int(anoFinal):
    while int(anoInicial) <= int(anoFinal):
        anos.append(int(anoInicial))
        anoInicial = int(anoInicial) + 1
else:
    while int(anoInicial) >= int(anoFinal):
        anos.append(int(anoInicial))
        anoInicial = int(anoInicial) - 1
    
arqLivros = open("BX_Books.csv", encoding="iso-8859-1")
arqBooks = ler_arquivo(arqLivros)

#Buscando os livros daquele intervalo;
for linha in arqBooks:
    for i in range (len(anos)):
        if int(linha[3]) == anos[i]:
            livros.append(linha)

arqLivros.close()

isbn_list = []
for livro in livros:
    isbn_list.append(livro[0])

arqAvaliacoes = open("BX-Book-Ratings.csv", "r")
arqAvaliacoes = ler_arquivo(arqAvaliacoes)

avaliacoes_por_ano = {}
posicao_melho_nota = 0
melhor_nota = 0

#Buscando as avaliações dos livros no intervalo, e pegando quantidade de avaliações por cada ano;
for i in range(len(arqAvaliacoes)):
    avaliacao = arqAvaliacoes[i]
    for isbn in isbn_list:
        if isbn == avaliacao[1]:
            for livro in livros:
                if livro[0] == isbn:
                    ano_publicacao = int(livro[3])
                    if ano_publicacao in avaliacoes_por_ano:
                        avaliacoes_por_ano[ano_publicacao] += 1
                        if melhor_nota < int(avaliacao[2]):
                            melhor_nota  = int(avaliacao[2])
                            ano_melhor_nota = int(livro[3])
                            posicao_melho_nota = i
                    else:
                        avaliacoes_por_ano[ano_publicacao] = 1
                        


melhor_avaliacao = arqAvaliacoes[posicao_melho_nota]


if len(avaliacoes_por_ano) == 0:
    print("Não foram encontradas avaliações durante esse intervalo!")
    exit()

#Verificando ano com mais avaliações;
ano_com_mais_avaliacoes = max(avaliacoes_por_ano, key=avaliacoes_por_ano.get)

print(f"O ano com mais avaliações é {ano_com_mais_avaliacoes} com {avaliacoes_por_ano[ano_com_mais_avaliacoes]} avaliações")
print(f"O ano com a melhor avaliação é {ano_melhor_nota} com {melhor_avaliacao[2]}")

print(f"Anos com mais avaliações entre {anoInicialBC} e {anoFinal}:")
for ano in sorted(avaliacoes_por_ano, key=avaliacoes_por_ano.get, reverse=True):
    if anoInicial <= ano <= anoFinal:
        print(f"{ano}: {avaliacoes_por_ano[ano]} avaliações")
