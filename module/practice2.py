import practice1 as user
from account import Account as UserAccount

user.greet('Samir')

print(user.age)

myAccount = UserAccount('Samir','shahriar.samir80@gmail.com',22)

myAccount.showAccount()