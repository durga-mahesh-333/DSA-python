import time
import cProfile
from count_max_or_subsets.count_max_or_subsets import Solution
start_time = time.time()
sol=Solution()
cProfile.run('sol.countMaxOrSubsets([89260,58129,16949,64128,9782,26664,96968,59838,27627,68561,4026,91345,26966,28876,46276,19878])')
print(f'execution time : {time.time() - start_time}')