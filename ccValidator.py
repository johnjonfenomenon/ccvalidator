

import pdb
import datetime
#global variable
b_validating = True

class CreditCard():
	'''
	no input
	creates credit card class()
	'''
	def __init__(self,number,exp,cc_code):
		self.number = number
		self.exp = exp
		self.cc_code = cc_code
		self.cctype = ''

	def __str__(self):
		the_card = ''
		the_card = f'card type: {self.cctype}  \nnumber: {self.number}  \nexp: {self.exp} \ncc_code: {self.cc_code}'
		return the_card


	def checksum(self):
		'''
		no input
		returns a boolean
		use check sum logic to replace every other digit in 16 digit card with double the value
		check to see if double the place holder is >=10 so replace by adding the digits together
		'''    
		cc_list = [int(i) for i in str(self.number)] #parse the cc entered by user into an individual iterable list
		digit = 0

		for num in range (0,16,2): 
			if (cc_list[num]*2) >= 10:
				d = ((cc_list[num]*2)%10) + 1
				cc_list[num] = d
			else:
				cc_list[num] = cc_list[num]*2

		for x in cc_list:  #add all the numbers together and check if mulitple of 10
			digit = digit + x

		if digit%10 == 0:
			return True
		else:
			return False

	def checkdate(self):
		'''
		no input
		Checks if the card is expired
		'''            
		if self.exp > datetime.datetime.now():
			return True
		else:
			return False

	def cc_type(self): 
		'''
		no input
		checks to see what type of credit card and sets the cctype of the object to that credit card type 
		returns a string
		'''  
		num_s = str(self.number)
		if (int(num_s[:2]) >= 51 and int(num_s[:2]) <= 55 and len(num_s) == 16):
			self.cctype = 'Master Card'
			return 'Master Card'
		elif(int(num_s[0]) == 4 and  len(num_s) == 16):
			self.cctype = 'Visa'
			return 'Visa'
		elif(int(num_s[:4]) == 6011 and len(num_s) == 16):
			self.cctype = 'Discover'
			return 'Discover'
		else:
			self.cctype = 'card not accepted'
			return 'card not accepted'

#Function list designed to get user input       
def enter_cc():
    while True:
        try:
            cc_number = int(input('\nPlease manually enter the credit card number? '))
        except ValueError:
            print('Sorry, the credit card must be a 16 digits and all numerical!')
        else:
            if len(str(cc_number)) != 16:
                print(f'Sorry, you have entered {len(str(cc_number))} digits only 16 are allowed')
                continue
            else:
                break

    return cc_number


def enter_exp():
    isValid=False
    next_month = 0
    while not isValid:
        userIn = input("Expiration date mm/yy: ")
        try: # strptime throws an exception if the input doesn't match the pattern
             # by default exp_date will be set to first of the month, but cc use can go all the way to the last day of the month
            exp_date = datetime.datetime.strptime(userIn, "%m/%y")
            next_month = (exp_date.month + 1)%12
            exp_date = exp_date.replace(month=next_month)
            exp_date = exp_date-datetime.timedelta(days=1) 
            isValid=True
        except:
            print('Not a valid date!\n')

    return exp_date


def enter_ccy():
    while True:
        try:
            ccy = int(input('Please manually enter the security code? '))
        except ValueError:
            print('Sorry, the credit card must be a 3 digits and all numerical!')
        else:
            if len(str(ccy)) != 3:
                print(f'Sorry, you have entered {len(str(ccy))} digits, only 3 are allowed')
                continue
            else:
                break    

    return ccy

def validate_another():
    validate_another = input("\nWould you like to validate another card? Enter 'y' or 'n' ")
    if validate_another[0].upper()=='Y':
        return True
    else:
        return False

#main routine
print(f'\nWelcome to the card checker app, where you can validate a Visa, Master Card, or Discover card\n')

while b_validating:
    #retrieve manual input
    cc = enter_cc()
    exp = enter_exp()
    ccy = enter_ccy()

    #instantiate false values
    
    valid_num = False
    valid_exp = False
    valid_type = ''

    #create cc object from manual input
    card_entry = CreditCard(cc, exp, ccy)

    #pdb.set_trace()
    valid_type = card_entry.cc_type()
    valid_num = card_entry.checksum()
    valid_exp = card_entry.checkdate()

    #print(valid_type)

    if (valid_type == 'Visa' or valid_type == 'Master Card' or valid_type =='Discover'):
        valid_num = card_entry.checksum()
        valid_exp = card_entry.checkdate()
    else:
        (print(f'\nWe only accept Visa, Master Card or Discover\n'))
        b_validating = validate_another()
        continue

    if (valid_num and valid_exp):
        #pdb.set_trace()
        (print(f'\nThe following \n{card_entry} \nIs a valid credit card, please proceed with transaction\n'))
    else:
        (print(f'\nWARNING!!!! \nThe following {card_entry} is not a valid credit card, please void transaction\n'))

    b_validating = validate_another()
    continue

print('\nThanks for using our validation system!')