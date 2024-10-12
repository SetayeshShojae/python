adad= list(map(int,input('lotfan_adad_vared_konid(ba_fasele_joda_konid)').split())) 
adad_zoj= list(filter(lambda adad: adad%2==0,adad)) 
print(f'adad_zoj:{adad_zoj}')