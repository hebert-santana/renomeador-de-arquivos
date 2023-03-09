import os

print('\n=========== RENOMEADOR DE ARQUIVOS ===========\n')

pasta_original = input("Cole aqui o endereço do diretório desejado: ")
pasta = pasta_original.replace('\\', '/') + '/'

def renomeador():
    i = 0    
    for arquivo in os.listdir(pasta):
        nome_arquivo ="arquivo_" + str(i)
        pesquisa =pasta + arquivo
        nome_arquivo =pasta + nome_arquivo
        os.rename(pesquisa, nome_arquivo)
        i += 1
        
if __name__ == '__main__':
    renomeador()
    
print("\nOs arquivos foram renomeados!\n=========== ====================== ===========\n")