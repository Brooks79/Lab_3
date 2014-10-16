# my file to open
text = open('C:\Users\Ray\Desktop\School\python\GIS_is_the_best.txt')
# the file 
document = text.read()
# blanket terms with null values to begin with
systems, science, total = 0, 0, 0
# telling it to search all the words and count each by adding 1 each time
for word in document.split(' '):
    
    if word.lower() == 'systems':
            systems = systems + 1
    elif word.lower() == 'science':
            science = science + 1
    else:
            total = total + 1
# adds the totals up
total = total + science + systems

print "Word Count Totals"
print ("\n")
print "'systems' is found = " + str(systems) 
print ("\n")
print "'science' is found = " + str(science) 
print ("\n")
print "Total words in the document = " + str(total)
print ("\n")

raw_input('Press the ENTER key to finish: ')






