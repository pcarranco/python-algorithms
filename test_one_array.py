# Definir una matriz unidimensional de puntajes

from array import array

def main():
    scores = array('i')
    scores = array('i',[10,20,31,43,65,45,84])
    
    for i in range(0,len(scores)):
        print(scores[i],",", end="")
    
if __name__ == '__main__':
    main()