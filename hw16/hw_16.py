class CurrencyMixin:
    def __init__(self, amount, USD_rate = 27.3, EUR_rate = 32.0):
        self.amount = amount
        self.USD_rate = USD_rate
        self.EUR_rate = EUR_rate

    def chosen_currency(self, USD_rate = 27.3, EUR_rate = 32.0):
        chosen_currency = input("Choose the currency to convert UAH: \n1)EUR \n2)USD \n3)UAH\n\n")

        if chosen_currency == "1":
            EUR_amount = round(float(input("How many EUR do you want to add/get?\n")))
            amount = EUR_amount * EUR_rate
            return amount

        elif chosen_currency == "2":
            USD_amount = round(float(input("How many USD do you want to add/get?\n")))
            amount = USD_amount * USD_rate
            return amount

        elif chosen_currency == "3":
            UAH_amount = round(float(input("How many UAH do you want to add/get?\n")))
            amount = UAH_amount
            return amount
        else:
            print("Error, try again later. \nEnter 1 as USD, 2 as RUB or 3 as GBP.")


class Account(CurrencyMixin):
    min_limit = 0
    max_limit = 10000000
    bank_name = 'Mono'

    def __init__(self, amount, balance = 0):
        self.balance = balance
        super().__init__(amount)

    def validate_amount(self, amount):
        if amount < 0:
            raise ValueError
        return amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("There is not enough money")
        elif amount > self.max_limit:
            raise ValueError
        self.balance -= amount

    def add_money(self, amount):
        self.balance += amount

    def __str__(self):
        return self.balance


def main():
    acc = Account(100, 10000)
    while True:
        print("\n1 - Check Balance \t 2 = Withdraw \t 3 - Deposit \t 4 - Exit")

        selection = int(input("\n What would you like to choose?:"))
        if selection == 1:
            a = acc.balance
            print(f"Your balance is {a}")

        elif selection == 2:
            amount = acc.chosen_currency()
            acc.withdraw(amount)
            print("\nYour Updated balance is: " + str(acc.balance) + " n")

        elif selection == 3:
            amount = acc.chosen_currency()
            acc.add_money(amount)
            print("\nYour updated balance is: " + str(acc.balance) + " n")

        elif selection == 4:
            print("The transaction is done.")
            exit()

        else:
            print("An incorrect choice.")


if __name__ == "__main__":
    main()









