# ============================================================
#         PROJETO DE MATEMÁTICA - COMPLETO
# ============================================================

PI = 3.14159265358979  # valor de pi que vamos usar em tudo


# ============================================================
# FUNÇÕES AUXILIARES (usadas em vários cálculos)
# ============================================================

def raiz(x):
    # calcula raiz quadrada pelo método de Newton (sem math.sqrt)
    if x < 0:
        return None
    if x == 0:
        return 0
    g = x / 2.0
    for i in range(1000):
        g = (g + x / g) / 2.0
    return g

def fat(n):
    # calcula fatorial de n (ex: 5! = 120)
    n = int(n)
    if n < 0:
        return None
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

def seno(graus):
    # calcula seno usando a série de Taylor (entrada em graus)
    rad = graus * PI / 180
    # normaliza o ângulo entre -PI e PI para a série funcionar bem
    while rad > PI:
        rad -= 2 * PI
    while rad < -PI:
        rad += 2 * PI
    s = 0
    for i in range(15):  # 15 termos da série já dão muita precisão
        n = 2 * i + 1
        s += ((-1) ** i) * (rad ** n) / fat(n)
    return s

def cosseno(graus):
    # calcula cosseno pela série de Taylor (entrada em graus)
    rad = graus * PI / 180
    while rad > PI:
        rad -= 2 * PI
    while rad < -PI:
        rad += 2 * PI
    c = 0
    for i in range(15):
        n = 2 * i
        c += ((-1) ** i) * (rad ** n) / fat(n)
    return c

def tangente(graus):
    # tangente = seno / cosseno
    c = cosseno(graus)
    if abs(c) < 0.00001:
        return None  # tangente indefinida (90°, 270°...)
    return seno(graus) / c

def arcoseno(y):
    # calcula arcosseno em graus (inverso do seno) - método de Newton
    if y < -1 or y > 1:
        return None
    if y >= 1:
        return 90.0
    if y <= -1:
        return -90.0
    x = y  # chute inicial em radianos
    for i in range(60):
        s = seno(x * 180 / PI)
        c = cosseno(x * 180 / PI)
        if abs(c) < 0.000001:
            break
        x = x - (s - y) / c
    return x * 180 / PI

def mdc(a, b):
    # máximo divisor comum pelo algoritmo de Euclides
    a, b = int(abs(a)), int(abs(b))
    while b != 0:
        a, b = b, a % b
    return a

def mmc(a, b):
    # mínimo múltiplo comum usando o mdc
    a, b = int(abs(a)), int(abs(b))
    return a * b // mdc(a, b)

def arred(x, casas=4):
    # atalho para arredondar com menos escrita
    return round(x, casas)

def poligono_regular(n, l):
    # calcula área e apotema de qualquer polígono regular
    # apotema: a = L / (2 * tan(180/n))  <- fórmula com apotema
    ang = 180 / n
    t = tangente(ang)
    if t is None or t == 0:
        return None, None, None
    apo = l / (2 * t)    # apotema
    per = n * l          # perímetro
    area = (per * apo) / 2  # área pelo apotema
    return apo, per, area


# ============================================================
# LOOP PRINCIPAL - o programa fica rodando até o usuário sair
# ============================================================

while True:
    print("\n" + "="*60)
    print("------ Seja bem-vindo a meu projeto de matemática ------")
    print("       Obrigado por estar aqui :)       ")
    print("="*60)

    print("\n O que vc deseja fazer primeiro")
    print("[1] Aritmética")
    print("[2] Álgebra")
    print("[3] Geometria e Trigonometria")
    print("[4] Análise de Dados e Cotidiano")
    print("[5] Sair")
    f_choose = input("Escolha: ")


    # ============================================================
    # [1] ARITMÉTICA
    # ============================================================
    if f_choose == "1":
        print()
        print("[1] Soma, Subtração, Divisão, Multiplicação")
        print("[2] Potenciação e Radiciação")
        print("[3] Frações, MMC e MDC")
        print("[4] Regra de Três, Razão e Proporção")
        s_choose = input("Escolha: ")

        # ---------- [1.1] Operações básicas ----------
        if s_choose == "1":
            fum_s = input(" Vc quer somar, subtrair, dividir ou multiplicar: ").lower()[0:2]
            if fum_s == "so":
                x = float(input("Qual o primeiro valor: "))
                y = float(input("Qual o segundo valor: "))
                result = x + y
                print(f"O resultado foi de {result}")
            elif fum_s == "su":
                x = float(input("Qual o primeiro valor: "))
                y = float(input("Qual o segundo valor: "))
                result = x - y
                print(f"O resultado foi de {result}")
            elif fum_s == "di":
                x = float(input("Qual o primeiro valor: "))
                y = float(input("Qual o segundo valor: "))
                if y == 0:
                    print("Erro: divisão por zero!")
                else:
                    result = x / y
                    print(f"O resultado foi de {result}")
            elif fum_s == "mu":
                x = float(input("Qual o primeiro valor: "))
                y = float(input("Qual o segundo valor: "))
                result = x * y
                print(f"O resultado foi de {result}")
            else:
                print("Não tem essa opção...")

        # ---------- [1.2] Potenciação e Radiciação ----------
        elif s_choose == "2":
            fdois_s = input(" Vc quer fazer potenciação ou radiciação: ").lower()[0:2]
            if fdois_s == "po":
                x = float(input("Qual o valor base: "))
                y = float(input("Qual o expoente: "))
                result = x ** y
                print(f"O resultado foi de {result}")
            elif fdois_s == "ra":
                x = float(input("Qual o valor do radicando: "))
                if x < 0:
                    print("Erro: raiz de número negativo não é real!")
                else:
                    rad_q = raiz(x)       # raiz quadrada
                    rad_c = x ** (1/3)    # raiz cúbica
                    print(f"Raiz quadrada = {arred(rad_q, 6)}")
                    print(f"Raiz cúbica   = {arred(rad_c, 6)}")
                    ind = float(input("Quer a raiz de qual índice? (ex: 4): "))
                    rad_n = x ** (1/ind)
                    print(f"Raiz de índice {int(ind)} = {arred(rad_n, 6)}")
            else:
                print("Não tem essa opção...")

        # ---------- [1.3] Frações, MMC e MDC ----------
        elif s_choose == "3":
            fdois_s = input(" Vc quer fazer frações, MMC ou MDC: ").lower()[0:2]

            if fdois_s == "fr":
                print("--- Fração 1 ---")
                n1 = int(input("  Numerador: "))
                d1 = int(input("  Denominador: "))
                print("--- Fração 2 ---")
                n2 = int(input("  Numerador: "))
                d2 = int(input("  Denominador: "))
                op = input("Operação (soma/sub/mult/div): ").lower()[0:2]

                if op == "so":
                    # (n1/d1) + (n2/d2) = (n1*d2 + n2*d1) / (d1*d2)
                    rn = n1*d2 + n2*d1
                    rd = d1*d2
                elif op == "su":
                    rn = n1*d2 - n2*d1
                    rd = d1*d2
                elif op == "mu":
                    rn = n1*n2
                    rd = d1*d2
                elif op == "di":
                    # dividir = multiplicar pelo inverso da segunda fração
                    rn = n1*d2
                    rd = d1*n2
                else:
                    print("Não tem essa opção...")
                    rn, rd = 0, 1

                # simplifica a fração pelo mdc
                div = mdc(abs(rn), abs(rd))
                if div > 0:
                    print(f"Resultado: {rn//div}/{rd//div}")
                    print(f"Em decimal: {arred(rn/rd, 6)}")

            elif fdois_s == "mm":
                a = int(input("Primeiro número: "))
                b = int(input("Segundo número: "))
                print(f"MMC de {a} e {b} = {mmc(a, b)}")

            elif fdois_s == "md":
                a = int(input("Primeiro número: "))
                b = int(input("Segundo número: "))
                print(f"MDC de {a} e {b} = {mdc(a, b)}")
            else:
                print("Não tem essa opção...")

        # ---------- [1.4] Regra de Três, Razão e Proporção ----------
        elif s_choose == "4":
            fquatro_s = input(" Regra de três simples ou composta? (simples/composta): ").lower()[0:2]

            if fquatro_s == "si":
                # A/B = C/X  =>  X = B*C/A
                print("Formato: A está para B  assim como  C está para X")
                a = float(input("Valor de A: "))
                b = float(input("Valor de B: "))
                c = float(input("Valor de C: "))
                if a == 0:
                    print("Erro: A não pode ser zero!")
                else:
                    x = (b * c) / a
                    print(f"X = {arred(x, 4)}")

            elif fquatro_s == "co":
                # Regra de três composta com duas grandezas
                print("Duas grandezas (A e B) para achar X")
                print("  A1 --- A2")
                print("  B1 --- B2")
                print("  ??  --- X")
                a1 = float(input("A1 (valor base de A): "))
                a2 = float(input("A2 (valor comparado de A): "))
                b1 = float(input("B1 (valor base de B): "))
                b2 = float(input("B2 (valor comparado de B): "))
                ref = float(input("Valor de referência (do '??'): "))
                ta = input("A é DIRETA ou INVERSA a X? (d/i): ").lower()
                tb = input("B é DIRETA ou INVERSA a X? (d/i): ").lower()

                # fator de cada grandeza conforme o tipo de proporcionalidade
                fa = a2/a1 if ta == "d" else a1/a2
                fb = b2/b1 if tb == "d" else b1/b2
                x = ref * fa * fb
                print(f"X = {arred(x, 4)}")
            else:
                print("Não tem essa opção...")
        else:
            print("Não tem essa opção...")


    # ============================================================
    # [2] ÁLGEBRA
    # ============================================================
    elif f_choose == "2":
        print()
        print("[1] Equações 1° e 2° grau")
        print("[2] Sistemas de equações (2x2)")
        print("[3] Funções")
        s_choose = input("Escolha: ")

        # ---------- [2.1] Equações ----------
        if s_choose == "1":
            grau = input("Equação de 1° ou 2° grau? (1/2): ")

            if grau == "1":
                # ax + b = 0  =>  x = -b/a
                print("Formato: ax + b = 0")
                a = float(input("Valor de a: "))
                b = float(input("Valor de b: "))
                if a == 0:
                    if b == 0:
                        print("Infinitas soluções (0 = 0)")
                    else:
                        print("Sem solução (equação impossível)")
                else:
                    x = -b / a
                    print(f"x = {arred(x, 4)}")

            elif grau == "2":
                # ax² + bx + c = 0  =>  delta = b² - 4ac
                print("Formato: ax² + bx + c = 0")
                a = float(input("Valor de a: "))
                b = float(input("Valor de b: "))
                c = float(input("Valor de c: "))
                if a == 0:
                    print("Não é 2° grau (a=0). Use equação de 1° grau.")
                else:
                    delta = b**2 - 4*a*c
                    print(f"Delta = {delta}")
                    if delta < 0:
                        print("Sem raízes reais (delta negativo)")
                    elif delta == 0:
                        x = -b / (2*a)
                        print(f"Raiz dupla: x = {arred(x, 4)}")
                    else:
                        x1 = (-b + raiz(delta)) / (2*a)
                        x2 = (-b - raiz(delta)) / (2*a)
                        print(f"x1 = {arred(x1, 4)}")
                        print(f"x2 = {arred(x2, 4)}")
                        print(f"Soma das raízes  = {arred(x1+x2, 4)}")
                        print(f"Produto das raízes = {arred(x1*x2, 4)}")
            else:
                print("Não tem essa opção...")

        # ---------- [2.2] Sistemas de equações 2x2 ----------
        elif s_choose == "2":
            print("Sistema 2x2 pelo método de Cramer:")
            print("  a1*x + b1*y = c1")
            print("  a2*x + b2*y = c2")
            a1 = float(input("a1: "))
            b1 = float(input("b1: "))
            c1 = float(input("c1: "))
            a2 = float(input("a2: "))
            b2 = float(input("b2: "))
            c2 = float(input("c2: "))

            # determinante principal
            det = a1*b2 - a2*b1
            if det == 0:
                print("Sistema sem solução única (determinante = 0)")
            else:
                # regra de Cramer: x = det_x/det, y = det_y/det
                x = (c1*b2 - c2*b1) / det
                y = (a1*c2 - a2*c1) / det
                print(f"x = {arred(x, 4)}")
                print(f"y = {arred(y, 4)}")

        # ---------- [2.3] Funções ----------
        elif s_choose == "3":
            print()
            print("[1] Função Linear       f(x) = ax + b")
            print("[2] Função Quadrática   f(x) = ax² + bx + c")
            print("[3] Função Exponencial  f(x) = a * b^x")
            t_func = input("Escolha: ")

            if t_func == "1":
                a = float(input("Valor de a (coeficiente angular): "))
                b = float(input("Valor de b (coeficiente linear): "))
                x = float(input("Calcular f(x) para x = "))
                print(f"f({x}) = {a*x + b}")
                if a != 0:
                    zero = -b / a  # ponto onde f(x) = 0
                    print(f"Zero da função: x = {arred(zero, 4)}")
                if a > 0:
                    print("Função crescente")
                elif a < 0:
                    print("Função decrescente")
                else:
                    print("Função constante")

            elif t_func == "2":
                a = float(input("Valor de a: "))
                b = float(input("Valor de b: "))
                c = float(input("Valor de c: "))
                x = float(input("Calcular f(x) para x = "))
                print(f"f({x}) = {a*x**2 + b*x + c}")
                delta = b**2 - 4*a*c
                print(f"Delta = {delta}")
                if delta >= 0 and a != 0:
                    x1 = (-b + raiz(delta)) / (2*a)
                    x2 = (-b - raiz(delta)) / (2*a)
                    print(f"Raízes: x1 = {arred(x1,4)}, x2 = {arred(x2,4)}")
                if a != 0:
                    vx = -b / (2*a)         # x do vértice
                    vy = a*vx**2 + b*vx + c  # y do vértice
                    print(f"Vértice: ({arred(vx,4)}, {arred(vy,4)})")
                    if a > 0:
                        print("Parábola voltada pra cima (mínimo no vértice)")
                    else:
                        print("Parábola voltada pra baixo (máximo no vértice)")

            elif t_func == "3":
                a = float(input("Valor de a (coeficiente): "))
                b = float(input("Valor de b (base, b > 0 e b ≠ 1): "))
                x = float(input("Calcular f(x) para x = "))
                if b <= 0 or b == 1:
                    print("Base inválida! (b deve ser > 0 e diferente de 1)")
                else:
                    print(f"f({x}) = {arred(a * b**x, 6)}")
                    if b > 1:
                        print("Função exponencial crescente")
                    else:
                        print("Função exponencial decrescente")
            else:
                print("Não tem essa opção...")
        else:
            print("Não tem essa opção...")


    # ============================================================
    # [3] GEOMETRIA E TRIGONOMETRIA
    # ============================================================
    elif f_choose == "3":
        print()
        print("[1] Geometria Plana (2D)")
        print("[2] Trigonometria")
        print("[3] Geometria Espacial (3D)")
        print("[4] Geometria Analítica")
        s_choose = input("Escolha: ")

        # ---------- [3.1] Geometria Plana ----------
        if s_choose == "1":
            print()
            print("[1] Triângulo")
            print("[2] Quadrado")
            print("[3] Retângulo")
            print("[4] Círculo")
            print("[5] Trapézio")
            print("[6] Losango")
            print("[7] Pentágono regular  (5 lados - usa apotema)")
            print("[8] Hexágono regular   (6 lados - usa apotema)")
            print("[9] Polígono regular   (qualquer - usa apotema)")
            figura = input("Escolha: ")

            if figura == "1":
                print("--- Triângulo ---")
                b = float(input("Base: "))
                h = float(input("Altura: "))
                area = (b * h) / 2
                print(f"Área = {arred(area, 4)}")
                l1 = float(input("Lado 1: "))
                l2 = float(input("Lado 2: "))
                l3 = float(input("Lado 3: "))
                per = l1 + l2 + l3
                print(f"Perímetro = {per}")
                # semi-perímetro para fórmula de Heron
                sp = per / 2
                area_h = raiz(sp * (sp-l1) * (sp-l2) * (sp-l3))
                if area_h is not None:
                    print(f"Área (Heron) = {arred(area_h, 4)}")
                # classifica o triângulo pelos lados
                lados = sorted([l1, l2, l3])
                if lados[0] == lados[1] == lados[2]:
                    print("Tipo: Equilátero")
                elif lados[0] == lados[1] or lados[1] == lados[2]:
                    print("Tipo: Isósceles")
                else:
                    print("Tipo: Escaleno")
                # classifica pelos ângulos (usando teorema de Pitágoras)
                if abs(lados[0]**2 + lados[1]**2 - lados[2]**2) < 0.001:
                    print("Ângulos: Retângulo")
                elif lados[0]**2 + lados[1]**2 > lados[2]**2:
                    print("Ângulos: Acutângulo")
                else:
                    print("Ângulos: Obtusângulo")

            elif figura == "2":
                print("--- Quadrado ---")
                l = float(input("Lado: "))
                area = l ** 2
                per  = 4 * l
                diag = l * raiz(2)
                print(f"Área = {area}")
                print(f"Perímetro = {per}")
                print(f"Diagonal = {arred(diag, 4)}")

            elif figura == "3":
                print("--- Retângulo ---")
                b = float(input("Base: "))
                h = float(input("Altura: "))
                area = b * h
                per  = 2 * (b + h)
                diag = raiz(b**2 + h**2)
                print(f"Área = {area}")
                print(f"Perímetro = {per}")
                print(f"Diagonal = {arred(diag, 4)}")

            elif figura == "4":
                print("--- Círculo ---")
                r = float(input("Raio: "))
                area = PI * r**2
                circ = 2 * PI * r
                print(f"Área = {arred(area, 4)}")
                print(f"Circunferência = {arred(circ, 4)}")
                print(f"Diâmetro = {2*r}")

            elif figura == "5":
                print("--- Trapézio ---")
                B = float(input("Base maior: "))
                b = float(input("Base menor: "))
                h = float(input("Altura: "))
                area = ((B + b) * h) / 2
                print(f"Área = {arred(area, 4)}")

            elif figura == "6":
                print("--- Losango ---")
                d1 = float(input("Diagonal maior: "))
                d2 = float(input("Diagonal menor: "))
                area = (d1 * d2) / 2
                # lado pelo teorema de Pitágoras (metades das diagonais)
                lado = raiz((d1/2)**2 + (d2/2)**2)
                per  = 4 * lado
                print(f"Área = {arred(area, 4)}")
                print(f"Lado = {arred(lado, 4)}")
                print(f"Perímetro = {arred(per, 4)}")

            elif figura == "7":
                print("--- Pentágono Regular (usa apotema) ---")
                l = float(input("Lado: "))
                apo, per, area = poligono_regular(5, l)
                print(f"Apotema = {arred(apo, 4)}")
                print(f"Perímetro = {per}")
                print(f"Área = {arred(area, 4)}")

            elif figura == "8":
                print("--- Hexágono Regular (usa apotema) ---")
                l = float(input("Lado: "))
                apo, per, area = poligono_regular(6, l)
                print(f"Apotema = {arred(apo, 4)}")
                print(f"Perímetro = {per}")
                print(f"Área = {arred(area, 4)}")

            elif figura == "9":
                print("--- Polígono Regular (usa apotema) ---")
                n = int(input("Número de lados: "))
                l = float(input("Comprimento do lado: "))
                if n < 3:
                    print("Um polígono precisa de pelo menos 3 lados!")
                else:
                    apo, per, area = poligono_regular(n, l)
                    print(f"Apotema = {arred(apo, 4)}")
                    print(f"Perímetro = {per}")
                    print(f"Área (pela apotema) = {arred(area, 4)}")
            else:
                print("Não tem essa opção...")

        # ---------- [3.2] Trigonometria ----------
        elif s_choose == "2":
            print()
            print("[1] Sen, Cos e Tan de um ângulo")
            print("[2] Lei dos Senos")
            print("[3] Lei dos Cossenos")
            t_trig = input("Escolha: ")

            if t_trig == "1":
                ang = float(input("Ângulo em graus: "))
                s = seno(ang)
                c = cosseno(ang)
                t = tangente(ang)
                print(f"sen({ang}°) = {arred(s, 6)}")
                print(f"cos({ang}°) = {arred(c, 6)}")
                if t is None:
                    print(f"tan({ang}°) = indefinida")
                else:
                    print(f"tan({ang}°) = {arred(t, 6)}")
                # relação fundamental: sen²+cos²=1
                print(f"Verificação (sen²+cos² deve ser 1): {arred(s**2+c**2, 6)}")

            elif t_trig == "2":
                # Lei dos senos: a/sen(A) = b/sen(B) = c/sen(C)
                print("Lei dos senos: a/sen(A) = b/sen(B)")
                a = float(input("Lado a: "))
                A = float(input("Ângulo A em graus (oposto ao lado a): "))
                b = float(input("Lado b: "))
                sen_A = seno(A)
                if abs(sen_A) < 0.00001:
                    print("Ângulo inválido!")
                else:
                    razao = a / sen_A  # a/sen(A) = constante
                    print(f"Razão constante a/sen(A) = {arred(razao, 4)}")
                    sen_B = b / razao  # sen(B) = b / razão
                    if abs(sen_B) > 1:
                        print("Triângulo impossível!")
                    else:
                        B = arcoseno(sen_B)
                        print(f"Ângulo B = {arred(B, 4)}°")
                        C = 180 - A - B
                        print(f"Ângulo C = {arred(C, 4)}°")
                        c = razao * seno(C)
                        print(f"Lado c = {arred(c, 4)}")

            elif t_trig == "3":
                # Lei dos cossenos: c² = a² + b² - 2ab*cos(C)
                print("Lei dos cossenos: c² = a² + b² - 2ab·cos(C)")
                a = float(input("Lado a: "))
                b = float(input("Lado b: "))
                C = float(input("Ângulo C entre a e b (graus): "))
                c2 = a**2 + b**2 - 2*a*b*cosseno(C)
                if c2 < 0:
                    print("Triângulo impossível com esses valores!")
                else:
                    c = raiz(c2)
                    print(f"Lado c = {arred(c, 4)}")
                    # achar os outros ângulos pelo arcosseno
                    cos_A = (b**2 + c**2 - a**2) / (2*b*c)
                    cos_B = (a**2 + c**2 - b**2) / (2*a*c)
                    A = arcoseno(raiz(1 - cos_A**2)) if cos_A >= 0 else 180 - arcoseno(raiz(1 - cos_A**2))
                    B = 180 - A - C
                    print(f"Ângulo A ≈ {arred(A, 2)}°")
                    print(f"Ângulo B ≈ {arred(B, 2)}°")
            else:
                print("Não tem essa opção...")

        # ---------- [3.3] Geometria Espacial ----------
        elif s_choose == "3":
            print()
            print("[1] Cubo")
            print("[2] Paralelepípedo")
            print("[3] Esfera")
            print("[4] Cilindro")
            print("[5] Cone")
            print("[6] Pirâmide de base quadrada")
            print("[7] Prisma de base triangular")
            solid = input("Escolha: ")

            if solid == "1":
                print("--- Cubo ---")
                a = float(input("Aresta: "))
                vol    = a ** 3
                area_t = 6 * a**2
                diag   = a * raiz(3)
                print(f"Volume = {vol}")
                print(f"Área total = {area_t}")
                print(f"Diagonal do espaço = {arred(diag, 4)}")

            elif solid == "2":
                print("--- Paralelepípedo ---")
                a = float(input("Comprimento: "))
                b = float(input("Largura: "))
                c = float(input("Altura: "))
                vol    = a * b * c
                area_t = 2 * (a*b + b*c + a*c)
                diag   = raiz(a**2 + b**2 + c**2)
                print(f"Volume = {vol}")
                print(f"Área total = {area_t}")
                print(f"Diagonal = {arred(diag, 4)}")

            elif solid == "3":
                print("--- Esfera ---")
                r = float(input("Raio: "))
                vol    = (4/3) * PI * r**3
                area_t = 4 * PI * r**2
                print(f"Volume = {arred(vol, 4)}")
                print(f"Área da superfície = {arred(area_t, 4)}")

            elif solid == "4":
                print("--- Cilindro ---")
                r = float(input("Raio da base: "))
                h = float(input("Altura: "))
                area_base = PI * r**2
                area_lat  = 2 * PI * r * h
                area_t    = area_lat + 2 * area_base
                vol       = area_base * h
                print(f"Volume = {arred(vol, 4)}")
                print(f"Área lateral = {arred(area_lat, 4)}")
                print(f"Área total = {arred(area_t, 4)}")

            elif solid == "5":
                print("--- Cone ---")
                r = float(input("Raio da base: "))
                h = float(input("Altura: "))
                g        = raiz(r**2 + h**2)   # geratriz
                area_base = PI * r**2
                area_lat  = PI * r * g
                area_t    = area_lat + area_base
                vol       = (1/3) * area_base * h
                print(f"Geratriz = {arred(g, 4)}")
                print(f"Volume = {arred(vol, 4)}")
                print(f"Área lateral = {arred(area_lat, 4)}")
                print(f"Área total = {arred(area_t, 4)}")

            elif solid == "6":
                print("--- Pirâmide de base quadrada ---")
                l = float(input("Lado da base: "))
                h = float(input("Altura: "))
                area_base = l**2
                # apótema da face triangular lateral
                apo_face  = raiz(h**2 + (l/2)**2)
                area_lat  = 4 * (l * apo_face / 2)   # 4 triângulos laterais
                area_t    = area_base + area_lat
                vol       = (1/3) * area_base * h
                print(f"Apótema da face lateral = {arred(apo_face, 4)}")
                print(f"Volume = {arred(vol, 4)}")
                print(f"Área da base = {area_base}")
                print(f"Área lateral = {arred(area_lat, 4)}")
                print(f"Área total = {arred(area_t, 4)}")

            elif solid == "7":
                print("--- Prisma de base triangular ---")
                b = float(input("Base do triângulo: "))
                ht = float(input("Altura do triângulo: "))
                comp = float(input("Comprimento do prisma: "))
                area_base = (b * ht) / 2
                vol       = area_base * comp
                print(f"Volume = {arred(vol, 4)}")
                print(f"Área da base = {arred(area_base, 4)}")
            else:
                print("Não tem essa opção...")

        # ---------- [3.4] Geometria Analítica ----------
        elif s_choose == "4":
            print()
            print("[1] Distância entre dois pontos")
            print("[2] Ponto médio")
            print("[3] Equação da reta (por dois pontos)")
            print("[4] Distância de ponto a reta")
            print("[5] Baricentro do triângulo")
            t_anal = input("Escolha: ")

            if t_anal == "1":
                x1 = float(input("x1: "))
                y1 = float(input("y1: "))
                x2 = float(input("x2: "))
                y2 = float(input("y2: "))
                d = raiz((x2-x1)**2 + (y2-y1)**2)
                print(f"Distância = {arred(d, 4)}")

            elif t_anal == "2":
                x1 = float(input("x1: "))
                y1 = float(input("y1: "))
                x2 = float(input("x2: "))
                y2 = float(input("y2: "))
                mx = (x1 + x2) / 2
                my = (y1 + y2) / 2
                print(f"Ponto médio = ({arred(mx, 4)}, {arred(my, 4)})")

            elif t_anal == "3":
                x1 = float(input("x1: "))
                y1 = float(input("y1: "))
                x2 = float(input("x2: "))
                y2 = float(input("y2: "))
                if x2 == x1:
                    print(f"Reta vertical: x = {x1}")
                else:
                    m = (y2 - y1) / (x2 - x1)   # coeficiente angular
                    b = y1 - m * x1               # coeficiente linear
                    print(f"Equação: y = {arred(m,4)}x + ({arred(b,4)})")
                    print(f"Forma geral: {arred(m,4)}x - y + ({arred(b,4)}) = 0")
                    print(f"Coeficiente angular (m) = {arred(m,4)}")

            elif t_anal == "4":
                # d = |a*px + b*py + c| / sqrt(a²+b²)
                print("Reta na forma: ax + by + c = 0")
                a  = float(input("a: "))
                b  = float(input("b: "))
                c  = float(input("c: "))
                px = float(input("x do ponto: "))
                py = float(input("y do ponto: "))
                num = abs(a*px + b*py + c)
                den = raiz(a**2 + b**2)
                if den == 0:
                    print("Reta inválida!")
                else:
                    d = num / den
                    print(f"Distância = {arred(d, 4)}")

            elif t_anal == "5":
                # baricentro G = média das coordenadas dos 3 vértices
                print("Informe os 3 vértices do triângulo:")
                x1 = float(input("x1: "))
                y1 = float(input("y1: "))
                x2 = float(input("x2: "))
                y2 = float(input("y2: "))
                x3 = float(input("x3: "))
                y3 = float(input("y3: "))
                gx = (x1 + x2 + x3) / 3
                gy = (y1 + y2 + y3) / 3
                print(f"Baricentro G = ({arred(gx, 4)}, {arred(gy, 4)})")
            else:
                print("Não tem essa opção...")
        else:
            print("Não tem essa opção...")


    # ============================================================
    # [4] ANÁLISE DE DADOS E COTIDIANO
    # ============================================================
    elif f_choose == "4":
        print()
        print("[1] Análise Combinatória")
        print("[2] Probabilidade")
        print("[3] Estatística")
        print("[4] Matemática Financeira")
        s_choose = input("Escolha: ")

        # ---------- [4.1] Análise Combinatória ----------
        if s_choose == "1":
            print()
            print("[1] Fatorial")
            print("[2] Permutação simples")
            print("[3] Arranjo")
            print("[4] Combinação")
            t_comb = input("Escolha: ")

            if t_comb == "1":
                n = int(input("n: "))
                print(f"{n}! = {fat(n)}")

            elif t_comb == "2":
                # P(n) = n!  (quantas formas de organizar n elementos)
                n = int(input("n (total de elementos): "))
                print(f"Permutação P({n}) = {fat(n)}")

            elif t_comb == "3":
                # A(n,p) = n! / (n-p)!  (ordem importa, escolhe p de n)
                n = int(input("n (total): "))
                p = int(input("p (quantos escolher, com ordem): "))
                if p > n:
                    print("Erro: p não pode ser maior que n!")
                else:
                    result = fat(n) // fat(n - p)
                    print(f"Arranjo A({n},{p}) = {result}")

            elif t_comb == "4":
                # C(n,p) = n! / (p! * (n-p)!)  (ordem não importa)
                n = int(input("n (total): "))
                p = int(input("p (quantos escolher, sem ordem): "))
                if p > n:
                    print("Erro: p não pode ser maior que n!")
                else:
                    result = fat(n) // (fat(p) * fat(n - p))
                    print(f"Combinação C({n},{p}) = {result}")
            else:
                print("Não tem essa opção...")

        # ---------- [4.2] Probabilidade ----------
        elif s_choose == "2":
            print()
            print("[1] Probabilidade simples P(A)")
            print("[2] P(A e B) — eventos independentes")
            print("[3] P(A ou B)")
            print("[4] Probabilidade complementar P(não A)")
            t_prob = input("Escolha: ")

            if t_prob == "1":
                fav   = float(input("Casos favoráveis: "))
                total = float(input("Total de casos possíveis: "))
                if total == 0:
                    print("Erro: total não pode ser zero!")
                else:
                    prob = fav / total
                    print(f"P(A) = {fav}/{int(total)} = {arred(prob, 4)} = {arred(prob*100, 2)}%")

            elif t_prob == "2":
                # P(A e B) = P(A) * P(B)
                pa = float(input("P(A) (valor de 0 a 1): "))
                pb = float(input("P(B) (valor de 0 a 1): "))
                print(f"P(A e B) = {arred(pa * pb, 6)}")

            elif t_prob == "3":
                # P(A ou B) = P(A) + P(B) - P(A ∩ B)
                pa  = float(input("P(A): "))
                pb  = float(input("P(B): "))
                pab = float(input("P(A e B) (0 se mutuamente exclusivos): "))
                print(f"P(A ou B) = {arred(pa + pb - pab, 6)}")

            elif t_prob == "4":
                # P(não A) = 1 - P(A)
                pa = float(input("P(A): "))
                print(f"P(não A) = {arred(1 - pa, 6)}")
            else:
                print("Não tem essa opção...")

        # ---------- [4.3] Estatística ----------
        elif s_choose == "3":
            print("Digite os números separados por espaço:")
            entrada = input("Números: ")
            nums = [float(x) for x in entrada.split()]
            n    = len(nums)

            if n == 0:
                print("Nenhum número digitado!")
            else:
                # Média aritmética
                media = sum(nums) / n

                # Mediana (valor central após ordenar)
                nums_ord = sorted(nums)
                if n % 2 == 1:
                    mediana = nums_ord[n // 2]
                else:
                    mediana = (nums_ord[n//2 - 1] + nums_ord[n//2]) / 2

                # Moda (valor que aparece mais vezes)
                contagem = {}
                for v in nums:
                    contagem[v] = contagem.get(v, 0) + 1
                max_c = max(contagem.values())
                moda  = [v for v, c in contagem.items() if c == max_c]

                # Variância e desvio padrão populacionais
                variancia = sum((x - media)**2 for x in nums) / n
                dp        = raiz(variancia)

                # Amplitude total
                amp = max(nums) - min(nums)

                print(f"\nQuantidade   = {n}")
                print(f"Soma         = {sum(nums)}")
                print(f"Média        = {arred(media, 4)}")
                print(f"Mediana      = {mediana}")
                print(f"Moda         = {moda}")
                print(f"Variância    = {arred(variancia, 4)}")
                print(f"Desvio padrão = {arred(dp, 4)}")
                print(f"Amplitude    = {amp}")
                print(f"Mínimo       = {min(nums)}")
                print(f"Máximo       = {max(nums)}")

        # ---------- [4.4] Matemática Financeira ----------
        elif s_choose == "4":
            print()
            print("[1] Porcentagem")
            print("[2] Juros Simples")
            print("[3] Juros Compostos")
            print("[4] Desconto Simples (comercial)")
            print("[5] Desconto Composto")
            t_fin = input("Escolha: ")

            if t_fin == "1":
                print("[1] Calcular x% de um valor")
                print("[2] Aumento percentual")
                print("[3] Desconto percentual")
                print("[4] Variação percentual entre dois valores")
                t_perc = input("Escolha: ")

                if t_perc == "1":
                    v = float(input("Valor total: "))
                    p = float(input("Porcentagem (%): "))
                    print(f"{p}% de {v} = {arred(v * p / 100, 4)}")

                elif t_perc == "2":
                    v = float(input("Valor original: "))
                    p = float(input("Aumento (%): "))
                    novo = v * (1 + p/100)
                    print(f"Valor após aumento: {arred(novo, 4)}")

                elif t_perc == "3":
                    v = float(input("Valor original: "))
                    p = float(input("Desconto (%): "))
                    novo = v * (1 - p/100)
                    print(f"Valor após desconto: {arred(novo, 4)}")

                elif t_perc == "4":
                    v1 = float(input("Valor inicial: "))
                    v2 = float(input("Valor final: "))
                    if v1 == 0:
                        print("Erro: valor inicial não pode ser zero!")
                    else:
                        var = ((v2 - v1) / v1) * 100
                        sinal = "aumento" if var >= 0 else "redução"
                        print(f"Variação: {arred(abs(var), 2)}% de {sinal}")
                else:
                    print("Não tem essa opção...")

            elif t_fin == "2":
                # J = C * i * t   |   M = C * (1 + i*t)
                c = float(input("Capital inicial (C): "))
                i = float(input("Taxa de juros por período (%): ")) / 100
                t = float(input("Tempo (períodos): "))
                j = c * i * t
                m = c + j
                print(f"Juros    J = {arred(j, 2)}")
                print(f"Montante M = {arred(m, 2)}")

            elif t_fin == "3":
                # M = C * (1 + i)^t
                c = float(input("Capital inicial (C): "))
                i = float(input("Taxa de juros por período (%): ")) / 100
                t = float(input("Tempo (períodos): "))
                m = c * (1 + i)**t
                j = m - c
                print(f"Montante M = {arred(m, 2)}")
                print(f"Juros    J = {arred(j, 2)}")

            elif t_fin == "4":
                # Desconto simples (comercial): D = N * i * t   |   A = N - D
                n_val = float(input("Valor nominal (N): "))
                i     = float(input("Taxa de desconto por período (%): ")) / 100
                t     = float(input("Tempo (períodos): "))
                d     = n_val * i * t
                a     = n_val - d
                print(f"Desconto D = {arred(d, 2)}")
                print(f"Valor atual A = {arred(a, 2)}")

            elif t_fin == "5":
                # Desconto composto: A = N * (1 - i)^t
                n_val = float(input("Valor nominal (N): "))
                i     = float(input("Taxa de desconto por período (%): ")) / 100
                t     = float(input("Tempo (períodos): "))
                a     = n_val * (1 - i)**t
                d     = n_val - a
                print(f"Desconto D = {arred(d, 2)}")
                print(f"Valor atual A = {arred(a, 2)}")
            else:
                print("Não tem essa opção...")
        else:
            print("Não tem essa opção...")


    # ============================================================
    # [5] SAIR
    # ============================================================
    elif f_choose == "5":
        print()
        print("Tchauzinhoo.....")
        break  # sai do while e encerra o programa

    else:
        print()
        print("Não tem essa opção...")