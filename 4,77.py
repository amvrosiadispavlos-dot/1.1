a, b = int(input("a (вертикаль белой): ")), int(input("b (горизонталь белой): "))
c, d = int(input("c (вертикаль чёрной): ")), int(input("d (горизонталь чёрной): "))
e, f = int(input("e (вертикаль цели): ")), int(input("f (горизонталь цели): "))
if not all(1 <= x <= 8 for x in [a, b, c, d, e, f]):
    print("Координаты вне доски")
else:
    def rook_threat(x1, y1, x2, y2):
        return (x1 == x2) or (y1 == y2)
    def bishop_threat(x1, y1, x2, y2):
        return abs(x1 - x2) == abs(y1 - y2)
    def queen_threat(x1, y1, x2, y2):
        return rook_threat(x1, y1, x2, y2) or bishop_threat(x1, y1, x2, y2)
    def knight_threat(x1, y1, x2, y2):
        return (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2)
    def king_threat(x1, y1, x2, y2):
        return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1
    def white_can_move(white_type):
        if white_type == "ладья":
            return rook_threat(a, b, e, f)
        elif white_type == "ферзь":
            return queen_threat(a, b, e, f)
        elif white_type == "конь":
            return knight_threat(a, b, e, f)
        elif white_type == "слон":
            return bishop_threat(a, b, e, f)
        elif white_type == "король":
            return king_threat(a, b, e, f)
        return False
    def black_threatens_target(black_type):
        if black_type == "ладья":
            return rook_threat(c, d, e, f)
        elif black_type == "ферзь":
            return queen_threat(c, d, e, f)
        elif black_type == "конь":
            return knight_threat(c, d, e, f)
        elif black_type == "слон":
            return bishop_threat(c, d, e, f)
        elif black_type == "король":
            return king_threat(c, d, e, f)
        return False
    white_pieces = ["ладья", "ферзь", "конь", "слон", "король"]
    black_pieces = ["ладья", "ферзь", "конь", "слон", "король"]
    white_type = "ладья"
    black_type = "ладья"
    move_possible = white_can_move(white_type)
    under_attack = black_threatens_target(black_type)
    print(f"Белая {white_type} может пойти на ({e},{f}): {move_possible}")
    print(f"Чёрная {black_type} угрожает полю ({e},{f}): {under_attack}")
    print(f"Белая фигура может безопасно пойти: {move_possible and not under_attack}")
