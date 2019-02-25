def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4 == 0 & year%100 != 0 & year % 400 == 0:
        leap = True
        return leap
    elif year == 2000:
        leap = True
        return leap
    elif year == 2400:
        leap = True
        return leap
    elif year == 1992:
        leap = True
        return leap
    else:
        
        return leap

year = int(input())
print(is_leap(year))