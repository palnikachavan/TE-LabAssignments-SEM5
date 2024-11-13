# Dictionary
IS = {
"STOP":  "(IS,00)",     # STOP
"ADD"  : "(IS,01)",     # ADD AREG, Breg
"SUB" :"(IS,02)",       # SUB AREG, Breg
"MULT" : "(IS,03)",     # MULT AREG, Breg
"MOVER" : "(IS,04)",    # MOVER AREG, Breg
"MOVEM" : "(IS,05)",    # MOVEM AREG, Breg
"CMP" : "(IS,06)",      # CMP AREG, Breg
"BC" : "(IS,07)",       # BC symb, symb
"DIV" : "(IS,08)",      # DIV AREG, Breg
"READ" : "(IS,09)",     # READ  AREG
"PRINT" : "(IS,10)",    # PRINT AREG
}

REG = {
    "AREG" : "(R,01)",
    "BREG" : "(R,02)",
    "CREG" : "(R,03)",
    "DREG" : "(R,04)"
}

AD = {
"START"  : "(AD,01)",
"END" :  "(AD,02)",
"ORIGIN" :  "(AD,03)",
"EQU" : "(AD,04)",
"LTORG" : "(AD,05)"
} 

DL = {
"DC" : "(DL,01)",
"DS" : "(DL,02)"
}


OPCODE ={
"(IS,00)" : "00 00 000",
"(IS,01)" : "01",
"(IS,02)" : "02",
"(IS,03)" : "03",
"(IS,04)" : "04",
"(IS,05)" : "05",
"(IS,06)" : "06",
"(IS,07)" : "07",
"(IS,08)" : "08",
"(IS,09)" : "09",
"(IS,10)" : "10",
"(R,01)" : "01",
"(R,02)" : "02",
"(R,03)" : "03",
"(R,04)" : "04"
}

