#Read in a po file and create flashcards based on the source and target strings
#TODO:
#some sort of more 'fuzzy' duplicate detection - some strings are very similar - for now just using sort|uniq...
#remove numbers before duplicate detection?
#ignore anything with no Chinese characters
import polib
import sys
po = polib.pofile(sys.argv[1])
for entry in po:
        print(entry.msgstr.strip() + "\t" + entry.msgid.strip())
