"""Forward (PRNG/babelia.cpp) and inverse (imagesearch.cpp) with the published constants, in Python + gmpy2.
Checks: location->image->location, image->location->image, and whether two locations can share one image."""
import re, sys, time, random
import gmpy2
from gmpy2 import mpz
sys.set_int_max_str_digits(0)
D = "/home/rendier/Projects/ThePlace/Ainulindale/references/babel/"
def consts(path):
    out = {}
    for line in open(D + path):
        m = re.match(r'\s*static const boost::multiprecision::mpz_int (\w+)\("(\d+)"\);', line)
        if m: out[m.group(1)] = mpz(m.group(2))
    return out
P = consts("PRNG"); I = consts("imagesearch.cpp")
m, a, c, mk1, mk2, dv = (P[k] for k in ("m", "a", "c", "maskone", "masktwo", "divver")); ainv = I["ainverse"]
S1, S2, S3, S4 = 1098239, 698879, 1497599, 1797118          # shifts in the published source
Q = 399361                                                   # bits per quarter chunk; 33280 pixels * 12 = 399360 are drawn
def forward(loc):
    p = (a * mpz(loc) + c) % m
    p ^= p >> S1
    p ^= (p % mk1) << S2
    p ^= (p % mk2) << S3
    p ^= p >> S4
    return p
def inverse(p):
    p = mpz(p)
    p ^= p >> S4
    r = p ^ ((p % mk2) << S3); p = p ^ ((r % mk2) << S3)
    r = p ^ ((p % mk1) << S2)
    for _ in range(3): r = p ^ ((r % mk1) << S2)
    p = p ^ ((r % mk1) << S2)
    r = p ^ (p >> S1); r = p ^ (r >> S1); p = p ^ (r >> S1)
    x = (ainv * (p - c)) % m
    return x + m if x < 0 else x
def image_words(p):                                           # what the 8 quarters draw: 12-bit pixels, low 399360 bits of each chunk
    out = []
    for i in range(8):
        chunk = (p >> (Q * i)) % (mpz(1) << Q)                # divver = 2^399361
        out.append(chunk % (mpz(1) << 399360))                # the 399361st bit is never drawn
    return tuple(out)
rnd = random.Random(1)
print("m bits", int(gmpy2.bit_length(m)))
t = time.time(); L = mpz(rnd.getrandbits(3194890)) % m; p = forward(L); print("forward %.2fs" % (time.time() - t), "| p bits", int(gmpy2.bit_length(p)))
t = time.time(); L2 = inverse(p); print("inverse %.2fs" % (time.time() - t), "| inverse(forward(L)) == L:", L2 == L)
# image -> location -> image (what the search does, then the site displays)
img = image_words(p)
p_from_img = sum(w << (Q * i) for i, w in enumerate(img))     # imagesearch: chunks placed at 399361-bit offsets, dropped bits = 0
Lstar = inverse(p_from_img); print("search location == L:", Lstar == L, "| forward(search location) image == image:", image_words(forward(Lstar)) == img)
# do two locations share an image? flip a bit the image never reads and see whether the result is still a valid forward output
for name, pos in (("dropped bit of chunk 0", 399360), ("dropped bit of chunk 3", 3 * Q + 399360), ("top bit 3194890", 3194890)):
    p2 = p ^ (mpz(1) << pos); Lp = inverse(p2); ok = forward(Lp) == p2
    print("%-24s -> inverse gives a location: %s | forward(location) == that value: %s | distinct from L: %s | same image: %s" % (name, True, ok, Lp != L, image_words(p2) == img))
