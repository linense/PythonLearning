import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-display") # when invoking the script, the option -display is accepted
args = parser.parse_args()

print(args.display)

