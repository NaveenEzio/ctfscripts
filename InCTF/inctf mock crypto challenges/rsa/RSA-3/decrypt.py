from libnum import n2s
from gmpy2 import iroot
e = 3


c = 8592189941159194019638374656645314531794594817969276219719896262783399305078321272446425694560466488324588008584076180132234252901623431284180375307325469386945048638649767716875964468502011502602465017301218485372246561864464961807262025394637518776430733413


m = iroot(c,e)
print n2s(m[0])