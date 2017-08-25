import csv

txt_file = r"task.txt"
csv_file = r"New.csv"

in_txt = csv.reader(open(txt_file, "rb"), delimiter = ',')
out_csv = csv.writer(open(csv_file, 'wb'))

out_csv.writerows(in_txt)
print 'done! go check your NewProcessedDoc.csv file'