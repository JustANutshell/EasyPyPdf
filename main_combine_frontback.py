import os
import sys
from generalLib import CustomException, exception_traceback

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
    frontpages = []
    backpages = []

    if len(args) == 0:
        raise CustomException("no files given")

    for arg in args:
        if not arg.endswith(".pdf"):
            raise CustomException("wrong file format", arg)
        if arg.endswith(".front.pdf"):
            frontpages.append(arg[:-10])
        elif arg.endswith(".back.pdf"):
            backpages.append(arg[:-9])
        else:
            raise CustomException(
                "pdf file doesn't have .front.pdf oder .back.pdf", arg)

    out = []
    for x in frontpages:
        if x in backpages:
            backpages.remove(x)
            out.append(x)
        else:
            raise CustomException(
                "front file doesn't have a back file", x+".front.pdf")

    if len(backpages) != 0:
        raise CustomException("back file(s) do(es) not have front page", "\n".join(
            [x+".back.pdf" for x in backpages]))

    return out


def combine_one_file(filename):
    frontfilename = filename+".front.pdf"
    backfilename = filename+".back.pdf"

    print("using\n"+frontfilename+" as front\n"+str(backfilename)+" as back")

    try:
        front = pikepdf.Pdf.open(frontfilename)
        back = pikepdf.Pdf.open(backfilename)

        out = pikepdf.Pdf.new()

        l = len(front.pages)+len(back.pages)

        for i in range(0, l):
            thispage = None
            try:
                if(i % 2 == 0):
                    thispage = front.pages[i//2]
                else:
                    thispage = back.pages[i//2]
            except IndexError as e:
                raise CustomException("a file ends to soon")
            out.pages.insert(i, thispage)

        out.save(filename+".pdf")

    finally:
        front.close()
        back.close()
        out.close()


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
            combine_one_file(file)
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
