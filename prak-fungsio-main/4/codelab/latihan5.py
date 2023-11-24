def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    # TODO 1: Rumus untuk mendapatkan nilai M (gradien)
    M = (p2[1] - p1[1]) / (p2[0] - p1[0])
    
    # TODO 2: Rumus untuk mendapatkan nilai C (konstanta)
    C = p1[1] - M * p1[0]
    
    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik A dan B:")
print(line_equation_of(point(1, 2), point(4, 0)))
