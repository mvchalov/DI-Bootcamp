try:
    f = open('nameslist.txt', 'r+')
    # Exercise 1
    # Read the file line by line
    line_by_line = list(map(lambda e: e[:-1], [e for e in f]))
    print(line_by_line)
    # Exercise 2
    # Read only the 5th line of the file
    f.seek(0)
    for i in range(5):
        line5 = f.readline()
    print("5th line:", line5)
    # Exercise 3
    # Read only the 13th first characters of the file
    f.seek(4)
    print("5th character:", f.read(1))
    # Exercise 4
    # Read all the file and return it as a list of strings. Then split each word
    # 1st part is done, the rest:
    split_lines = list(map(lambda e: [*e], line_by_line))
    print(split_lines)
    # Exercise 5
    # Find out how many occurrences of the names "Darth", "Luke" and "Lea" are in the file
    word_frequency = {}
    for i in line_by_line:
        if i in word_frequency.keys():
            word_frequency[i] += 1
        else:
            word_frequency[i] = 1
    print(line_by_line)
    chosen_word = line_by_line[0] or ''
    print(f"There are {word_frequency[chosen_word]} occurrences of word '{chosen_word}'")
    # Exercise 6
    # Append your first name at the end of the file
    f.seek(0, 2)
    f.write('\nMax')
    # Exercise 7
    # Append "SkyWalker" next to each first name "Luke"
    line_by_line.append('Max')
    f.close()
    lines_edited = map(lambda e: e + ' SkyWalker\n' if e == 'Luke' else e + '\n', line_by_line)
    f = open('nameslist.txt', 'w')
    for i in lines_edited:
        f.write(i)
    f.close()

except OSError as e:
    print("There's an I/O error", e)