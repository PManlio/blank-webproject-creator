import os
def projectfolder(dirname):
    try:
        os.mkdir(dirname)
        subfolder(dirname)

    except OSError as err:
        if err.errno == 17:
            print("Directory already exists.")
            main()
        else:
            print("Could not create folder.")
            main()
    else:
        print("Directory created.")


def subfolder(dirname):
    os.mkdir(dirname+"/css")
    os.mkdir(dirname+"/js")
    files(dirname)

def files(dirname):
    open(os.path.join(dirname, 'home.html'), 'w')
    html = open(dirname+'/home.html', 'w+')
    htmltext='<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t<meta http-equiv="X-UA-Compatible" content="ie=edge">\n\t<script src="./js/main.js"></script>\n\t<link href="./css/mycss.css" rel="stylesheet" type="text/css">\n\t<title>Document</title>\n</head>\n<body>\n\n</body>\n</html>'
    html.write(htmltext)

    cssdir = dirname + "/css"
    open(os.path.join(cssdir, 'mycss.css'), 'w')
    css = open(cssdir+'/mycss.css', 'w+')
    css.write("html, body {margin: 0;}")

    jsdir = dirname + "/js"
    open(os.path.join(jsdir, 'main.js'), 'w')

def main():
    dirname = input()
    projectfolder(dirname)

main()
