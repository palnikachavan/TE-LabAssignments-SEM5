
from mnemonics import OPCODE
# Initialized SYMBOL with required values
# SYMBOL = {'N': 114, 'ONE': 116, 'TERM': 117, 'AGAIN': 104, 'TWO': 118, 'RESULT': 115}
# LITERAL = {}

SYMBOL = {'X': 131, 'Y': 133, 'A': 129, '+': 130, 'Z': 134, 'M1': 129}
LITERAL = {"='9'": '123', "='5'": '125', "='4'": '127'}
code = []
with open("intermediateCode.txt") as f1:
    for line in f1:
        if "AD" in line:
            continue
        else:
            subline = line.split()
            code.append(subline)

# Function to handle declarative statements (DS, DC)
def declareStatement(line):
    if "(DL,01)" in line:
        # Handle DC: Define Constant
        word = int(line[1].replace("(C,", "").replace(")", ""))
        word_str = str(word).zfill(3)
        f2.write(f"+ 00 00 {word_str}\n")
    elif "(DL,02)" in line:
        # Handle DS: Define Storage
        word = int(line[1].replace("(C,", "").replace(")", ""))
        while word > 0:
            f2.write("+ -- -- --- \n")
            word -= 1

# Opening the output file
with open('output.txt', "w") as f2:
    for line in code:
        if len(line) > 3:
            line = line[1:]
        if "(DL,01)" in line or "(DL,02)" in line:
            declareStatement(line)
        else:
            f2.write("+ ")
            for word in line:
                if word in OPCODE:
                    f2.write(OPCODE[word] + " ")
                elif "(S," in word:
                    sym = word.replace("(S,","").replace(")","")
                    upd = SYMBOL[list(SYMBOL.keys())[int(sym) - 1]]
                    f2.write(str(upd) + " ")
                elif "(L," in word:
                    sym = word.replace("(L,","").replace(")","")
                    upd = LITERAL[list(LITERAL.keys())[int(sym) - 1]]
                    # print(sym)
                    f2.write(str(upd) + " ")
                else:
                    f2.write(word + " ")
            f2.write("\n")
