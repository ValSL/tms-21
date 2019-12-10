import os, argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument('-dn', default='new_dir')
args = parser.parse_args()
current_dir = os.getcwd()
os.mkdir(f'{current_dir}/{args.dn}')
