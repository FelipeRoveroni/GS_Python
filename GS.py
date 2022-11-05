from datetime import datetime
import os

print("Olá Seja bem vindo. A seguir escolha uma das Seguintes Opções:")
print("1 – Cadastrar mês de referência\n2 – Exibir dados do mês de referência [pesquisa por mês]\n3 – Relatório comparativo – Referência 2019\n4 – Listar todos os meses cadastrados")

'''
Colocar o Diretorio onde o arquivo python sera executado
'''
path = r"C:\Users\Felipe\Desktop\Global_Solutions\Computational Thinking Using Python\GS_Python"
os.chdir(path)

opcao = int(input("Digite a opção desejada:"))

def escolha():
    if opcao == 1:
        dt = input("Digite o mês e o ano a seguir(EX:05-2022): ")
        th = int(input("Digite o Total de Habitantes:"))
        to = int(input("Agora digite o Total de Obitos:"))
        dados = open(f'{dt}.txt', 'w')
        dados.write(f"Mes e ano: {dt}\nTotal de Habitantes: {th}\nTotal de Obitos: {to}")
        print("***** Gravado com sucesso *****")
    elif opcao == 2:
        dte = input("Digite o mes-ano que deseja consultar: ")
        arquivo = f'{dte}.txt'
        if os.path.isfile(arquivo):
            dados = open(f'{dte}.txt', 'r')
            print(dados.read())
            print("***** Registro encontrado *****")
        else:
            print(" ***** Mês-ano não cadastrado! *****")
    elif opcao == 3:
        ano = input("Digite ano a ser comparado:")
        
    elif opcao == 4:
        print("Itens armazenados dentro do TxT:")
        def read_text_file(file_path): 
            with open(file_path, 'r') as f: 
                print(f.read()) 
        for file in os.listdir(): 
            if file.endswith(".txt"): 
                file_path = f"{path}\{file}"
                read_text_file(file_path)    
escolha()
