import sys

outFile = 'sample.csv'


print('Please input file will be opened:')
# [_, inputPath] = sys.argv
inputPath = input()
#%% def work for main reading
def  IsInteger(text: str) ->bool:
    try:
        int(text)
        return True
    except ValueError:
        return False
#%%read and clean file
with open(inputPath, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    newLines = []
    for i in range(0, len(lines), 10000):
        newLine = lines[i].replace('\n', '')
        col = newLine.split(',')
        for j in range(20, len(col)):
            if not IsInteger(col[j]):
                col[j] == 0
        newLine = ','.join(col)
        newLines.append(newLine)
    output = '\n'.join(newLines)
#%%create new file
with open(outFile,'w', encoding='utf-8') as file:
    file.write(output)