#Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes =[]
not_primes = []
is_prime=0

for i in range(1,len(numbers)+1):
    for j in range(2,len(numbers)+1):

        if i == 1:
            break
        quotient_=numbers[i-1]/numbers[j-1]
        remainder_=numbers[i-1]%numbers[j-1]
        if numbers[i-1]<numbers[j-1]:
            continue

        if remainder_==0 and numbers[i-1]==numbers[j-1]:
            is_prime="true"
            break
        elif remainder_!=0:
            continue
        elif remainder_==0 and quotient_!=1:
            is_prime="false"
            break
        else: continue

    if is_prime=="true":
        primes.append(i)
    elif is_prime=="false":
        not_primes.append(i)


print ("primes: ",primes)
print ("not_primes: ",not_primes)