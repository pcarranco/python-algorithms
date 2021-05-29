
# __________________________________ ALGORITMO DE ORDENAR __________________________



def sort_insert(arr):

    for i in range(len(arr)-1):
        val = arr[i+1]
        position = i+1
        for j in range(position-1,-1,-1):
            if val <= arr[j]:
                temp = arr[j]
                arr[j]= val
                arr[position] = temp
                position = j
    
    print(arr)
    
if __name__ == '__main__':
    boubles = [80,70,60,50,95]
    sort_insert(boubles)