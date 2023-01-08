from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)

# open the text file in read mode
f = open("example.txt", "r")
 
# insert the texts in pdf
for txt in f:
    #pdf.cell(200, 10, txt = txt, ln = 1, align = 'C')
    pdf.multi_cell(200, 10, txt = txt, align = 'C')
  
# save the pdf with name .pdf
pdf.output('sample-from-file.pdf', 'F')
