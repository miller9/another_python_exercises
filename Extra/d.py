data = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

# This script creates a file ".txt" and saves it with some text on it
# Open for 'w'riting
f = open('data.txt', 'w')
# Write text to file
f.write(data)
# Close the file
f.close()

# If no mode is specified,
# 'r'ead mode is assumed by default
f = open('data.txt')
while True:
    line = f.readline()
    # Zero length indicates EOF
    if len(line) == 0:
        break
    # The `line` already has a newline
    # at the end of each line
    # since it is reading from a file.
    print(line, end='')
# close the file
f.close()
