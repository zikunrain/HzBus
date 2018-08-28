import requests
from lineinfoParser import LineInfoParser
import re
import json

# parse all stops
stops = []
with open('allstop.html') as file_object:
  contents = file_object.read()
  result = re.findall(".*<a href=\"stop.php\?stop_id=(.*)\" target=\"_blank\">(.*)</a></li>.*", contents)
  for x in result:
    stop = {}
    stop["name"] = x[1]
    stop["id"] = int(x[0])
    stops.append(stop)
  print("there are", len(result), "stops")

fw = open('hzbusstops.json', 'w')
fw.write(json.dumps(stops, indent=4, ensure_ascii=False))
fw.close()

# parse all lines
lines = []
with open('allline.html') as file_object:
  contents = file_object.read()
  result = re.findall(".*<a href=\"line.php\?line_id=(.*)\" target=\"_blank\">(.*)</a></li>.*", contents)
  for x in result:
    line = {}
    line["id"] = int(x[0])
    line["name"] = x[1]
    lines.append(line)
  print("there are", len(result), "lines")

fw = open('hzbuslines.json', 'w')
fw.write(json.dumps(lines, indent=4, ensure_ascii=False))
fw.close()

requestHeaders = {
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
  "host": "bus.hangzhou.com.cn"
}

data = []
# i = 1
# errorlineids = []
# for line in lines:
#   lineid = line["id"]
#   print("processing line with id of %s (%d/533)" % (lineid, i))  
#   r = requests.get('http://bus.hangzhou.com.cn/line.php?line_id=' + str(lineid), headers=requestHeaders)
#   parser = LineInfoParser(r.text)
#   status = parser.startParse()

#   stopsOfLine = {}
#   if status:
#     upstops = parser.getUpStops()
#     downstops = parser.getDownStops()
#     stopsOfLine["up"] = upstops
#     stopsOfLine["down"] = downstops
#     stopsOfLine["id"] = lineid
#     stopsOfLine["name"] = line["name"]
#     data.append(stopsOfLine)
#   else:
#     print("error line id", lineid)
#     errorlineids.append(lineid)
#   i += 1
# print("Error line ids")
# print(errorlineids)

# fw = open('hzbuslinesinfo2.json', 'w')
# fw.write(json.dumps(data, indent=4, ensure_ascii=False))
# fw.close()

lineids = [260, 308, 640, 957, 912, 681, 654, 805]
errorlineids = []
for lineid in lineids:
  print("processing line with id of %s" % lineid)  
  r = requests.get('http://bus.hangzhou.com.cn/line.php?line_id=' + str(lineid), headers=requestHeaders)
  parser = LineInfoParser(r.text)
  status = parser.startParse()

  stopsOfLine = {}
  if status:
    upstops = parser.getUpStops()
    downstops = parser.getDownStops()
    stopsOfLine["up"] = upstops
    stopsOfLine["down"] = downstops
    stopsOfLine["id"] = lineid
    stopsOfLine["name"] = line["name"]
    data.append(stopsOfLine)
  else:
    print("error line id", lineid)
    errorlineids.append(lineid)
print("Error line ids")
print(errorlineids)

fw = open('hzbuslinesinfo2_2.json', 'w')
fw.write(json.dumps(data, indent=4, ensure_ascii=False))
fw.close()





# debug

# i = 152
# lineid = lines[i]["id"]
# r = requests.get('http://bus.hangzhou.com.cn/line.php?line_id=610', headers=requestHeaders)
# # r = requests.get('http://bus.hangzhou.com.cn/line.php?line_id=' + str(lineid), headers=requestHeaders)
# parser = LineInfoParser(r.text)
# # print(r.text)
# print("processing line with id of %s (%d/533)" % (lineid, i)) 
# parser = LineInfoParser(r.text)
# parser.startParse()
# upstops = parser.getUpStops()
# downstops = parser.getDownStops()
# print(upstops)
# print(downstops)
# stopsOfLine = {}
# stopsOfLine["up"] = upstops
# stopsOfLine["down"] = downstops

# fw = open('hzbuslinesinfo_debug.json', 'w')
# fw.write(json.dumps(stopsOfLine, indent=4, ensure_ascii=False))
# fw.close()


# 805 466
# 654 446
# 681 397
# 912 394
# 957 363
# 640 153
# 308 111
# 260 88