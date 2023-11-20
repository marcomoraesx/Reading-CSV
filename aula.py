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

ano = int(input("Digite o ano"))
livros = {}

arqLivros = open("BX_Books.csv", encoding="iso-8859-1")
arqLivros.readline()

for linha in arqLivros:
    entrada = [retiraspa(x) for x in linha.split(";")]
    try:
        if int(entrada[3]) == ano:
            livros[entrada[0]] = [0,0, entrada[1]]
    except:
        continue    

arqLivros.close()

arqNotas = open("BX-Book-Ratings.csv", encoding="iso-8859-1")
arqNotas.readline()

for linha in arqNotas:
    entrada = [retiraspa(x) for x in linha[:-1].split(";")]
    if entrada[1] in livros:
            livros[entrada[1]][0] = livros[entrada[1]][0] + int(entrada[2])
            livros[entrada[1]][1] = livros[entrada[1]][1] + 1

arqNotas.close()

medias = sorted([x[0] for x in livros.values()])
maiorMedia = medias[-1]

melhores = [ x for x in livros.values() if x[1] > 2 and x[0] == maiorMedia]

for livro in melhores:
    print(livro[2], media(livro), livro[1])
