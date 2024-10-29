def procure_pela_chave(caixa):
  for item in caixa:
    if item.e_uma_caixa():
      procure_pela_chave(item) #Aqui entra a recursão.
    elif item.e_uma_chave():
      print("Achei a chave!")

"""

Recursão é quando uma função chama a sí mesma.

def procure_pela_chave(caixa):
  # Define a função 'procure_pela_chave' que recebe uma caixa como argumento.
    
for item in caixa:
  # Inicia um loop que itera sobre cada item presente na caixa.
    
if item.e_uma_caixa():
  # Verifica se o item atual é uma caixa, usando o método 'e_uma_caixa'.
        
procure_pela_chave(item)  
  # Se o item for uma caixa, chama a função 'procure_pela_chave' recursivamente,
  # passando a caixa atual como argumento. Isso permite a busca em caixas aninhadas.
            
elif item.e_uma_chave():
  # Verifica se o item atual é uma chave, usando o método 'e_uma_chave'.
        
print("Achei a chave!")  
  # Se o item for uma chave, imprime a mensagem "Achei a chave!" indicando que a chave foi encontrada.

"""