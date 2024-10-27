def pesquisa_binaria(lista, item):
  baixo = 0 #1
  alto = len(lista) - 1 #1

  while baixo <= alto: #2
    meio = (baixo + alto) // 2 #3
    chute = lista[meio]
    if chute == item: #4
      return meio
    if chute > item: #5
      alto = meio - 1
    else: #6
      baixo = meio + 1
  return None #7

minha_lista = [1, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista, 3))
print(pesquisa_binaria(minha_lista, -1))

'''

1. baixo e alto acompanham a parte da lista que você está procurando.
2. Enquanto ainda não conseguiu chegar a um único elemento...
3. ...Verifica o elemento central.
4. Acha o item.
5. O chute foi muito alto.
6. O chute foi muito baixo.
7. O item não existe.

'''