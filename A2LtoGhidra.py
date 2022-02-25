from ghidra.program.model.symbol import SourceType

file = open("5G0906259F.txt") #Here we open the A2L that we previously truncated

hi = currentProgram.getListing() #grab listing (whole BIN from Ghidra)
while True: # simple loop
    for line in file:
        printf(" start: ")
        firstline = file.next().rstrip() #grab first line of A2L
        splitter = firstline.split(',') #split each word in our line into an array
        address = splitter[2]  #We grab the Memory Address: [0] = Name & [1] = Translated Name & [2] Memory Address
        printf(address)
        addr = toAddr(address)
        d = hi.getDataAt(addr) #give the opened BIN file our Memory Address
        if d == None: #if our opened BIN file does not contain the Memory Address
            printf(" does not exist, skipping... ")
            continue
        if not d.isDefined(): #if it is defined in our A2L but not our BIN file we skip
            printf(" is not defined, skipping... ")
            continue
        name = splitter[0] #we grab name here
        #name.replace(" ", "")
        name2 = name.strip()
        d.getPrimarySymbol().setName(name2, SourceType.USER_DEFINED) #set address's name
        printf(" done ")
        continue
