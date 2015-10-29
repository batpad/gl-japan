
TEMPLATE_FILE = 'template.json'

def do(lang_name):
    txt = open(TEMPLATE_FILE).read()
    new_txt = txt.replace("<LANGUAGE>", lang_name)
    out = open("%s.json" % lang_name, "w")
    out.write(new_txt)
    out.close()
        
