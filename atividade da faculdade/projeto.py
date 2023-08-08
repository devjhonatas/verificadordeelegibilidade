def main():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    if idade < 18:
        print("Menor de idade")
        print("Não é permitida sua inscrição")
        return  # Encerra o programa para menores de idade

    print("Maior de idade")
    sexo = input('Digite (F) para Feminino, (M) para Masculino: ').upper()

    if sexo == 'M':
        print('Sexo Masculino.')
        print("Número CAM:")
    elif sexo == 'F':
        print('Sexo Feminino.')
    else:
        print('Sexo Inválido.')

if __name__ == "__main__":
    main()
