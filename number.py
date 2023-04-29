import random

guessesTaken = 0

print('안녕! 이름이 뭐야?')
Name = input()

number = random.randint(1, 20)
print(Name + ', 1부터 20까지 숫자 중 하나를 골랐어. 맞춰봐.')

while guessesTaken < 6:
    print('숫자를 입력해봐.')
    guess = input()
    guess = int(guess)

    guessesTaken += 1

    if guess < number:
        print('그거보단 높아.')
    if guess > number:
        print('그거보단 낮아.')
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('잘했어, ' + Name + '! ' + guessesTaken + '번 만에 맞췄어!')
if guess != number:
    number = str(number)
    print('안타깝지만, 내가 생각한 숫자는 ' + number + '였어.')