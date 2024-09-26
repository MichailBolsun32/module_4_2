def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()

# Пробую вызывать inner_function вне test_function
try:
    inner_function()
except NameError as error:
    print(f"Ошибка: {error}")
