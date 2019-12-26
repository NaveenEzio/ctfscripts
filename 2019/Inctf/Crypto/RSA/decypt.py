from Crypto.Util.number import *

import gmpy2
from gmpy2 import *
import binascii
e= 65537
n= 149266147508816355003988434187305026105389099375967782218997969936976403940380316619745071899303760487488157860897030437398951376717513444388765481113360531722580212075571116454661564285569473655807490606674379748664882488458785248281874208340615796969795257211136199825307679034735206423765902911166558114230936248807511700515131247178437105036145151610662730431279753382694414717677759665923166370393702333405935986184632026073263050211159346569506878639942959520779957460401034049474243573659236616752848063659971596432819685017074243781230031780752146809101189516067040767613054997017089541051702913739460742678571


p=iroot(n/13,2)[0]

for i in range(1000):
	if n %(p-i)==0:
		p= p-i



q=n/p


cipher=int('b91d24ca213fbad4adce591805b855c8ad6540f0d3c27881325b1a45130d7ff7bdc8973830276bcbe19523b07d824e3a1a19fc901d6dc2333bf20de09b5d7ba10145578be29b42774c1792ebacf6205adad6324230024a19146a7c116c0c50bea3d05a0a8626f89f25d558437c11b1a7b34314fb67f3c63e08c9fad96145e48915aa6087f021de8a0c87d0ad498723373fc7d532a1513f3919cbb860383654df66a5cf418c1943fc028c08dc258d1369f4b9e23d45b890f896eac0bb3ffa041f1e1a71abdda14bb6e3c49e4065922c5280b696056f3d13acc72416e0403866b8f0391072c314463a1d66b2eea930b4d5e3f082c3fdfeb6dcc460c041ecfce201',16)



t = (p-1)*(q-1)


# returns d value such that e * d == 1 modulo t, or 0 if no such y exists.
d = gmpy2.invert(e,t)

# Decryption
decimalmessage = pow(cipher,d,n)
print(long_to_bytes(decimalmessage))

