import requests, csv, json, argparse
from bs4 import BeautifulSoup

file_name = "utd_pmi"

def get_content():
    url = "http://ayodonor.pmi.or.id/table.php"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    tableRow = soup.select("table tbody tr")
    return tableRow

def to_csv(tableRow):
    with open(file_name + ".csv", mode="w") as utd_pmi_file:
        utd_pmi_writer = csv.writer(utd_pmi_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        for item in tableRow:
            column = item.select("td")
            row = []
            for col in column:
                row.append(col.text)
            utd_pmi_writer.writerow(row)

def to_json(tableRow):
    jsons = []
    for item in tableRow:
        column = item.select("td")
        jsons.append({
            "no": column[0].text,
            "nama_utd": column[1].text,
            "provinsi": column[2].text,
            "alamat": column[3].text,
            "telp": column[4].text,
            "fax": column[5].text,
        })
    json_result = json.dumps(jsons, indent=4)

    with open(file_name + ".json", "w") as utd_pmi_file:
        utd_pmi_file.write(json_result)

parser = argparse.ArgumentParser()
parser.add_argument("type", help="export data to type csv or json", type=str)
args = parser.parse_args()
output_type = args.type

if args.type == "csv":
    to_csv(get_content())
elif args.type == "json":
    to_json(get_content())
else:
    print("invalid export type, choose between csv or json")

