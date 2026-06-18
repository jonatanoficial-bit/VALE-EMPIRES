from math import isfinite

def clamp(v, mi=0, ma=100):
    return max(mi, min(ma, float(v or 0)))

def score(state):
    return round(clamp(state['reputation']*.28 + state['influence']*.20 + state['credibility']*.24 + state['propaganda']*.12 + state['defense']*.12 - state['disinformation']*.16 - state['foreignTension']*.08))

base={'reputation':54,'influence':34,'credibility':58,'propaganda':28,'disinformation':20,'defense':42,'foreignTension':18}
assert score(base)==40
success=base.copy()
for k,v in {'reputation':7,'credibility':6,'propaganda':2,'disinformation':-3}.items():
    success[k]=clamp(success[k]+v)
assert score(success)>score(base)
crisis=base.copy(); crisis['disinformation']=80; crisis['foreignTension']=60
assert score(crisis)<score(base)
for v in [score(base), score(success), score(crisis)]:
    assert isfinite(v) and 0 <= v <= 100
print('F38 logic checks OK')
