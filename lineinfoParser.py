import re
import json

# parse all stops
# with open('lineinfo_example.html') as file_object:
#   contents = file_object.read()

class LineInfoParser:
  def __init__(self, contents):
    self.contents = contents
    self.upStops = []
    self.downStops = []
  
  def startParse(self):
    self.startParseDown()
    self.startParseUp()

  def getUpStops(self):
    return self.upStops
  
  def getDownStops(self):
    return self.downStops
  
  def startParseUp(self):
    # parse up stops
    upResult = re.findall(".*var stopmaps_up=(.*)var stopmaps_down.*", self.contents, re.DOTALL)
    if (len(upResult) == 0):
      print("down!!!!!!!!!!!!")
      return

    string = upResult[0].replace("\n", "")
    string = string.replace("\t", "")
    string = string.replace(" ", "")

    stops = string.split("},")
    for stopinfo in stops:
      attributes = stopinfo.split(",")

      if len(attributes[0].split(":\"")) < 2:
        print(attributes)
        continue
      stopname = attributes[0].split(":\"")[1][:-1]

      content = attributes[1]
      linesinfo = content.split("'+'")
      passinglines = []
      for lineinfo in linesinfo:
        linetuples = re.findall(".*<ahref=\"line.php\?line_id=(.*)\"target=\"_blank\">(.*)</a>", lineinfo)
        linetuple = linetuples[0]
        lineid = linetuple[0]
        linename = linetuple[1].replace("<fontcolor=\"red\">", "").replace("</font>", "")
        line = {}
        line["id"] = lineid
        line["name"] = linename
        passinglines.append(line)

      point = attributes[2].split("\"")[1].split("|")
      lng = float(point[0])
      lat = float(point[1])
      latlng = {}
      latlng["lat"] = lat
      latlng["lng"] = lng

      orderlist = attributes[3]
      order = int(re.findall("orderlist:'(.*)'.*", orderlist)[0])
      
      stop = {}
      stop["name"] = stopname
      stop["lines"] = passinglines
      stop["latlng"] = latlng
      stop["order"] = order

      self.upStops.append(stop)

  def startParseDown(self):
    # parse down stops
    downResult = re.findall(".*var stopmaps_down=(.*)function createIcon\(num.*", self.contents, re.DOTALL)
    if (len(downResult) == 0):
      print("down!!!!!!!!!!!!")
      return
    
    string = downResult[0].replace("\n", "")
    string = string.replace("\t", "")
    string = string.replace(" ", "")

    stops = string.split("},")
    for stopinfo in stops:
      attributes = stopinfo.split(",")
      
      if len(attributes[0].split(":\"")) < 2:
        print(attributes)
        continue
      stopname = attributes[0].split(":\"")[1][:-1]

      content = attributes[1]
      linesinfo = content.split("'+'")
      passinglines = []
      for lineinfo in linesinfo:
        linetuples = re.findall(".*<ahref=\"line.php\?line_id=(.*)\"target=\"_blank\">(.*)</a>", lineinfo)
        if len(linetuples) == 0:
          continue
        linetuple = linetuples[0]
        lineid = linetuple[0]
        linename = linetuple[1].replace("<fontcolor=\"red\">", "").replace("</font>", "")
        line = {}
        line["id"] = lineid
        line["name"] = linename
        passinglines.append(line)

      point = attributes[2].split("\"")[1].split("|")
      lng = float(point[0])
      lat = float(point[1])
      latlng = {}
      latlng["lat"] = lat
      latlng["lng"] = lng

      orderlist = attributes[3]
      # print(orderlist)
      order = int(re.findall("orderlist:'(.*)'.*", orderlist)[0])
      
      stop = {}
      stop["name"] = stopname
      stop["lines"] = passinglines
      stop["latlng"] = latlng
      stop["order"] = order

      self.downStops.append(stop)