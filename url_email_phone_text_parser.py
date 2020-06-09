# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 14:14:19 2020

@author: bradl
"""


#! python3

import re
import pyperclip


#Create a regular expression object for phone numbers
phone_number_regex = re.compile(r'''
#Phone number types 123-555-1234,123-5555,(123)-123-5555,(123) 123-1234,3333331234,123.123.1234,123-1234 ext 123, ext. 123, x1234           
(((\d{3}) | (\(\d{3\)))?       #area code (optional)
(\.|\-|\s)                     #first separator
\d{3}                          #first 3 digits
(\.|\-|\s)                     #second seperator
\d{4}                          #last 4 digits
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
    return [thing[0] for thing in extracted_list_variable_name]

#Make a function that counts the number of items returned from a list

def count_of_things(extracted_list_variable_name):
    return len([thing[0] for thing in extracted_list_variable_name])

#Get the text off the clipboard

text = pyperclip.paste()

#Extract the email/phone/websites from the text

extracted_phone = phone_number_regex.findall(text)
extracted_email = email_regex.findall(text)
extracted_url = website_regex.findall(text)

#Add results to a list calling the make_list() function for extractions with 2+ groups

all_phone = make_list(extracted_phone)
all_url = make_list(extracted_url)

#Get the count of items in each list

phone_number_count = len(all_phone)
email_count = len(extracted_email)
url_count = len(all_url)

#Copy the extracted email/phone numbers to the cliboard
nl = '\n'    
output = f'''
Found the Following {phone_number_count} Phone Numbers:
{nl.join(all_phone)}

Found the Following {email_count} Email Addresses:
{nl.join(extracted_email)}

Found the following {url_count} URLs:
{nl.join(all_url)}
'''

pyperclip.copy(output)
