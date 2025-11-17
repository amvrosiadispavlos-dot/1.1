n = int(input("Введите номер места: "))
sections = 8
tiers = 10
places_per_section = 15
places_per_tier = sections * places_per_section 
tier = (n - 1) // places_per_tier + 1
position_on_tier = (n - 1) % places_per_tier + 1
section = (position_on_tier - 1) // places_per_section + 1
position_in_section = (position_on_tier - 1) % places_per_section + 1
print("Секция:", section)
print("Ярус:", tier)
print("Позиция в секции:", position_in_section)
