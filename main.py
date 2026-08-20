from datetime import datetime
import pandas as pd
from tabulate import tabulate
import csv
import sys

FILE_NAME = "transactions.csv"

def menu():
    print("==== FINANCE MANAGER ====")
    print("1 - Adicionar Receita")
    print("2 - Adicionar Despesa")
    print("3 - Resumo")
    print("4 - Relatórios")
    print("5 - Sair")

    while True:
        try:
            option = int(input("Digite a opção desejada: "))

            if option in [1, 2, 3, 4, 5]:
                return option

            print("Digite uma opção entre 1 e 5.")

        except ValueError:
            print("Digite apenas números.")

def save_receita(valor, descricao, categoria, categorias, data):
    tipo = "Receita"
    with open(FILE_NAME, "a", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow([data,tipo,descricao,f"{valor:.2f}",categorias[categoria - 1]])


def save_despesa(valor, descricao, categoria, categorias, data, pagamento, qtd_parcelas):
    tipo = "Despesa"
    with open(FILE_NAME, "a", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow([data,tipo,descricao,f"{valor:.2f}",categorias[categoria - 1], pagamento, qtd_parcelas])

def add_receita():
    categorias = [
        "Receitas Fixa", #Salário
        "Receita Variável", #Pagamentos de terceiros
        "Receita Extraordinária" #Presentes, doações
    ]
    data = get_date()
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

    for i, categoria in enumerate(categorias, start=1):
            print(f"{i} - {categoria}")

    while True:
        try:
            categoria = int(input("Categoria: "))
            if 1 <= categoria <= len(categorias):
                break
            print("Categoria inválida")
        except ValueError:
            print("Digite apenas números.")

    if descricao == "":
        descricao = "Sem descrição"

    save_receita(valor, descricao,categoria, categorias, data)

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
    data = get_date()

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
    pagamento = get_payment_method()
    if pagamento == "Crédito":
        while True:
            try:
                qtd_parcelas = int(input("Quantidade de parcelas: "))
                if qtd_parcelas <= 0:
                    print("A quantidade de parcelas deve ser maior que zero.")
                    continue
                break
            except ValueError:
                print("Digite um valor válido.")
    else:
        qtd_parcelas = 1

    save_despesa(valor, descricao, categoria, categorias, data, pagamento, qtd_parcelas)

def show_summary():
    df = create_dataframe()

    if df.empty:
        print("\nNenhuma transação cadastrada.\n")
        return

    receitas = df[df["tipo"] == "Receita"]["valor"].sum()
    despesas = df[df["tipo"] == "Despesa"]["valor"].sum()

    saldo = receitas - despesas

    gastos = (
        df[df["tipo"] == "Despesa"]
        .groupby("categoria")["valor"]
        .sum()
    )

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
        with open(FILE_NAME, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.reader(file, delimiter=";")

            for row in reader:

                if row[1] == "Receita":
                    transactions.append({
                        "data": row[0],
                        "tipo": row[1],
                        "descricao": row[2],
                        "valor": float(row[3]),
                        "categoria": row[4]
                    })

                elif row[1] == "Despesa":
                    transactions.append({
                        "data": row[0],
                        "tipo": row[1],
                        "descricao": row[2],
                        "valor": float(row[3]),
                        "categoria": row[4],
                        "met_pagamento": row[5],
                        "qtd_parcelas": row[6]
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

def get_date():
    while True:
        data = input("Data(DD/MM/AAAA): ")

        try: 
            data = datetime.strptime(data, "%d/%m/%Y").date()
            break
        except ValueError:
            print("Data inválida. Tente novamente.")
    return data

def get_payment_method():
    pagamentos = ["Dinheiro", "Pix", "Débito", "Crédito"]

    while True:
        try:
            for i, pagamento in enumerate(pagamentos, start=1):
                print(f"{i} - {pagamento}")

            opcao = int(input("Forma de pagamento: "))

            if 1 <= opcao <= len(pagamentos):
                return pagamentos[opcao - 1]

            print("Opção inválida.")

        except ValueError:
            print("Digite apenas números.")

def create_dataframe(): #Transformo minha lista de dicionários em um df e converto a "data" de string para data
    transactions = load_transactions()

    df = pd.DataFrame(transactions)

    df["data"] = pd.to_datetime(
    df["data"],
    dayfirst=True,
    errors="coerce"
)

    return df

def get_relatorio():
    while True:
        print("\n1 - Relatório Mensal")
        print("2 - Relatório Anual")

        try:
            opcao = int(input("Opção desejada: "))

        except ValueError:
            print("Digite apenas um número.")
            continue

        if opcao == 1:
            relatorio_mensal()
            break

        elif opcao == 2:
            relatorio_anual()
            break

        else:
            print("Opção inválida. Digite 1 ou 2.")

def relatorio_mensal():
    df = create_dataframe()

    while True:
        try:
            mes = int(input("Digite o mês (1-12): "))
            ano = int(input("Digite o ano: "))

            if mes < 1 or mes > 12:
                print("Mês inválido. Digite um valor entre 1 e 12.")
                continue

            break

        except ValueError:
            print("Digite apenas números.")

    relatorio = df[
        (df["data"].dt.month == mes) &
        (df["data"].dt.year == ano)
    ]

    if relatorio.empty:
        print("\nNão existem transações nesse período.")
        return

    mostrar_relatorio(relatorio, f"RELATÓRIO DE {mes:02d}/{ano}")

def relatorio_anual():
    df = create_dataframe()

    while True:
        try:
            ano = int(input("Digite o ano: "))

            relatorio = df[df["data"].dt.year == ano]

            if relatorio.empty:
                print("\nNão existem transações nesse período.")
                continue

            mostrar_relatorio(relatorio, f"RELATÓRIO DE {ano}")
            return

        except ValueError:
            print("\nDigite um ano válido.")

def mostrar_relatorio(relatorio, titulo):

    print("\n" + "=" * 80)
    print(f"{titulo:^80}")
    print("=" * 80)

    receitas = relatorio.loc[
        relatorio["tipo"] == "Receita", "valor"
    ].sum()

    despesas = relatorio.loc[
        relatorio["tipo"] == "Despesa", "valor"
    ].sum()

    saldo = receitas - despesas

    print(f"\nReceitas: R$ {receitas:.2f}")
    print(f"Despesas: R$ {despesas:.2f}")
    print(f"Saldo:    R$ {saldo:.2f}")

    tabela = relatorio[
        [
            "data",
            "tipo",
            "descricao",
            "valor",
            "categoria",
            "met_pagamento",
            "qtd_parcelas"
        ]
    ].rename(columns={
        "data": "Data",
        "tipo": "Tipo",
        "descricao": "Descrição",
        "valor": "Valor",
        "categoria": "Categoria",
        "met_pagamento": "Pagamento",
        "qtd_parcelas": "Parcelas"
    })

    print(tabulate(
        tabela,
        headers="keys",
        tablefmt="grid",
        showindex=False
    ))

    # Gastos por categoria
    gastos_categoria = (
        relatorio[relatorio["tipo"] == "Despesa"]
        .groupby("categoria")["valor"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n" + "-" * 80)
    print("GASTOS POR CATEGORIA")
    print("-" * 80)

    tabela_categoria = gastos_categoria.reset_index()
    tabela_categoria.columns = ["Categoria", "Total"]

    print(tabulate(
        tabela_categoria,
        headers="keys",
        tablefmt="grid",
        showindex=False,
        floatfmt=".2f"
    ))

def create_file():
    try:
        with open(FILE_NAME, "x", encoding="utf-8-sig") as file:
            pass
    except FileExistsError:
        pass


def main():
    create_file()
    while True:
        option = menu()
        if option == 1:
            add_receita()
        elif option == 2:
            add_despesa()
        elif option == 3:
            show_summary()
        elif option == 4:
            get_relatorio()
        elif option == 5:
            sys.exit("Programa encerrado.")
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()