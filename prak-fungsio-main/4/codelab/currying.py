def perkalian(a):
    def dengan(b):
        return a * b
    return dengan

# Panggil fungsi dengan currying
hasil_perkalian = perkalian(5)(3)

# Output hasil perkalian
print(hasil_perkalian)
