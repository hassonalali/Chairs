f = open("reservations")

for reservation in f:
    name, number = reservation.split(",")
    try:
        chairs_per_person = 50 / int(number)
    except ValueError: 
        break
    print("{} will get {} chairs per person".format(name, chairs_per_person))


