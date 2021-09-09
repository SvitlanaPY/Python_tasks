# Напишите функцию, которая имя и возраст водителя.
# Функция должна распечатать на экран заключение, может ли данный водитель управлять транспортом и
# определять она должна это по возрасту водителя: он должен быть больше или равен MIN_DRIVING_AGE.
#
# Если водитель может управлять, выведите фразу "<name> может водить> " ,
# в противном случае "<name> еще рано садиться за руль".
#
# MIN_DRIVING_AGE = 18
# allowed_driving('tim', 17) # выведет "tim еще рано садиться за руль"
# allowed_driving('bob', 18) # выведет "bob может водить"

MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    global MIN_DRIVING_AGE
    if age >= MIN_DRIVING_AGE:
        return "%s может водить" % name
    #       print(f"{name} может водить")
    #       return ("%s может водить" % name)
    else:
        return "%s еще рано садиться за руль" % name


#       print(f"{name} еще рано садиться за руль")
#       return ("%s еще рано садиться за руль" % name)

print(allowed_driving('tim', 17))
print(allowed_driving('bob', 18))
