from dados import pedidos
from dados import fila_preparo
from dados import pilha_entregues
from dados import status_pedido
from dados import prioridades

import dados


# =========================
# CADASTRAR PEDIDO
# =========================
def cadastrar_pedido():

    try:

        mesa = int(input("Número da mesa: "))
        item = input("Nome do item: ").capitalize()
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço do item: R$ "))

        prioridade = input(
            "Prioridade (Baixa/Média/Alta): "
        ).capitalize()

        if prioridade not in prioridades:
            print("\n❌ Prioridade inválida.")
            return

        pedido = {
            "id": dados.contador_id,
            "mesa": mesa,
            "item": item,
            "quantidade": quantidade,
            "preco": preco,
            "prioridade": prioridade,
            "status": status_pedido[0]
        }

        dados.contador_id += 1

        pedidos.append(pedido)

        # FIFO
        fila_preparo.append(pedido)

        print("\n✅ Pedido cadastrado com sucesso!")

    except ValueError:
        print("\n❌ Digite valores válidos.")


# =========================
# LISTAR PEDIDOS
# =========================
def listar_pedidos():

    if len(pedidos) == 0:
        print("\n❌ Nenhum pedido cadastrado.")
        return

    print("\n📋 LISTA DE PEDIDOS")

    for pedido in pedidos:

        print("-" * 50)

        print(f"ID: {pedido['id']}")
        print(f"Mesa: {pedido['mesa']}")
        print(f"Item: {pedido['item']}")
        print(f"Quantidade: {pedido['quantidade']}")
        print(f"Preço: R$ {pedido['preco']:.2f}")
        print(f"Prioridade: {pedido['prioridade']}")
        print(f"Status: {pedido['status']}")

    print("-" * 50)


# =========================
# ATUALIZAR STATUS
# =========================
def atualizar_status():

    try:

        id_pedido = int(input("ID do pedido: "))

        for pedido in pedidos:

            if pedido["id"] == id_pedido:

                # Aguardando -> Em preparo
                if pedido["status"] == status_pedido[0]:

                    pedido["status"] = status_pedido[1]

                    print("\n🍳 Pedido agora está EM PREPARO.")
                    return

                # Em preparo -> Entregue
                elif pedido["status"] == status_pedido[1]:

                    pedido["status"] = status_pedido[2]

                    # Remove da fila FIFO
                    if pedido in fila_preparo:
                        fila_preparo.remove(pedido)

                    # Adiciona na pilha LIFO
                    pilha_entregues.append(pedido)

                    print("\n✅ Pedido ENTREGUE.")
                    return

                else:
                    print("\n⚠️ Pedido já foi entregue.")
                    return

        print("\n❌ Pedido não encontrado.")

    except ValueError:
        print("\n❌ Digite um ID válido.")


# =========================
# MOSTRAR FILA FIFO
# =========================
def mostrar_fila():

    print("\n🍳 FILA DE PREPARO (FIFO)")

    if len(fila_preparo) == 0:
        print("\nNenhum pedido aguardando.")
        return

    for pedido in fila_preparo:

        if pedido["status"] != status_pedido[2]:

            print(
                f"ID {pedido['id']} | "
                f"Mesa {pedido['mesa']} | "
                f"{pedido['item']} | "
                f"Status: {pedido['status']}"
            )


# =========================
# MOSTRAR PILHA LIFO
# =========================
def mostrar_entregues():

    print("\n📦 PEDIDOS ENTREGUES (LIFO)")

    if len(pilha_entregues) == 0:
        print("\nNenhum pedido entregue.")
        return

    for pedido in reversed(pilha_entregues):

        print(
            f"ID {pedido['id']} | "
            f"Mesa {pedido['mesa']} | "
            f"{pedido['item']}"
        )


# =========================
# CANCELAR PEDIDO
# =========================
def cancelar_pedido():

    try:

        id_pedido = int(input("ID do pedido: "))

        for pedido in pedidos:

            if pedido["id"] == id_pedido:

                if pedido in fila_preparo:
                    fila_preparo.remove(pedido)

                pedidos.remove(pedido)

                print("\n🗑️ Pedido cancelado.")
                return

        print("\n❌ Pedido não encontrado.")

    except ValueError:
        print("\n❌ Digite um ID válido.")


# =========================
# TOTAL DA MESA
# =========================
def total_mesa():

    try:

        mesa = int(input("Número da mesa: "))

        total = 0

        for pedido in pedidos:

            if pedido["mesa"] == mesa:

                total += (
                    pedido["preco"] *
                    pedido["quantidade"]
                )

        print(f"\n💰 Total da mesa {mesa}: R$ {total:.2f}")

    except ValueError:
        print("\n❌ Digite uma mesa válida.")


# =========================
# ITENS MAIS PEDIDOS
# =========================
def itens_mais_pedidos():

    print("\n📊 ITENS MAIS PEDIDOS")

    if len(pedidos) == 0:
        print("\nNenhum pedido cadastrado.")
        return

    contador = {}

    for pedido in pedidos:

        item = pedido["item"]

        if item in contador:
            contador[item] += pedido["quantidade"]
        else:
            contador[item] = pedido["quantidade"]

    for item, quantidade in contador.items():

        print(f"{item}: {quantidade} pedidos")