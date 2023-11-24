import math

def translasi(x, y, tx, ty):
    x_baru = x + tx
    y_baru = y + ty
    return x_baru, y_baru

def dilatasi(x, y, sx, sy):
    x_baru = x * sx
    y_baru = y * sy
    return x_baru, y_baru

def rotasi(x, y, sudut):
    sudut_rad = math.radians(sudut)
    x_baru = x * math.cos(sudut_rad) - y * math.sin(sudut_rad)
    y_baru = x * math.sin(sudut_rad) + y * math.cos(sudut_rad)
    return x_baru, y_baru

# Contoh kasus
titik_awal = (3, 5)

# Translasi
tx, ty = 2, -1
titik_setelah_translasi = translasi(*titik_awal, tx, ty)
print("Koordinat titik setelah translasi:", titik_setelah_translasi)

# Dilatasi
sx, sy = 2, -1
titik_setelah_dilatasi = dilatasi(*titik_awal, sx, sy)
print("Koordinat titik setelah dilatasi:", titik_setelah_dilatasi)

# Rotasi
sudut_rotasi = 30
titik_setelah_rotasi = rotasi(*titik_awal, sudut_rotasi)
print("Koordinat titik setelah rotasi:", titik_setelah_rotasi)
