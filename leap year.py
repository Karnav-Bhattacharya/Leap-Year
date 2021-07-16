def is_leap(year):
    leap = False
    # Logic

    if 1900<=year<=10**5:
        if year%4 == 0:
            if year%100 == 0 and year%400 == 0: return True
            elif year%100 == 0 and year%400 != 0: return False
            else: return True



        else: return False

    else:
        print("Please enter within the range of 1900 to 10^5")


    

    return leap

year = int(input("Enter the year you want to check for leap: "))

print(is_leap(year))