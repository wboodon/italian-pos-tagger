f_input = open("data/original/it_isdt-ud-train.conllu", "r", encoding='utf8')
f_output = open("data/formatted/it_isdt-ud.train", "w", encoding='utf8')

for line in f_input.readlines():
    if line.strip() != "":
        if line[0] != "#":
            f_output.write(line)
    else:
        f_output.write("\n")

f_input.close()
f_output.close()