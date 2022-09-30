import math  
# Below function will print the  
# all prime factor of given number  
def prime_factors(num):  
    # Using the while loop, we will print the number of two's that divide n  
    prime_f = []
    while num % 2 == 0:  
        prime_f.append(2)  
        num = num / 2  
  
    for i in range(3, int(math.sqrt(num)) + 1, 2):  
  
        # while i divides n , print i ad divide n  
        while num % i == 0:  
            prime_f.append(i)  
            num = num / i  
    if num > 2:  
        print(num)
    return prime_f  
# calling function   

print(max(set(prime_factors(600851475143)))) 