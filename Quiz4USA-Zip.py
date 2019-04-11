import re

def main(file):
        f = open(file,"rt")
        corpus = f.read()
        f.close()
	
        pattern = re.compile("\d\d(\d)\d\d.(\w*)")
        li0 = []
        li1 = []
        li2 = []
        li3 = []
        li4 = []
        li5 = []
        li6 = []
        li7 = []
        li8 = []
        li9 = []

        for i in pattern.finditer(corpus):
                if i.group(1) == '0':
                        li0.append(i.group(2))
                elif i.group(1) == '1':
                        li1.append(i.group(2))
                elif i.group(1) == '2':
                        li2.append(i.group(2))
                elif i.group(1) == '3':
                        li3.append(i.group(2))
                elif i.group(1) == '4':
                        li4.append(i.group(2))
                elif i.group(1) == '5':
                        li5.append(i.group(2))
                elif i.group(1) == '6':
                        li6.append(i.group(2))
                elif i.group(1) == '7':
                        li7.append(i.group(2))
                elif i.group(1) == '8':
                        li8.append(i.group(2))
                elif i.group(1) == '9':
                        li9.append(i.group(2))
        nf = open("quiz 4.txt", 'wt')
        print(("0: ",li0,
               "1: ",li1,
               "2: ",li2,
               "3: ",li3,
               "4: ",li4,
               "5: ",li5,
               "6: ",li6,
               "7: ",li7,
               "8: ",li8,
               "9: ",li9),file=nf)
        nf.close()
                #print(nums)
        #print(sum(nums))
main("Quiz 04 - USA-Zip.csv")
