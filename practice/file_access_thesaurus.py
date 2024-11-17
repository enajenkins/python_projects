'''
Given a set of text files containing synonyms for different words, complete the main program to output the synonyms for a specific word. Each text file contains synonyms for the word specified in the file’s name, and each row within the file lists the word’s synonyms that begin with the same letter, separated by a space. The program reads a word and a letter from the user and opens the text file associated with the input word. The program then stores the contents of the text file into a dictionary predefined in the program. Finally the program searches the dictionary and outputs all the synonyms that begin with the input letter, one synonym per line, or a message if no synonyms that begin with the input letter are found.

Hints: Use the first letter of a synonym as the key when storing the synonym into the dictionary. Assume all letters are in lowercase.

Ex: If the input of the program is:

educate
c
the program opens the file educate.txt, which contains:

brainwash brief
civilize coach cultivate
develop discipline drill
edify enlighten exercise explain
foster
improve indoctrinate inform instruct
mature
nurture
rear
school
train tutor
then the program outputs:

civilize
coach
cultivate
Ex: If the input of the program is:

educate
a
then the program outputs:

No synonyms for educate begin with a.
'''

synonyms = {}   # Define dictionary

# Type your code here