import headpy.hfile.hpickle as hpickle
import sys

filename = sys.argv[1]
output = hpickle.pkl_read(filename)
hpickle.pkl_dump(filename,output)
