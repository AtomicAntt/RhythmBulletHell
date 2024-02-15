import json

data = '''
- StartTime: 21900
  Lane: 4
  KeySounds: []
- StartTime: 22350
  Lane: 4
  KeySounds: []
- StartTime: 23100
  Lane: 4
  KeySounds: []
- StartTime: 23700
  Lane: 4
  KeySounds: []
- StartTime: 24300
  Lane: 4
  KeySounds: []
- StartTime: 24750
  Lane: 4
  KeySounds: []
- StartTime: 25500
  Lane: 4
  KeySounds: []
- StartTime: 26100
  Lane: 4
  KeySounds: []
- StartTime: 26700
  Lane: 4
  KeySounds: []
- StartTime: 27150
  Lane: 4
  KeySounds: []
- StartTime: 27900
  Lane: 4
  KeySounds: []
- StartTime: 28500
  Lane: 4
  KeySounds: []
- StartTime: 28575
  Lane: 4
  KeySounds: []
- StartTime: 28650
  Lane: 4
  KeySounds: []
- StartTime: 28725
  Lane: 4
  KeySounds: []
- StartTime: 29100
  Lane: 4
  KeySounds: []
- StartTime: 29550
  Lane: 4
  KeySounds: []
- StartTime: 30300
  Lane: 4
  KeySounds: []
- StartTime: 30900
  Lane: 4
  KeySounds: []
- StartTime: 31500
  Lane: 4
  KeySounds: []
- StartTime: 31950
  Lane: 4
  KeySounds: []
- StartTime: 32700
  Lane: 4
  KeySounds: []
- StartTime: 33300
  Lane: 4
  KeySounds: []
- StartTime: 33900
  Lane: 4
  KeySounds: []
- StartTime: 34350
  Lane: 4
  KeySounds: []
- StartTime: 35100
  Lane: 4
  KeySounds: []
- StartTime: 35700
  Lane: 4
  KeySounds: []
- StartTime: 36300
  Lane: 4
  KeySounds: []
- StartTime: 36750
  Lane: 4
  KeySounds: []
- StartTime: 37500
  Lane: 4
  KeySounds: []
- StartTime: 38100
  Lane: 4
  KeySounds: []
- StartTime: 72300
  Lane: 4
  KeySounds: []
- StartTime: 72750
  Lane: 4
  KeySounds: []
- StartTime: 73500
  Lane: 4
  KeySounds: []
- StartTime: 74100
  Lane: 4
  KeySounds: []
- StartTime: 74700
  Lane: 4
  KeySounds: []
- StartTime: 75150
  Lane: 4
  KeySounds: []
- StartTime: 75900
  Lane: 4
  KeySounds: []
- StartTime: 76500
  Lane: 4
  KeySounds: []
- StartTime: 77100
  Lane: 4
  KeySounds: []
- StartTime: 77550
  Lane: 4
  KeySounds: []
- StartTime: 78300
  Lane: 4
  KeySounds: []
- StartTime: 78900
  Lane: 4
  KeySounds: []
- StartTime: 78975
  Lane: 4
  KeySounds: []
- StartTime: 79050
  Lane: 4
  KeySounds: []
- StartTime: 79125
  Lane: 4
  KeySounds: []
- StartTime: 79500
  Lane: 4
  KeySounds: []
- StartTime: 79950
  Lane: 4
  KeySounds: []
- StartTime: 80700
  Lane: 4
  KeySounds: []
- StartTime: 81300
  Lane: 4
  KeySounds: []
- StartTime: 81900
  Lane: 4
  KeySounds: []
- StartTime: 82350
  Lane: 4
  KeySounds: []
- StartTime: 83100
  Lane: 4
  KeySounds: []
- StartTime: 83700
  Lane: 4
  KeySounds: []
- StartTime: 84300
  Lane: 4
  KeySounds: []
- StartTime: 84750
  Lane: 4
  KeySounds: []
- StartTime: 85500
  Lane: 4
  KeySounds: []
- StartTime: 86100
  Lane: 4
  KeySounds: []
- StartTime: 86700
  Lane: 4
  KeySounds: []
- StartTime: 87150
  Lane: 4
  KeySounds: []
- StartTime: 87900
  Lane: 4
  KeySounds: []
- StartTime: 88500
  Lane: 4
  KeySounds: []
- StartTime: 88575
  Lane: 4
  KeySounds: []
- StartTime: 88650
  Lane: 4
  KeySounds: []
- StartTime: 88725
  Lane: 4
  KeySounds: []
'''
lane1Data = []
lane2Data = []
lane3Data = []
lane4Data = []
lane5Data = []
lane6Data = []
lane7Data = []

# Split the data into individual lines
lines = data.strip().split('\n')

# Initialize an empty array
result_array = []

# Loop through each line and extract StartTime value if Lane is 4
for j in range(7):
    for i in range(len(lines)):
    # if lines[i].startswith("- StartTime:") and "Lane: 4" in lines[i + 1]:
      if lines[i].startswith("- StartTime:") and "Lane: "+str((j+1)) in lines[i+1]:
          start_time = int(lines[i].split(":")[1].strip())
          result_array.append(start_time)
          
      # Print the resulting array
    if (i == len(lines)-1):
      print("Array " + str(j+1) + ": " + str(result_array))
      result_array.clear()