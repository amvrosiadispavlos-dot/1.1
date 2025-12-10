total_money = 100
total_animals = 100
count = 0
for bulls in range(0, total_money // 10 + 1):
    for cows in range(0, (total_money - bulls*10) // 5 + 1):
        calves = total_animals - bulls - cows
        if calves >= 0 and bulls*10 + cows*5 + calves*0.5 == total_money:
            count += 1
            print(f"Быков: {bulls}, Коров: {cows}, Телят: {calves}")
print(f"\nВсего вариантов: {count}")
