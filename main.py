#import Day1.day1
#day2
print("welcome to the tip calculator.")
totalbill = float(input("what was the total bill? Rs."))
tip = int(input("what percentange tip would you like to give? 10 15 20?"))
people = int(input("how many people to split the bill?"))
tip_percent = tip / 100 
totaltip = totalbill * tip_percent 
totalbill = totalbill + totaltip 
sablaibill = totalbill / people 
final = round (sablaibill, 2)
print (f"Each person should pay: Rs. {final}")