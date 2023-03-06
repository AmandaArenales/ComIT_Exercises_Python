"""Translate a time expressed in seconds to a time expressed in 
days, hours, minutes and  seconds."""

def second_to_days():
    t = int(input("Please, insert the seconds: "))

    day = t // 86400
    
    hour = (t % 86400) // 3600
 
    minutes = ((t % 86400)%3600) // 60 
   
    seconds = (((t % 86400)%3600)%60)
	    
    print (f"Time {t} is igual day {day}, hour {hour}, minutes {minutes} and seconds {seconds}.")
    print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))

second_to_days()
