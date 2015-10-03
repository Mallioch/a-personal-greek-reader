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

docOptions = [
        { 'filename': 'reader_treadmill', 'fontsize': '20', 'footnotesize': '17' },
        { 'filename': 'reader', 'fontsize': '14', 'footnotesize': '12' },
    ]

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
