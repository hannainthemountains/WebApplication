import time
from datetime import date, datetime
import base64
import json
import demjson3
import random
import time


# Opening JSON file
f = open("C:\\temp\\Commutator.json")

# returns JSON object as
# a dictionary
Commutator = json.load(f)
# Commutator = demjson3.encode(Commutator)
AntennasDB = Commutator['AntennasDB']
# for item in AntennasDB:
    # print(type(item['CoPolBeamPattern']))
CoPolBeamPattern = AntennasDB[1]['CoPolBeamPattern']

st = time.time()
#CoPolBeamPatternDecoded = base64.b64decode(CoPolBeamPattern).decode("utf-8")
#CoPolBeamPatternDecoded = base64.b64decode(CoPolBeamPattern, '-_').decode("utf-8")
CoPolBeamPatternDecoded = base64.b64decode(CoPolBeamPattern)
et = time.time()
# get the execution time
print('Execution time:', et - st, 'seconds')

print(CoPolBeamPatternDecoded)
'''
time.sleep(5)

log = open("log.txt", 'a')

msg = 'Current user completed. Process ended! ' + str(datetime.now())
log.write(msg + "\n")

time.sleep(5)

msg = 'Current user completed. Process ended! ' + str(datetime.now())
log.write(msg + "\n")

time.sleep(5)

msg = 'Current user completed. Process ended! ' + str(datetime.now())
log.write(msg + "\n")

log.close()
'''