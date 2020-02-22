import re
# r means raw, won't translate some backslash like \t

print('\tTAB')
print(r'\tTAB')

text_to_search="""
abcd
ABCD
312-321-5677
242-968-3995
123*343*9494
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
"""

Urls="""
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""

pattern= re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')
pattern1=re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
pattern2=re.compile(r'[a-zA-Z.-]+@[a-zA-Z-]+\.(com|edu|net)')
# use () to make group, for example group(2) is domain name, group(3) is .com | .gov
pattern3=re.compile(r'https?://(www.)?(\w+)(\.\w+)')

matches=pattern3.finditer(Urls)

for match in matches:
    print(match.group(3))

sub_url=pattern3.sub(r'\2\3',Urls)
print('how to use sub')
print(sub_url)

# pattern.match() VS pattern.search() 
# match only match the first, search match the whole string, but both cannot do line by line match like findall and finditer
sentence= 'Start a course on Monday'
pattern4=re.compile(r'Start')
matches=pattern4.match(sentence)
print(matches)
pattern5=re.compile(r'on')
matches=pattern5.search(sentence)
print(matches)

# add re.IGNORECASE or re.I to match word whether it's lowercase or uppercase

pattern6=re.compile(r'start',re.IGNORECASE)
matches=pattern6.search(sentence)
print(matches)
