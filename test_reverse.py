
# __________________________ ALGORITMO PARA INVERTIR EL ORDEN EN LISTA ________________________
# Con esta funcion se intercambian los valores la primera y ultima posicion, y se repite
# avanzando hacia el centro haste que todos los valores se hallan intercambiado

def invert_oder(arr):
    for i in range(int(round(len(arr)/2,0))):
        temp = arr[i]
        arr[i] = arr[len(arr)-i-1]
        arr[len(arr)-i-1] = temp

    print(arr)
if __name__ == '__main__':
    boubles = [50,60,70,80,90]
    invert_oder(boubles)