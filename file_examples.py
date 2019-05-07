# Read a file and print it to the console
def print_file(filename="sample.csv"):
    f = open(filename)
    contents = f.read()
    print(contents)
    f.close()


# Read a file and walk through it line by line
def walk_file(filename="sample.csv"):
    f = open(filename)
    for line in f:
        print(line, end="")
    f.close()


# Read a file, and write each line to a different file
# if that line contains the string "Teacher"
def write_new_file(infilename="sample.csv", outfilename="output.csv"):
    infile = open(infilename, "r")
    outfile = open(outfilename, "w")
    for line in infile:
        if "Teacher" in line:
            outfile.write(line)
    infile.close()
    outfile.close()
    return outfilename
