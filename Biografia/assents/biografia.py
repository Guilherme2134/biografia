def obter_informacoes_biograficas():
    print("Por favor, forneça algumas informações biográficas:")
    nome = input("Nome: ")
    idade = input("Idade: ")
    local_nascimento = input("Local de nascimento: ")
    interesses = input("Interesses: ")
    
    informacoes = {
        "Nome": nome,
        "Idade": idade,
        "Local de Nascimento": local_nascimento,
        "Interesses": interesses
    }
    return informacoes

def exibir_informacoes_biograficas(informacoes):
    print("\nInformações Biográficas:")
    for chave, valor in informacoes.items():
        print(f"{chave}: {valor}")

def main():
    informacoes = obter_informacoes_biograficas()
    exibir_informacoes_biograficas(informacoes)

if __name__ == "__main__":
    main()
