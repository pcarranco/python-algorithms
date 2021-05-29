
# ___________________ ALGORITMO PARA ORDENAR ____________________________
# Se asume que el primer valor es el más bajo y se compara con el resto de
# valores en el arreglo en busca del valor minimo, una vez encontrado 
# se coloca en la primera posición, el valor que anteriormente estaba en la 
# primera posición se coloca en la posicion anterior del valor mínimo, se 
# realiza el mismo procedimiento por cada numero hasta que ya no se ralice
# ningun cambio.


bubbles = [60,80,95,50,70]

def sorts(arr):
    c = 0
    change = True
    while change:
        change = False
        minindex = c
        for i in range(minindex,len(arr)-1):
            
            if arr[minindex] > arr[i+1]:
                minindex = i+1
                change = True    
        
        val = arr[c]
        arr[c] = arr[minindex]
        arr[minindex] = val
        
        c+= 1
        
        
    print(arr)
    

if __name__ == '__main__':
    sorts(bubbles)