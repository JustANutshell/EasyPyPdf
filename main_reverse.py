import os
import sys
import pikepdf

keepopen = False

for filename in sys.argv[1:]:
    try:
        pdf = None
        try:
            pdf = pikepdf.Pdf.open(filename, allow_overwriting_input=True)
            pdf.pages.reverse()
            pdf.save(filename)
        finally:
            pdf.close()
    except Exception as e:
        print("Exception:"+str(e))
        print("")
        keepopen = True

if(keepopen):
    print("")
    os.system("pause")
