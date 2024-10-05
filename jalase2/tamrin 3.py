def masahet (tol ,arz): 
    return tol*arz 
def mohit (tol ,arz): 
    return 2*(tol+arz) 
tol=int(input('vared konid_tol :')) 
arz=int(input('vared konid_arz :')) 
s = masahet(tol,arz) 
p = mohit(tol,arz) 
print(f'masahat={s}') 
print(f'mohit={p}')