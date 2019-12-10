import argparse

parser = argparse.ArgumentParser(description='converter')
parser.add_argument('-in', '--indir', default= 2, type=str)
parser.add_argument('-out', '--outdir', type=str)
args = parser.parse_args()
print(args.indir)