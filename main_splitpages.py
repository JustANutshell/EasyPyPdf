import os
import sys
from generalLib import CustomException, exception_traceback, requirefolder

try:
    import pikepdf
except ImportError as e:
    print("")
    print("Unable to import "+str(e.name))
    print("")
    os.system("pause")
    sys.exit()


def getfiles():
    args = sys.argv[1:]
    out = []

    if len(args) == 0:
        raise CustomException("no files given")

    for arg in args:
        if not arg.endswith(".pdf"):
            raise CustomException("wrong file format", arg)
        else:
            out.append(arg)

    return out


def splitpdf(filename):

    print("using\n"+filename)

    foldername = filename+" split\\"

    requirefolder(foldername)

    try:
        inp = pikepdf.Pdf.open(filename)

        l = len(inp.pages)

        for i in range(0, l):
            try:
                out = pikepdf.Pdf.new()
                try:
                    thispage = inp.pages[i]
                except IndexError as e:
                    raise CustomException("a file ends to soon")
                out.pages.insert(0, thispage)
                out.save(foldername+str(i)+".pdf")

            finally:
                out.close()

    finally:
        inp.close()


keepopen = False


def main():
    global keepopen

    try:
        files = getfiles()
    except CustomException as e:
        print("")
        print("ERROR: "+str(e.message))
        if(e.data != None):
            print(e.data)
        keepopen = True
        return

    for file in files:
        try:
            splitpdf(file)
        except CustomException as e:
            print("")
            print("ERROR: "+str(e.message))
            if(e.data != None):
                print(e.data)
            print("")
            print("")
            keepopen = True


try:
    main()
except Exception as e:
    print("")
    print("An Exception occured: "+str(e))
    print("")
    print(exception_traceback(e))
    keepopen = True

if(keepopen):
    print("")
    os.system("pause")
