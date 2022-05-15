# Airline / Hotel Reservation System - Create a reservation system which books airline seats or hotel rooms. 
# It charges various rates for particular sections of the plane or hotel. 
# Example, first class is going to cost more than coach. 
# Hotel rooms have penthouse suites which cost more. Keep track of when rooms will be available and can be scheduled.

class Airline:
    def __init__(self, name, surname, balance, seat_type):
        self.name = name
        self.surname = surname
        self.balance = balance

    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + self.balance

    # def choose_seat(self, seat_type):
    #     if int(self.balance) >= 20000 and seat_type == "1st class":
    #         self.balance = str(int(self.balance) - 2000)

    #     if int(self.balance) >= 10000 and seat_type == "2nd class":
    #         self.balance = str(int(self.balance) - 670)

    #     if int(self.balance) >= 700 and seat_type == "3rd class":
    #         self.balance = str(int(self.balance) - 200)

    def choose_seats(self):
        for client in clients:
            if int(client.balance) < 1000 and int(client.balance) > 200:
                client.seat_type = "3rd class"

            if int(self.balance) < 2500 and int(self.balance) > 800:
                self.seat_type = "2nd class"

            if int(self.balance) > 3200:
                self.seat_type = "1st class"
            print(client)

clients = [Airline("Jack", "Black", "700", None),
           Airline("Anakin", "Skywalker", "25000", None),
           Airline("Marie", "Hoffmann", "1300", None)]

clients[0].choose_seats()
