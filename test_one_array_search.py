# _____________________ BUSQUEDA DE UN VALOR EN ARREGLO ____________________

def search(arr,val):
    for i in range(0,len(arr)):
        if (arr[i] == val):
            return i
    return -1

if __name__ == '__main__':
    boubles = [90,70,80,60,85]
    a = search(boubles, 85)
    print(a)