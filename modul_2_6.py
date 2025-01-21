#Задание "Слишком древний шифр"

numbers=(3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
n=input("Введите первое число (от 3 до 20): ")

while int(n)<3 or int(n)>20:
   n=input("Внимательно введите первое число (от 3 до 20): ")

#print(n)
parol=[]
cycle_1=1
cycle_2=1
for i in range(1,21):
    for j in range(1,21):
        if cycle_1>cycle_2 or cycle_1==cycle_2:
            cycle_2+=1
            continue
        sum=cycle_1+cycle_2
        if int(n)%sum==0:
            parol.append(cycle_1)
            parol.append(cycle_2)
            cycle_2+=1

        else: cycle_2+=1
    cycle_1+=1
    cycle_2=1

print(f"Вот список пар чисел для {n}: ",*parol)