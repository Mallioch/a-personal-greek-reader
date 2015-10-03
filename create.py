import codecs
from subprocess import call

def writeToFile(path, contents):
    destination = codecs.open(path, 'w', 'utf-8')
    destination.write(contents)
    destination.close()

def getTemplateText():
    source = open('./personal_greek_reader.tex')
    return source.read()

def getTextOfSubFile(filename):
    source = open('./docs/' + filename)
    return source.read()




#Personalize below

#These are the supported font sizes: 8pt, 9pt, 10pt, 11pt, 12pt, 14pt, 17pt, and 20pt.
#See http://ctan.mackichan.com/macros/latex/contrib/extsizes/extsizes.pdf for more info.

docOptions = [
        #This one defines the filename and sizes for the large text version
        { 'filename': 'reader_treadmill', 'fontsize': '20', 'footnotesize': '17' },
        #The normal version
        { 'filename': 'reader', 'fontsize': '14', 'footnotesize': '12' },
        #If you want a third version, you can add it.
    ]

#You won't read the same texts I read, so create your own files in the "docs" directory and
#   add them here. They will be added to the output in the order you specify below.
subtextFilenames = ['eusebius_commentary_on_isaiah.tex', 'plato_euthyphro.tex']
template = getTemplateText()

allSubtextData = ''
for filename in subtextFilenames:
    allSubtextData = allSubtextData + '\n\n\n\n\n\n\n%----------------------------------'
    allSubtextData = allSubtextData + '\n%New File - ' + filename
    allSubtextData = allSubtextData + getTextOfSubFile(filename)

for optionSet in docOptions:

    template = getTemplateText()
    output = template.replace('$text$', allSubtextData)
    output = output.replace('$textsize$', optionSet['fontsize'])
    output = output.replace('$footnotesize$', optionSet['footnotesize'])

    writeToFile(optionSet['filename'] + '.tex', output)

    call(['xelatex', optionSet['filename'] + '.tex'])
    call(['rm', optionSet['filename'] + '.tex'])
    call(['rm', optionSet['filename'] + '.log'])
    call(['rm', optionSet['filename'] + '.aux'])

    call(['open', optionSet['filename'] + '.pdf'])
