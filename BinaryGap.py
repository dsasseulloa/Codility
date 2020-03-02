def gap_binario(N):
    lista=[]
    lista_contadores=[]
    num = (bin(N)[2:])
    contador = 0
    for i in num:
        lista.append(i)

    print(lista)
    print("numero em binario:",num)
    for i in lista:
        if i == '0':
            contador+=1
        if i == '1':
            if contador != 0:
                lista_contadores.append(contador)
                contador=0

    print(f"A quantidade de lacunas binária é de {len(lista_contadores)}")
    if len(lista_contadores) != 0:
        print(f"maior valor e o tamanho da lacuna binária é {max(lista_contadores)}")


    return num

gap_binario(52353453463463)