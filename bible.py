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



#Open bible file in read mode

source = open('C:\\Users\\bradl\\OneDrive\\Documents\\Bible.txt')
bible = source.read()

#Regex to capture number of verses

verses = re.compile(r'''
(\d{1,3}[:]\d{1,3})         #Captures Verse Number                        
''', re.VERBOSE)



#TODO: Reges for Chapters

chapter_names = re.compile(r'''
([\n]{2,}           #starts with multiple returns
(\w+)               #followed by one word
((\s\w+)*          #followed by a space word zero or more times
([:  ]\w+\s{1,})*)
[\n]{2,})                   

''',re.VERBOSE)

#TODO: Extract Verses from text

extracted_verse_count = verses.findall(bible)
extracted_chapter_names = chapter_names.findall(bible)
print(extracted_chapter_names)

#TODO: Looping function

#TODO: Loop over each verse to see number of words per verse length
#TODO: Loop over each Chapter to see number of verses per chapter
#TODO: Multiply the number of words per verse and verses per chapter to get words per chapter?
#TODO: Put chapters in list/dictionary and sort by length?

#Close the source txt file
source.close()