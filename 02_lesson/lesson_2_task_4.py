# Такой код мне кажется более правильным, поскольку в каждом ветвлении прописаны все условия его исполнения.
def fizz_buzz(n):
    for n in range(1, n + 1):
        if n % 3 == 0 and n % 5 != 0:
            print('Fizz')
        elif n % 5 == 0 and n % 3 != 0:
            print('Buzz')
        elif n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz')
        else:
            print(n)

fizz_buzz(int(input('Enter a number: ')))

#Более компактный код , возможно исполняется быстрее,
#(не уверен, но возможно могут быть ошибки, т.к. не все условия прописаны в каждом ветвлении,
#верное исполнение возможна только при правильной последовательностьи ветвления.
def fizz_buzz(n):
    for n in range(1, n + 1):
        if n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz')
        elif n % 3 == 0:
            print('Fizz')
        elif n % 5 == 0:
            print('Buzz')
        else:
            print(n)

fizz_buzz(int(input('Enter a number: ')))
#
