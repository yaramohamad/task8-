n = int(input("number_of_loaves_of_day_old_bread: "))  
bread_price = 3.49   

def regular_price(b):  
    print("Regular price for the bread:")  
    print(b)  

def discount(d):  
    print("The discount because it is a day old:")  
    print(d)  

total_price = bread_price * n  
regular_price(total_price)  
 
discounted_price = total_price * 0.94  
discount(discounted_price)