"""2 - Write an algorithm (Vehicles.py) that, from reading and storing in vectors the commercial 
value of 20 vehicles and the type (family (1), public transportation (2), load (3)), calculate the new
value based on:

• For vehicles with a value greater than 100000, charge VAT of 20%, for others VAT is 16%
• For vehicles type 1, with value up to 50000, apply a discount equivalent to 50% of the VAT charged
• For vehicles type 2 and 3, with a value higher than 80000, apply an additional cost of 5%
• For all vehicles, if the final value is less than 80000, apply an additional discount 
of 5% of the commercial value"""

def vehicles_price():
    vehicles_price_type = []
    total_vehicles = 0

    while total_vehicles < 2:
        total_vehicles += 1
        vehicles_price = int(input(f"\nPlease, insert the vehicle {total_vehicles} price: "))
        vehicles_type = int(input(f"\nPlease, insert the vehicle {total_vehicles} type number" 
                              + " (family (1), public transportation (2), load (3): "))
        
        vehicle = {}
        vehicle["Vehicles_price"] = vehicles_price
        vehicle["Vehicles_type"] = vehicles_type

        vehicles_price_type.append(vehicle)

    for v in vehicles_price_type:   
        if v["Vehicles_price"] > 100000:
            vat = v["Vehicles_price"] * (20/100)
            new_value_vat = v["Vehicles_price"] + vat 
            v["Vehicles_price"] = new_value_vat
        else:
            vat = v["Vehicles_price"] * (16/100)
            new_value_vat = v["Vehicles_price"] + vat
            v["Vehicles_price"] = new_value_vat

        if (v["Vehicles_type"] == 1) and (v["Vehicles_price"] < 50000): 
            new_value = v["Vehicles_price"] - (vat * (50/100)) 
            v["Vehicles_price"] = new_value
        elif ((v["Vehicles_type"] == 2) or (v["Vehicles_type"] == 3)) and (v["Vehicles_price"] > 80000):
            new_value = (v["Vehicles_price"] * (5/100)) + v["Vehicles_price"]
            v["Vehicles_price"] = new_value
        
        if v["Vehicles_price"] < 80000:
            v["Vehicles_price"] = v["Vehicles_price"] - (v["Vehicles_price"] * (5/100))

    print(f"\nThe new comercial price of 20 vehicles are: \n {vehicles_price_type}.")        
        
vehicles_price()