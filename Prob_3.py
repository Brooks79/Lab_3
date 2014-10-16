# load the bad
bad_text = open('C:\Users\Ray\Desktop\School\python\GIS_is_the_best.txt')
# what it will end up being
how_it_should_be = bad_text.read()
# definitions for what to replace
def replace_all(text, dic):
        for i, j in dic.iteritems():
                text = text.replace(i, j)
        return text

my_text = how_it_should_be
# things to replace the wrong words with the word to replace it with after
reps = {'Science':'System','science':'system'}
# replaces ALL the words mentioned above with the word after the :
txt = replace_all(my_text, reps)
# the file to deposit the newly made correct file
out_file = open('C:\Users\Ray\Desktop\School\python\GIS_is_the_best_solved1.txt', 'w+')
# creates a file in that location
out_file.write (txt)
# writes the new file
out_file.close()
# Csaves the file
print out_file 
