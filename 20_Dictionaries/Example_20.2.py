eng2sp = {"one": "uno", "two": "dos", "three": "tres"}

for k in eng2sp.keys():
    print("Got Key {} which maps to value {}".format(k, eng2sp[k]))

# create a list of keys
ks = list(eng2sp.keys())
print(ks)

# default method for dictionary is keys()
for k in eng2sp:
    print("Got Key: {}".format(k))

# Put key and value into a tuple for later processing
for (k, v) in eng2sp.items():
    print("Got {} that maps to {}".format(k, v))

# Check for key in dictionary
"one" in eng2sp
