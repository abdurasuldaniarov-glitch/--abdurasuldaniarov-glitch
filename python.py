# /* # 1. ТААНЫШТЫРУУ
# # Бул жерге өзүңүздүн атыңызды жана шаарыңызды жазыңыз:
# at = "Расул"
# jash = 20
# shaar = "Кызыл-кыя"

# print("1. Тааныштыруу")
# print(f"Салам, {at}! сен {jash} жаштасын, {shaar} шаарынан экенсиң\n")

# # 2. КОШУУЧУ

# print("2. Кошуучу")
# num1 = 15
# num2 = 5

# summa = num1 + num2
# aiyrma = num1 - num2
# koboytundu = num1 * num2

# print(f"Сандар: {num1} жана {num2}")
# print(f"Суммасы: {summa}")
# print(f"Айырмасы: {aiyrma}")
# print(f"Көбөйтүндүсү: {koboytundu}\n")

# # 3. ТИК БУРЧТУК

# print("3. Тик бурчтук")
# a = 8  # узундугу
# b = 4  # туурасы

# aant = a * b
# perimetr = 2 * (a + b)

# print(f"Узундугу: {a}, Туурасы: {b}")
# print(f"Аянты (a*b): {aant}")
# print(f"Периметри (2*(a+b)): {perimetr}\n")

# # 4. УБАКЫТ

# print("4. Убакыт")
# sekund = int(input("секунд санын кыргизиниз"))


# saat = sekund // 3600
# minuta = (sekund % 3600) // 60
# kalgan_sekund = sekund % 60

# print(f"{sekund} секунд = {saat} саат, {minuta} минута./n")

# # 5. ЧАКАНИЕ КАССИР

# print("5. Чакан кассир")
# baa =400   # товардын баасы
# san = 6    # товардын саны

# jalpy = baa * san
# arzandatuu = jalpy * 0.10  # 10% арзандатуу
# akyrky_basa = jalpy - arzandatuu

# print(f"Баасы: {baa} сом, Саны: {san} даана")
# print(f"Жалпы сумма: {jalpy} сом")
# print(f"10% арзандатуу менен: {akyrky_basa} сом") */
 




# san = int(input("Бир сан киргизиниз:"))
# if san % 2 == 0:
#    print("Бул жуп сан")
# else:
#    print("Бул так сан")


# jash = int(input("жашынызды киргизиниз:"))

# if jash >= 18:
#    print("Кируу 250 сом:")
# elif jash >=7:
#    print("Кируу 100 сом")
# else:
#    print("Киру бекер:")


# san = int(input("Бир сан киргизиниз"))
# if san >= 0:
#     print("Бул он сан")
# else:
#     print("Бул терс сан")
   

# correct_password = "omur"
# user_password = input("Купуя созду киргизиниз:")

# if user_password == correct_password:
#     print("Купуя соз туура! Кош келиниз")
# else:
#     print("Купуя соз туура эмес")    


# correct_password = "omur[span_2](start_span)"[span_2](end_span)
# attempts = 3  # Количество доступных попыток

# while attempts > 0:
#     user_password = input("Купуя созду киргизиниз:")[span_3](start_span)[span_3](end_span)
    
#     if user_password == correct_password:[span_4](start_span)[span_4](end_span)
#         print("Купуя соз туура! Кош келиниз")[span_5](start_span)[span_5](end_span)
#         break  
#     else:
#         attempts -= 1 
#         if attempts > 0:
#             print(f"Купуя соз туура эмес. Калган попытка: {attempts}")
#         else:
#             print("Система кулпуланды! (Доступ заблокирован)")


# aty = "Abdurasul"
# Parol = "     "
# login_neme =input("Атынызды киргизиниз:")
# login_parol =input("Паролунузду киргизиниз:")
# if login_neme == aty and login_parol == Parol:
#     print("Кош келиниз")
# elif login_neme != aty and login_parol == Parol:
#     print("Аты туура эмес")
# elif login_neme == aty and login_parol != Parol:
#     print("Парол туура эмес")
# else:
#     print("Атыныз туура эмес, Парол туура эмес")


# aty = "Abdurasul"
# Parol = 12398
# login_neme =input("Атынызды киргизиниз")
# login_parol =input("Паролунузду киргизиниз")
# if login_neme == aty and login_parol == Parol:
#     print("Кош келиниз")
# elif login_neme != aty and login_parol == Parol:
#     print("Аты туура эмес")
# elif login_neme == aty and login_parol != Parol:
#     print("Парол туура эмес")
# else:
#     print("Атыныз туура эмес, Парол туура эмес")




# for i in range (15):
#     print("Салам")


# a = 1
# while a <= 5:
#     print("a")
#     a += 1


# for i in range (1, 10):
#     if i == 5:
#         break
#     print(i)
    

# for i in range (5):
#     if i == 3:
#         continue
#     print(i)


# for i in range (3):
#      print(i)
# else:
#      print("уч")


# n = 9
# for i in range(1, 11):
#     print (f"{n} x {i} = {n * i}")


# marks = [5, 4, 3, 5, 4]
# total = 0
# for m in marks:
#     total += m
# print ("Сумма:", total)
# print ("Орточо:", total / len (marks))   


# i = 1
# while i <= 5:
#     print (i)
#     i += 1


# for i in range (1, 31, 3,):
#     print(i)


# summa = 0

# for i in range(1, 11,):
#     summa += i

# print(summa)




# 1ден 10го чейин сандарды чыгаруу

# i = 1
# while i <= 10:
#     print(i, end=" ")
#     i += 1


# 2. 10дон 1ге чейин

# for i in range(10, 0, -1):
#     print(i)

# # 3. Жуп сандар

# for i in range(2, 21, 2):
#     print(i)

# 4. Так сандар

# for i in range(1, 21, 2):
#     print(i)

# 5. 1ден 10го чейинки сумма

# summa = 0
# for i in range(1, 11):
#     summa += i
# print(summa)

# 6. 1ден n ге чейинки сандар

# n = int(input("n = "))
# for i in range(1, n + 1):
#     print(i)

# 7. Көбөйтүү таблицасы

# n = 5
# for i in range(1, 11):
#     print(f"{n} × {i} = {n * i}")

# 8. while менен 1ден 10го чейин

# i = 1
# while i <= 10:
#     print(i)
#     i += 1


# i = 1
# while i <= 10:
#     print(i)
#     i += 1


# 9. while менен 10дон 1ге чейин

# i = 10
# while i >= 1:
#     print(i)
#     i -= 1



# 10. while менен жуп сандар

# i = 2
# while i <= 20:
#     print(i)
#     i += 2



# 11. 0 киргизилгенге чейин

# while True:
#     san = int(input("Сан: "))
#     if san == 0:
#         break
#     print(san)



# 12. while менен сумма

# n = int(input("Сан икиргиз:"))
# i = 1
# summa = 0
# while i <= n:
#     summa += i
#     i += 1
# print("Сумма:", summa )



# 13. 5ке бөлүнгөн сандар

# for i in range(1, 51):
#     if i % 5 == 0:
#         print(i)



# 14. 3кө бөлүнгөн сандар

# for i in range(1, 101):
#     if i % 3 == 0:
#         print(i)



# 15. Сандагы цифралардын санын тап

# n = int(input("Сан киргиз: "))
# n = abs(n)
# count = 0
# if n == 0:
#     count = 1
# else:
#     while n > 0:
#         n //= 10
#         count += 1
# print(f"{count} цифра")