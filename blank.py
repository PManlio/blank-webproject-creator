#!/usr/bin/env python3
import os, sys

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
    open(os.path.join(dirname, 'index.html'), 'w')
    html = open(dirname+'/index.html', 'w+')
    htmltext='<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t<meta http-equiv="X-UA-Compatible" content="ie=edge">\n\t<link href="./css/mycss.css" rel="stylesheet" type="text/css">\n\t<title>Document</title>\n</head>\n<body>\n\n<script src="./js/main.js"></script>\n\t</body>\n</html>'
    html.write(htmltext)

    cssdir = dirname + "/css"
    open(os.path.join(cssdir, 'mycss.css'), 'w')
    css = open(cssdir+'/mycss.css', 'w+')
    css.write("html, body {margin: 0;}")

    jsdir = dirname + "/js"
    open(os.path.join(jsdir, 'main.js'), 'w')

def main():
    if len(sys.argv) > 2:
        print("Argument must be only one (it should be your project name).")
        exit()
    arg = sys.argv[1]
    # dirname = arg
    projectfolder(arg)

main()
