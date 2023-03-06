# We are being informed of three environmental temperature values, and we are asked to develop an 
# algorithm to  calculate and report the sum and average of these values.

def temperature_sum_avg(): 
    t1 = int(input("Please, insert the first temperature: "))
    t2 = int(input("Please, insert the second temperature: "))
    t3 = int(input("Please, insert the third temperature: "))
    
    sum_temp = t1 + t2 + t3
    print(f"The sum of all temperature are: {sum_temp}")
	
    avg_temp = (t1 + t2 + t3)/3
    print(f"The average of all temperature are: {avg_temp}")

temperature_sum_avg()

