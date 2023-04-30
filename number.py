import random

token = 0

print('이름이 뭔가요?')
Name = input()

number = random.randint(1, 20)
print(Name + '님', '1부터 20까지 숫자 중 하나를 골랐어요 맞춰보세요')

while token < 6:
    print('숫자를 입력해보세요')
    guess = input() #입력받은게 문자열
    guess = int(guess) #정수형으로 변환

    token += 1

    if guess < number:
        print('그거보단 높아요')
    if guess > number:
        print('그거보단 낮아요')
    if guess == number:
        break

if guess == number:
    token = str(token)
    print('잘했어요 ' + Name + '! ' + token + '번 만에 맞췄어요!')
if guess != number:
    number = str(number)
    print('아쉽지만 내가 생각한 숫자는 ' + number + '였어요')