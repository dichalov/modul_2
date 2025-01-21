#Домашняя работа по уроку "Функции в Python.Функция с параметром"

def get_matrix (n,m,value):
    matrix=[]
    number_cycle=0
    matrix_1=[]

    for i in range (1,n+1):
        matrix.append(matrix_1)#подскажите, как проще?
        for j in range (1,m+1):

            matrix_1.insert(number_cycle,value)
            number_cycle+=1

        number_cycle=0
        matrix_1=[]

    return matrix

n=int(input("введите N; "))
m=int(input("введите M: "))
value=int(input("введите Value: "))

result=get_matrix(n,m,value)
print(result)

