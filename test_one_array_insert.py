
# ________________________ INSERTAR NUEVO ELEMENTO EN UN ARREGLO __________________

# Nota: Al insertar un elemento este debe de ir el una posición intermedia, ni al
# principio, ni al final




def insertnew(new,index):
    scores = [90,70,50,80,60,85]

    temparr = [0 for _ in range(len(scores)+1)]

    for i in range(len(scores)):
        if i < index:
            temparr[i] = scores[i]  
        else:
            temparr[i+1] = scores[i]

        temparr[index] = new
    print(temparr)
    
    
if __name__ == '__main__':
    insertnew(75,2)