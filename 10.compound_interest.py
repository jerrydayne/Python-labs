investment = int(input("how much are you investing? "))

fist_year_interest = (investment*0.04*1) + investment
second_year_interest = ((investment + fist_year_interest)*0.04) + investment
third_year_interest = (( investment + second_year_interest) *0.04) + investment

print("after investing",investment,", the ammount in your account over 3 years will look like this:")
print("after first year;", fist_year_interest)
print("after the second year :", second_year_interest)
print("after the third year :", third_year_interest)

