import string

s = "VRPHWLPHV L ZDQW WR FKDW ZLWK BRX, EXW L KDYH QR UHDVRQ WR FKDW ZLWK BRX"
from_s = string.ascii_uppercase
for i in range(1, 26):
    to_s = from_s[i:] + from_s[:i]
    print string.translate(s, string.maketrans(from_s, to_s)).lower()
