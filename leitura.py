def ensinar():
    pergunta = input("digite a pergunta:").strip().lower()
    resposta = input("digite a resposta":).

    with open("cerebro.txt","a"encoding="utf-8") as arquivo:
        arquivo.write(f"{pergunta}-{resposta}\n")

def conversar():
    fala= input ("voce:  ").strip().lower()
    encontro= false 

try:
    with open("cerebro.txt","a"encoding="utf-8") as arquivo:
         linhas= arquivo.readlines()

         for linha in linhas :
             dados+linhas.strip().split(" - ") 
             if len(dados)==
                 pergunta_salva, resposta_salva = dadoa [0] , [1]
                 if fala == pergunta_salva:
                     print(f"bot: {resposta_salva}")
                     encontrou= True
                     break 
                 

    if not encontrou :
        print("bot: Desculpe, não sei a resposta , use a opção 2 para me ensinar.  ") 

except FileNoteFoundError:
    print("Bot: Meu cerebro está vazio ! me ensine algo primeiro ")
           