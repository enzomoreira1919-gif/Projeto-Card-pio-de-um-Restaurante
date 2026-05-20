# 🍽️ Gerenciador de Restaurante

Projeto desenvolvido em Python para gerenciamento de pedidos de restaurante.

## 📚 Conceitos Utilizados

### ✅ Fila FIFO

A fila FIFO (First In, First Out) funciona como uma fila normal:
o primeiro pedido que entra é o primeiro a ser preparado.

No projeto, a fila de preparo utiliza:

```python
fila_preparo.append(pedido)
```

e

```python
fila_preparo.remove(pedido)
```

---

### ✅ Pilha LIFO

A pilha LIFO (Last In, First Out) funciona como uma pilha de pratos:
o último pedido entregue aparece primeiro.

No projeto:

```python
pilha_entregues.append(pedido)
```

e

```python
reversed(pilha_entregues)
```

---

### ✅ Dicionário

Cada pedido é armazenado em um dicionário:

```python
pedido = {
    "id": 1,
    "mesa": 5,
    "item": "Pizza",
    "quantidade": 2
}
```

---

### ✅ Lista e Tupla

As listas armazenam pedidos dinamicamente:

```python
pedidos = []
```

As tuplas armazenam valores fixos:

```python
status_pedido = (
    "Aguardando",
    "Em Preparo",
    "Entregue"
)
```

---

### ✅ Modularização

O sistema foi dividido em arquivos:

- `main.py`
- `dados.py`
- `tarefas.py`
- `utils.py`

Cada arquivo possui uma responsabilidade específica.

---

# ⚙️ Funcionalidades

- Cadastro de pedidos
- Listagem de pedidos
- Atualização de status
- Cancelamento de pedidos
- Fila FIFO
- Pilha LIFO
- Total da mesa
- Itens mais pedidos
- Tratamento de erros

---

# ▶️ Como executar

Necário possuir Python 3.10 ou superior.

Execute:

```bash
python main.py
```

Não é necessário instalar bibliotecas externas.

---

# 💡 Dificuldades e Aprendizados

Durante o desenvolvimento do projeto tivemos dificuldades em organizar corretamente a lógica da fila FIFO e da pilha LIFO. Também foi necessário aprender como dividir o sistema em vários arquivos utilizando modularização.

Aprendemos a trabalhar com listas, dicionários, tuplas e funções em Python. Além disso, entendemos a importância do tratamento de erros utilizando try/except para evitar falhas no programa.

O projeto ajudou bastante no entendimento das estruturas de dados estudadas em aula e mostrou como elas funcionam em um sistema real.