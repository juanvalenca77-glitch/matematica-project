print("\n" + "="*60)
print("------ Seja bem-vindo a meu projeto de matemática ------")
print("       Obrigado por estar aqui :)       ")
print("="*60)

#Escolha inicial
print("\n O que vc deseja fazer primeiro")
print("[1] Aritmética")
print("[2] Álgebra") 
print("[3] Geometria e Trigonometria")
print("[4] Análise de Dados e Cotidiano")
print("[5] Sair")

f_choose = input("Escolha: ") #First choose = Primeira escolha
#Analisar quais realmente são possíveis de realizar em Python
if f_choose == "1":
    print()
    print("[1] Soma, Subtração, Divisão, Multiplicação")
    print("[2] Potenciação e Radiciação") 
    print("[3] Frações, MMC e MDC")
    print("[4] Regra de Três, Razão e Proporção") #como funcionaria a regra de 3 aqui?
    s_choose = input("Escolha: ") #Second choose = segunda escolha
    if s_choose == "1":
        fum_s = input(" Vc quer somar, subtrair, dividir ou multiplicar: ").lower()[0:2]
        if fum_s == "so":
            x = float(input("Qual o primeiro valor: "))
            y = float(input("Qual o segundo valor: "))
            result = x + y
            print(f"O resultado foi de {result}")
        if fum_s == "su":
            x = float(input("Qual o primeiro valor: "))
            y = float(input("Qual o segundo valor: "))
            result = x - y
            print(f"O resultado foi de {result}")
        if fum_s == "di":
            x = float(input("Qual o primeiro valor: "))
            y = float(input("Qual o segundo valor: "))
            result = x / y
            print(f"O resultado foi de {result}")
        if fum_s == "mu":
            x = float(input("Qual o primeiro valor: "))
            y = float(input("Qual o segundo valor: "))
            result = x * y
            print(f"O resultado foi de {result}")
    else:
        print("Não tem essa opção...")
elif f_choose == "2":
    print()
    print("[1] Equações 1° e 2°")
    print("[2] Sistemas de equações") 
    print("[3] Funções")
    s_choose = input("Escolha: ")

elif f_choose == "3":
    print()
    print("[1] Geometria Plana (2D)")
    print("[2] Trigonometria") 
    print("[3] Geometria Espacial (3D)")
    print("[4] Geometria Analítica")
    s_choose = input("Escolha: ")

elif f_choose == "4":
    print()
    print("[1] Análise Combinatória") #Formas de misturar e agrupar coisas (Fatorial, Permutação e Combinação).
    print("[2] Probabilidade") 
    print("[3] Estatística")
    print("[4] Matemática Financeira") #Porcentagem aplicada ao dinheiro (Juros Simples, Juros Compostos e Descontos).
    s_choose = input("Escolha: ")

elif f_choose == "5":
    print()
    print("Tchauzinhoo.....")

else:
    print()
    print("Não tem essa opção...")  