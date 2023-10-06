class Bank:
    def __init__(self, name, surname, balance, pin, country, number):
        self.__name = name
        self.__surname= surname
        self.__balance = balance
        self.__pin = pin
        self.__country = country
        self.__number = number

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name
    
    def set_surname(self, new_surname):
        self.__surname = new_surname

    def get_surname(self):
        return self.__surname
    

    def set_balance(self, new_balance):
        self.__balance = new_balance

    def get_balance(self):
        return self.__balance
    
    def set_pin(self, new_pin):
        self.__pin = new_pin

    def get_pin(self):
        return self.__pin
    
    # возвращает действующий счет 
    def current_balance(self):
        return self.get_balance()
    
    # добавить деньги к счету 
    # amount - количество денег которые добавляем к балансу
    def add_money(self, amount):
        self.__balance += amount

    # снять деньги со счета 
    # снимает деньги с осн счета
    def withdraw_money(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("haha yavrey")
        


    # добавить функции getter/setter для country and number

account = Bank("Marina", "Ramazanova", 500, "6789", "UK", "0987654321")
# print(account.get_name())
# account.set_name("Gurgen")
# print(account.get_name())
account.add_money(20)
print(account.current_balance())
account.withdraw_money(520)
print(account.current_balance())
