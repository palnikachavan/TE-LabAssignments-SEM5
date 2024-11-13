
from mnemonics import IS, DL, AD, REG

SYMBOL = {}
LITERAL = {}
POOL = []
code = []
lc = 0  # Initialize location counter

# Reading source code
with open('input.txt', 'r') as f:
    for line in f:
        line = line.replace(",", "")
        opcodeline = line.split()
        code.append(opcodeline)  # nested list

def AssemblerDirective(line, word):
    global lc
    if word.lower() == "start":  # start <number>
        try:
            lc = int(line[1])
        except (IndexError, ValueError):
            lc = 0
    elif word.lower() == 'end':
        for lit in LITERAL:
            if LITERAL[lit] == 'notset':
                LITERAL[lit] = str(lc)
                lc += 1
                POOL.append(list(LITERAL.keys()).index(lit) + 1)
    elif word.lower() == 'ltorg':
        for lit in LITERAL:
            if LITERAL[lit] == 'notset':
                LITERAL[lit] = str(lc)
                lc += 1
                POOL.append(list(LITERAL.keys()).index(lit) + 1)
    elif word.lower() == "equ":
        SYMBOL[line[0]] = SYMBOL[line[2]]
    elif (word.lower() == "origin"):
        if len(line) == 4 and line[2] == "+":
            symbol = line[1]
            increment = line[3]
            if symbol in SYMBOL:
                lc = int(SYMBOL[symbol]) 
            else:
                print("Symbol not found in SYMBOL table")
                return   
            try:
                increment_value = int(increment)
                lc += increment_value
            except ValueError:
                print("Increment value is not a valid number")
                return

def Declarative(line, word):
    global lc
    for w in line:
        if not w.isdigit() and w not in DL:
            if w not in SYMBOL:
                SYMBOL[w] = lc  # Update symbol table with lc address
    if word.lower() == "ds":
        if line[2].isdigit():
            lc += int(line[2])
    elif word.lower() == "dc":
        lc += 1  # DC allocates a single memory unit

f1 = open("intermediateCode.txt", "w")

# PASS 1
for line in code:
    if "EQU" in line:
        AssemblerDirective(line, "equ")
        f1.write(f"(S,{list(SYMBOL.keys()).index(line[0]) + 1}) " + AD[line[1]] + f" (S,{list(SYMBOL.keys()).index(line[2]) + 1}) \n")
        continue
    if "DS" in line:
        Declarative(line, "DS")
        f1.write(f"{DL[line[1]]} " + f"(C,{line[2]}) \n")
        continue
    if "DC" in line:
        Declarative(line, "DC")
        SYMBOL[line[0]] = lc  # Update symbol table with lc for DC statement
        f1.write(f"{DL[line[1]]} " + f"(C,{line[2]}) \n")
        lc += 1  # Increment lc for DC
        continue

    for word in line:
        if word in IS:
            lc += 1
            f1.write(IS[word] + " ")
        elif word in AD:
            AssemblerDirective(line, word)
            f1.write(AD[word] + " ")
        elif ("='" in word):
            LITERAL[word] = 'notset' 
            f1.write(f"(L,{list(LITERAL.keys()).index(word) + 1})" + " ")     
        elif word in REG:
            f1.write(REG[word] + " ")
        elif word in SYMBOL:
            f1.write(f"(S,{list(SYMBOL.keys()).index(word) + 1})" + " ")
        elif word.isdigit():
            f1.write(f"(C,{word}) ")
        else:
            if word == '+' or word == '-':
                f1.write(f"{word} ")
                continue
            if word not in SYMBOL:
                SYMBOL[word] = "notset"  # Add new symbols with current lc
            f1.write(f"(S,{list(SYMBOL.keys()).index(word) + 1}) ")
        

    f1.write("\n")
f1.close()

print(f'The location counter is {lc}')
print("Symbol Table\n", SYMBOL)
print("Literal Table\n", LITERAL)
print("Pool Table\n", POOL)


# # from mnemonics import IS, DL, AD, REG

# # SYMBOL = {}
# # LITERAL = {}
# # POOL = []
# # code = []
# # with open('input.txt', 'r') as f:
# #     for line in f:
# #         line = line.replace(",","")
# #         opcodeline = line.split()
# #         code.append(opcodeline)  # nested list

# # def AssemblerDirective(line, word):
# #     global lc        
# #     if word.lower() == "start":  # start <number>
# #         try:
# #             lc = int(line[1])
# #         except (IndexError, ValueError):
# #             lc = 0
# #     elif word.lower() == 'end':
# #         for lit in LITERAL:
# #             if LITERAL[lit] == 'notset':
# #                 LITERAL[lit] = str(lc)
# #                 lc += 1
# #                 POOL.append(list(LITERAL.keys()).index(lit) + 1)
# #     elif word.lower() == 'ltorg':
# #         for lit in LITERAL:
# #             if LITERAL[lit] == 'notset':
# #                 LITERAL[lit] = str(lc)
# #                 lc += 1
# #                 POOL.append(list(LITERAL.keys()).index(lit) + 1)
# #     elif word.lower() == 'origin':
# #         if len(line) == 4:
# #             symb = line[1]
# #             inc = line[3]
# #             if symb in SYMBOL:
# #                 lc = int(SYMBOL[symb])
# #             else:
# #                 print(f"Error: Symbol {symb} undefined")
# #                 return
# #             try:
# #                 increment_value = int(inc)
# #                 lc += increment_value
# #             except ValueError:
# #                 print("Increment value is not a valid number")
# #                 return
# #     elif word.lower() == "equ":
# #         SYMBOL[line[0]] = SYMBOL[line[2]]

# # def Declarative(line,word):
# #     global lc
# #     for w in line:
# #         if w.isdigit() == False and w not in DL:
# #             SYMBOL[w] = str(lc)
# #     if word.lower() == "DS":
# #         if line[2].isdigit():
# #             lc += int(line[2])

# # f1 = open("intermediateCode.txt", "w")
# # # PASS 1
# # for line in code:
# #     # print(line)
# #     if "EQU" in line:
# #         AssemblerDirective(line, "equ")
# #         f1.write(f"(S,{list(SYMBOL.keys()).index(line[0]) + 1}) " + AD[line[1]] + f" (S,{list(SYMBOL.keys()).index(line[2]) + 1}) \n")
# #         # f1.write("Done")
# #         continue
# #     if "DS" in line:
# #         Declarative(line, "DS")
# #         f1.write(f"{DL[line[1]]} " + f"(C,{line[2]}) \n")
# #         continue
# #     if "DC" in line:
# #         Declarative(line, "DC")
# #         f1.write(f"{DL[line[1]]} " + f"(C,{line[2]}) \n")
# #         continue
    
# #     for word in line:
# #         if word in IS:
# #             lc += 1
# #             # print(word)
# #             f1.write(IS[word] + " ")
            
# #         elif word in AD:
# #             AssemblerDirective(line, word)
# #             f1.write(AD[word]+ " ")
# #         elif ("='" in word):
# #             LITERAL[word] = 'notset' 
# #             f1.write(f"(L,{list(LITERAL.keys()).index(word) + 1})" + " ")     
# #         elif word in REG:
# #             # print(word)
# #             f1.write(REG[word] + " ")
# #         elif word in SYMBOL:
# #             # print(line)
# #             # print(word)
# #             f1.write(f"(S,{list(SYMBOL.keys()).index(word) + 1})" + " ")   
# #         elif word.isdigit():
# #             f1.write(f"(C,{word}) ")
# #         else:
# #             print(word)
# #             f1.write(f"{word} ")
            
# #     f1.write("\n")        
# # f1.close()
# # print(f'The location counter is {lc}')
# # print("Symbol Table\n", SYMBOL)
# # print("Literal Table\n", LITERAL)
# # print("Pool Table\n", POOL)


# # from mnemonics import IS, DL, AD, REG

# # SYMBOL = {}
# # LITERAL = {}
# # POOL = []
# # code = []
# # lc = 0
# # with open('input.txt', 'r') as f:
# #     for line in f:
# #         line = line.replace(",", "")
# #         opcodeline = line.split()
# #         code.append(opcodeline)  # nested list

# # def AssemblerDirective(line, word):
# #     global lc
# #     if word.lower() == "start":  # start <number>
# #         try:
# #             lc = int(line[1])
# #         except (IndexError, ValueError):
# #             lc = 0
# #     elif word.lower() == 'end':
# #         for lit in LITERAL:
# #             if LITERAL[lit] == 'notset':
# #                 LITERAL[lit] = str(lc)
# #                 lc += 1
# #                 POOL.append(list(LITERAL.keys()).index(lit) + 1)
# #     elif word.lower() == 'ltorg':
# #         for lit in LITERAL:
# #             if LITERAL[lit] == 'notset':
# #                 LITERAL[lit] = str(lc)
# #                 lc += 1
# #                 POOL.append(list(LITERAL.keys()).index(lit) + 1)
# #     elif word.lower() == 'origin':
# #         if len(line) == 4:
# #             symb = line[1]
# #             inc = line[3]
# #             if symb in SYMBOL:
# #                 lc = int(SYMBOL[symb])
# #             else:
# #                 print(f"Error: Symbol {symb} undefined")
# #                 return
# #             try:
# #                 increment_value = int(inc)
# #                 lc += increment_value
# #             except ValueError:
# #                 print("Increment value is not a valid number")
# #                 return
# #     elif word.lower() == "equ":
# #         SYMBOL[line[0]] = SYMBOL[line[2]]

# # def Declarative(line, word):
# #     global lc
# #     for w in line:
# #         if w.isdigit() == False and w not in DL:
# #             if w not in SYMBOL:
# #                 SYMBOL[w] = str(lc)
# #     if word.lower() == "ds":
# #         if line[2].isdigit():
# #             lc += int(line[2])

# # f1 = open("intermediateCode.txt", "w")
# # # PASS 1
# # for line in code:
# #     if "EQU" in line:
# #         AssemblerDirective(line, "equ")
# #         f1.write(f"(S,{list(SYMBOL.keys()).index(line[0]) + 1}) " + AD[line[1]] + f" (S,{list(SYMBOL.keys()).index(line[2]) + 1}) \n")
# #         continue
# #     if "DS" in line:
# #         Declarative(line, "ds")
# #         f1.write(f"{DL[line[1]]} " + f"(C,{line[2]}) \n")
# #         continue
# #     if "DC" in line:
# #         Declarative(line, "dc")
# #         f1.write(f"{DL[line[1]]} " + f"(C,{line[2]}) \n")
# #         continue

# #     for word in line:
# #         if word in IS:
# #             lc += 1
# #             f1.write(IS[word] + " ")
            
# #         elif word in AD:
# #             AssemblerDirective(line, word)
# #             f1.write(AD[word] + " ")
# #         elif ("='" in word):
# #             LITERAL[word] = 'notset' 
# #             f1.write(f"(L,{list(LITERAL.keys()).index(word) + 1})" + " ")     
# #         elif word in REG:
# #             f1.write(REG[word] + " ")
# #         elif word in SYMBOL or word.isalpha():
# #             if word not in SYMBOL:
# #                 SYMBOL[word] = 'notset'
# #             f1.write(f"(S,{list(SYMBOL.keys()).index(word) + 1})" + " ")
# #         elif word.isdigit():
# #             f1.write(f"(C,{word}) ")
# #         else:
# #             f1.write(f"{word} ")
            
# #     f1.write("\n")        
# # f1.close()

# # print(f'The location counter is {lc}')
# # print("Symbol Table\n", SYMBOL)
# # print("Literal Table\n", LITERAL)
# # print("Pool Table\n", POOL)


# from mnemonics import IS, DL, AD, REG

# SYMBOL = {}
# LITERAL = {}
# POOL = []
# code = []
# lc = 0  # Initialize location counter

# # Reading source code
# with open('input.txt', 'r') as f:
#     for line in f:
#         line = line.replace(",", "")
#         opcodeline = line.split()
#         code.append(opcodeline)  # nested list

# def AssemblerDirective(line, word):
#     global lc
#     if word.lower() == "start":  # start <number>
#         try:
#             lc = int(line[1])
#         except (IndexError, ValueError):
#             lc = 0
#     elif word.lower() == 'end':
#         for lit in LITERAL:
#             if LITERAL[lit] == 'notset':
#                 LITERAL[lit] = str(lc)
#                 lc += 1
#                 POOL.append(list(LITERAL.keys()).index(lit) + 1)
#     elif word.lower() == 'ltorg':
#         for lit in LITERAL:
#             if LITERAL[lit] == 'notset':
#                 LITERAL[lit] = str(lc)
#                 lc += 1
#                 POOL.append(list(LITERAL.keys()).index(lit) + 1)
#     elif word.lower() == 'origin':
#         if len(line) == 4:
#             symb = line[1]
#             inc = line[3]
#             if symb in SYMBOL:
#                 lc = int(SYMBOL[symb])
#             else:
#                 print(f"Error: Symbol {symb} undefined")
#                 return
#             try:
#                 increment_value = int(inc)
#                 lc += increment_value
#             except ValueError:
#                 print("Increment value is not a valid number")
#                 return
#     elif word.lower() == "equ":
#         SYMBOL[line[0]] = SYMBOL[line[2]]

# def Declarative(line, word):
#     global lc
#     for w in line:
#         if not w.isdigit() and w not in DL:
#             if w not in SYMBOL:
#                 SYMBOL[w] = lc  # Update symbol table with lc address
#     if word.lower() == "ds":
#         if line[2].isdigit():
#             lc += int(line[2])

# f1 = open("intermediateCode.txt", "w")
# # PASS 1
# for line in code:
#     if "EQU" in line:
#         AssemblerDirective(line, "equ")
#         f1.write(f"(S,{list(SYMBOL.keys()).index(line[0]) + 1}) " + AD[line[1]] + f" (S,{list(SYMBOL.keys()).index(line[2]) + 1}) \n")
#         continue
#     if "DS" in line:
#         Declarative(line, "DS")
#         f1.write(f"{DL[line[1]]} " + f"(C,{line[2]}) \n")
#         continue
#     if "DC" in line:
#         Declarative(line, "DC")
#         SYMBOL[line[0]] = lc  # Update symbol table with lc for DC statement
#         f1.write(f"{DL[line[1]]} " + f"(C,{line[2]}) \n")
#         lc += 1  # Increment lc for DC
#         continue

#     for word in line:
#         if word in IS:
#             lc += 1
#             f1.write(IS[word] + " ")
#         elif word in AD:
#             AssemblerDirective(line, word)
#             f1.write(AD[word] + " ")
#         elif ("='" in word):
#             LITERAL[word] = 'notset' 
#             f1.write(f"(L,{list(LITERAL.keys()).index(word) + 1})" + " ")     
#         elif word in REG:
#             f1.write(REG[word] + " ")
#         elif word in SYMBOL:
#             f1.write(f"(S,{list(SYMBOL.keys()).index(word) + 1})" + " ")
#         elif word.isdigit():
#             f1.write(f"(C,{word}) ")
#         else:
#             if word not in SYMBOL:
#                 SYMBOL[word] = lc  # Add new symbols with current lc
#             f1.write(f"(S,{list(SYMBOL.keys()).index(word) + 1}) ")

#     f1.write("\n")        
# f1.close()

# # Output tables for debugging
# print(f'The location counter is {lc}')
# print("Symbol Table\n", SYMBOL)
# print("Literal Table\n", LITERAL)
# print("Pool Table\n", POOL)

