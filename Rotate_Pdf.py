import pikepdf

old_pdf = pikepdf.Pdf.open("C:\Python_AK\Akash_CV.pdf")
for i in old_pdf.pages:
    i.Rotate = 180
    old_pdf.save("New_Pdf.pdf")