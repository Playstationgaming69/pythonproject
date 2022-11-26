def clockangle(hour, minutes):
    if 00 <= hour <= 24 and 00 <= minutes <= 60:
        #converting thr 24hr format to 12 to make calculation esaier
        if hour > 12:
            hour = hour - 12
        #if user inputs 3:60 the program will assume the time as 4:00
        if minutes == 60:
            hour = hour + 1
            minutes = 00
        #calculating the angle
        hour = hour + minutes / 60
        handiff = abs(hour - minutes / 5)
        preangle = handiff * 30
        postangle = min(perangle, 360 - preangle)
        return postangle
    else:
        print("Enter a correct time.")
        exit()


print("__________________________________________\n")
print("Give a time in hh:mm format in 24hr notation")
print("__________________________________________\n")
postangle=clockangle(int(input("Hour: ")), int(input("Minutes: ")))
angle=format(postangle,".2f")
print("\nThe difference between the hour and the minute hand is", angle + "o")
