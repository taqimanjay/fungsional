def title_decorator(function):
    def wrapper():
        func = function()
        make_title = func.title()
        print(make_title + " " + "-Data is converted to title case")
        return make_title
    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        print(str(splitted_string) + " " + "-Then data is splitted")
        return splitted_string
    return wrapper

@title_decorator
@split_string
def say_hi():
    return 'hello there'

# Panggil fungsi say_hi yang sudah didekorasi
hasil = say_hi()

# Output hasil
print(hasil)
