# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 14:45:01 2020

@author: bradl
"""

#Designed to be used with the text found here: http://www.gutenberg.org/cache/epub/10/pg10.txt
'''This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.org'''


import re, pyperclip, docx



##############FUNCTIONS#################

def make_list(extracted_list_variable_name):
    return [thing[0] for thing in extracted_list_variable_name]



#########################################


#Open bible file in read mode

source = open('C:\\Users\\bradl\\OneDrive\\Documents\\Bible.txt')
bible = source.read()

#Regex to capture number of verses

verses = re.compile(r'''
(\d{1,3}[:]\d{1,3})         #Captures Verse Number                        
''', re.VERBOSE)


#Reges for Chapter Names

chapter_names = re.compile(r'''
([\n]{2,}           #starts with multiple returns
(\w+)               #followed by one word
(\s\w+)*            #followed by a space word zero or more times
([:][ ]{,2}\w+)*    #followed by :, up to two spaces and a word zero or more times
(\s\w+)*            #followed by a space and word, zero or more times
([\n]{2,}))          #followed by 2 or more new lines         

''',re.VERBOSE)

#TODO: Extracted Data Variables

extracted_verse_count = verses.findall(bible)
extracted_chapter_names = chapter_names.findall(bible)

######for testing##########
#print(extracted_chapter_names)
#print(len(extracted_chapter_names))

#TODO: add chapters to list

chapter_list = make_list(extracted_chapter_names)
count_of_chapters = len(extracted_chapter_names)

verses_count = len(extracted_verse_count)


#Output Operations

nl = '\n'

output = f'''
Found the Following Number of Verses {verses_count}.
Found the Following {count_of_chapters} Chapters:
{nl.join(chapter_list)}'''

#pyperclip.copy(output)
#print(verses_count)
print(output)

#TODO: Loop over each verse to see number of words per verse length
#TODO: Loop over each Chapter to see number of verses per chapter
#TODO: Multiply the number of words per verse and verses per chapter to get words per chapter?
#TODO: Put chapters in list/dictionary and sort by length?
