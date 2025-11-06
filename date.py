d = int(input("Enter the day: "))
m = int(input("Enter the month: "))
y = int(input("Enter the year: "))
print("Original date:", d, m, y)

add = int(input("Enter the number of days to add: "))
d = d + add
while(add!=0):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if d > 31:
            m = m + 1
            d = d - 31
            add=add-31
    elif m == 4 or m == 6 or m == 9 or m == 11:
        if d > 30:
            m = m + 1
            d = d - 30
            add=add-30
    elif m == 2:
        if ( y % 4 == 0):
            if d > 29:
                m = m + 1
                d = d - 29
                add=add-29
        else:
            if d > 28:
                m = m + 1
                d = d - 28
                add=add-28

 
    if m > 12:
        y = y + m // 12
        m = m % 12
        if m == 0:
            m = 12
            y = y - 1
    
    if(add<=30):
         
        break

print("Updated date:", d, ":", m, ":", y)
