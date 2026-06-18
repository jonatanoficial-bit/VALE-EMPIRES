def clamp(v, lo=0, hi=100):
    return max(lo, min(hi, float(v)))

def social_stability(c):
    return round(clamp(c['morale']*.22+c['unity']*.24+c['faith']*.12+c['civil']*.14+c['arts']*.10+c['chroniclers']*.10-c['unrest']*.20-c['pressure']*.14))

base={'morale':58,'unity':52,'faith':46,'civil':45,'arts':30,'chroniclers':28,'unrest':22,'pressure':18}
assert social_stability(base)==36
festival={**base,'morale':67,'unity':59,'arts':32,'unrest':18}
assert social_stability(festival)>social_stability(base)
crisis={**base,'unrest':75,'pressure':70}
assert social_stability(crisis)<social_stability(base)
trained={**base,'chroniclers':45,'arts':44}
assert social_stability(trained)>social_stability(base)
print('F39 logic OK')
