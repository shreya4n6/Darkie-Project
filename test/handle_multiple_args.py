import sys
import statics

print(sys.argv)
engineList = []

argLen = len(sys.argv)
print(argLen)

i=0
while i < argLen:
    arg = sys.argv[i]
    if "-e" in arg:
        break
    i += 1
    
i += 1
while i < argLen:
    arg = sys.argv[i]
    if arg in statics.SEARCH_ENGINES:
        engineList.append(arg)
    else:
        print("Invalid engine name : ", arg)
        print("Current available search engines : ", statics.SEARCH_ENGINES)
        print()
    i += 1

print(engineList)