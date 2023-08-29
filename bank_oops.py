class bank:
    def __init__(self,name,balance,account_no):
        self.name=name
        self.balance=balance
        self.account_no=account_no
    def creditated(self):
        total_balance=crediated_amount+self.balance
        print("the amount{crediated_amount} has been crediated to your bank account.total account balance is{total_balance}"\
              .format(crediated_amount=crediated_amount,total_balance=total_balance))
    def debited(self):
        if debited_amount <self.balance:
            total_balance=self.balance-debited_amount
            print( "the amount{debited_amount} has been debited from your bank account.total account balance is{total_balance}" \
                .format(debited_amount=debited_amount, total_balance=total_balance))
        else:
            print("insufficiant balance and please check your balance")

crediated_amount=eval(input("enter an amount"))
debited_amount=eval(input("enter an amount"))
bank_obj=bank("dp",20000.00,2345678)
bank_obj.creditated()
bank_obj.debited()