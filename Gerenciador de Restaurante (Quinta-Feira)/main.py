from tarefas import *
from utils import titulo, pausar, limpar


while True:

    limpar()

    titulo("🍽️ CARDÁPIO RESTAURANTE")

    print("1 - Cadastrar pedido")
    print("2 - Listar pedidos")
    print("3 - Atualizar status")
    print("4 - Mostrar fila de preparo")
    print("5 - Mostrar pedidos entregues")
    print("6 - Cancelar pedido")
    print("7 - Total da mesa")
    print("8 - Itens mais pedidos")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar_pedido()

    elif opcao == "2":
        listar_pedidos()

    elif opcao == "3":
        atualizar_status()

    elif opcao == "4":
        mostrar_fila()

    elif opcao == "5":
        mostrar_entregues()

    elif opcao == "6":
        cancelar_pedido()

    elif opcao == "7":
        total_mesa()

    elif opcao == "8":
        itens_mais_pedidos()

    elif opcao == "0":
        print("\nPrograma encerrado.")
        break

    else:
        print("\n❌ Opção inválida.")

    pausar()