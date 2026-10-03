"""T1: does HyperGallery.spectral_address_range bound the images satisfying the band constraint?
Brute force on a tiny spec: 2x2 pixels, 2 bands, 2-bit depth (N=4), n=8 values, 4^8=65536 images."""
import sys, itertools, importlib.util
p='/home/rendier/Projects/ThePlace/PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hypergallery.py'
spec=importlib.util.spec_from_file_location('hg',p); hg=importlib.util.module_from_spec(spec); spec.loader.exec_module(hg)
s=hg.ImageSpec(2,2,hg.PixelMode.SPECTRAL,n_bands=2,bit_depth=2)
G=hg.HyperGallery(s)
cons={0:(1,2)}                      # band 0 in [1,2] at every pixel
lo,hi=G.spectral_address_range(cons)
sat=[];inr=[]
for v in itertools.product(range(4),repeat=s.n_values):
    a=G._pixels_to_int(list(v))
    ok=all(cons[0][0]<=v[px*2+0]<=cons[0][1] for px in range(4))
    if ok: sat.append(a)
    if lo<=a<=hi: inr.append((a,ok))
print("range",lo,hi,"width",hi-lo+1)
print("images satisfying constraint:",len(sat))
print("satisfying images INSIDE range:",sum(lo<=a<=hi for a in sat))
print("images in range:",len(inr),"of which satisfy:",sum(o for _,o in inr))
print("satisfying set spans addresses",min(sat),"..",max(sat),"; count of maximal contiguous runs:",
      1+sum(1 for x,y in zip(sorted(sat),sorted(sat)[1:]) if y!=x+1))
