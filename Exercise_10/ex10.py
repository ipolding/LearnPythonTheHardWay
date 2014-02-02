tabby_cat = "\tI'm \btabbed in"
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat fo\aod
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat + "for cat's who say %s" % tabby_cat

print "string %s " % "double quoted string with %r"
print "string %r " % "double quoted string with %s"


while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
