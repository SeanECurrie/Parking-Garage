license_plate = input("What is your license?")


class ParkingGarage():
    def __init__(self, license_plate, customerTicket={}) :
        self.total_tickets = 20
        self.parking_spots = 20
        self.license_plate = license_plate
        self.customerTicket = customerTicket

    def takeTicket(self):
        if self.total_tickets and self.parking_spots !=0:
            self.total_tickets - 1
            self.parking_spots -1
            self.customerTicket[self.license_plate] = False
        else:
            print("Sorry, we are full")

     def payForTicket(self): 
        payment_amount=int(input( "Please enter your payment of $20:"))
        if payment_amount == 20 :
            print("Your payment has been accepted. You have 15 minutes to leave the parking lot.")
            self.customer_ticket[self.license_plate] = True
        else:
            print("That is not a valid amount. Please try again.")

        

    def leaveGarage(self):
        if self.customerTicket[license_plate] == True:
            print("Thanks have a nice day")

        else:
            payment_amount = input("Please enter $20:")
            
            

    

    def runner(self):       

        while True:
                
                user_choice= input('\n\n[T]ake a ticket\n[P]ay for parking\n[L]eavea character\n\nWhat would you like to do?  ').lower()

                if user_choice == 't':
                    self.takeTicket()
                

                elif user_choice == 'p':
                    self.payForTicket()
                
                elif user_choice == 'l':
                    self.leaveGarage()
                    
                    print("Thanks you have a nice day")
                    break
                
                else:
                    print('Invalide choice, try again...')  






