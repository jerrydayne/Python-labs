##In many jurisdictions a small deposit is added to drink containers to encourage people
##to recycle them. In one particular jurisdiction, drink containers holding one liter or
##less have a $0.10 deposit, and drink containers holding more than one liter have a $0.25 deposit.

##Write a program that reads the number of containers of each size from the user.
##Your program should continue by computing and displaying the refund that will be
##received for returning those containers. Format the output so that it includes a dollar
##sign and always displays exactly two decimal places.

one_litre_or_less_container = float(input("How many 1 litre or less containers do you have : "))
more_than_a_litre_containers = float(input("How many more than a litre container do you have : "))

lower_deposit = one_litre_or_less_container * 0.10
higher_deposit = more_than_a_litre_containers * 0.25

total_deposit = lower_deposit + higher_deposit

print("your total depoit is $%.2f" % total_deposit)