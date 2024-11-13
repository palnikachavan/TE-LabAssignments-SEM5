mnttab = []
pntab = []
kpdtab = []
mdttab = []

def macroProcessor(macrolines, start_idx):
    mntinfo = []
    mntLine = macrolines[start_idx].replace('\n', "").replace("="," ").split()
    mntinfo.append(mntLine[0])
    pntInfo = {}
    # print(mntLine)
    for i in range(len(mntLine)):
        if "&" in mntLine[i]:
            pntInfo[mntLine[i]] = "P" + str(i)
    mntinfo.append(len(pntInfo))
    # print(pntInfo)
    
    keyDict = {}
    temp = macrolines[start_idx].split()
    for i in range(len(temp)):
        if "=" in temp[i]:
            temp2 = temp[i].split('=')
            try: 
                keyDict[temp2[0]] = temp2[1]
            except (IndexError, ValueError):
                keyDict[temp2[0]] = 'notset'
    kpdtab.append(keyDict)
    
    mntinfo.append(len(kpdtab)) 
    mnttab.append(mntinfo)
    pntab.append(pntInfo)
    
    mdtinfo = []
    for i in range(start_idx + 1, len(macrolines)):
        mdtline = ''
        if "MEND" in macrolines[i]:
            mdtline = "MEND"
            mdtinfo.append(mdtline)
            mdttab.append(mdtinfo)
            return i
        else:
            macrolineArr = macrolines[i].replace(',','').split()
            for j in range(len(macrolineArr)):
                if macrolineArr[j] in pntInfo:
                    mdtline += pntInfo[macrolineArr[j]] + " "
                else:
                    mdtline += macrolineArr[j] + " "
            mdtinfo.append(mdtline)
    return len(macrolines)

macrolines = []
with open('sourceCode.txt') as f1:
    macrolines = f1.readlines()
    
# print(macrolines)
index = 0
while index < len(macrolines):
    line = macrolines[index]
    if "MACRO" in line:
        index = macroProcessor(macrolines, index + 1)
    else:
        index += 1
        
print(f"MNTAB \n{mnttab}")
print(f"PNTAB \n{pntab}")
print(f"KPDTAB \n{kpdtab}")
print(f"MDTAB \n{mdttab}")

# with open("pnt.txt", "w") as pnt:
#     for i in pntab:
#         print(i)
#         pnt.write(" ".join(i) + "\n")