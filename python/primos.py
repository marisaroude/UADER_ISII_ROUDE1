# prime number calculator: find all primes up to n
#max = int(input("Find primes up to what number? : "))#()
import sys

if len(sys.argv) == 3:
    max = int(sys.argv[1])
    count = int(sys.argv[2])
else:
    print ("ERROR: Introdujo uno (1) o mas de dos (2) argumentos")
    print("SOLUCION: Introduce los argumentos correctamente")
    print ('Ejemplo: entrada_dos_argumentos.py "Texto" 5')
primeList = []
#for loop for checking each number
for x in range(2, max + 1):
	isPrime = True
	index = 0
	root = int(x ** 0.5) + 1
	while index < len(primeList) and primeList[index] <= root:
		if x % primeList[index] == 0:
			isPrime = False
			break
		index += 1
	if isPrime:
		primeList.append(x)
print(primeList)
#-------------------------------------------------------------
# prime number calculator: find the first n primes
#count = int(input("Find how many primes?: "))
primeList = []
x = 2
while len(primeList) < count:
	isPrime = True
	index = 0
	root = int(x ** 0.5) + 1
	while index < len(primeList) and primeList[index] <= root:
		if x % primeList[index] == 0:
			isPrime = False
			break
		index += 1
	if isPrime:
		primeList.append(x)
	x += 1
print(primeList)