def main(lang_):
        distance = 0
        dist_dict = {}
        dist_list = []
        for x in list(lang_):
                print("yay")
                for a in list(lang_):
                        L = len(a)
                        for i in range(L):
                                if a[i] != x[i]:
                                        distance += 1
                        dist_dict.update({(x,"vs",a):distance})
                        distance = 0
        count = 0
        for s in sorted(dist_dict.values()):
                if s == 0:
                        count += 1
                else:
                     dist_list.append(s)
        answr = dist_list[count]
        print('Dictionary of every Hamming length: ', dist_dict)
        print('Hamming length of alphabet: ', answr)
main()
