
# ___________________ ALGORITMO VALOR MINIMO _________________________
# Busca el valor minimo dentro de un arreglo de números, iniciando con
# la premisa de que el valor en la primera posicione es el menor, de ahí
# se itera por toda la lista comparando con el valor minimo, en case de 
# encontrar un valor más bajo al que actualmente se considera como el
# menor se actualiza la posicion del valor minimo hasta haber recorrido
# toda la lista.


bubbles = [55,80,96,30,12,45,72,25]


def min_value(arr):
   
    min_index = 0
    
    for i in range(len(arr)-1):
        if arr[min_index] > arr[i+1]:
            min_index = i+1
   
    print(arr[min_index])


if __name__ == '__main__':
    min_value(bubbles)