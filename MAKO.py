from mako.template import Template

SubjectName = "Walter"

#Set the template file to a variable
mytemplate = Template(filename='Mako-MyTemplate.txt')

#Fill in the variables
FilledTemplate =(mytemplate.render(ThisGuysName=SubjectName))

#Create a file:
FileName = "NamingNames.txt"
f=open(FileName,"w+")

#Write template data to the file created
f.write(FilledTemplate)

#Close file
f.close()