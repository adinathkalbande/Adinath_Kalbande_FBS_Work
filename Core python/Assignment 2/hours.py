#Convert the time entered in hh,min and sec into seconds.
second = int(input("Enter Second ="))
temp = second

hours = temp//3600
temp = temp%3600

minute = temp//60
temp = temp%60

remaining_second = temp // 3600
temp = temp % 3600

print(f'Hours : {hours}, Minutes : {minute}, Remaining Minutes = {remaining_second} ')
