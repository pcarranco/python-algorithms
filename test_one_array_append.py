
# ______________________ ANEXAR NUEVO ELEMENTO A UN ARREGLO ______________________

# Nota: Se incerta un elemento al final


def appendnew(new):

    scores = [90,70,50,80,60,85]

    temparr = [0 for _ in range(len(scores)+1)]

    for i in range(0,len(scores)):

        temparr[i] = scores[i]
        
    temparr[len(scores)] = new
    
    print(temparr)    
    
    
if __name__ == '__main__':
    appendnew(75)