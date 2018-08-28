import json

f = open("hzbuslinesinfo2.json", encoding='utf-8')
data = json.load(f)

f2 = open("hzbuslinesinfo2_2.json", encoding='utf-8')
data2 = json.load(f2)

alldata = data + data2

f2 = open("hzbusstops.json", encoding='utf-8')
busstop = json.load(f2)

stopIndex = {}
for stop in busstop:
  id = stop["id"]
  name = stop["name"]
  stopIndex[name] = id

stops = []
stopids = {}

for line in alldata:
  upStops = line["up"]
  downStops = line["down"]
  for stop in upStops:
    # stop: name lines order latlng(lat, lng)

    stopname = stop["name"]
    stopid = stopIndex[stopname]
    stop["id"] = stopid
  
  for stop in downStops:
    # stop: name lines order latlng(lat, lng)

    stopname = stop["name"]
    stopid = stopIndex[stopname]
    stop["id"] = stopid


fw = open('hzbuslinesdetail.json', 'w')
fw.write(json.dumps(alldata, ensure_ascii=False))
fw.close()


