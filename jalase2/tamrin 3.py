def masahet (tol ,arz): 
    return tol*arz 
def mohit (tol ,arz): 
    return 2*(tol+arz) 
tol=int(input("tol vared kon :")) 
arz=int(input("arz ra vared kon :")) 
m = masahet(tol,arz) 
l = mohit(tol,arz) 
print(f'masahat={m}') 
print(f'mohit={l}')