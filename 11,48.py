import random
june = [random.randint(0, 20) for _ in range(30)]
decade1 = sum(june[:10])
decade2 = sum(june[10:20])
decade3 = sum(june[20:])
print(f"Осадки за 1-ю декаду: {decade1}")
print(f"Осадки за 2-ю декаду: {decade2}")
print(f"Осадки за 3-ю декаду: {decade3}")
