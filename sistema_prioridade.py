#O mini projeto foi feito por:
#Tárik Moussa Alma - RM: 571411
#Fábricio Aquiles - RM: 570985
#Giovanne Dias - RM: 569750

#Entrada de dados.
#Severidade
try:
    severidade_do_problema = int(input("Dígite a severidade do problema (1 a 3): "))
except ValueError:
    print("Erro: você deve digitar um número!!")
if severidade_do_problema < 1 or severidade_do_problema > 3:
    print("Erro: severidade inválida!!")
    exit()

#Horas
try:
    quantidade_de_horas = int(input("Digíte a quantas horas o chamado está em aberto: "))
except ValueError:
    print("Erro: você deve digitar um número!!")
if quantidade_de_horas < 0:
    print("Erro: Horas não podem ser negativas!!")

#Usuários afetados
try:
    usuarios_afetados = int(input("Digíte a quantidade de usuários afetados pelo prbloema: "))
except ValueError:
    print("Erro: você deve digitar um número!!")
if usuarios_afetados < 0:
    print("Erro: número de usuários inválido!!")
    exit()

#Ambiente
    ambiente = input("Digite o ambiente (produção ou teste): ").lower()
if ambiente not in ["produção", "teste"]:
    print("Erro: ambiente inválido ")
    exit()


#Validação dos dados
if severidade_do_problema < 1 or severidade_do_problema > 3:
    print("Erro: severidade inválida!!")


#Classificação de prioridades.
if severidade_do_problema == 3 and ambiente == "produção":
    prioridade = "Crítica"
elif severidade_do_problema == 3 and usuarios_afetados > 100:
    prioridade = "Alta"
elif severidade_do_problema == 2 and quantidade_de_horas > 4:
    prioridade = "Média"
else:
    prioridade = "Baixa"

#O que fazer baseado na prioridade.
if prioridade == "Crítica":
    acao = "Acionar plantão imediatamente!!"
elif prioridade == "Alta":
    acao = "Iremos te encaminhar para a equipe responsável."
elif prioridade == "Média":
    acao = "Se regristre e acompanhe."
else:
    acao = "Colocar na fila de atendimento."

#Saída de Dados.
print("\n----Resultado----")
print(f"Prioridade: {prioridade}")
print(f"Ação Recomendada: {acao}")