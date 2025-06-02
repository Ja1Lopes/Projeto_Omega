# Bibliotecas usadas
import math
from math import exp
from math import log
import time
import os
from os import sys

# Variáveis matemáticas
pi = float(math.pi)
na = float(6.02214129e23)
k = float(8.62e-5)
r = float(8.31)
# Caminho dos arquivos de texto
caminho = os.environ["HOMEPATH"]
diretorio = "C:" + caminho + "\\Desktop\\"
pasta = diretorio + "ResultadosProjetoOmega\\"

# Recepção do usuário
username = os.environ["USERNAME"]
print(f"Olá {username}.\n")

while True:

    init_Select = input(
        "Selecione sua operação: \n"
        " Estruturas cristalinas (1) \n"
        " Direções e Planos cristalográficos (2) \n"
        " Difração de raios-x (3) \n"
        " Imperfeições (4) \n"
        " Difusão (5) \n"
        # " Propriedades Mecânicas (6) \n"
        " Informações (0) \n"
        " Sair(n) \n"
    )

    if init_Select == "n":
        print("Saindo. Obrigado por usar o app :)")
        time.sleep(1)
        sys.exit()

    if init_Select == "1":

        op_1 = input(
            "Selecione a operação desejada: \n"
            " CS (1) \n"
            " CCC (2) \n"
            " CFC (3) \n"
            " Densidade atômica (4) \n"
            " Alotropia (5) \n"
            " Sair(n) \n"
        )

        if op_1 == "n":
            print("Saindo. Obrigado por usar o app :)")
            time.sleep(1)
            sys.exit()

        if op_1 == "1":

            save_File = input("Deseja salvar os resultados? (s) ou (n) \n")
            if save_File == "s":
                if not os.path.isdir(pasta):
                    os.mkdir(pasta)
                try:
                    file1 = open(pasta + "ResultadosCS.txt", "r+")
                except FileNotFoundError:
                    print("Arquivo não encontrado, criando....")
                    file1 = open(pasta + "ResultadosCS.txt", "w+")
            elif save_File == "n":
                pass

            user_input = input("Parâmetro de rede(a) ou Raio atômico(r)?  ")

            if user_input == "a":
                try:
                    a = float(input("Parametro de rede:  "))
                except ValueError:
                    print("Erro! Insira um valor válido \n")
                    continue

                r = float(a / 2)
                vc = float(a ** 3)
                va = float(4 / 3 * pi * r ** 3)
                n = 1
                fe = float((n * va) / vc)
                print(f"Parâmetro de rede = {a} \n")
                print(f"Raio atômico = {r} \n")
                print(f"Número de átomos que ocupam a célula = {n} \n")
                print(f"Volume unitário = {vc} \n")
                print(f"Volume atômico = {va} \n")
                print(f"Fator de empacotamento = {fe} \n")

            if user_input == "r":
                try:
                    r = float(input("Raio Atomico:  "))
                except ValueError:
                    print("Erro! Insira um valor válido \n")
                    continue

                a = float(2 * r)
                vc = float(8 * r ** 3)
                va = float(4 / 3 * pi * r ** 3)
                n = 1
                fe = float((n * va) / vc)
                print(f"Parâmetro de rede = {a} \n")
                print(f"Raio atômico = {r} \n")
                print(f"Número de átomos que ocupam a célula = {n} \n")
                print(f"Volume unitário = {vc} \n")
                print(f"Volume atômico = {va} \n")
                print(f"Fator de empacotamento = {fe} \n")

            if save_File == "s":
                resultados = list()
                resultados.append("Resultados: \n")
                resultados.append(f"\t Parâmetro de rede = {a} \n")
                resultados.append(f"\t Raio atômico = {r} \n")
                resultados.append(f"\t Número de átomos que ocupam a célula = {n} \n")
                resultados.append(f"\t Volume unitário = {vc} \n")
                resultados.append(f"\t Volume atômico = {va} \n")
                resultados.append(f"\t Fator de empacotamento = {fe} \n")
                file1.writelines(resultados)
                file1.close()

        if op_1 == "2":

            save_File = input("Deseja salvar os resultados? (s) ou (n) \n")
            if save_File == "s":
                if not os.path.isdir(pasta):
                    os.mkdir(pasta)
                try:
                    file2 = open(pasta + "ResultadosCCC.txt", "r+")
                except FileNotFoundError:
                    print("Arquivo não encontrado, criando....")
                    file2 = open(pasta + "ResultadosCCC.txt", "w+")
            elif save_File == "n":
                pass

            user_input = input("Parâmetro de rede(a) ou Raio atômico(r)?  ")

            if user_input == "a":
                try:
                    a = float(input("Parametro de rede:  "))
                except ValueError:
                    print("Erro! Insira um valor válido \n")
                    continue

                r = float((a * 3 ** 0.5) / 4)
                vc = float(a ** 3)
                va = float(4 / 3 * pi * r ** 3)
                n = 2
                fe = float((n * va) / vc)
                print(f"Parâmetro de rede = {a} \n")
                print(f"Raio atômico = {r} \n")
                print(f"Número de átomos que ocupam a célula = {n} \n")
                print(f"Volume unitário = {vc} \n")
                print(f"Volume atômico = {va} \n")
                print(f"Fator de empacotamento = {fe} \n")

            if user_input == "r":
                try:
                    r = float(input("Raio Atomico:  "))
                except ValueError:
                    print("Erro! Insira um valor válido \n")
                    continue

                a = float((4 * r) / 3 ** 0.5)
                vc = float(a ** 3)
                va = float(4 / 3 * pi * r ** 3)
                n = 2
                fe = float((n * va) / vc)
                print(f"Parâmetro de rede = {a} \n")
                print(f"Raio atômico = {r} \n")
                print(f"Número de átomos que ocupam a célula = {n} \n")
                print(f"Volume unitário = {vc} \n")
                print(f"Volume atômico = {va} \n")
                print(f"Fator de empacotamento = {fe} \n")

            if save_File == "s":
                resultados = list()
                resultados.append("Resultados: \n")
                resultados.append(f"\t Parâmetro de rede = {a} \n")
                resultados.append(f"\t Raio atômico = {r} \n")
                resultados.append(f"\t Número de átomos que ocupam a célula = {n} \n")
                resultados.append(f"\t Volume unitário = {vc} \n")
                resultados.append(f"\t Volume atômico = {va} \n")
                resultados.append(f"\t Fator de empacotamento = {fe} \n")
                file2.writelines(resultados)
                file2.close()

        if op_1 == "3":

            save_File = input("Deseja salvar os resultados? (s) ou (n) \n")
            if save_File == "s":
                if not os.path.isdir(pasta):
                    os.mkdir(pasta)
                try:
                    file3 = open(pasta + "ResultadosCFC.txt", "r+")
                except FileNotFoundError:
                    print("Arquivo não encontrado, criando....")
                    file3 = open(pasta + "ResultadosCFC.txt", "w+")
            elif save_File == "n":
                pass

            user_input = input("Parâmetro de rede(a) ou Raio atômico(r)?  ")

            if user_input == "a":
                try:
                    a = float(input("Parametro de rede:  "))
                except ValueError:
                    print("Erro! Insira um valor válido \n")
                    continue

                r = float((2 * a) ** 0.5 / 4)
                vc = float(16 * r ** 3 * (2 ** 0.5))
                va = float(4 / 3 * pi * r ** 3)
                n = 4
                fe = float((n * va) / vc)
                print(f"Parâmetro de rede = {a} \n")
                print(f"Raio atômico = {r} \n")
                print(f"Número de átomos que ocupam a célula = {n} \n")
                print(f"Volume unitário = {vc} \n")
                print(f"Volume atômico = {va} \n")
                print(f"Fator de empacotamento = {fe} \n")

            if user_input == "r":
                try:
                    r = float(input("Raio Atomico:  "))
                except ValueError:
                    print("Erro! Insira um valor válido \n")
                    continue

                a = float(2 * r * (2 ** 0.5))
                vc = float(16 * r ** 3 * (2 ** 0.5))
                va = float(4 / 3 * pi * r ** 3)
                n = 4
                fe = float((n * va) / vc)
                print(f"Parâmetro de rede = {a} \n")
                print(f"Raio atômico = {r} \n")
                print(f"Número de átomos que ocupam a célula = {n} \n")
                print(f"Volume unitário = {vc} \n")
                print(f"Volume atômico = {va} \n")
                print(f"Fator de empacotamento = {fe} \n")

            if save_File == "s":
                resultados = list()
                resultados.append("Resultados: \n")
                resultados.append(f"\t Parâmetro de rede = {a} \n")
                resultados.append(f"\t Raio atômico = {r} \n")
                resultados.append(f"\t Número de átomos que ocupam a célula = {n} \n")
                resultados.append(f"\t Volume unitário = {vc} \n")
                resultados.append(f"\t Volume atômico = {va} \n")
                resultados.append(f"\t Fator de empacotamento = {fe} \n")
                file3.writelines(resultados)
                file3.close()

        if op_1 == "4":

            save_File = input("Deseja salvar os resultados? (s) ou (n) \n")
            if save_File == "s":
                if not os.path.isdir(pasta):
                    os.mkdir(pasta)
                try:
                    file4 = open(pasta + "ResultadosDensiAtom.txt", "r+")
                except FileNotFoundError:
                    print("Arquivo não encontrado, criando....")
                    file4 = open(pasta + "ResultadosDensiAtom.txt", "w+")
            elif save_File == "n":
                pass

            try:
                n = float(input("Numero de átomos:  \n"))
                a = float(input("Peso atômico:  \n"))
            except ValueError:
                print("Erro! Insira um valor válido \n")
                continue

            if n == 1:
                tipo_celula = "CS"

            elif n == 2:
                tipo_celula = "CCC"

            elif n == 4:
                tipo_celula = "CFC"

            elif n == 3:
                tipo_celula = "HS"

            elif n == 6:
                tipo_celula = "HC"

            user_input = input(
                "Qual valor deseja calcular?  \n"
                " Densidade (1) \n"
                " Volume unitário (2) \n"
            )

            if user_input == "1":
                try:
                    vc = float(input("Volume unitário (pm):  \n"))
                except ValueError:
                    print("Erro! Insira um valor válido \n")
                    continue

                p = float((n * a) / (vc * na))
                print(f"Número de átomos = {int(n)} \n")
                print(f"Tipo de célula: {tipo_celula} \n")
                print(f"Peso atômico = {a} \n")
                print(f"Densidade atômica (g/cm³) = {p} \n")
                print(f"Volume unitário (pm) = {vc} \n")
                print(f"Número de Avogadro = {na} \n")

            if user_input == "2":
                try:
                    p = float(input("Densidade atômica (g/cm³):  \n"))
                except ValueError:
                    print("Erro! Insira um valor válido \n")
                    continue

                vc = float(((n * a) / p) / na)
                print(f"Número de átomos = {int(n)} \n")
                print(f"Tipo de célula: {tipo_celula} \n")
                print(f"Peso atômico = {a} \n")
                print(f"Densidade atômica (g/cm³) = {p} \n")
                print(f"Volume unitário (pm) = {vc} \n")
                print(f"Número de Avogadro = {na} \n")

            if save_File == "s":
                resultados = list()
                resultados.append("Resultados: \n")
                resultados.append(f"\t Número de átomos = {n} \n")
                resultados.append(f"\t Tipo de célula: {tipo_celula} \n")
                resultados.append(f"\t Peso atômico = {a} \n")
                resultados.append(f"\t Densidade atômica = {p} \n")
                resultados.append(f"\t Volume unitário = {vc} \n")
                resultados.append(f"\t Número de Avogadro = {na} \n")
                file4.writelines(resultados)
                file4.close()

        if op_1 == "5":

            alotropia = """
    METAL	         ESTRUTURA TEMP AMBIENTE	        EM OUTRAS TEMPERATURAS
    Calcio(Ca)	            CFC	                           CCC(> 447°C)
    Cobalto(Co)	            HC	                           CFC(> 927°C)
    Háfnio(Hf)	            HC	                           CFC(> 1742°C)
    Ferro(Fe)	            CCC	                           CFC(912-1394°C)/CCC(> 1394°C)
    Lítio(Li)	            CCC	                           HC(< -193°C)
    Sódio(Na)	            CCC	                           HC(< -233°C)
    Tálio(Tl)	            HC	                           CCC(> 234°C)
    Titânio(Ti)	            HC	                           CCC(> 883°C)
    Ítrio(Y)	            HC	                           CCC(> 1481°C)
    Zirconio(Zr)	            HC	                           CCC(> 872°C)
    """

            print(alotropia)
            save_File = input("Deseja salvar a tabela? (s) ou (n) \n")
            if save_File == "s":
                if not os.path.isdir(pasta):
                    os.mkdir(pasta)
                try:
                    file5 = open(pasta + "Tabela Alotropia.txt", "r+")
                except FileNotFoundError:
                    print("Arquivo não encontrado, criando.... \n")
                    file5 = open(pasta + "Tabela Alotropia.txt", "w+")
                file5.writelines(alotropia)
                file5.close()
            elif save_File == "n":
                print("\n")
                pass

    if init_Select == "2":
        op_2 = input(
            "Selecione a operação desejada: \n"
            " Conversão sistema Miller(cristais hexagonais) (1) \n"
            " Passo a passo para determinação do Índice de Miller (2) \n"
            " Densidade linear e planar (3) \n"
            " Sair(n) \n"
        )

        if op_2 == "n":
            print("Saindo. Obrigado por usar o app :)")
            time.sleep(1)
            sys.exit()

        if op_2 == "1":
            op_3 = input(
                "Miller para Miller-Bravais (1) \n" "Miller-Bravais para Miller (2) \n"
            )
            if op_3 == "1":
                op_4 = input("[UVW] (1) \n" "(hkl) (2) \n")
                if op_4 == "1":
                    try:
                        user_input = input(
                            "Digite os valores em ordem: U,V,W. Ex: 1,1,1 \n"
                        )
                    except ValueError:
                        print("Erro! Insira um valor válido \n")
                        continue
                    u, v, w = user_input.split(",")

                    u = float(u)
                    v = float(v)
                    w = float(w)

                    u_ = (2 * u - v) / 3
                    v_ = (2 * v - u) / 3
                    t_ = -(u_ + v_)
                    w_ = w

                    u_ = int(u_)
                    v_ = int(v_)
                    w_ = int(w_)
                    t_ = int(t_)

                    u_ = str(u_)
                    v_ = str(v_)
                    w_ = str(w_)
                    t_ = str(t_)

                    print("[UVWT] = [{} {} {} {}]".format(u_, v_, w_, t_), "\n")

                if op_4 == "2":
                    try:
                        user_input = input(
                            "Digite os valores em ordem: h,k,l. Ex: 1,1,1 \n"
                        )
                    except ValueError:
                        print("Erro! Insira um valor válido \n")
                        continue

                    h, k, l = user_input.split(",")

                    h = float(h)
                    k = float(k)
                    l = float(l)

                    h_ = h
                    k_ = k
                    l_ = l
                    i_ = -(h + k)

                    h_ = int(h_)
                    k_ = int(k_)
                    l_ = int(l_)
                    i_ = int(i_)

                    h_ = str(h_)
                    k_ = str(k_)
                    l_ = str(l_)
                    i_ = str(i_)

                    print("(hkli) = ({} {} {} {})".format(h_, k_, l_, i_), "\n")

            if op_3 == "2":
                op_5 = input("[UVWT] (1) \n" "(hkli) (2) \n")
                if op_5 == "1":
                    try:
                        user_input = input(
                            "Digite os valores em ordem: U,V,W,T. Ex: 1,1,1,1 \n"
                        )
                    except ValueError:
                        print("Erro! Insira um valor válido \n")
                        continue

                    u, v, w, t = user_input.split(",")

                    u = float(u)
                    v = float(v)
                    w = float(w)
                    t = float(t)

                    u_ = u - t
                    v_ = v - t
                    w_ = w

                    u_ = int(u_)
                    v_ = int(v_)
                    w_ = int(w_)

                    u_ = str(u_)
                    v_ = str(v_)
                    w_ = str(w_)

                    print("[UVW] = [{} {} {}]".format(u_, v_, w_), "\n")

                if op_5 == "2":
                    try:
                        user_input = input(
                            "Digite os valores em ordem: h,k,l,i. Ex: 1,1,1,1 \n"
                        )
                    except ValueError:
                        print("Erro! Insira um valor válido \n")
                        continue

                    h, k, l, i = user_input.split(",")

                    h = float(h)
                    k = float(k)
                    l = float(l)
                    i = float(i)

                    h_ = h
                    k_ = k
                    l_ = l

                    h_ = int(h_)
                    k_ = int(k_)
                    l_ = int(l_)

                    h_ = str(h_)
                    k_ = str(k_)
                    l_ = str(l_)

                    print("(hkl) = ({} {} {})".format(h_, k_, l_), "\n")

        if op_2 == "2":

            ind_miller = """
    1. Se o plano passar através da selecionada origem, quer um outro plano paralelo deve ser
    construído dentro da célula unitária por uma apropriada translação, quer uma nova
    origem deve ser estabelecida no canto de uma outra célula unitária.

    2. Neste ponto o plano cristalográfico ou intersectará ou ficará paralelo a cada um dos 3 eixos;
    o comprimento da interseção planar para cada eixo é determinado em termos dos
    parâmetros da rede a, b e c.

    3. Os recíprocos destes números são tomados. Um plano que seja paralelo a um eixo pode ser
    considerado como um intercepto infinito, e, portanto, um índice zero.

    4. Se necessário, estes 3 números são mudados para resultar o conjunto dos mínimos inteiros por
    multiplicação ou divisão usando um fator comum.

    5. Finalmente, os índices inteiros, não separados por vírgulas, são colocados dentro de
    parêntesis, assim: (hkl). \n"""

            print(ind_miller)

        if op_2 == "3":
            op_6 = input("Linear(l) ou Planar(p) \n")
            if op_6 == "l":
                try:
                    n = float(input("Número de átomos sobre o vetor de direção: \n"))
                    ar = float(input("Comprimento do vetor de direção: \n"))
                except ValueError:
                    print("Erro! Insira um valor válido \n")
                    continue

                dl = n / ar
                print("Densidade linear = ", dl)
            if op_6 == "p":
                try:
                    n = float(input("Número de átomos no plano: \n"))
                    a = float(input("Area do plano: \n"))
                except ValueError:
                    print("Erro! Insira um valor válido \n")
                    continue

                dp = n / a
                print("Densidade planar = ", dp)

    if init_Select == "3":
        op_7 = input(
            "Selecione a operação desejada: \n"
            " Lei de Bragg (1) \n"
            " Dhkl (2) \n"
            " Sair(n) \n"
        )

        if op_7 == "n":
            print("Saindo. Obrigado por usar o app :)")
            time.sleep(1)
            sys.exit()

        if op_7 == "1":
            save_File = input("Deseja salvar os resultados? (s) ou (n) \n")
            if save_File == "s":
                if not os.path.isdir(pasta):
                    os.mkdir(pasta)
                try:
                    file6 = open(pasta + "ResultadosLeideBragg.txt", "r+")
                except FileNotFoundError:
                    print("Arquivo não encontrado, criando....")
                    file6 = open(pasta + "ResultadosLeideBragg.txt", "w+")
            elif save_File == "n":
                pass

            print("Defina o valor desejado como 0 para calcular\n")
            try:
                alfa = float(input("Alfa(nm): \n"))
                alfa = alfa * (10 ** -10)
                teta = float(input("Teta: \n"))
                n = float(input("Ordem de difração: \n"))
                d = float(input("Dhkl: \n"))
            except ValueError:
                print("Erro! Insira um valor válido \n")
                continue
            rad_teta = math.radians(teta)
            sin_teta = math.sin(rad_teta)
            if teta == 0:
                sin_teta = (n * alfa) / (2 * d)
                teta = math.degrees(sin_teta)
            elif n == 0:
                n = (2 * d * sin_teta) / alfa
            elif d == 0:
                d = (n * alfa) / (2 * sin_teta)
            print(f"Alfa(nm) = {alfa}")
            print(f"Teta(graus) = {teta:.0f}°")
            print(f"Seno de teta = {sin_teta:.6f}")
            print(f"Ordem de difração = {int(n)}")
            print(f"Dhkl = {d}")
            if save_File == "s":
                resultados = list()
                resultados.append("Resultados: \n")
                resultados.append(f"\t Alfa(nm) = {alfa} \n")
                resultados.append(f"\t Teta(graus) = {teta:.0f}° \n")
                resultados.append(f"\t Sena de teta = {sin_teta:.6f} \n")
                resultados.append(f"\t Ordem de difração = {int(n)} \n")
                resultados.append(f"\t Dhkl = {d} \n")
                file6.writelines(resultados)
                file6.close()

        if op_7 == "2":
            save_File = input("Deseja salvar os resultados? (s) ou (n) \n")
            if save_File == "s":
                if not os.path.isdir(pasta):
                    os.mkdir(pasta)
                try:
                    file7 = open(pasta + "ResultadosDhkl.txt", "r+")
                except FileNotFoundError:
                    print("Arquivo não encontrado, criando....")
                    file7 = open(pasta + "ResultadosDhkl.txt", "w+")
            elif save_File == "n":
                pass
            print("Defina o valor desejado como 0 para calcular \n")
            try:
                a = float(input("Parâmetro de rede: \n"))
                h = float(input("h: \n"))
                k = float(input("k: \n"))
                l = float(input("l: \n"))
                d = float(input("Dhkl: \n"))
            except ValueError:
                print("Erro! Insira um valor válido \n")
                continue
            if a == 0:
                a = d * math.sqrt(h ** 2 + k ** 2 + l ** 2)
            elif d == 0:
                d = a / math.sqrt(h ** 2 + k ** 2 + l ** 2)
            print(f"Parâmetro de rede = {a}")
            print(f"Índices de Miller = ({int(h)}{int(k)}{int(l)})")
            print(f"Dhkl = {d}")
            if save_File == "s":
                resultados = list()
                resultados.append("Resultados: \n")
                resultados.append(f"\t Parâmetro de rede = {a} \n")
                resultados.append(
                    f"\t Índices de Miller = ({int(h)}{int(k)}{int(l)}) \n"
                )
                resultados.append(f"\t Dhkl = {d} \n")
                file7.writelines(resultados)
                file7.close()

    if init_Select == "4":
        op_8 = input(
            "Selecione a operação desejada: \n"
            " Cálculo de vacâncias (1) \n"
            " Cálculo de sítios atômicos (2) \n"
            " Tamanho de grão (3) \n"
            " Sair(n) \n"
        )

        if op_8 == "1":
            save_File = input("Deseja salvar os resultados? (s) ou (n) \n")
            if save_File == "s":
                if not os.path.isdir(pasta):
                    os.mkdir(pasta)
                try:
                    file8 = open(pasta + "ResultadosVacancia.txt", "r+")
                except FileNotFoundError:
                    print("Arquivo não encontrado, criando....")
                    file8 = open(pasta + "ResultadosVacancia.txt", "w+")
            elif save_File == "n":
                pass
            try:
                qv = float(
                    input("Energia necessária para formação de vacância (Qv): \n")
                )
                n = float(input("Número de sítios atômicos (N): \n"))
                t = float(input("Temperatura absoluta (K): \n"))
            except ValueError:
                print("Erro! Insira um valor válido \n")
                continue
            nv = n * exp(-(qv) / (k * t))
            print(f"Número de sítios atômicos = {n} atomos/m³ \n")
            print(f"Número de vacâncias = {nv} vacancias/m³ \n")
            print(f"Energia necessária para formação de vacância = {qv} eV/atomo \n")
            print(f"Temperatura abosluta = {t}K \n")
            print(f"Constante de Boltzmann = {k} eV/K \n")
            print("Não esqueça que para metais: Nv/N ~ 10^-4")
            if save_File == "s":
                resultados = list()
                resultados.append("Resultados: \n")
                resultados.append(f"\t Número de sítios atômicos = {n} atomos/m³ \n")
                resultados.append(f"\t Número de vacâncias = {nv} vacancias/m³ \n")
                resultados.append(
                    f"\t Energia necessária para formação de vacância = {qv} eV/atomo \n"
                )
                resultados.append(f"\t Temperatura abosluta = {t}K \n")
                resultados.append(f"\t Constante de Boltzmann = {k} eV/K \n")
                resultados.append("\t Não esqueça que para metais: Nv/N ~ 10^-4")
                file8.writelines(resultados)
                file8.close()

        if op_8 == "2":
            save_File = input("Deseja salvar os resultados? (s) ou (n) \n")
            if save_File == "s":
                if not os.path.isdir(pasta):
                    os.mkdir(pasta)
                try:
                    file9 = open(pasta + "ResultadosSitosAtomicos.txt", "r+")
                except FileNotFoundError:
                    print("Arquivo não encontrado, criando....")
                    file9 = open(pasta + "ResultadosSitiosAtomicos.txt", "w+")
            elif save_File == "n":
                pass
            try:
                d = float(input("Densidade na temperatura dada em g/m³ (d): \n"))
                m = float(input("Massa atômica g/mol (M): \n"))
            except ValueError:
                print("Erro! Insira um valor válido \n")
                continue
            n = (na * d) / m
            print(f"Número de sítios atômicos = {n} atomos/m³ \n")
            print(f"Densidade = {d} g/m³ \n")
            print(f"Massa atômica = {m} g/mol \n")
            print(f"Número de avogrado = {na} atomos/mol \n")
            if save_File == "s":
                resultados = list()
                resultados.append("Resultados: \n")
                resultados.append(f"\t Número de sítios atômicos = {n} atomos/m³ \n")
                resultados.append(f"\t Densidade = {d} g/m³ \n")
                resultados.append(f"\t Massa atômica = {m} g/mol \n")
                resultados.append(f"\t Número de avogrado = {na} atomos/mol \n")
                file9.writelines(resultados)
                file9.close()

        if op_8 == "3":
            save_File = input("Deseja salvar os resultados? (s) ou (n) \n")
            if save_File == "s":
                if not os.path.isdir(pasta):
                    os.mkdir(pasta)
                try:
                    file9 = open(pasta + "ResultadosGraos.txt", "r+")
                except FileNotFoundError:
                    print("Arquivo não encontrado, criando....")
                    file9 = open(pasta + "ResultadosGraos.txt", "w+")
            elif save_File == "n":
                pass
            try:
                print("Defina o valor desejado como 0 para calcular \n")
                n = float(input("Número de grãos/pol² em 100x de aumento (N): \n"))
                g = float(input("Número de tamanho de grão (G): \n"))
            except ValueError:
                print("Erro! Insira um valor válido \n")
                continue
            if n == 0:
                n = 2 ** (g - 1)
            if g == 0:
                g = ((log(n)) / (log(2))) + 1

            print(f"Número de grãos/pol² em 100x aumento = {n} graos/pol² \n")
            print(f"Número de tamanho de grão = {g} \n")

            if save_File == "s":
                resultados = list()
                resultados.append("Resultados: \n")
                resultados.append(
                    f"\t Número de grãos/pol² em 100x aumento = {n} graos/pol² \n"
                )
                resultados.append(f"\t Número de tamanho de grão = {g} \n")
                file9.writelines(resultados)
                file9.close()

        if op_8 == "n":
            print("Saindo. Obrigado por usar o app :)")
            time.sleep(1)
            sys.exit()

    if init_Select == "5":
        op_9 = input(
            "Selecione a operação desejada \n"
            " Fluxo de difusão (1) \n"
            " Coeficiente de difusão (2) \n"
        )

        if op_9 == "1":
            try:
                d = float(input("Coeficiente de difusão (D): \n"))
                dcdx = float(input("Gradiente de concentração (dC/dX): \n"))
            except ValueError:
                print("Erro! Insira um valor válido \n")
                continue

            j = -d * dcdx
            print(f"O fluxo de difusão(J) é: {j}kg/m²s \n")

        if op_9 == "2":
            try:
                d0 = float(
                    input(
                        "Constante pré-exponencial independente da temperatura(D0): \n"
                    )
                )
                qd = float(input("Energia de ativação para a difusão(Qd): \n"))
                t = float(input("Temperatura absoluta(K): \n"))
            except ValueError:
                print("Erro! Insira um valor válido \n")
                continue

            d = d0 * exp((-qd) / (r * t))
            print(f"O coeficiente de difusão é: {d}m²s \n")

    if init_Select == "0":
        print(
            "Dev: João Pedro Lopes \n"
            "GitHub: ja1-lopes \n"
            "Contato: Telegram(@ja1_lopes) E-mail(lopes_230202@outlook.com) \n"
        )
