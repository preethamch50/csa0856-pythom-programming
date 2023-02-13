#The year is divided into four seasons: spring, summer, fall and winter. While the exact dates that the seasons change vary a little bit from year to year because of the way that the calendar is constructed, we will use the following dates for this exercise: 
Sol:
month = input("Input the month (e.g. Jan, Feb etc.): ")
day = int(input("Input the day: "))

if(month=="Mar"and day>19)or(month=="Apr")or(month=="May")or(month=="Jun" and day<21):
    season = 'Summer'
elif(month=="Jun"and day>20)or(month=="Jul")or(month=="Aug")or(month=="Sep" and day<22):
    season = 'Spring'
elif(month=="Sep"and day>21)or(month=="Oct")or(month=="Nov")or(month=="Dec" and day<21):
    season = 'Fall'
else:
    season = 'winter'

print("The Season is currently",season)

Output:
Input the month (e.g. Jan, Feb etc.): Dec
Input the day: 25
The Season is currently winter
