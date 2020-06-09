# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 14:14:19 2020

@author: bradl
"""


#! python3

import re
import pyperclip


#TODO: Create a regular expression object for phone numbers
phone_number_regex = re.compile(r'''
#Phone number types 123-555-1234,123-5555,(123)-123-5555,(123) 123-1234,3333331234,123.123.1234,123-1234 ext 123, ext. 123, x1234           

(((\d\d\d) | (\(\d\d\d\)))?    #area code (optional)
(\.|\-|\s)                     #first separator
\d\d\d                         #first 3 digits
(\.|\-|\s)                     #second seperator
\d\d\d\d                       #last 4 digits
(((ext(\.)?\s)|x)              #extension word part (optional)
(\d{2,5}))?)                   #extension number (optional)           
           
''',re.VERBOSE)


#Create a regular expression object for email addresses

email_regex = re.compile(r'''
        [a-zA-Z0-9._%+-]+ #first part of the email
        @               # @ symbol
        [a-zA-Z0-9._-]+ # email domain
        \.              # period before .com etc
        [a-zA-Z0-9]{2,} # edu, com or other extension               

''',re.VERBOSE)

#Create a regular expression object for websites

website_regex = re.compile(r'''
(?i)                    #ignores case throughout
\b                      #looks for a continuous set of characters not broken by whitespace    
((?:https?://|          #may or may not start with a url protocol;
www\d{0,3}[.]|          #a www or host name 'mirror' domain;
[a-z0-9.\-]+[.]         #or a subdomain.
[a-z]{2,4}/)            #url domain
(?:[^\s()<>]+|          #the rest looks for page or seperator characters
\(([^\s()<>]+|
(\([^\s()<>]+\)))*\))+
(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|
[^\s`!()\[\]{};:'\".,<>?«»“”‘’])
)''',re.VERBOSE)

#Make a function that adds extracted text to a list    
def make_list(extracted_list_variable_name):
    new_empty_list = []
    for thing in extracted_list_variable_name:
        new_empty_list.append(thing[0])
    return new_empty_list


#Get the text off the clipboard

text = pyperclip.paste()

#Extract the email/phone/websites from the text

extracted_phone = phone_number_regex.findall(text)
extracted_email = email_regex.findall(text)
extracted_url = website_regex.findall(text)

#Add results to a list calling the make_list() function
all_phone = make_list(extracted_phone)
all_url = make_list(extracted_url)

#Copy the extracted email/phone numbers to the cliboard
    
output = 'Found Phone Numbers:' + '\n' + '\n'.join(all_phone) + '\n' + '\n' + 'Found Email Addresses:' + '\n' + '\n'.join(extracted_email) + '\n' + '\n' + 'Found URLs:' + '\n' + '\n'.join(all_url)
pyperclip.copy(output)
