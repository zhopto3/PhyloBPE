#Script that calculates productivity, idiosyncrasy, cumulative frequency for each subword. 
#Source: https://github.com/ximenina/BPEProductivity/blob/master/scripts/productivity.py


from collections import Counter
import sys
sys.stdout.reconfigure(encoding='utf-8')
import csv
import re

inputcorpus=sys.argv[1]  #BPE MODEL 
inputcorpus2=sys.argv[2]  #BPE freqsprod, e.g.,  o@@d@@o@@c@@o@@b	605
i=1

merge=[]
subwords=[]

####1. We read the BPE model
with open(inputcorpus,'r', encoding="utf-8") as myfile: 
	content = myfile.readlines()
	del content[0]
	for x in content:
		tmp=x.split()	
		merge.append(tmp)
			


for x in merge:
	subword =''.join(x)
	subwords.append(subword)  #contains the subword constructed at each merge (we remove the space)  iha nec</w> -> ihanec</w>    ce ba-->ceba

#print(len(subwords))


###2. We read the freqsprod file 
myfile=open(inputcorpus2,'r', encoding="utf-8")
with myfile as file_in:
	rows = []
	for row in file_in:
		if (not '"' in row):
        		rows.append(row)  #csv library is buggy, cannot deal with this: ", so we have to erase those lines

entries = list(csv.reader(rows, delimiter='\t'))  #Example: "o@@d@@o@@c@@o@@b	605"   (frequency of each word in the current merge)

words={}
for lines in entries:
	#print(lines)
	words[lines[0]]= int(lines[1]) 


#total_productivity=0
k=0;
for wsub in subwords:
	k=k+1
	counter_words=0
	cumulative_freq=0
	
	#If the subword it's at final word position:
	if (wsub.endswith("</w>")):
		wsub_aux = wsub.replace("</w>", "") #we eliminate the end of word symbol
		for w in words:
			if (w.endswith(wsub_aux)):    #if the subword is at the end of the word, then we take the frequency.
				#TRY THIS SO WHOLE WORDS ARE COUNTED
				if wsub_aux in w.split("@@"):
					printing_list=[wsub, w, words[w]]
					print(*printing_list, sep='\t')	   #TODO: fACTORIZE CODE!!!
					counter_words=counter_words+1
					cumulative_freq=cumulative_freq+words[w] #cumulative frequency of each type in which the subword appears
		if counter_words==0 & cumulative_freq==0:
			#No more occurences of this subword in the later merges.
			idiosyn=0
		else:
			idiosyn=cumulative_freq/(counter_words)

		printing_list=["subword:"+wsub,"productivity:"+str(counter_words), "cum_freq:"+str(cumulative_freq), "idiosyncrasy:"+ str(idiosyn)]
		print(*printing_list, sep='\t')

	#If the subword it's not at final word position subword (no <w>)
	else:
		for w in words:
			subword_split = w.split("@@")[:-1]
			if wsub in subword_split: 
				printing_list=[wsub, w, words[w]]
				print(*printing_list, sep='\t')	
				counter_words=counter_words+1
				cumulative_freq=cumulative_freq+words[w]  #cumulative frequency of each type in which the subword appears
		
		if counter_words==0 & cumulative_freq==0:
			#No more occurences of this subword in the later merges.
			idiosyn=0
		else:
			idiosyn=cumulative_freq/(counter_words)

		printing_list=["subword:"+wsub,"productivity:"+str(counter_words), "cum_freq:"+str(cumulative_freq), "idiosyncrasy:"+ str(idiosyn)]
		print(*printing_list, sep='\t')


