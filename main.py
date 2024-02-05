import pandas as pd
from twilio.rest import Client
#código twilio XB264V4FNFHD1XK533LBZABG

# pandas e openpyxl -> integração do python com Excel
# twilio -> integração do python com SMS

# Passo a passo de solução

# Abrir os 6 arquivos em Excel

# Para cada arquivo:

# Verificar se algum valor na coluna Vendas daquele arquivo é maior de 55.000

# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior do que 55.000 não quero fazer nada

# import pandas as pd -> as pd é uma abreviação de pendas, quando for chamar o pandas no código podemos nos referir como pd


# Your Account SID and Auth Token from console.twilio.com
account_sid = "ACb20e078924792094a6d816c782f491fa"
auth_token  = "8bcc03e1481edb742047cd1ec88c08b3"

client = Client(account_sid, auth_token)



lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for c in lista_meses:
    tabela_vendas = pd.read_excel(f"{c}.xlsx")                                          #tabela_vendas irá ler o arquivo em excel
    if (tabela_vendas["Vendas"] > 55000).any():                                         #.any() = se algum valor na coluna tabela_vendas for maior que 55000
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]       #.loc[linha, coluna] é para localizar uma ou mais linhas da minha tabela
        total_vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"].values[0]
        print(f"No mês de {c}, o vendedor {vendedor} vendeu R$ {total_vendas:,}")   #loc te dá como respota uma tabela, não um valor. .values[0] para pegar apenas o valor
        message = client.messages.create(
            to="+5511992916202",
            from_="+16282775712",
            body=f"No mês de {c}, o vendedor {vendedor} vendeu R$ {total_vendas:,}")
        print(message.sid)      



                                                                                 