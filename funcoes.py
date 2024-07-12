def resposta ( ):
    #capturando a resposta do usuario e preprocessando-a
    resp = input(">: ")
    resp = resp.lower( )
    resp = resp.replace("é", "eh")
    return resp

def pegaNome (nome):
    if "o meu nome eh " in nome:
        nome = nome[14: ]

    nome = nome.tittle( )
    return nome

def respondeNome(nome):
    conhecidos = ["Raimundo", "Will", "Joao"]

    if nome in conhecidos:
        frase = "Eaew "
    else:
        frase = "Muito prazer "

    return frase + nome