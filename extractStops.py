import json

f = open("hzbuslinesdetail.json", encoding='utf-8')
data = json.load(f)

f2 = open("hzbusstops.json", encoding='utf-8')
busstop = json.load(f2)

stopIndex = {}

nData = len(data)

newstops = []
warningCount = 0

for index, line in enumerate(data[0:2]):
  print("processing %d / %d" % (index, nData))
  upStops = line["up"]
  downStops = line["down"]

  upAndDownStops = upStops + downStops

  for i,stop in enumerate(upAndDownStops):
    # stop: name id lines order latlng(lat, lng)
    # print(stop.keys())

    stopid = stop["id"]
    latlng = stop["latlng"]
    stopname = stop["name"]
    
    if stopid not in stopIndex:
      newstop = {}
      newstop["latlng"] = latlng
      newstop["name"] = stopname
      newstop["id"] = stopid

      newstops.append(newstop)

      stopIndex[stopid] = float(latlng["lat"])
    else:
      if stopIndex[stopid] != float(latlng["lat"]):
        print("warning %d. %f" % (warningCount, stopIndex[stopid] - float(latlng["lat"]) ))
        print(i)
        warningCount += 1



fw = open('hzbusstops2.json', 'w')
fw.write(json.dumps(data, indent=4, ensure_ascii=False))
fw.close()

    
    # if stopid not in stopids:
    #   stopids[stopid] = stopname
      
    #   lat = stop

    #   s = {}
    #   s[]
    # else:
    #   stopids[stopid] != stopname
    #   print("warning id do not match name")
