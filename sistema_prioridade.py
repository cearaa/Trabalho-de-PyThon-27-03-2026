#O mini projeto foi feito por:
#Tárik Moussa Alma - RM: 571411
#Fábricio Aquiles - RM: 570985
#Giovanne Dias - RM: 569750

#Entrada de dados
severidade_do_problema = int(input("Dígite a severidade do problema (1 a 3): "))
quantidade_de_horas = int(input("Digíte a quantas horas o chamado está em aberto: "))
usuarios_afetados = int(input("Digíte a quantidade de usuários afetados pelo prbloema: "))
ambiente = input("Digite o ambiente (produção ou teste): ").lower()

#Classificação de prioridades
if severidade_do_problema == 3 and ambiente == "produção":
    prioridade = "Prioridade Crítica"
elif severidade_do_problema == 3 and usuarios_afetados > 100:
    prioridade = "Prioridade Alta"
elif severidade_do_problema == 2 and quantidade_de_horas > 4:
    prioridade = "Prioridade Média"
else:
    prioridade = "Prioridade Baixa"


