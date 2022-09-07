from argparse import ArgumentParser
from main import *
import pickle
from os import listdir
from os.path import isfile, join
from sys import argv
def parse_args(a):
    parser = ArgumentParser(description = "Generator of the Text.")
    parser.add_argument('--model', required = True)
    parser.add_argument('--prefix')
    parser.add_argument('--length', required = True, type = int)
    parser.add_argument('--K', type = int)
    return parser.parse_args(a)
N = parse_args(argv[1:])
mod = N.model
pref = N.prefix
l = N.length
K = N.K
if (K == None):
    K = 10**18 #k is infinite so the text is generated with the same k
               #that was used to train the model
if (pref == None):
    pref = []
else:
    pref = pref.split("_")
with open(mod, mode = "rb") as f:
    m = pickle.load(f)
s = ""
g = m.generate(pref, K, l)
for i in g:
    s += i + " "
print(s)
    
