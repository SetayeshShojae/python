kharid_ha = {}
num_kharid = int(input("tedad kharid hara vared kon:"))
for _ in range("nam_kharid"): 
    kala = input("jens kharid ra vared kon:")
    andazeh = float(input("mablagehe kharid ra vared kon:"))
    if kala in kharid_ha:
        kharid_ha[kala] += andazeh
    else: 
         kharid_ha[kala] = andazeh
kol_hazine = sum(kharid_ha.values())
bodje = float(input("bodje mahane ra vared kon:"))

if kol_hazine > bodje:
    print("tavajo : majmoe hazine ha bishtar az bodje hast")
else:
    print("majmoe hazine ha dar mahdode bodje hast.")