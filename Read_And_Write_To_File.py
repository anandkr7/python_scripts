btidfilepath = '/home/anand/Support_Files/Bug_5258/Final/Lifestyle_BTIDs.txt'  
sqlscriptfilepath = '/home/anand/Support_Files/Bug_5258/Final/Content_Scripts_28_Panlow.sql'
a = open(sqlscriptfilepath, 'r')
content = a.read()
w = open("/home/anand/LifestyleResultFile.sql","a+")
with open(btidfilepath) as fp:  
	for cnt, line in enumerate(fp):
		w.write("\n\n")
		w.write("#%d" % cnt + "--" + line)
		changedContent = content.replace("27091983", line.strip())
		w.write(changedContent)
		
		
