import inspect


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__

def open_browser(browser_name):
    pass


def go_to_companyname_homepage(page_url):
    pass


def find_registration_button_on_login_page(page_url, button_text):
    pass


def your_function():
    pass


def information_of_func(func):
    arguments = str(inspect.signature(func)).replace("_", " ")[1: -1]#преобразовать список arguments функции в строку
    # обрезать первый и последний знаки, заменить нижнее подчеркивание на пробел
    name_func = func.__name__.replace("_", " ").capitalize()#вытащить имя функции
    # заменить нижнее подчеркивание на пробел, писать с заглавной
    if len(arguments) > 0:
        print(name_func+": " + arguments) # если есть arguments - писать с arguments через запятую
    else:
        print(name_func+": no have arguments")# нет arguments - пишем, что нет

functions = [open_browser, go_to_companyname_homepage, find_registration_button_on_login_page,
             your_function] #список функций

#цикл
for element in functions: # иди по всем элементам из списка functions
    information_of_func(element) # выполняй information_of_func для каждого элемента


