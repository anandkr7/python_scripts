btidfilepath = '/home/anand/ListOfEntries'  
sqlscriptfilepath = '/home/anand/Content.txt'
a = open(sqlscriptfilepath, 'r')
content = a.read()
w = open("/home/anand/ResultFile.sql","a+")
with open(btidfilepath) as fp:  
	for cnt, line in enumerate(fp):
		w.write("\n\n")
		w.write("#%d" % cnt + "--" + line)
		changedContent = content.replace("Content", line.strip())
		w.write(changedContent)
		
		

