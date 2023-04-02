# Exercise 1 : Call History
import re


class Phone:
    def __init__(self, phone_number):
        self.call_history = []
        self.messages = []
        self.phone_number = phone_number

    def call(self, other_phone):
        print(f"Attention! {other_phone.phone_number} called {self.phone_number}")
        self.call_history.append(other_phone.phone_number)

    def show_call_history(self):
        print("\nYour call history:")
        print("\n".join(self.call_history) or "Empty")

    def send_message(self, other_phone, message):
        print(f"""{other_phone.phone_number}'s got mail!\nThe message is: {message}""")
        self.messages.append({
            'to':       other_phone.phone_number,
            'from':     self.phone_number,
            'message':  message
        })
        other_phone.messages.append({
            'to': other_phone.phone_number,
            'from': self.phone_number,
            'message': message
        })

    def show_outgoing_messages(self):
        print("\nOutgoing messages for the number", self.phone_number)
        for e in list(filter(lambda item: item['from'] == self.phone_number, self.messages)):
            print('—' * 30)
            print("To", e['to']+':', e['message'])
            print('—' * 30)

    def show_incoming_messages(self):
        print("\nIncoming messages for the number", self.phone_number)
        for e in list(filter(lambda item: item['to'] == self.phone_number, self.messages)):
            print('—' * 30)
            print("From", e['from']+':', e['message'])
            print('—' * 30)

    def show_messages_from(self):
        pass


# Testing code
class PhoneBase:
    def __init__(self, phone_numbers):
        self.phones = []
        for i in range(len(phone_numbers)):
            self.phones.append(Phone(phone_numbers[i]))
            print(phone_numbers[i], "is added")
        self.current_number = self.phones[0]
        self.show_menu()

    def show_numbers(self):
        for i, phone in enumerate(e.phone_number for e in self.phones):
            print(f"{i+1}: {phone}")

    def show_menu(self):
        while True:
            print(f"""
                Your number is {self.current_number.phone_number}
                ————————————————————————————————————————
                You can choose the following:
                1: change your number
                2: call another number                
                3: send a message to another number
                4: show your call history
                5: show your incoming messages
                6: show your outgoing messages
                q: quit the program
            """)
            choice = input("Enter your choice: ")
            if choice == 'q':
                break
            if not re.match(r'\d', choice):
                continue
            if choice == '1':
                self.show_numbers()
                while True:
                    new_number = input("Enter the number of your phone number (1, 2, ...): ")
                    if not re.match(r'\d', new_number):
                        print("The number you entered is incorrect. Please, try again")
                        continue
                    else:
                        self.current_number = self.phones[int(new_number)-1]
                        print(f"Your number is {self.current_number.phone_number} now")
                        break
            elif choice == '2':
                self.show_numbers()
                while True:
                    call_number = input("Enter the number of the phone number you'd like to call (1, 2, ...): ")
                    if not re.match(r'\d', call_number) or self.phones[int(call_number)-1] == self.current_number:
                        print("The number you entered is incorrect. Please, try again")
                        continue
                    else:
                        self.current_number.call(self.phones[int(call_number)-1])
                        break
            elif choice == '3':
                self.show_numbers()
                while True:
                    msg_number = input("Enter the number of the phone number you'd like to message (1, 2, ...): ")
                    if not re.match(r'\d', msg_number) or self.phones[int(msg_number) - 1] == self.current_number:
                        print("The number you entered is incorrect. Please, try again")
                        continue
                    else:
                        message = input("Enter your message: ")
                        self.current_number.send_message(self.phones[int(msg_number) - 1], message)
                        break
            elif choice == '4':
                self.current_number.show_call_history()
            elif choice == '5':
                self.current_number.show_incoming_messages()
            elif choice == '6':
                self.current_number.show_outgoing_messages()


main_base = PhoneBase(['+12345', '+12356', '+12367', '+123468909'])
