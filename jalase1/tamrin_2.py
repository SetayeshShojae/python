import random
number = random.randint(1,100)

while True :
    try:
        hads=int(input("adad khod ra vared konid"))
        if number >= hads:
                print("adad bozorg tare")
        elif number <=hads:
                print("adad kochek tare")
        else
                print("dorost hads zady")
    except ValueError :
                print("adad sahih vared kon")