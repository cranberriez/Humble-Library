output = open("parsed.txt", 'w', encoding="utf-8")

with open("source.html",'r', encoding="utf-8") as f:
    output.truncate
    for line in f:
        if "<h2" in line:
            newline = line.split("\">")
            newline = newline[1].split("</")
            output.write(newline[0]+"\n")



output.close()