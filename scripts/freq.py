#################################################################################
#Script for calculating frequencies of types for a given file                   #
#input: Text file                                                               #
#Output: .freqs.tsv file        
# Adapted from: https://github.com/ximenina/theturningpoint/blob/main/Detailed/scripts/freq.py			                                #
#################################################################################

import os
import sys
from re import sub
import numpy as np
from collections import defaultdict, Counter
import re
import string 


inputcorpus=sys.argv[1]
myfile=open(inputcorpus,'r', encoding="utf-8")
output=inputcorpus+".freqs.tsv"
outputfile=open(output,'w', encoding="utf-8")
strings=myfile.read().split() #we normalize lower case, strip blank spaces at the beginning end.

frequency=Counter(strings)

#We print Frequencies:
for value, key in sorted([(j,i) for i,j in frequency.items()], reverse=True):
	if (key != ""):
		outputfile.write(str(key)+ '\t'+str(value)+'\n')

myfile.close()
outputfile.close()
