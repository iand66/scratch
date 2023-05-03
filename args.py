import sys, getopt

# Usage: args.py -f filename -m message

print(sys.argv) # Array of command line parameters

opts, args = getopt.getopt(sys.argv[1:],"f:m", ['filname','message'])
print(opts)

for opt, arg in opts:
    print(opt, arg)

# with open(filename, 'w+') as f:
#     f.write(message) 