import json
import re

def regCheck(partial):
    reg = re.compile(r"^[CAGTcagt]+$")
    if reg.search(partial):
        return True
    else:
        return False

def checkSequence(sequence):
    mutantSequences = ["AAAA", "CCCC", "GGGG", "TTTT"]
    sequence = sequence.upper()
    if any(x in sequence for x in mutantSequences):
        print('Mutant sequence found: ' + sequence)
        return True
    
    return False

def checkHorizontal(partial, count):
    countMutantSequences = count

    if checkSequence(partial):
        countMutantSequences = countMutantSequences + 1
        
    return countMutantSequences

def convertVertical(dna):
    rowsCount = len(dna)
    array = []

    #r to row
    #c to column
    for r in range(rowsCount):
        nuevoString = ""
        for c in range(rowsCount):
            nuevoString = nuevoString + dna[c][r]
        
        array.append(nuevoString)

    return array

def convertDiagonal(dna):
    rowsCount = len(dna)
    limit =  rowsCount - 3
    array = []

    #r to row
    #c to column
    #rCon to row counter
    #Diagonales medio e inferior
    for r in range(0, limit, 1):
        rCon = r
        nuevoString = ""
        for c in range(0, rowsCount, 1):
            nuevoString = nuevoString + dna[rCon][c]
            if rCon + 1 != rowsCount:
                rCon += 1
            else:
                break
        array.append(nuevoString)
    
    #r to row
    #c to column
    #cCon to column counter
    #Diagonales superiores
    for c in range(1, limit, 1):
        cCon = c
        nuevoString = ""
        for r in range(0, rowsCount, 1):
            nuevoString = nuevoString + dna[r][cCon]
            if cCon + 1 != rowsCount:
                cCon += 1
            else:
                break
        array.append(nuevoString)
    
    return array

def convertReverseDiagonal(dna):
    rowsCount = len(dna)
    limit =  rowsCount - 3
    array = []

    #r to row
    #c to column
    #rCon to row counter
    #Diagonal central e inferiores
    for r in range(0, limit, 1):
        rCon = r
        nuevoString = ""
        for c in range(rowsCount - 1, -1, -1):
            nuevoString = nuevoString + dna[rCon][c]
            if rCon + 1 != rowsCount:
                rCon += 1
            else:
                break
        array.append(nuevoString)
    
    #r to row
    #c to column
    #cCon to column counter
    #Diagonales superiores
    for c in range(rowsCount - 2, 2, -1):
        cCon = c
        nuevoString = ""
        for r in range(0, rowsCount - 1, 1):
            nuevoString = nuevoString + dna[r][cCon]
            if cCon - 1 != -1:
                cCon -= 1
            else:
                break
        array.append(nuevoString)

    return array

def isDna(dna):
    invalid = False

    dnaLen = len(dna)
    # Valida la longitud
    if dnaLen < 4:
        invalid = True

    for sequence in dna:
        # Validar cuadridula y longitud
        if len(sequence) != dnaLen:
            invalid = True
            break

        # Validar formato de ADN.
        if regCheck(sequence) == False:
            invalid = True
            break

    print('')
    print('')
    print('')
    if invalid:
        print('Invalid sequence.')
        return False
    else:
        print('Valid sequence.')
        return True

def isMutant(dna):
    # Validar ADN mutante.
    countMutantDna = 0
    
    # 1 step: search mutant sequences horizontally
    for row in dna:
        countMutantDna = checkHorizontal(row,countMutantDna)
        if countMutantDna == 2:
            break

    # 2 step: search mutant sequences vertically
    if countMutantDna < 2:
        dnaV = convertVertical(dna)
        for row in dnaV:
            countMutantDna = checkHorizontal(row,countMutantDna)
            if countMutantDna == 2:
                break

    # 3 step: search mutant sequences diagonally
    if countMutantDna < 2:
        dnaO = convertDiagonal(dna)
        for row in dnaO:
            countMutantDna = checkHorizontal(row,countMutantDna)
            if countMutantDna == 2:
                break

    # 4 step: search mutant sequences on reverse diagonal
    if countMutantDna < 2:
        dnaCO = convertReverseDiagonal(dna)
        for row in dnaCO:
            countMutantDna = checkHorizontal(row,countMutantDna)
            if countMutantDna == 2:
                break
    
    if countMutantDna == 2:
        return True
    else:
        return False

