import csv
csv_file = input('Enter the name of your input file: ')
txt_file = input('Enter the name of your output file: ')

with open(txt_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        [ my_output_file.write("|".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()
# ======C:\\Users\\Madhurani L\\Downloads\\records.csv=======================================================================
# C:\\Users\\Madhurani L\\Desktop\\stu.txt
# =============================================================================
file1=open(r"C:\Users\Madhurani L\Desktop\stu.txt","r+")
file2=open(r"C:\Users\Madhurani L\Desktop\stu1.txt","r+")
file3=open(r"C:\Users\Madhurani L\Desktop\stu2.txt","r+")
position1=file1.tell()
line1=file1.readline()
while line1:
    a=line1.split("|")
    st=""
    st=st+str(a[6])+"|"+str(position1)+"|"
    file2.write(st)
    file2.write("\n")
    st3=""
    st3=st3+str(a[2])+"|"+str(position1)+"|"
    file3.write(st3)
    file3.write("\n")
    position1=file1.tell()
    line1=file1.readline()
file1.close()
file2.close()
file3.close()
    
    
    