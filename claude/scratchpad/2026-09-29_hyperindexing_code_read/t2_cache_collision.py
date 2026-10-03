"""T2: index_image caches the address by the first 16 (Data-Storage) / 32 (v09) values -> wrong address for a different image with the same prefix."""
import importlib.util
p='/home/rendier/Projects/ThePlace/PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hypergallery.py'
spec=importlib.util.spec_from_file_location('hg',p); hg=importlib.util.module_from_spec(spec); spec.loader.exec_module(hg)
s=hg.ImageSpec(8,8,hg.PixelMode.GRAY8); G=hg.HyperGallery(s)
a=[0]*64; b=[0]*64; b[63]=200          # differ only in the LAST pixel
ra=G.index_image(a,"a"); rb=G.index_image(b,"b")
print("labels equal:", ra.label==rb.label)
print("regenerate(b) == b:", G.regenerate_image(rb)==b, "; regenerate(b) == a:", G.regenerate_image(rb)==a)
