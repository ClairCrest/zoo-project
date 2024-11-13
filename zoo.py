class Zoo:
    def get_ticket_price(self, age):
        if 0 <= age <= 12: #Add '=' before 'age' ///Fault 2
            return 50
        elif 13 <= age <= 20: #Add '=' after '<' sign before 20 ///Fault 3
            return 100
        elif 21 <= age <= 60: #Add '=' after '<' sign after 21 ///Fault 4
            return 150
        elif age >= 60:
            return 100
        else:
            return "ERROR" #Case age < 0 ///Fault 1