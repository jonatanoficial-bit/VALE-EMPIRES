def clamp(v,minv=0,maxv=100):
    return max(minv,min(maxv,float(v)))

def chance(agent_power, network, infiltration, counter, secrecy, suspicion, heat, difficulty):
    base=42+agent_power+(network*.16)+(infiltration*.14)+(counter*.08)+(secrecy*.08)-suspicion*.16-heat*.18-difficulty
    return clamp(base,18,92)

assert chance(20,32,24,28,74,14,8,26) > 35
assert chance(12,10,10,10,20,90,90,58) == 18
assert chance(55,90,90,80,90,5,5,26) == 92
network=32
network=clamp(network+4)
assert network == 36
heat=8
suspicion=14
for _ in range(20):
    heat=clamp(heat-.015+(suspicion>70)*.012)
assert heat < 8
print('F37 logic checks OK')
