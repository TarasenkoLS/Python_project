def user_f(name, surname, year, town, email, tel):
    return (f'Имя - {name}; Фамилия - {surname}; год рождения - {year},'
            f' город проживания - {town}, email - {email}, телефон - {tel}')


print(user_f(year=2006, email="com@bk.ru", town="Tomsk", tel='+7(983)436-25-41', name='Alex', surname='Pavlov'))
