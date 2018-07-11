btidfilepath = '/home/anand/BTID_Issues_5258'  
sqlscriptfilepath = '/home/anand/Bug_5258_HDFC _lookup_entries_27091975.sql'
a = open(sqlscriptfilepath, 'r')
content = a.read()
w = open("/home/anand/Bug_5258_Scripts.sql","a+")
with open(btidfilepath) as fp:  
	for cnt, line in enumerate(fp):
		w.write("\n\n")
		w.write("#%d" % cnt + "--" + line)
		changedContent = content.replace("27091975", line.strip())
		w.write(changedContent)
		
		
