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

livro1 = input("Digite o isbn do livro 1: ")
livro2 = input("Digite o isbn do livro 2: ")

if len(livro1) == 0 or len(livro2) == 0:
    print("Livros não informados")
    exit()

arqAvaliacoes = open("BX-Book-Ratings.csv", "r")
arqAvaliacoes = ler_arquivo(arqAvaliacoes)

#Avaliacao livro 1;
avaliacoes_livro_1 = []
for i in range(len(arqAvaliacoes)):
    avaliacao = arqAvaliacoes[i]
    if livro1 == avaliacao[1]:
        avaliacoes_livro_1.append(int(avaliacao[2]))

media_avaliacao_livro_1 = sum(avaliacoes_livro_1) / len(avaliacoes_livro_1)

#Avaliacao livro 2;
avaliacoes_livro_2 = []
for i in range(len(arqAvaliacoes)):
    avaliacao = arqAvaliacoes[i]
    if livro2 == avaliacao[1]:
        avaliacoes_livro_2.append(int(avaliacao[2]))

media_avaliacao_livro_2 = sum(avaliacoes_livro_2) / len(avaliacoes_livro_2)

print("A media de avaliacao do livro 1 é: " + str(media_avaliacao_livro_1))
print("A media de avaliacao do livro 2 é: " + str(media_avaliacao_livro_2) + "\n")

#Verificando qual média é a pior;
if media_avaliacao_livro_1 > media_avaliacao_livro_2:
    print("O livro de pior avaliação é o livro 2")
else:
    print("O livro de pior avaliação é o livro 1")
