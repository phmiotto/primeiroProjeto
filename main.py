import pandas as pd
from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "ACb20e078924792094a6d816c782f491fa"
auth_token  = "8bcc03e1481edb742047cd1ec88c08b3"

client = Client(account_sid, auth_token)



lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for c in lista_meses:
    tabela_vendas = pd.read_excel(f"{c}.xlsx")                                          
    if (tabela_vendas["Vendas"] > 55000).any():                                         
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]       
        total_vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"].values[0]
        print(f"No mês de {c}, o vendedor {vendedor} vendeu R$ {total_vendas:,}")   
        message = client.messages.create(
            to="+5511*********",
            from_="+16282775712",
            body=f"No mês de {c}, o vendedor {vendedor} vendeu R$ {total_vendas:,}")
        print(message.sid)      



                                                                                 
