print("\n" + "="*60)
print("------ Seja bem-vindo a meu projeto de matemática ------")
print("="*60)

#Escolha inicial
print("\n O que vc deseja fazer primeiro")
print("[1] Aritmética")
print("[2] Álgebra") 
print("[3] Geometria e Trigonometria")
print("[4] Análise de Dados e Cotidiano")

f_choose = input("Escolha: ") #First choose = Primeira escolha
#Analisar quais realmente são possíveis de realizar em Python
if f_choose == "1":
    print("[1] Soma, Subtração, Divisão, Multiplicação")
    print("[2] Potenciação e Radiciação") 
    print("[3] Frações, MMC e MDC")
    print("[4] Regra de Três, Razão e Proporção") #como funcionaria a regra de 3 aqui?

elif f_choose == "2":
    print("[1] Equações 1° e 2°")
    print("[2] Sistemas de equações") 
    print("[3] Funções")

elif f_choose == "3":
    print("[1] Geometria Plana (2D)")
    print("[2] Trigonometria") 
    print("[3] Geometria Espacial (3D)")
    print("[4] Geometria Analítica")

elif f_choose == "4":
    print("[1] Análise Combinatória") #Formas de misturar e agrupar coisas (Fatorial, Permutação e Combinação).
    print("[2] Probabilidade") 
    print("[3] Estatística")
    print("[4] Matemática Financeira") #Porcentagem aplicada ao dinheiro (Juros Simples, Juros Compostos e Descontos).