##collects length and width n feet and displays area in acres 

length = float(input("Enter the length of the field :"))
width = float(input("Enter the width of the field : "))

area_sq = length * width
area_acres = area_sq/34560

print("the area of the field is",area_acres,"acres")