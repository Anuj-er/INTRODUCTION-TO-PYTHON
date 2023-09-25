import itertools
def removeConsecutiveDuplicates(s1):
     return (''.join(i for i, _ in itertools.groupby(s1)))