from random import shuffle

list_of_lotto = list(range(1,49))
shuffle(list_of_lotto)
shuffle_list = list_of_lotto[:6]
list_of_numbers = []
list_of_gets = []
x = 0
while x < 6:
    x+=1
    try:
       number = int(input("podaj sześć liczb"))
    except Exception:
        print("to nie jest liczba")

    if number in list_of_numbers:
        print("ta liczba juz zostala wprowadzona")
        break

    if number not in range(1, 49):
        print("liczba nie spelnia warunkow")
        break

    else:
        list_of_numbers.append(number)

for i in list_of_numbers:
    if i in shuffle_list:
        list_of_gets.append(i)
        number_of_gets = len(list_of_gets)

print(f"trafiłeś {number_of_gets}")

