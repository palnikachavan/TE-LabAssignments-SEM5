MNTAB = [['PICT', 3, 1], ['TE1', 2, 2], ['N1BATCH', 2, 3]]
PNTAB = [{'&T': 'P1', '&E': 'P2', '&S': 'P3'}, {'&F': 'P1', '&G': 'P2'}, {'&A': 'P1', '&B': 'P2'}]
KPDTAB = [{'&E': '', '&S': 'AREG'}, {}, {'&B': ''}]
MDTAB = [['MOVER AREG P1 ', 'ADD P1 P2 ', 'SUB P2 P1 ', 'MEND'], ['MOVER P1 P2 ', 'SUB P2 P1 ', 'MEND'], ['ADD P1 P2 ', 'MEND']]

macroCall = []
aptab = {}

for i in range(len(MNTAB)):
    macroCall.append(MNTAB[i][0])

with open('sourceCode.txt') as f2:
    codelines = f2.readlines()

f3 = open('output.txt', 'w')

index = 0
while index < len(codelines):
    if "MACRO" in codelines[index]:
        while "MEND" not in codelines[index]:
            index += 1
        index += 1

    else:
        if codelines[index].split()[0] in macroCall:
            serialNo = macroCall.index(codelines[index].split()[0])  # index of macro call
            aptabIdx = 1
            while aptabIdx < len(codelines[index].split()):
                aptab[f'P{str(aptabIdx)}'] = codelines[index].split()[aptabIdx].split('=')
                aptabIdx += 1
            if len(aptab) != MNTAB[serialNo][1]:
                kptabDict = KPDTAB[serialNo]
                for k, v in kptabDict.items():
                    temp3 = v[0] if v else None
                    if temp3 is not None and all(temp3 not in x for x in aptab.values()):
                        aptab[f'P{str(aptabIdx)}'] = [k, v]
                        aptabIdx += 1
            
            for i in range(len(MDTAB[serialNo]) - 1):
                mdttmp = MDTAB[serialNo][i].split()
                for word in mdttmp:
                    if word in aptab:
                        try:
                            # print(aptab[word][1])
                            f3.write(f"{aptab[word][1]} ")
                        except (IndexError, ValueError):
                            f3.write(f"{aptab[word][0]} ")
                    else:
                        f3.write(f"{word} ")
                f3.write('\n')
            index += 1
            print(f"APTAB for {macroCall[serialNo]}\n {aptab}")
            aptab.clear()
        else:
            f3.write(codelines[index])
            index += 1