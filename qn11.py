#11. Create a variable, filename. Assuming that it has a three-letter
#extension, and using slice operations, find the extension. For
#README.txt, the extension should be txt. Write code using slice
#operations that will give the name without the extension. Does your
#code work on filenames of arbitrary length?

filename = 'readme.txt'
variable = ''
if '.' in filename:
    variable = filename[:-4]
print("filename without extension:",variable)