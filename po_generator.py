#Read in a po file and create flashcards based on the source and target strings
import polib
import sys
po = polib.pofile(sys.argv[1])
for entry in po:
        print(entry.msgstr.strip() + "\t" + entry.msgid.strip())
