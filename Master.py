import mysql.connector as pymysql
import datetime
import pickle
print('''Welcome to Library Management System
    Please enter your credentials to continue:''')

pas=input("enter password for root: ")
con = pymysql.connect(host = 'localhost' ,user = 'root' ,passwd = pas ,database = 'Library')
l=open("log.dat",'ab')
date0time=datetime.datetime()
d=date0time+"\n"
l.close()
cursor = con.cursor()
cursor.execute
def insert_user(a,b,c,d,):
    try:
        cursor.execute("INSERT INTO MEMBERS VALUES(",a,',',b,',',0,',',d,");")
        cursor.execute("ISERT INTO ISSUED VALUES(",a,",NULL,NULL,NULL);")
        myrecords=cursor.fetchall()
    except pymysql.errors.ProgrammingError:
        cursor.execute("""CREATE TABLE MEMBERS(UID INT(5) PRIMARY KEY,
        UNAME VARCHAR(15),
        DATEMISSUE DATE,
        DATEMEXPIRY DATE);""")
        cursor.execute("""CREATE TABLE ISSUED(UID INT(5) PRIMARY KEY,
        Book INT(5),
        ISSUEDON DATE,
        DUEBY DATE
        );""")
        insert_user(a,b,c,d)
def insert_book(a,b,c,d,e):
    try:
      cursor.execute("INSERT INTO BOOKS VALUES(",a,',',b,',',c,',',d,',',e,");")
      myrecords=cursor.fetchall()
    except pymysql.errors.ProgrammingError:
        cursor.execute("""CREATE TABLE BOOKS (IdCode INT(5) PRIMARY KEY,
        BName VARCHAR(15),
        BAuthor VARCHAR(15),
        PubYear INT(4),
        BCoverStyle CHAR(1));""")
        insert_book(a,b,c,d,e)
def update_Book_issue(a,b,c,d):
    cursor.execute("UPDATE ISSUED SET BOOK =",b,", ISSUEDON =",c,", DUEBY =",d,"WHERE UID =",a,';')
    myrecords=cursor.fetchall()
def locate_book():
    print("""Locate book by:
    1. Name
    2. Author
    3. Book ID
    4. Exit
    """)
    a= input("Enter your choice(No.) :")
    if (a==1):
        b = input("Enter Book name:")
        c= "%"+b+"%"
        cursor.execute("select* from BOOKS where BName=",c,';')
        myrecords=cursor.fetchall()
        for x in myrecords:
            print(x)
    elif (a==2):
        b = input("Enter Author name:")
        c= "%"+b+"%"
        cursor.execute("select* from BOOKS where BAuthor LIKE",c,';')
        myrecords=cursor.fetchall()
        for x in myrecords:
            print(x)
    elif (a==3):
        b=int(input("Enter book code :"))
        cursor.execute("select* from BOOKS where IdCode=",b,';')
        myrecords=cursor.fetchall()
        for x in myrecords:
            print(x)
    elif (a==4):
        break
    else:
        print("""Option not available... 
        Make sure you input the number corresponding to you're choice...""")
        locate_book()
def View_table():
    x=input("""Select which table to output:
    1. Members
    2. Books
    3. ISSUED""")
    if (x==1):
        a="MEMBERS"
    elif (x==2):
        a="BOOKS"
    elif (x==3):
        a="ISSUED"
    elif (a==4):
        break        
    else:
        print("""Option not available... 
        Make sure you input the number corresponding to you're choice...""")
        View_table()
    cursor.execute("select* from ",a,';')
    myrecords=cursor.fetchall()
    for x in myrecords:
        print(x)
def delete_user(a):
    cursor.execute("DELETE * FROM MEMBERS where UID=",a,';')
    cursor.execute("DELETE * FROM ISSUED where UID=",a,';')
    con.commit()
    print(cursor.rowcount,"record(s) deleted")
def del_book(a):
    cursor.execute("DELETE * FROM BOOKS where IdCode =",a)
    cursor.execute("UPDATE ISSUED SET BOOK = NULL, ISSUEDON = NULL , DUEBY = NULL WHERE BOOK =",a,';')
    con.commit()
    print(cursor.rowcount,"record(s) deleted")
def update_user(a,b,c):
    cursor.execute("UPDATE MEMBERS SET DATEMISSUE =",b,", DATEMEXPIRY =",c, "WHERE UID =",a,';')
    con.commit()
    print("Profile updated...")
def locate_user():
    print("""Locate user by:
    1. UID
    2. Initials
    3. Exit
    """)
    a=input("Enter your choice(No.) :")
    if (a==1):
        x= input("Enter UID :")
        cursor.execute("SELECT * FROM MEMBER WHERE UID =",x,';')
        myrecords=cursor.fetchall()
        for x in myrecords:
            print(x)
    elif (a==2):
        x= input("Enter initials :")
        y= "%"+x+"%"
        cursor.execute()
        myrecords=cursor.fetchall("SELECT * FROM MEMBER WHERE UNAME =",y,';')
        for x in myrecords:
            print(x)
    elif (a==3):
        break
    else:
        print("""Option not available... 
        Make sure you input the number corresponding to you're choice...""")
        locate_user()
while (option!=6):
    print("""Tables:
    1.Members
    2.Books
    3.Issued
    4.View table as a whole
    5.Open log""")
    option= int(input("Enter the table you wish to operate or enter '5' if you wish to exit:"))
    if (option == 1):
        print("""Available operations:
        1. Add Member
        2. Remove Member
        3. Show list of members
        4. Update Member details
        5. Back to tables list""")
        tab=int(input("Enter your choice(No.) :"))
        if (tab == 1):
            UID=int(input("Enter member id :"))
            UNAME=input("Emter member name :")
            DATEISSUE=input("Enter date of membership issue :")
            DATEEXPIRY=input("Enter date membership valid till :")
            insert_user(UID,UNAME,DATEISSUE,DATEEXPIRY)
        elif (tab == 2):
            UID=int(input("Enter id of member :"))
            delete_user(UID)
        elif (tab == 3):
            locate_user()
        elif (tab == 4):
            UID=int(input("Enter member id :"))
            DATEISSUE=input("Enter date of membership issue :")
            DATEEXPIRY=input("Enter date membership valid till :")
            update_user(UID,DATEISSUE,DATEEXPIRY)
        elif (tab == 5):
            break
        else:
            print("""Option not available... 
            Make sure you input the number corresponding to you're choice...""")
    elif(option == 2):
        print("""Available operations:
        1. Add Book
        2. Remove Book
        3. Show list of Books
        4. Back to tables list""")
        tab=int(input("Enter your choice(No.) :"))
        if(tab == 1 ):
            IdCode =int(input("Enter book code :"))
            BName  = input("Enter book name :")
            BAuthor = input("Enter author name :")
            PubYear = input("Enter year of publishing :")
            BCover = input("Enter book cover type (B/H) :")
            insert_book(IdCode,BName,BAuthor,PubYear,BCover)
        elif (tab == 2 ):
            IdCode=int(input("Enter book code :"))
            del_book(IdCode)
        elif (tab == 3):
            locate_book()
        elif (tab == 4):
            break
        else:
            print("""Option not available... 
            Make sure you input the number corresponding to you're choice...""")
    elif(option == 3):
        print("Available operation : Update an entry")
        y = ('y','Y')
        n = ('n','N')
        x=input("Continue? (y/n):")
        if (x in y):
            UID=int(input("Enter member id :"))
            BOOK=int(input("Enter book code :"))
            Issue=input("Enter issued date :")
            due=input("Enter due date :")
            update_Book_issue(UID,BOOK,Issue,due)
        elif (x in n):
            break
        else:
            print("Option not available...")
    elif(option == 4):
        View_table()
    elif(option == 5):
        f=open("log.dat",'rb')
        x=pickle.load(f)
        print(x)
    else:
        print("""Option not available... 
        Make sure you input the number corresponding to you're choice...""")
