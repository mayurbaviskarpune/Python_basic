import csv

def read_csv_file(samplefile):
    with open(samplefile,mode="r",newline='') as file:
        reader = csv.reader(file)
        for i in reader:
            print(i)

def write_csv_file(filename,data):
    with open(filename,mode="a",newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)





file = "demo.csv"
data=["baviskar","Mayur","pralhad"]
write_csv_file(file,data)
# read_csv_file(file)