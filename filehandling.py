#copying a file
infile = open("selectionsort.py", "r")
outfile = open("output.txt", "w")
contents = infile.readlines()
outfile.writelines(contents)
infile.close()
outfile.close()

#strip new line character(\n)
contents =infile.readlines()  #gets rid off \n
for line in contents:
    s = line[:-1]
    print(line,end="") #end = "" removes the extra line that print adds while execution
#instead use rstrip() to remove all kind of whitespaces
for line in contents:
    s = line.rstrip()
#also strip()- both sides, lstrip() - from left
#if we have reached the end of file read() or readlines() will return empty string so once the file is read we cannot
#read it again until the file is closed and read again.
#if we use .write(line) it returns the number of characters in every line including \n as a character too.
#s.find(any other text strring, can also add range of posn to findlike 5,len(s))
# returns the first position in string s where that text occurs . it returns -1 if the string is not found.
# s. replace(fromstr,tostr) replaces every occurence of that string
# s.replace(fromstr,tostr,n) replaces first n occurence of string.