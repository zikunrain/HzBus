import re

# parse all stops
with open('allstop.html') as file_object:
  contents = file_object.read()
  result = re.findall(".*<a href=\"stop.php\?stop_id=(.*)\" target=\"_blank\">(.*)</a></li>.*", contents)
  for x in result:
    print(x[0], x[1])
  print("there are", len(result), "stops")

# parse all lines
with open('allline.html') as file_object:
  contents = file_object.read()
  result = re.findall(".*<a href=\"line.php\?line_id=(.*)\" target=\"_blank\">(.*)</a></li>.*", contents)
  for x in result:
    print(x[0], x[1])
  print("there are", len(result), "lines")