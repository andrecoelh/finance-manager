import csv
import sys

def menu():
    print("==== FINANCE MANAGER ====\n")
    print("1 - Adicionar Receita\n")
    print("2 - Adicionar Despesa\n")
    print("3 - Resumo\n")
    print("4 - Sair\n")

    while True:
        try:
            option = int(input("Digite a opção desejada: "))

            if option in [1, 2, 3, 4]:
                return option

            print("Digite uma opção entre 1 e 4.")

        except ValueError:
            print("Digite apenas números.")

def save_receita(valor, descricao):
    tipo = "Receita"
    with open("transactions.csv", "a", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow([tipo,descricao,f"{valor:.2f}"])


def save_despesa(valor, descricao, categoria, categorias):
    tipo = "Despesa"
    with open("transactions.csv", "a", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow([tipo,descricao,f"{valor:.2f}",categorias[categoria - 1]])

def add_receita():
    while True:
        try:
            valor = float(input("Valor: "))

            if valor <= 0:
                print("O valor deve ser maior que zero.")
                continue

            break

        except ValueError:
            print("Digite um valor válido.")

    descricao = input("Descrição: ").strip()

    if descricao == "":
        descricao = "Sem descrição"

    save_receita(valor, descricao)

def add_despesa():

    categorias = [
        "Contas de Consumo",
        "Alimentacao",
        "Transporte",
        "Saude / Bem-estar",
        "Educacao",
        "Lazer / Entretenimento",
        "Vestuario / Cuidados Pessoais",
        "Financeiro / Dividas",
        "Eventuais / Extras"
    ]

    while True:
        try:
            valor = float(input("Valor: "))

            if valor <= 0:
                print("O valor deve ser maior que zero.")
                continue

            break

        except ValueError:
            print("Digite um valor válido.")

    descricao = input("Descrição: ").strip()

    if descricao == "":
        descricao = "Sem descrição"

    print()

    for i, categoria in enumerate(categorias, start=1):
        print(f"{i} - {categoria}")

    while True:
        try:
            categoria = int(input("Categoria: "))

            if 1 <= categoria <= len(categorias):
                break

            print("Categoria inválida.")

        except ValueError:
            print("Digite apenas números.")

    save_despesa(valor, descricao, categoria, categorias)

def show_summary():
    transactions = load_transactions()

    if not transactions:
        print("\nNenhuma transação cadastrada.\n")
        return

    receitas, despesas = calculate_totals(transactions)
    gastos = calculate_category(transactions)

    saldo = receitas - despesas

    print("\n========== RESUMO ==========\n")

    print(f"Receitas:      R$ {receitas:.2f}")
    print(f"Despesas:      R$ {despesas:.2f}")
    print(f"Saldo:         R$ {saldo:.2f}")

    print("\nGastos por categoria:\n")

    for categoria, valor in gastos.items():
        print(f"{categoria:<30} R$ {valor:.2f}")

def load_transactions():
    transactions = []

    try:
        with open("transactions.csv", "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.reader(file, delimiter=";")

            for row in reader:

                if row[0] == "Receita":
                    transactions.append({
                        "tipo": row[0],
                        "descricao": row[1],
                        "valor": float(row[2])
                    })

                elif row[0] == "Despesa":
                    transactions.append({
                        "tipo": row[0],
                        "descricao": row[1],
                        "valor": float(row[2]),
                        "categoria": row[3]
                    })

    except FileNotFoundError:
        return []

    return transactions

def calculate_totals(transactions):
    receitas = 0
    despesas = 0

    for transaction in transactions:
            if transaction["tipo"] == "Receita":
                receitas += transaction["valor"]
            else:
                despesas += transaction["valor"]
    return receitas, despesas

def calculate_category(transactions):
    gastos = {
        "Contas de Consumo": 0,
        "Alimentacao": 0,
        "Transporte": 0,
        "Saude / Bem-estar": 0,
        "Educacao": 0,
        "Lazer / Entretenimento": 0,
        "Vestuario / Cuidados Pessoais": 0,
        "Financeiro / Dividas": 0,
        "Eventuais / Extras": 0
    }

    for transaction in transactions:
        if transaction["tipo"] == "Despesa":
            gastos[transaction["categoria"]] += transaction["valor"]

    return gastos

def main():
    while True:
        option = menu()
        if option == 1:
            add_receita()
        elif option == 2:
            add_despesa()
        elif option == 3:
            show_summary()
        elif option == 4:
            sys.exit("Programa encerrado.")
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()