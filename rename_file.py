filenames = ['1.report', '2.document', '3.presentation', '4.slides']

filenames = [filename.replace('.', ':- ') + '.txt' for filename in filenames]
print(filenames)