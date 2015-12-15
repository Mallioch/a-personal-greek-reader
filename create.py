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
        { 'filename_extension': '_treadmill', 'fontsize': '20', 'footnotesize': '17' },
        #The normal version
        { 'filename_extension': '', 'fontsize': '14', 'footnotesize': '12' },
        #If you want a third version, you can add it.
    ]

#You won't read the same texts I read, so create your own files in the "docs" directory and
#   add them here. They will be added to the output in the order you specify below.
subtextFilenames = [
    #{ 'file': 'eusebius_commentary_on_isaiah.tex', 'title': 'Eusebius, Commentary on Isaiah', 'version': '_0_1_1' },
    #{ 'file': 'lxx_psalms.tex', 'title': 'Psalms (LXX)', 'version': '_0_1_1' },
    #{ 'file': 'lxx_isaiah.tex', 'title': 'Isaiah (LXX)', 'version': '_0_1_1' },
    #{ 'file': 'lxx_habbakuk.tex', 'title': 'Habakkuk (LXX)', 'version': '_0_1_1' },
    { 'file': 'plato_euthyphro.tex', 'title': 'Plato, Euthyphro', 'version': '_0_2_0'},
    { 'file': 'theophilus_to_autolycus.tex', 'title': 'Theophylus to Autolycus', 'version': '_0_1_1' }
]
template = getTemplateText()

for doc in subtextFilenames:
    allSubtextData = ''
    allSubtextData = allSubtextData + '\n\n\n\n\n\n\n%----------------------------------'
    allSubtextData = allSubtextData + '\n%New File - ' + doc['file']
    allSubtextData = allSubtextData + getTextOfSubFile(doc['file'])

    for optionSet in docOptions:

        template = getTemplateText()
        output = template.replace('$text$', allSubtextData)
        output = output.replace('$title$', doc['title'])
        output = output.replace('$textsize$', optionSet['fontsize'])
        output = output.replace('$footnotesize$', optionSet['footnotesize'])

        outputFilename = doc['file'].replace('.tex', '') + optionSet['filename_extension']

        writeToFile(outputFilename + '.tex', output)

        call(['xelatex', outputFilename + '.tex'])
        #Yes, this needs to be called twice, for the TOC. Whacky.
        call(['xelatex', outputFilename + '.tex'])

        call(['cp', outputFilename + '.pdf', '/Users/ericsowell/Dropbox/Mobile/' + outputFilename + doc['version'] + '.pdf'])

        #call(['open', outputFilename + '.pdf'])

        call(['rm', outputFilename + '.aux'])
        call(['rm', outputFilename + '.log'])
        call(['rm', outputFilename + '.out'])
        call(['rm', outputFilename + '.tex'])
        call(['rm', outputFilename + '.toc'])
