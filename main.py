

file = open("record.txt", "w")

class Account:
  account_number: None
  first_name: None
  last_name: None
  balance: None
  transactions: 0

  def read_data(self):
   self.account_number = input('what is your account number: ')
   self.first_name = input('what is your first name: ')
   self.last_name = input('what is your first last name: ')
   self.balance = 0
   self.transactions = 0
   user_file = open("user.txt", "w")
   seq = ['first name : ', self.first_name, ' last name: ', self.last_name , ' account number: ', self.account_number]
   user_file.writelines(seq)
   user_file.close()
   print('Hey %s %s your account is all set!' % (self.first_name, self.last_name))

  def make_deposit(self):
    deposit = input('how much would you like to deposit? ')
    self.balance = (self.balance + int(deposit))
    self.transactions += 1
    transactionHistory =  "\n" + 'Your account balance is $' + str(self.balance) + "\n"
    file.writelines(transactionHistory)
    file.close()

  def get_balance(self):
    file = open('record.txt', 'r')
    print(file.read())

  def init_dummy(self):
    self.balance = 0
    self.transactions = 0

  def update_balance(self):
    file = open('record.txt', 'r')
    confirm = input('Would you like to modify this transaction your balance is ' + file.read() + '\n' + 'type yes or no: ')
    if confirm == 'yes':
      deposit = input('how much would you like deposit ? ')
      self.balance = int(deposit)
      transactionHistory =  "\n" + 'Your account balance is $' + str(self.balance) + "\n"
      path = open('record.txt', 'w')
      path.writelines(transactionHistory)
    else:
      return

    # file = open('record.txt', 'w')
    

    

print('*** Acount Information System***')
boolean = True
while boolean: 
  print('Select an option from below ')
  print('select 1 to make a deposit  \n')
  print('Select 2 to get your account balance \n')
  selection = input(' make a selection: ')
  acct = Account()
  acct.init_dummy()
  if(int(selection) == 1):
    acct.read_data()
    acct.make_deposit()
  elif(int(selection) == 2):
    acct.get_balance()
  elif(int(selection) == 3):
    acct.update_balance()
  else:
    boolean = False
    break
  









