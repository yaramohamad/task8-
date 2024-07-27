 
lst = []  
range1 = int(input("Enter the range: "))  

def is_sorted(lst):  
    for i in range(len(lst) - 1):  
        if lst[i] > lst[i + 1]: 
            return 'FALSE'  
    return 'TRUE'  

for o in range(range1):  
    num = int(input("is_sorted: "))   
    lst.append(num)  

ans = is_sorted(lst)  
print(ans) 