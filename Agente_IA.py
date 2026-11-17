import ollama

instrucao= "Voce e um agente de IA especifico para atender os nossos cliente e fornecedores da ofinca de Mecanica"
print("Agente Pronto !!! Digite 'Sair' para encerrarmos a aplicação")

while True:
    pergunta = input ("\nVocê: ")
    if pergunta == "Sair":
        break

    resposta = ollama.chat(model="llama3.2", messages=[
        {"role": "system", "content": instrucao},
        {"role": "user", "content": pergunta},
    ])
    
    print("Agente:", resposta["message"]["content"])     


