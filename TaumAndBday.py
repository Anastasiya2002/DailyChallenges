def taumBday(b,w,bc,wc,z):
   if bc+z<wc and wc+z<bc: 
      if bc+z < wc+z: 
        return b*bc+w*(bc+z)
      else:
         return w*wc+ b*(wc+z) 
   if bc+z<wc: 
       return b*bc+w*(bc+z)
   elif wc+z<bc:
       return w*wc+ b*(wc+z)
   return b*bc + w*wc

print(taumBday(10,10,1,1,1))