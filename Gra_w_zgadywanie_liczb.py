import random

get_number = random.randint(1, 100)

x = 0
while x < 10:
    x +=1
    try:
        number = (int(input("Zgadnij liczbę!")))
    except Exception:
        print ("to nie jest liczba")
        continue
    if get_number > number:
        print("za mało!")
        continue
    elif get_number < number:
        print("za dużo!")
        continue
    else:
        print("Zgadłeś!")
        break


