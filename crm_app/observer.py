class BusinessCustomer:
    def __init__(self, acct_id, money_owned):
        self.acct_id = acct_id
        self.money_owned = money_owned
    def update(self):
        if self.money_owned > 0:
            print(f" {self.acct_id}: Call the company finance department")
        else:
            print(f" {self.acct_id}: Corporate balance paid")
class ConsumerCustomer:
    def __init__(self, acct_id, money_owned):
        self.acct_id = acct_id
        self.money_owned = money_owned
    def update(self):
        if self.money_owned > 0:
            print(f" {self.acct_id}: Send a polite remainder email")
        else: 
            print(f" {self.acct_id}: Individual balance paid ")
class AccountingSystem:
    def __init__(self):
        self.customers = set()
    def register(self,customer):
        self.customers.add(customer)
    def unregister(self,customer):
        self.customers.remove(customer)
    def notify(self):
        for customer in self.customers:
            customer.update()
def main():
    cust1 = BusinessCustomer("ACCT100", 10)
    cust2 = BusinessCustomer("ACCT200", 0)
    cust3 = ConsumerCustomer("ACCT300", -10)
    cust4 = ConsumerCustomer("ACCT400", 20)

    accounting_sys = AccountingSystem()
    accounting_sys.register(cust1)
    accounting_sys.register(cust2)
    accounting_sys.register(cust3)
    accounting_sys.register(cust4)

    accounting_sys.notify()

    accounting_sys.unregister(cust2)
    print("** cust2 has cancelled their account")

    accounting_sys.notify()
if __name__ == "__main__":
        main()
    






