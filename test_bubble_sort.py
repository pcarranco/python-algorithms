from array import array

# _________________________ ALGORITMO PARA ORDENAR _____________________________
# Revisa el primer elemento con el segundo y en dado caso de que el primero sea 
# mayor los intercambia, después continua comparando el segundo con el tercero y 
# asi sucesivamente hasta que no tenga se tenga que realizar ningun cambio


# Nota: En este algorimo se compara con el siguiente numero consecutivo al que
# se esta evaluando

def sort(arr):
    
    change = True
    while change:    
        change = False

        for i in range(0,len(arr)-1):
                         
            if arr[i] > arr[i+1]:
                val = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = val            
                change = True


def main():
    scores = array('i')
    scores = array('i', [5,2,6,4,9,3,7,1,8])

    sort(scores)

    for score in scores:
        print(score, ",", end="")

if __name__ == '__main__':
    main()
