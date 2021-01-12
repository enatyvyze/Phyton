
def my_func(name, last_name, year, city, email, number):
    print(f"Имя - {name} | "
          f"Фамилия - {last_name} | "
          f"Год рождения - {year} | "
          f"Город проживания - {city} | "
          f"Email - {email} | "
          f"Номер телефона- {number}")
my_func(name = input('Введите имя - '),
        last_name = input('Введите Фамилию - '),
        year = input('Введите год рождения - '),
        city = input('Введите город проживания - '),
        email = input('Введите email - '),
        number = input('Введите номер - '))