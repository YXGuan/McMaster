# Brute force solution
import datetime
start_time = datetime.datetime.now()
[(a, b) for a in (1, 3, 5) for b in (2, 4, 6)] # example snippet
end_time = datetime.datetime.now()
print(end_time - start_time)
# timeit solution
import timeit
min(timeit.repeat("[(a, b) for a in (1, 3, 5) for b in (2, 4, 6)]"))
# cProfile solution
import cProfile
cProfile.run("[(a, b) for a in (1, 3, 5) for b in (2, 4, 6)]")