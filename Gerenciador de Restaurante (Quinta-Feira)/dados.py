# Lista principal
pedidos = []

# Fila FIFO
fila_preparo = []

# Pilha LIFO
pilha_entregues = []

# Contador de ID
contador_id = 1

# Status fixos
status_pedido = (
    "Aguardando",
    "Em Preparo",
    "Entregue"
)

# Prioridades fixas
prioridades = (
    "Baixa",
    "Média",
    "Alta"
)