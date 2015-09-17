"""
    write some annoying code to generate a byte[10] array and iterate through all the possibilities in either go or c
"""

variables = "ijklmnopqrstuv" 
c = False
go = True
for i in range(0,10):
    if c:
        print "while(1){"
    if go:
        var = variables[i]
        print "for ;;;{\n"


for i in range(0,10):
    if c:
        "bytes["+str(9-i)+"] += 1;\n print_bytes(bytes,10);\nif ( bytes["+str(9-i)+"] == UCHAR_MAX ){\n bytes["+str(9-i)+"] = 0; break;}}"
    if go:
        var = 9-i
        print "bytes["+str(var)+"] += 1\nif bytes["+str(var)+"] == 255 {\n\tbytes["+str(var)+"] = 0\n\tbreak\n}\n}\n"

