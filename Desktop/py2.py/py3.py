import pyautogui as py
import time as ts
import webbrowser
import pywhatkit
import pyperclip
import re

print("Roteiro turistico iniciado")

nome = input("Nome do cliente: ").strip()
nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
cidade = input("Cidade destino: ").strip()
ida = input("Data da ida (DD/MM/AAAA): ").strip()
volta = input("Data da volta (DD/MM/AAAA): ").strip()
telefone = input("Telefone (+5511123456789): ").strip()

print(f"\n Dados coletados: {nome} indo para {cidade}")

prompt = f"""Crie um roteiro turístico completo e pRofissional para:

Cliente: {nome}
Destino: {cidade}
Data de ida: {ida}
Data de volta: {volta}
Formato:
1. "Olá, Sr(a). {nome}!"
2. Data da viagem de ida: {ida}
3. Data da volta: {volta}
4. Principais pontos turísticos (3 principais)
5. Roteiro explicativo dia a dia
6. Sugestao de roupas por clima
7. Dicas finais
Responda apenas com o roteiro do jeito que esta ai, sem explicações extras, não precisa Cliente:, nao inclua a palavra cliente na resposta"""

print("\n Abrindo inteligencia artificial...")
webbrowser.open("https://gemini.google.com")
ts.sleep(10)
py.hotkey('ctrl', 'a')
ts.sleep(0.5)
pyperclip.copy(prompt)
py.hotkey('ctrl', 'v')
ts.sleep(1)
py.press('enter')

print("Aguardando IA gerar roteiro (40s)...")
ts.sleep(35)

print("Copiando resposta...")
py.scroll(-1000000)
ts.sleep(4)
py.click(739, 741)
ts.sleep(2)
py.hotkey('alt', 'tab')
py.sleep(2)

textogemini = pyperclip.paste().strip()

if len(textogemini) <100:
    textogemini = f"""Olá, Sr(a). {nome}!

Data da Viagem (ida): {ida}
Data da Volta: {volta}

Principais pontos turísticos de {cidade}:
1. 
2. 
3. 

Roteiro dos dias:
Dia 1: 
Dia 2: 

Roupas recomendadas:"""

print("Roteiro gerado:")
print(textogemini)

enviar = input("\nDeseja enviar no WhatsApp? (s/n): ").lower()

if enviar == "s":
    try:
        print("Enviando WhatsApp...")
        pywhatkit.sendwhatmsg_instantly(
            telefone,
            textogemini,
        )
        ts.sleep(3)
        py.click(1862, 975)
        ts.sleep(1)
        py.hotkey('alt', 'tab')
        print("Mensagem enviada")
        print(f"para: {telefone}")
    except Exception as e:
        print(f"Erro WhatsApp: {e}")
else:
    print("Envio cancelado.")
print("\nRoteiro concluido")
input("Pressione ENTER para sair.")
