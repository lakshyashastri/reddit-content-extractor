from extract import FILE_PATH

a_file = open(FILE_PATH, 'r')
lines=a_file.readlines()
a_file.close()

# see comment at end of file
with open(FILE_PATH, "w") as new_file:
    for line in lines:
        if line.split()!=[] and len(line.split())>4:
            new_file.write(line)

# update lines to new file
a_file = open(FILE_PATH, 'r')
lines=a_file.readlines()
a_file.close() 

lines_seen = set() # holds lines already seen
with open(FILE_PATH, "w") as outfile:
    for line in lines:
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)

# overall: to remove empty lines, lines with 4 or less words AND duplicate lines

# use and/or edit this however you want to modify the dataset to fit your conditions, if any