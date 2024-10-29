def procure_pela_chave(caixa_principal):
  pilha = caixa_principal.crie_uma_pilha_para_busca()
  while not pilha.esta_vazia:
    caixa = pilha.pegue_caixa()
    for item in caixa:
      if item.e_uma_caixa():
        pilha.append(item)
      elif item.e_uma_chave():
        print("Achei a chave")

"""

Enquanto o monte existir, pegue uma caixa e olhe o que tem dentro dela.

def procure_pela_chave(caixa_principal):
    # Define a função 'procure_pela_chave' que recebe uma caixa principal como argumento.
    
pilha = caixa_principal.crie_uma_pilha_para_busca()
    # Cria uma pilha para busca a partir da caixa principal, usando o método 'crie_uma_pilha_para_busca'.
    
while not pilha.esta_vazia():  
    # Inicia um loop que continuará enquanto a pilha não estiver vazia.
    
caixa = pilha.pegue_caixa()  
    # Pega a próxima caixa da pilha usando o método 'pegue_caixa' e armazena na variável 'caixa'.
        
for item in caixa:  
    # Inicia um loop para iterar sobre cada item presente na caixa.
        
if item.e_uma_caixa():  
    # Verifica se o item atual é uma caixa, usando o método 'e_uma_caixa'.
            
pilha.adicione(item)  
    # Se o item for uma caixa, adiciona-o à pilha para busca posterior, usando o método 'adicione'.
                
elif item.e_uma_chave():  
    # Verifica se o item atual é uma chave, usando o método 'e_uma_chave'.
            
print("Achei a chave")  
    # Se o item for uma chave, imprime a mensagem "Achei a chave".
                
# Nota: O código assume que as funções como 'crie_uma_pilha_para_busca', 'esta_vazia', 'pegue_caixa', 'adicione', 'e_uma_caixa', e 'e_uma_chave' estão implementadas corretamente em suas respectivas classes.


"""