"""Write an algorithm to translate a time expressed 
in days, hours, minutes and seconds to time expressed in seconds."""

def days_to_second(): 

    t = input("Please, insert the time using this format days: hours: minutes: seconds: ")

    day = int(t.split(":")[0])
    day_s =  day * 86400
    

    hour = int(t.split(":")[1])
    hour_s = hour * 3600

    minutes = int(t.split(":")[2])
    minutes_s = minutes * 60

    seconds = int(t.split(":")[3])

    days_to_seconds = day_s + hour_s + minutes_s + seconds

    print(f"A time expressed in {t} is equivalent of {days_to_seconds} seconds!!")

days_to_second()
