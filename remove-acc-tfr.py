import sys
if len(sys.argv) == 3:
	transFile = open(sys.argv[1], "r")
	transFileSplit = transFile.read().split("^")

	outFile = open(sys.argv[2], "w")
	outFile.write(transFileSplit[0])

	removedCount = 0
	keptCount = 0
	for line in transFileSplit[1:-1]:
			
			trans = line.split("\n")
			#if len(trans) > 2:
			if "TFR" in trans[2]:
					removedCount += 1
			else:
					keptCount += 1
					outFile.write(line + '^')
					
	transFile.close()
	outFile.close()


	print str(len(transFileSplit))+ " transactions found."
	print str(keptCount) + " were kept."
	print str(removedCount) + " were removed."
	raw_input("Press any key to end...")
else:
	print "Usage is <file to remove TFR from> <output file>"