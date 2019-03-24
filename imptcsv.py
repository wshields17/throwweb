import psycopg2
conn = psycopg2.connect("host=localhost dbname=throwerdata user=postgres password=991550sp")
cur = conn.cursor()
import csv

with open('spthrows.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        name = row[0]
        spbest = row[1]
        bench = int(row[3])
        squat = int(row[4])
        pclean = int(row[5])
        print(name,spbest,bench,squat,pclean)
        
        cur.execute("""insert into throwersd(name,year,spbest,bp,squat,clean)values(%s, %s, %s,%s, %s, %s);""",(name,2018,spbest,bench,squat,pclean))
        conn.commit()
    cur.close()  
    conn.close()  
        