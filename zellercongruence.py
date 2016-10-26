y=int(input('Enter year:(e.g,2008):'))
m=int(input('Enter month: 1-12:'))
q=int(input('Enter the day of the month:1-31:'))

if m==1 or m==2:
    n=12
    m=m+n
    
j=y/100
k=y%100


h = int((((q + (26 * (m + 1) / 10) + k + (k/4) + (j/4) -(2*j)))% 7))

d = ((h+5)% 7)+1
if d==0:
    print('Saturday')
elif d==1:
    print('Sunday')
elif d==2:
    print('Monday')
elif d==3:
    print('Thuesday')
elif d==4:
    print('Wednesday')
elif d==5:
    print('Thrusday')
elif d==6:
    print('Friday')