def perkalian(a):
    def dengan(b):
        return a * b
    return dengan

# Higher-Order Function (HOF)
def panggil_dengan(fungsi, arg1, arg2):
    return fungsi(arg1)(arg2)

# Panggil fungsi dengan HOF
hasil_perkalian = panggil_dengan(perkalian, 5, 3)

# Output hasil perkalian
print(hasil_perkalian)
