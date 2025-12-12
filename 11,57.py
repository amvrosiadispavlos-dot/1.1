import random
june_precipitation = [random.randint(0, 30) for _ in range(30)]
first_half = sum(june_precipitation[:15])
second_half = sum(june_precipitation[15:])
print(f"Осадки в первую половину: {first_half}")
print(f"Осадки во вторую половину: {second_half}")
if first_half > second_half:
    print("Больше осадков выпало в первую половину")
elif second_half > first_half:
    print("Больше осадков выпало во вторую половину")
else:
    print("Осадки равны")

decade1 = sum(june_precipitation[:10])
decade2 = sum(june_precipitation[10:20])
decade3 = sum(june_precipitation[20:])
print(f"Осадки по декадам: {decade1}, {decade2}, {decade3}")
max_decade = max(decade1, decade2, decade3)
if max_decade == decade1:
    print("Больше всего осадков в первой декаде")
elif max_decade == decade2:
    print("Больше всего осадков во второй декаде")
else:
    print("Больше всего осадков в третьей декаде")
