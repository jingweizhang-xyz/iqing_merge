import os
import sys
import json
walk_dir = './volume106045/'
write_file = '10.txt'

final_str = ''

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

for root, subdirs, files in os.walk(walk_dir):
    print('--\nroot = ' + root)
    for oneFile in files:
        print('\tfile =' + oneFile)
        if oneFile.lower().endswith(".json"):
            filePath = os.path.join(root, oneFile)
            with open(filePath, 'r', encoding="utf-8") as f:
                print("\t\t yes")
                data = json.load(f, object_hook=JSONObject)
                # print(data)
                for obj in data:
                    print(obj)
                    if obj.type == 1:
                        print("\tdebug type 1")
                    elif obj.type == 0:
                        print("\tdebug type 2")
                        final_str += obj.value
                    final_str += "\n"
        else: 
            print("\t\t no")
            
    with open(write_file, 'w', encoding="utf-8") as f:
        f.write(final_str)



