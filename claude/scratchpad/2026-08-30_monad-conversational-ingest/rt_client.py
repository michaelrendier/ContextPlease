import socket, sys, time

S = sys.argv[1]


def call(cmd, body=None):
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.settimeout(6)
    s.connect(S)
    f = s.makefile("rwb", buffering=0)
    f.write((cmd + "\n").encode())
    if body is not None:
        f.write((body + "\n").encode())
        f.write(b".\n")
    out = []
    try:
        for l in iter(f.readline, b""):
            if l.strip() == b".":
                break
            out.append(l.decode("utf8", "replace").rstrip())
    except socket.timeout:
        out.append("<TIMEOUT>")
    s.close()
    return out


def show(tag, lines):
    for o in lines:
        if "repack" in o or o == "<TIMEOUT>" or o.startswith("OK "):
            print(f"  [{tag}] {o}", flush=True)


show("pre", call("STATUS"))
big = "wandering god sedenion zero divisor box kite critical line " * 15  # ~870 B
for i in range(14):
    show(f"obs{i}", call("OBSERVE external", big))
show("post-burst", call("STATUS"))
print("  ... 5s for an idle sweep ...", flush=True)
time.sleep(5)
show("post-sweep", call("STATUS"))
print("  ... 20s silence (>2*TAU) — urgency should bleed toward 0 ...", flush=True)
time.sleep(20)
show("post-bleed", call("STATUS"))
