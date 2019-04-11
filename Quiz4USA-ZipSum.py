import re

def main(file):
        f = open(file,"rt")
        corpus = f.read()
        f.close()
	
        pattern = re.compile("\d(\d)\d(\d)\d")
        nums = []

        for i in pattern.finditer(corpus):
                if i.group(1) == i.group(2):
                        #print(i.group(1),i.group(2))
                        nums.append(int(i.group(1)))
                #print(nums)
        print(sum(nums))
main("Quiz 04 - USA-Zip.csv")
