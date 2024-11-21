import requests

def consultar_cpf(cpf, api_key):
    # URL fictícia da API
    url = "https://ws.hubdodesenvolvedor.com.br/v2/cpf/?cpf=$cpf&data=$data_de_nascimento_formato_pt_br&token=154264630LaJHGyFvgP278520112"
    
    # Parâmetros da requisição
    params = {
        "cpf": cpf,
        "api_key": api_key
    }
    
    try:
        # Enviando a requisição GET para a API
        response = requests.get(url, params=params)
        
        # Verificando se a requisição foi bem-sucedida
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Erro: {response.status_code}")
            return None
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None

def main():
    # CPF a ser consultado
    info = input("Esse é o nosso sistema de Consulta de CPF, digite enter para continuar ")
    cpf = input("Digite o cpf: ")  # Substitua pelo CPF desejado
    
    # Sua chave de API (substitua pelo valor correto)
    api_key = "154264630LaJHGyFvgP278520112"
    
    
    # Consultando o CPF
    resultado = consultar_cpf(cpf, api_key)
    
    if resultado:
        print("Resultado da consulta:")
        print(resultado)
    else:
        print("Não foi possível obter os dados.")

if __name__ == "__main__":
    main()
