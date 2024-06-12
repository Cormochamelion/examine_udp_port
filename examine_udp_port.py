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

output_file = "./examine_udp.txt"
request_pad_char = b"\x00"
payload_pad_char = b"\xfe"
response_pad_char = b"\xff"

with open(output_file, "wb") as out_con:
    for comb in combs:
        payload = (request_pad_char * 2) + comb + (request_pad_char * 7) + b"\x0a"
        nc.send(payload)
        # pad to 16 byte length for nicer presentation
        out_con.write(payload + (payload_pad_char * 4))
        recieved = nc.recv(12, timeout=2)
        out_con.write(recieved + (response_pad_char * 4))
