import sys
if len(sys.argv) == 3:
    fileIO = open(sys.argv[1], 'r')
    fileR = fileIO.read().split('\n')
    outStr = '{}\n'.format(fileR[0]) # add !Type:<type> back to top
    
    i = 1
    leadingComma = False
    while i < len(fileR):
        line = fileR[i].split(',')

        # join the property identify with its value
        j = 0
        while j < len(line):
            if len(line[j]) == 1 and line[j] != '^':
                outStr += '{}{}\n'.format(line[j], line[j + 1])
                j += 1
            if line[j] == '^':
                # end of transaction
                outStr += '^\n'
            j += 1

        i += 1
        
    # write the file
    output = open(sys.argv[2], 'w')
    output.write(outStr)
else:
    print "Usage is <CSV file location> <output file location>"
