from argparse import ArgumentParser
from main import *
import pickle #WHY???
from os import listdir
from os.path import isfile, join
from sys import argv
def parse_args(a):
    parser = ArgumentParser(description = "Enough.")
    parser.add_argument('--model')
    parser.add_argument('--input-dir')
    parser.add_argument('--K', type = int)
    return parser.parse_args(a)
N = parse_args(argv[1:])
mod = N.model
idir = N.input_dir
K = N.K
if (K == None):
    K = 2
if (mod == None):
    m = Model()
else:
    if (isfile(mod)):
        with open(mod, mode = "rb") as f:
            m = pickle.load(f)
    else:
        m = Model()
if (idir == None):
    txt = ""
    while True:
        inp = input()
        if (inp == ""):
            break
        txt += inp + "\n"
    m.fit(tokenize(txt), K)
else:
    for i in listdir(idir):
        if isfile(join(idir, i)):
            with open(join(idir, i), mode = 'r', encoding = "utf-8") as f:
                a = tokenize(f.read())
                m.fit(a, K)
if (mod == None):
    print(pickle.dumps(m))
else:
    with open(mod, mode = "wb") as f:
        pickle.dump(m, f)
    

