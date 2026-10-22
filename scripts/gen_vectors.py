"""ALU vectors from Python's arbitrary precision arithmetic, reduced to 32 bits."""
from pathlib import Path
import random

def main():
    rng=random.Random(20261022); mask=(1<<32)-1
    pairs=[(a,b) for a in (0,1,0x7fffffff,0x80000000,0xffffffff) for b in (0,1,0x7fffffff,0x80000000,0xffffffff)]
    pairs += [(rng.getrandbits(32),rng.getrandbits(32)) for _ in range(1000)]
    rows=[]
    for a,b in pairs:
        values=(a+b,a-b,a&b,a|b,a^b,a<<1,a>>1,0)
        for op,result in enumerate(values):
            rows.append(f'{a:x} {b:x} {op:x} {result&mask:x}')
    Path('build').mkdir(exist_ok=True)
    Path('build/vectors.txt').write_text('\n'.join(rows)+'\n')
    print(f'Generated {len(rows)} vectors, eight opcodes, seed=20261022')

if __name__=='__main__': main()
