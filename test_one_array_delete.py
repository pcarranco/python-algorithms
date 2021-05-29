
# ________________________ ELIMINAR ELEMENTO DE UN ARREGLO ___________________




def deletenum(index):
    scores = [90,70,50,80,60,85]

    temparr = [0 for _ in range(len(scores)-1)]

    for i in range(0, len(scores)):
        if i < index:
            temparr[i] = scores[i]
        elif i > index:
            temparr[i-1] = scores[i] 
            
    print(temparr)
    
    
if __name__ == '__main__':
    deletenum(2)