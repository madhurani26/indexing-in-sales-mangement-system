import time
class c3:
    def __init__(self,li1=[],li2=[],al1=[],al2=[],al3=[]):
        con=''
        self.list1=li1
        self.list2=li2
        self.avllist1=al1
        file1=open(r"C:\Users\Madhurani L\Desktop\stu.txt","r")
        pos=file1.tell()
        line=file1.readline()
        length=len(line)
        a=line.split("|")
        leng=len(a[0])
        while line:
            if a[0][0]=="*" :
                var=""
                var=var+str(length)+"|"+str(pos)+"|"
                self.avllist1.append(var)
            
                
            pos=file1.tell()
            line=file1.readline()
            length=len(line)
            a=line.split("|")
            
            
        file2=open(r"C:\Users\Madhurani L\Desktop\stu1.txt","r")
        pos=file2.tell()
        line=file2.readline()
        while line:
            con=''
            a=line.split("|")
            con=con+str(a[0])+"|"+str(pos)+"|"
            if(a[0][0]!="*"):
               self.list1.append(con)
            pos=file2.tell()
            line=file2.readline()
        self.list1.sort()
        file2.close()
        
        con2=''
        file3=open(r"C:\Users\Madhurani L\Desktop\stu2.txt","r")
        pos=file3.tell()
        line=file3.readline()
        while line:
            con2=''
            a=line.split("|")
            con2=con2+str(a[0])+"|"+str(pos)+"|"
            if(a[0][0]!="*"):
               self.list2.append(con2)
            pos=file3.tell()
            line=file3.readline()
            
        self.list2.sort()
        file3.close()
        
    
    def inputs(self):
        self.region=input("enter region")
        self.country=input("enter country")
        self.itemtype=input("enter itemtype")
        self.saleschannel=input("enter saleschannel")
        self.orderpriority=input("enter orderpriority")
        self.orderdate=input('enter orderdate')
        self.orderid=input('enter orderid')
        self.shipdate=input('shipdate')
        self.unitsold=input('enter unitsold')
        self.unitprice=input('enter unitprice')
        self.unitcost=input('enter unitcost')
        self.totalrevenue=input('enter totalrevenue')
        self.totalcost=input("enter totalcost")
        self.totalprofit=input("enter totalprofit")
    def pack(self):
        self.inputs()
        pack1=""
        pack1=pack1+self.region+"|"+self.country+"|"+self.itemtype+"|"+self.saleschannel+"|"+self.orderpriority+"|"+self.orderdate+"|"+self.orderid+"|"+self.shipdate+"|"+self.unitsold+"|"+self.unitprice+"|"+self.unitcost+"|"+self.totalrevenue+"|"+self.totalcost+"|"+self.totalprofit+"|"
        file1=open(r"C:\Users\Madhurani L\Desktop\stu.txt","r+")
        length=len(pack1)
        if len(self.avllist1) !=0:
            for i in range (0,len(self.avllist1)):
                ab=self.avllist1[i].split("|")
                if(length<=int(ab[0])):
                    file1.seek(int(ab[1]))
                    file1.write(pack1)
                    file1.write("\n")
                    print(pack1)
                    p2=file1.tell()
                    l2=file1.readline()
                    len2=len(l2)
                    a=l2.split("|")
                    leng=len(a[0])
                    if leng==1:
                        first=a[0]
                        sec="|"
                        file1.seek(p2)
                        file1.write(l2.replace(first,"*"))
                        file1.seek(p2)
                        file1.write(l2.replace(sec,"*"))
                    else:   
                        first=a[0][0]
                        file1.seek(p2)
                        file1.write(l2.replace(first,"*"))
                    var=""
                    var=var+str(len2)+"|"+str(p2)+"|"
                    self.avllist1.append(var)
                    self.avllist1.sort()
                    file2=open(r"C:\Users\Madhurani L\Desktop\stu1.txt","r+")
                    position2=file2.tell()
                    line2=file2.readline()
                    while line2:
                        position2=file2.tell()
                        line2=file2.readline()
                    pack2=""
                    pack2=pack2+self.orderid+"|"+str(ab[1])+"|"
                    file2.write(pack2)
                    file2.write("\n")
                    file2.close()
                    char1=""
                    char1=char1+self.orderid+"|"+str(position2)
                    self.list1.append(char1)
                    self.list1.sort()
                    file3=open(r"C:\Users\Madhurani L\Desktop\stu2.txt","r+")
                    position3=file3.tell()
                    line3=file3.readline()
                    while line3:
                        position3=file3.tell()
                        line3=file3.readline()
                    pack3=""
                    pack3=pack3+self.itemtype+"|"+str(ab[1])+"|"
                    file3.write(pack3)
                    file3.write("\n")
                    file3.close()
                    char2=""
                    char2=char2+self.itemtype+"|"+str(position3)
                    self.list2.append(char2)
                    self.list2.sort()
                    return()
        self.position1=file1.tell()            
        line=file1.readline()
        while line:
            self.position1=file1.tell()
            line=file1.readline()
        
        file1.write(pack1)
        file1.write("\n")
        print(pack1)
        file1.close()
        file2=open(r"C:\Users\Madhurani L\Desktop\stu1.txt","r+")
        line2=file2.readline()
        while line2:
            line2=file2.readline()
        position2=file2.tell()
        pack2=""
        pack2=pack2+self.orderid+"|"+str(self.position1)+"|"
        file2.write(pack2)
        file2.write("\n")
        file2.close()
        char1=""
        char1=char1+self.orderid+"|"+str(position2)
        self.list1.append(char1)
        self.list1.sort()
        file3=open(r"C:\Users\Madhurani L\Desktop\stu2.txt","r+")
        line3=file3.readline()
        while line3:
            line3=file3.readline()
        position3=file3.tell()
        pack3=""
        pack3=pack3+self.itemtype+"|"+str(self.position1)+"|"
        file3.write(pack3)
        file3.write("\n")
        file3.close()
        char2=""
        char2=char2+self.itemtype+"|"+str(position3)
        self.list2.append(char2)
        self.list2.sort()
        
        
    def unpack(self):
         start_time = time.time()
         file1=open(r"C:\Users\Madhurani L\Desktop\stu.txt","r")
         line=file1.readline()
         a=line.split("|")
        
         while line:
             if(a[0][0]!="*"):
                 print("Region:",a[0])
                 print("Country:",a[1])
                 print("Itemtype: ",a[2])
                 print("Saleschannel: ",a[3])
                 print("Orderpriority:",a[4])
                 print("Orderdate:",a[5])
                 print("Orderid: ",a[6])
                 print("Shipdate: ",a[7])
                 print("Unitsold:",a[8])
                 print("Unitprice:",a[9])
                 print("Unitcost: ",a[10])
                 print("Totalrevenue: ",a[11])
                 print("Totalcost:",a[12])
                 print("Totalprofit:",a[13],"\n")
             line=file1.readline()
             a=line.split("|")
         file1.close()
         print("--- %s seconds ---" % (time.time() - start_time))
    def pors(self)  :   
         self.based=int(input("searched based on\n1.primarykey(orderid) \n2.secondary key(itemtype)"))
         
    def search(self):
        self.pors()
        if self.based==1:
            nam=input("enter orderid")
            
            self.flag=self.binarysearchp(nam)
            if(self.flag==-1):
                print("NOT THERE IN THE RECORD")
                return()
            else:
                listline=self.list1[self.flag]
                c=listline.split("|")
                self.position2=c[1]
                file2=open(r"C:\Users\Madhurani L\Desktop\stu1.txt","r+")
                file2.seek(int(self.position2))
                self.line2=file2.readline()
                self.b=self.line2.split("|")
                self.position1=self.b[1]
                file1=open(r"C:\Users\Madhurani L\Desktop\stu.txt","r+")
                file1.seek(int(self.position1))
                self.line1=file1.readline()
                self.length=len(self.line1)
                self.a=self.line1.split("|")
                self.Region=self.a[0]
                self.Country=self.a[1]
                self.Itemtype=self.a[2]
                self.Saleschannel=self.a[3]
                self.Orderpriority=self.a[4]
                self.Orderdate=self.a[5]
                self.Orderid=self.a[6]
                self.Shipdate=self.a[7]
                self.Unitsold=self.a[8]
                self.Unitprice=self.a[9]
                self.Unitcost=self.a[10]
                self.Totalrevenue=self.a[11]
                self.Totalcost=self.a[12]
                self.Totalprofit=self.a[13]
                print("Region:",self.a[0])
                print("Country:",self.a[1])
                print("Itemtype: ",self.a[2])
                print("Saleschannel: ",self.a[3])
                print("Orderpriority:",self.a[4])
                print("Orderdate:",self.a[5])
                print("Orderid: ",self.a[6])
                print("Shipdate: ",self.a[7])
                print("Unitsold:",self.a[8])
                print("Unitprice:",self.a[9])
                print("Unitcost: ",self.a[10])
                print("Totalrevenue: ",self.a[11])
                print("Totalcost:",self.a[12])
                print("Totalprofit:",self.a[13],"\n")
        elif self.based==2:
            self.nam=input("enter itemtype")
            self.flag=self.binarysearchs(self.nam)
            if(self.flag==-1):
                print("NOT THERE IN THE RECORD")
                return()
            else:
                pos=self.flag
                a=self.list2[self.flag].split("|")
                self.readfile(a[1])
                pos=pos-1
                n=self.list2[pos].split("|")
                while(str(n[0])==self.nam):
                    if(pos<0):
                        break
                    self.readfile(n[1])
                    
                    pos=pos-1
                    n=self.list2[pos].split("|")
                pos=self.flag+1
                if(pos+1<=len(self.list2)):
                    
                 n=self.list2[pos].split("|")
                
                 while(str(n[0])==self.nam):
                    
                    self.readfile(n[1])
                    pos=pos+1
                    if(pos+1>=len(self.list2)):
                        break
                    n=self.list2[pos].split("|")
    def readfile(self,pos):

                file3=open(r"C:\Users\Madhurani L\Desktop\stu2.txt","r+")
                file3.seek(int(pos))
                self.position3=int(pos)
                self.line3=file3.readline()
                self.b=self.line3.split("|")
                self.position1=self.b[1]
                file1=open(r"C:\Users\Madhurani L\Desktop\stu.txt","r+")
                file1.seek(int(self.position1))
                self.line1=file1.readline()
                self.length=len(self.line1)
                self.a=self.line1.split("|")
                if self.a[0][0]=="*":
                    return()
                self.Region=self.a[0]
                self.Country=self.a[1]
                self.Itemtype=self.a[2]
                self.Saleschannel=self.a[3]
                self.Orderpriority=self.a[4]
                self.Orderdate=self.a[5]
                self.Orderid=self.a[6]
                self.Shipdate=self.a[7]
                self.Unitsold=self.a[8]
                self.Unitprice=self.a[9]
                self.Unitcost=self.a[10]
                self.Totalrevenue=self.a[11]
                self.Totalcost=self.a[12]
                self.Totalprofit=self.a[13]
                print("Region:",self.a[0])
                print("Country:",self.a[1])
                print("Itemtype: ",self.a[2])
                print("Saleschannel: ",self.a[3])
                print("Orderpriority:",self.a[4])
                print("Orderdate:",self.a[5])
                print("Orderid: ",self.a[6])
                print("Shipdate: ",self.a[7])
                print("Unitsold:",self.a[8])
                print("Unitprice:",self.a[9])
                print("Unitcost: ",self.a[10])
                print("Totalrevenue: ",self.a[11])
                print("Totalcost:",self.a[12])
                print("Totalprofit:",self.a[13],"\n")
                return
    def modi1(self):
            #file3=open(r"C:\Users\Madhurani L\Desktop\stu2.txt","r+")
            #file2=open(r"C:\Users\Madhurani L\Desktop\stu1.txt","r+")
            file1=open(r"C:\Users\Madhurani L\Desktop\stu.txt","r+")
            file1.seek(int(self.position1))
            field=input("which fied u r writing\n1.region\n2.country\n3.itemtype\n4.saleschannel\n5.orderpriority\n6.orderdate\n7.self.orderid\n8.shipdate\n9.unitsold\n10.unitprice\n11.unitcost\n12.totalrevenue\n13.totalcost\n14.totalprofit")
            if field=="1":
                self.Region=input("enter 1 region")
            elif field=="2":
                self.Country=input("enter 2 country")
            elif field=="3":
                self.Itemtype=input("enter 3 itemtype")
            elif field=="4":
                self.Saleschannel=input("enter 4 saleschannel")
            elif field=="5":
                self.Orderpriority=input("enter 5 orderpriority")
            elif field=="6":
                self.Orderdate=input("enter 6 orderdate")
            elif field=="7":
                self.Orderid=input("enter 7 orderid")
                print("primary index cannot be modify")
                return 0
            elif field=="8":
                self.Shipdate=input("enter 8 shipdate ")
            elif field=="9":
                self.Unitsold=input("enter 9 unitsold")
            elif field=="10":
                self.Unitprice=input("enter 10 unitprice")
            elif field=="11":
                self.Unitcost=input("enter 11 unitcost")
            elif field=="12":
                self.Totalrevenue=input("enter 12 totalrevenue")
            elif field=="13":
                self.Totalcost=input("enter 13 totalcost")
            elif field=="14":
                self.Totalprofit=input("enter 14 totalprofit")
            
             
            self.var=""
            self.var=self.var+self.Region+"|"+self.Country+"|"+self.Itemtype+"|"+self.Saleschannel+"|"+self.Orderpriority+"|"+self.Orderdate+"|"+self.Orderid+"|"+self.Shipdate+"|"+self.Unitsold+"|"+self.Unitprice+"|"+self.Unitcost+"|"+self.Totalrevenue+"|"+self.Totalcost+"|"+self.Totalprofit+"|"
            length2=len(self.var)
            if(length2<=self.length):
               file1.seek(int(self.position1))
               file1.write(self.var)
               print(self.var)
               print("modify as been done")
               file1.close()
               return()
            else:
                return 1
    def modify(self):
        self.pors()
        file1=open(r"C:\Users\Madhurani L\Desktop\stu.txt","r+")
        file2=open(r"C:\Users\Madhurani L\Desktop\stu1.txt","r+")
        file3=open(r"C:\Users\Madhurani L\Desktop\stu2.txt","r+")
        
            
        if self.based==1:
            self.search()
            n=input(" if u want to modify enter yes ")
            if n=="yes":
             ret=self.modi1() 
             if ret==1:
                first = self.a[0][0]
                file1.seek(int(self.position1))
                pos1=self.position1
                file1.write(self.line1.replace(first,"*"))
                while self.line1:
                    self.position1=file1.tell()
                    self.line1=file1.readline()
                file1.seek(int(self.position1))
                file1.write(self.var)
                print("modify as been done")
                file1.write("\n")
                file1.close()
                first = self.b[0][0]
                file2.seek(int(self.position2))
                file2.write(self.line2.replace(first,"*"))
                while self.line2:
                    position2=file2.tell()
                    self.line2=file2.readline()
                file2.seek(int(position2))
                vara=""
                vara=vara+self.Orderid+"|"+str(self.position1)+"|"
                file2.write(vara)
                file2.write("\n")
                file2.close()
                del self.list1[self.flag]
                varaa=""
                varaa=varaa+self.Orderid+"|"+str(position2)+"|"
                self.list1.append(varaa)
                self.list1.sort()
                posi=file3.tell()
                line3=file3.readline()
                c=line3.split("|")
                
                posi=file3.tell()
                line3=file3.readline()
                c=line3.split("|")
                while line3:
                    if int(c[1])==int(pos1):
                        first = c[0][0]
                        file3.seek(int(posi))
                        file3.write(line3.replace(first,"*"))
                        break
                    posi=file3.tell()
                    line3=file3.readline()
                    c=line3.split("|")
                flag=self.delep(int(posi))
                del self.list2[flag]
                while line3:
                    posi=file3.tell()
                    line3=file3.readline()
                file3.seek(int(posi))
                vara=""
                vara=vara+self.Itemtype+"|"+str(self.position1)+"|"
                file3.write(vara)
                file3.write("\n")
                file3.close()
                lvar=""
                lvar=lvar+self.Itemtype+"|"+str(posi)+"|"
                
                self.list2.append(lvar)
                self.list2.sort()
                return
            
                
                
        elif self.based==2:
                nam=input("enter item")
                self.fla=self.binarysearchs(nam)
                if(self.fla==-1):
                    print("NOT THERE IN THE RECORD")
                else:
                    pos=self.fla
                    c=self.list2[self.fla].split("|")
                    self.readfile(c[1])
                    cond=input("if u want to modify this enter yes else enter no")
                    if(cond=="yes"):
                        ret=self.modi1()
                        if ret==1:
                            self.modi(c[1])
                    elif(cond=="no"):
                        pos=pos-1
                        a=self.list2[pos].split("|") 
                        while(str(a[0])==nam):
                            self.readfile(a[1])
                            cond=input("if u want to modify this enter yes else enter no")
                            if(cond=="yes"):
                                ret=self.modi1()
                                if ret==1:
                                    self.modi(a[1])
                                break
                            elif(cond=="no"):
                                pos=pos-1
                                if(pos<0):
                                    break
                            a=self.list2[pos].split("|")
                    pos=self.fla+1
                    if(pos<len(self.list2)):
                        n=self.list2[pos].split("|")
                        while(str(n[0])==nam):
                            self.readfile(n[1])
                            cond=input("if u want to delete this enter yes else enter no")
                            if(cond=="yes"):
                                ret=self.modi1()
                                if ret==1:
                                    self.modi(a[1])
                                break
                            elif(cond=="no"):
                                pos=pos+1
                                if(pos<=len(self.list2)):
                                    break
                            n=self.list2[pos].split("|")
                                
                
    def modi(self,lposition):
                file3=open(r"C:\Users\Madhurani L\Desktop\stu2.txt","r+")
                file2=open(r"C:\Users\Madhurani L\Desktop\stu1.txt","r+")
                file1=open(r"C:\Users\Madhurani L\Desktop\stu.txt","r+")
                
                self.position3=lposition
                file3.seek(int(self.position3))
                self.line3=file3.readline()
                self.b=self.line3.split("|")
                self.position1=self.b[1]
                posi1=self.position1
                first = self.b[0][0]
                file3.seek(int(self.position3))
                file3.write(self.line3.replace(first,"*"))
                file1.seek(int(self.position1))
                self.line1=file1.readline()
                self.a=self.line1.split("|")
                first = self.a[0][0]
                file1.seek(int(self.position1))
                file1.write(self.line1.replace(first,"*"))
                while self.line1:
                    self.position1=file1.tell()
                    self.line1=file1.readline()
                file1.seek(int(self.position1))
                file1.write(self.var)
                print(self.var)
                print("modify as been done:")
                file1.write("\n")
                file1.close()
                
                while self.line3:
                    self.position3=file3.tell()
                    self.line3=file3.readline()
                file3.seek(int(self.position3))
                vara=""
                vara=vara+self.Itemtype+"|"+str(self.position1)+"|"
                file3.write(vara)
                file3.write("\n")
                file3.close()
                varaa=""
                del self.list2[self.fla]
                varaa=varaa+self.Itemtype+"|"+str(self.position3)+"|"
                self.list2.append(varaa)
                self.list2.sort()
                pos=file2.tell()
                line=file2.readline()
                c=line.split("|")
                while line:
                    if int(c[1])==int(posi1):
                        first = c[0][0]
                        file2.seek(pos)
                        file2.write(line.replace(first,"*"))
                        break
                    pos=file2.tell()
                    line=file2.readline()
                    c=line.split("|")
                position=file2.tell()
                line=file2.readline()
                while line:
                    position=file2.tell()
                    line=file2.readline()
                file2.seek(int(position))
                vara=""
                vara=vara+self.Orderid+"|"+str(self.position1)+"|"
                file2.write(vara)
                file2.write("\n")
                file2.close()
                lvar=""
                lvar=lvar+self.Orderid+"|"+str(position)+"|"
                fla=self.binarysearchp(self.Orderid)
                del self.list1[fla]
                self.list1.append(lvar)
                self.list1.sort()
                return
        
    def delete(self):
        self.pors()
        if self.based==1:
            nam=input("enter orderid")
            flag=self.binarysearchp(nam)
            if(flag==-1):
                print("NOT THERE IN THE RECORD")
            else:
                file3=open(r"C:\Users\Madhurani L\Desktop\stu2.txt","r+")
                line=self.list1[flag]
                a=line.split("|")
                position2=int(a[1])
                file2=open(r"C:\Users\Madhurani L\Desktop\stu1.txt","r+")
                file2.seek(position2)
                line2=file2.readline()
                b=line2.split("|")
                first = b[0][0]
                file2.seek(int(position2))
                file2.write(line2.replace(first,"*"))
                position=b[1]
                file=open(r"C:\Users\Madhurani L\Desktop\stu.txt","r+")
                file.seek(int(position))
                line=file.readline()
                length1=len(line)
                st=""
                st=str(length1)+"|"+str(position)
                self.avllist1.append(st)
                self.avllist1.sort()
                a=line.split("|")
                first = a[0][0]
                file.seek(int(position))
                file.write(line.replace(first,"*"))
                file.close()
                del self.list1[flag]
                self.list1.sort()
                print(nam," as deleted")
                posi=file3.tell()
                line3=file3.readline()
                c=line3.split("|")
                while line3:
                    if int(c[1])==int(position):
                        first = c[0][0]
                        file3.seek(int(posi))
                        file3.write(line3.replace(first,"*"))
                        break
                    posi=file3.tell()
                    line3=file3.readline()
                    c=line3.split("|")
                flag=self.delep(int(posi))
                del self.list2[flag]
                return()
                    
                
                        
                
                
                
        if self.based==2:
            print("enter name")
            name=input()
            flag=self.binarysearchs(name)
            if(flag==-1):
                print("NOT THERE IN THE RECORD")
            else:
                pos=flag
                a=self.list2[flag].split("|")
                self.readfile(a[1])
                cond=input("if u want to delete this enter yes else enter no")
                if(cond=="yes"):
                    self.mark(pos)
                elif(cond=="no"):
                    pos=pos-1
                    a=self.list2[pos].split("|") 
                    while(str(a[0])==name):
                        self.readfile(a[1])
                        cond=input("if u want to delete this enter yes else enter no")
                        if(cond=="yes"):
                            self.mark(pos)
                            break
                        elif(cond=="no"):
                            pos=pos-1
                            if(pos<0):
                                break
                            a=self.list2[pos].split("|")
                    pos=flag+1
                    if(pos<len(self.list2)):
                        n=self.list2[pos].split("|")
                        while(str(n[0])==name):
                           self.readfile(n[1])
                           cond=input("if u want to delete this enter yes else enter no")
                           if(cond=="yes"):
                               self.mark(pos)
                               break
                           elif(cond=="no"):
                               pos=pos+1
                               if(pos<len(self.list2)):
                                   break
                               n=self.list2[pos].split("|")
    def delep(self,pos):
        lis=[]
        l=0
        r=len(self.list2)-1
        
        for i in range(0,r+1):
            a=self.list2[i].split("|")
            lis.append(a[1])
        
        
        while(l<=r):
            m=(l+r)//2
            if(pos==int(lis[m])):
                return m
            if(int(lis[m])<pos):
                l=m+1
            else:
                r=m-1
        
        return -1     
    def deles(self,pos):
        lis=[]
        l=0
        r=len(self.list1)-1
        
        for i in range(0,r+1):
            a=self.list1[i].split("|")
            lis.append(a[1])
        
        
        while(l<=r):
            m=(l+r)//2
            if(pos==int(lis[m])):
                return m
            if(int(lis[m])<pos):
                l=m+1
            else:
                r=m-1
        
        return -1                 
    def mark(self,pos):
        a=self.list2[pos].split("|")
        file2=open(r"C:\Users\Madhurani L\Desktop\stu1.txt","r+")
        file3=open(r"C:\Users\Madhurani L\Desktop\stu2.txt","r+")
        file3.seek(int(a[1]))
        line=file3.readline()
        b=line.split("|")
        position=b[1]
        first = b[0][0]
        file3.seek(int(a[1]))       
        file3.write(line.replace(first,"*"))
        file3.close()
        file1=open(r"C:\Users\Madhurani L\Desktop\stu.txt","r+")
        file1.seek(int(position))
        line=file1.readline()
        length=len(line)
        b=line.split("|")
        first = b[0][0]
        file1.seek(int(position))       
        file1.write(line.replace(first,"*"))
        print(b[2],",",b[6],",","as been deleted")
        file1.close()
        st=""
        st=str(length)+"|"+str(position)
        self.avllist1.append(st)
        self.avllist1.sort()
        del self.list2[pos]
        posi=file2.tell()
        line2=file2.readline()
        c=line2.split("|")
        while line2:
            if int(c[1])==int(position):
                        first = c[0][0]
                        file2.seek(posi)
                        file2.write(line2.replace(first,"*"))
                        break
            posi=file2.tell()
            line2=file2.readline()
            c=line2.split("|")
        flag=self.deles(int(posi))
        del self.list1[flag]
        
    def binarysearchp(self,nam):
        lis=[]
        l=0
        r=len(self.list1)
        
        for i in range(0,r):
            a=self.list1[i].split("|")
            lis.append(a[0])
        
        while(l<=r):
            m=(l+r)//2
            if(nam==lis[m]):
                return m
            if(lis[m]<nam):
                l=m+1
            else:
                r=m-1
        
        return -1 
    def binarysearchs(self,nam):
        lis=[]
        l=0
        r=len(self.list2)
        
        for i in range(0,r):
            a=self.list2[i].split("|")
            lis.append(a[0])
       
        while(l<=r):
            m=(l+r)//2
            if(nam==lis[m]):
                return m
            if(lis[m]<nam):
                l=m+1
            else:
                r=m-1
        
        return -1 
 
        
        
s=c3()  
n=int(input("1.pack \n2.unpack \n3.search \n4.modify \n5.delete"))
while(n!=6):
    if(n==1):
        s.pack()
    elif(n==2):
        s.unpack()
    elif(n==3):
        s.search()
    elif(n==4):
        s.modify()
    elif(n==5):
        s.delete()
    n=int(input("1.pack \n2.unpack \n3.search \n4.modify \n5.delete"))
    
        