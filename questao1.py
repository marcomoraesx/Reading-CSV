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

autor = input("Digite o autor: ")

if len(autor) == 0:
    print("Autor não informado")
    exit()

livros = []

arqLivros = open("BX_Books.csv", encoding="iso-8859-1")
arqBooks = ler_arquivo(arqLivros)

#Buscando livros do autor passado;
for linha in arqBooks:
    if linha[2] == autor:
        livros.append(linha)

arqLivros.close()

#Criando uma com todos os ISBN do autor;
isbn_list = []
for livro in livros:
    isbn_list.append(livro[0])

avaliacoes = []
posicao_melho_nota = 0
melhor_nota = 0

arqAvaliacoes = open("BX-Book-Ratings.csv", "r")
arqAvaliacoes = ler_arquivo(arqAvaliacoes)

#Buscando as avaliações de todos os livros do autor, e verificando o de melhor nota;
for i in range(len(arqAvaliacoes)):
    avaliacao = arqAvaliacoes[i]
    for isbn in isbn_list:
        if isbn == avaliacao[1]:
            if melhor_nota < int(avaliacao[2]):
                melhor_nota  = int(avaliacao[2])
                posicao_melho_nota = i

melhor_avaliacao = arqAvaliacoes[posicao_melho_nota]

arquivo_usuarios = open("BX-Users.csv", "r")
arquivo_usuarios = ler_arquivo(arquivo_usuarios)

#Buscando a idade do melhor avaliador;
idade_melhor_avaliacao = 0
for usuario in arquivo_usuarios:
    if usuario[0] == melhor_avaliacao[0]:
        idade_melhor_avaliacao = usuario[2]

if len(livros) == 0:
    print(f"O {autor} não tem livros com avaliações")
else:
    print(f"A idade do user que melhor avaliou o(a) {autor} foi {idade_melhor_avaliacao}") 
