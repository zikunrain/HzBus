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
  "host": "bus.hangzhou.com.cn",
  "Cookie": "aliyungf_tc=AQAAAOTu6UsKsAMAEhfIb+GOggnukYy3; acw_tc=AQAAAB8iYUDztAMAEhfIb8q3DLfOl7+o; PHPSESSID=qde83oq1tmdv2vsaa2h9o0tar4; __utma=92774798.133552944.1535370541.1535370541.1535370541.1; __utmc=92774798; __utmz=92774798.1535370541.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; Hm_lvt_02070301bad24b5feb372c37bb6d887e=1535344732,1535344785,1535365542; pgv_pvi=6464888832; pgv_si=s7904759808; Hm_lvt_08261419fd973f118d693f2d1ce6e02b=1535344732,1535344785,1535365542; wdcid=472466a953a4fa83; wdses=012b6e803dc5e8e5; __utmb=92774798.3.10.1535370541; Hm_lpvt_02070301bad24b5feb372c37bb6d887e=1535370561; Hm_lpvt_08261419fd973f118d693f2d1ce6e02b=1535370561; wdlast=1535370562"
}

data = []
# i = 1
# for line in lines:
#   lineid = line["id"]
#   print("processing line with id of %s (%d/533)" % (lineid, i))  
#   r = requests.get('http://bus.hangzhou.com.cn/line.php?line_id=' + str(lineid), headers=requestHeaders)
#   parser = LineInfoParser(r.text)
#   parser.startParse()
#   upstops = parser.getUpStops()
#   downstops = parser.getDownStops()
#   stopsOfLine = {}
#   stopsOfLine["up"] = upstops
#   stopsOfLine["down"] = downstops

#   data.append(stopsOfLine)
#   i += 1

# fw = open('hzbuslinesinfo.json', 'w')
# fw.write(json.dumps(data, indent=4, ensure_ascii=False))
# fw.close()


lineids = [912, 654]
for lineid in lineids:
  print("processing line with id of %s " % lineid)  
  r = requests.get('http://bus.hangzhou.com.cn/line.php?line_id=' + str(lineid), headers=requestHeaders)
  parser = LineInfoParser(r.text)
  parser.startParse()
  upstops = parser.getUpStops()
  downstops = parser.getDownStops()
  stopsOfLine = {}
  stopsOfLine["up"] = upstops
  stopsOfLine["down"] = downstops

  data.append(stopsOfLine)

fw = open('hzbuslinesinfo_3.json', 'w')
fw.write(json.dumps(data, indent=4, ensure_ascii=False))
fw.close()

# debug

# i = 152
# lineid = lines[i]["id"]
# r = requests.get('http://bus.hangzhou.com.cn/line.php?line_id=629', headers=requestHeaders)
# # r = requests.get('http://bus.hangzhou.com.cn/line.php?line_id=' + str(lineid), headers=requestHeaders)
# parser = LineInfoParser(r.text)
# # print(r.text)
# print("processing line with id of %s (%d/533)" % (lineid, i)) 
# parser = LineInfoParser(r.text)
# parser.startParse()
# upstops = parser.getUpStops()
# downstops = parser.getDownStops()


# 805 466
# 654 446
# 681 397
# 912 394
# 957 363
# 640 153
# 308 111
# 260 88