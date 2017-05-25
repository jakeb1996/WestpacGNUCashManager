import sys
if len(sys.argv) == 3:
    fileIO = open(sys.argv[1], 'r')
    fileR = fileIO.read().split('\n')
    outStr = '{}\n'.format(fileR[0]) # keep !Type:<type> in the file

    i = 1
    leadingComma = False
    while i < len(fileR):
        if len(fileR[i]) > 1:
            # reformat from \n to commas
            outStr += '{}{},{}'.format((',' if leadingComma else ''), fileR[i][0], fileR[i][1:])
            leadingComma = True
        if fileR[i] == '^':
            # split each transaction by a line
            outStr += ',^\n'
            leadingComma = False
        i += 1

    # write the file
    output = open(sys.argv[2], 'w')
    output.write(outStr)
else:
    print "Usage is <QIF file location> <output file location>"
