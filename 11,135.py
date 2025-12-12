import random
results = [random.choice([0, 1, 3]) for _ in range(20)]
win_index = next((i for i, x in enumerate(results) if x == 3), None)
loss_index = next((i for i, x in enumerate(results) if x == 0), None)
if win_index is not None and loss_index is not None:
    if win_index < loss_index:
        print("Первый выигрыш был раньше первого проигрыша")
    elif loss_index < win_index:
        print("Первый проигрыш был раньше первого выигрыша")
    else:
        print("Выигрыш и проигрыш одновременно (невозможно)")
elif win_index is not None:
    print("Был выигрыш, но не было проигрыша")
elif loss_index is not None:
    print("Был проигрыш, но не было выигрыша")
else:
    print("Не было ни выигрышей, ни проигрышей")
