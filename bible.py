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

def make_list(extracted_list_variable_name): #adds things to a list
    return [thing[0] for thing in extracted_list_variable_name]

def strip_nl(list_to_strip): #strips \nl from list output
    new_list = []
    for item in list_to_strip:
        new_item = item.strip('\nl')
        new_list.append(new_item)
    return new_list    

#########################################


#Open bible file in read mode

source = open('location.txt')
bible = source.read()

#Regex to capture number of verses

verses = re.compile(r'''
(\d{1,3}[:]\d{1,3})         #Captures Verse Number                        
''', re.VERBOSE)


#Reges for Chapter Names

chapter_names = re.compile(r'''
([\n]+              #starts with multiple returns
([A-Z][a-z]+)       #followed by one word
(\s\w+)*            #followed by a space word zero or more times
([:][ ]{,2}\w+)*    #followed by :, up to two spaces and a word zero or more times
(\s\w+)*            #followed by a space and word, zero or more times
([\n]{2,}))         #followed by 2 or more new lines         

''',re.VERBOSE)

#Extracted Data Variables

extracted_verse_count = verses.findall(bible)
extracted_chapter_names = chapter_names.findall(bible)

#Close the source txt file
source.close()

#Add chapters to list

chapter_list = make_list(extracted_chapter_names)

#Add Count of Chapters and Verses

count_of_chapters = len(extracted_chapter_names)
verses_count = len(extracted_verse_count)

#Clean Up List Output from Regex Search

clean_chapter_list = strip_nl(chapter_list)

#Output Operations

nl = '\n' #for output list to return each chapter on a new line

output = f'''
Found the Following Number of Verses {verses_count}.
Found the Following {count_of_chapters} Chapters
And the following Chapter Titles:
{nl.join(clean_chapter_list)}'''

pyperclip.copy(output)

new_doc = docx.Document()
new_doc.add_paragraph(pyperclip.paste())
new_doc.save('yourfilpath\filename.ext')
