import json

data = '''
- StartTime: 9600
  Lane: 4
  KeySounds: []
- StartTime: 10050
  Lane: 4
  KeySounds: []
- StartTime: 10125
  Lane: 2
  KeySounds: []
- StartTime: 10725
  Lane: 2
  KeySounds: []
- StartTime: 10800
  Lane: 4
  KeySounds: []
- StartTime: 11250
  Lane: 4
  KeySounds: []
- StartTime: 11325
  Lane: 3
  KeySounds: []
- StartTime: 11925
  Lane: 3
  KeySounds: []
- StartTime: 12000
  Lane: 4
  KeySounds: []
- StartTime: 12450
  Lane: 4
  KeySounds: []
- StartTime: 12525
  Lane: 2
  KeySounds: []
- StartTime: 13125
  Lane: 2
  KeySounds: []
- StartTime: 13200
  Lane: 4
  KeySounds: []
- StartTime: 13650
  Lane: 4
  KeySounds: []
- StartTime: 13725
  Lane: 1
  KeySounds: []
- StartTime: 14325
  Lane: 1
  KeySounds: []
- StartTime: 14400
  Lane: 4
  KeySounds: []
- StartTime: 14850
  Lane: 4
  KeySounds: []
- StartTime: 15600
  Lane: 4
  KeySounds: []
- StartTime: 16050
  Lane: 4
  KeySounds: []
- StartTime: 16125
  Lane: 2
  KeySounds: []
- StartTime: 16725
  Lane: 2
  KeySounds: []
- StartTime: 16800
  Lane: 4
  KeySounds: []
- StartTime: 17250
  Lane: 4
  KeySounds: []
- StartTime: 17325
  Lane: 3
  KeySounds: []
- StartTime: 17925
  Lane: 3
  KeySounds: []
- StartTime: 18000
  Lane: 4
  KeySounds: []
- StartTime: 18450
  Lane: 4
  KeySounds: []
- StartTime: 19200
  Lane: 4
  KeySounds: []
- StartTime: 19275
  Lane: 1
  KeySounds: []
- StartTime: 19500
  Lane: 4
  KeySounds: []
- StartTime: 19800
  Lane: 4
  KeySounds: []
- StartTime: 20100
  Lane: 4
  KeySounds: []
- StartTime: 20325
  Lane: 1
  KeySounds: []
- StartTime: 20400
  Lane: 4
  KeySounds: []
- StartTime: 20850
  Lane: 4
  KeySounds: []
- StartTime: 21600
  Lane: 4
  KeySounds: []
- StartTime: 21675
  Lane: 3
  KeySounds: []
- StartTime: 21900
  Lane: 4
  KeySounds: []
- StartTime: 22200
  Lane: 4
  KeySounds: []
- StartTime: 22500
  Lane: 4
  KeySounds: []
- StartTime: 22725
  Lane: 3
  KeySounds: []
- StartTime: 22800
  Lane: 4
  KeySounds: []
- StartTime: 23250
  Lane: 4
  KeySounds: []
- StartTime: 23700
  Lane: 4
  KeySounds: []
- StartTime: 24000
  Lane: 4
  KeySounds: []
- StartTime: 24075
  Lane: 1
  KeySounds: []
- StartTime: 24300
  Lane: 4
  KeySounds: []
- StartTime: 24600
  Lane: 4
  KeySounds: []
- StartTime: 24900
  Lane: 4
  KeySounds: []
- StartTime: 25125
  Lane: 1
  KeySounds: []
- StartTime: 25200
  Lane: 4
  KeySounds: []
- StartTime: 25650
  Lane: 4
  KeySounds: []
- StartTime: 26400
  Lane: 4
  KeySounds: []
- StartTime: 26475
  Lane: 3
  KeySounds: []
- StartTime: 26700
  Lane: 4
  KeySounds: []
- StartTime: 27000
  Lane: 4
  KeySounds: []
- StartTime: 27300
  Lane: 4
  KeySounds: []
- StartTime: 27525
  Lane: 3
  KeySounds: []
- StartTime: 27600
  Lane: 4
  KeySounds: []
- StartTime: 28050
  Lane: 4
  KeySounds: []
- StartTime: 28500
  Lane: 4
  KeySounds: []
- StartTime: 40800
  Lane: 4
  KeySounds: []
- StartTime: 40875
  Lane: 7
  KeySounds: []
- StartTime: 42000
  Lane: 4
  KeySounds: []
- StartTime: 42300
  Lane: 4
  KeySounds: []
- StartTime: 43200
  Lane: 4
  KeySounds: []
- StartTime: 44325
  Lane: 7
  KeySounds: []
- StartTime: 44400
  Lane: 4
  KeySounds: []
- StartTime: 44700
  Lane: 4
  KeySounds: []
- StartTime: 45600
  Lane: 4
  KeySounds: []
- StartTime: 45675
  Lane: 3
  KeySounds: []
- StartTime: 46800
  Lane: 4
  KeySounds: []
- StartTime: 48000
  Lane: 4
  KeySounds: []
- StartTime: 49125
  Lane: 3
  KeySounds: []
- StartTime: 49200
  Lane: 4
  KeySounds: []
- StartTime: 49275
  Lane: 2
  KeySounds: []
- StartTime: 50400
  Lane: 2
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