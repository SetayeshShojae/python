import random
number = random.randint(1,100)
while True:
     hads_number = input("az beyn 1 ta 100 yek number ra entekhab kon:")
     try:
        hash_number = int(hads_number)
     except ValueError:
         print("number sahih vared kon")
         continue
     if hads_number < 1 or hads_number >100:
         print("number 1 ta 100 basheh")
         continue
     if hads_number == number
     print("dorost gofty")
     break
     elif hads_number <= number:
        print("number bozorg tare")
     elif hads_number >= number:
        print("number kochek tare")