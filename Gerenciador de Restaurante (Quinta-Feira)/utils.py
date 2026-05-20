import os


def linha():
    print("=" * 50)


def titulo(texto):
    linha()
    print(f"{texto:^50}")
    linha()


def pausar():
    input("\nPressione ENTER para continuar...")


def limpar():
    os.system("cls")