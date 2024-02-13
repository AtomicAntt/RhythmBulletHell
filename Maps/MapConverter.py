import json

data = '''
- StartTime: 18
  Lane: 4
  KeySounds: []
- StartTime: 18
  Lane: 1
  KeySounds: []
- StartTime: 360
  Lane: 4
  KeySounds: []
- StartTime: 703
  Lane: 4
  KeySounds: []
- StartTime: 1046
  Lane: 4
  KeySounds: []
- StartTime: 1389
  Lane: 4
  KeySounds: []
- StartTime: 1732
  Lane: 4
  KeySounds: []
- StartTime: 2075
  Lane: 4
  KeySounds: []
- StartTime: 2418
  Lane: 4
  KeySounds: []
- StartTime: 2760
  Lane: 4
  KeySounds: []
- StartTime: 3103
  Lane: 4
  KeySounds: []
- StartTime: 3446
  Lane: 4
  KeySounds: []
- StartTime: 3789
  Lane: 4
  KeySounds: []
- StartTime: 4132
  Lane: 4
  KeySounds: []
- StartTime: 4475
  Lane: 4
  KeySounds: []
- StartTime: 4818
  Lane: 4
  KeySounds: []
- StartTime: 5160
  Lane: 4
  KeySounds: []
- StartTime: 5503
  Lane: 4
  KeySounds: []
- StartTime: 5846
  Lane: 4
  KeySounds: []
- StartTime: 6189
  Lane: 4
  KeySounds: []
- StartTime: 6532
  Lane: 4
  KeySounds: []
- StartTime: 6875
  Lane: 4
  KeySounds: []
- StartTime: 7218
  Lane: 4
  KeySounds: []
- StartTime: 7560
  Lane: 4
  KeySounds: []
- StartTime: 7903
  Lane: 4
  KeySounds: []
- StartTime: 8246
  Lane: 4
  KeySounds: []
- StartTime: 8589
  Lane: 4
  KeySounds: []
- StartTime: 8932
  Lane: 4
  KeySounds: []
- StartTime: 9275
  Lane: 4
  KeySounds: []
- StartTime: 9618
  Lane: 4
  KeySounds: []
- StartTime: 9960
  Lane: 4
  KeySounds: []
- StartTime: 10303
  Lane: 4
  KeySounds: []
- StartTime: 10646
  Lane: 4
  KeySounds: []
- StartTime: 11332
  Lane: 4
  KeySounds: []
- StartTime: 12018
  Lane: 4
  KeySounds: []
- StartTime: 12703
  Lane: 4
  KeySounds: []
- StartTime: 13389
  Lane: 4
  KeySounds: []
- StartTime: 14075
  Lane: 4
  KeySounds: []
- StartTime: 14760
  Lane: 4
  KeySounds: []
- StartTime: 15446
  Lane: 4
  KeySounds: []
- StartTime: 16132
  Lane: 4
  KeySounds: []
- StartTime: 16475
  Lane: 4
  KeySounds: []
- StartTime: 17160
  Lane: 4
  KeySounds: []
- StartTime: 17846
  Lane: 4
  KeySounds: []
- StartTime: 18532
  Lane: 4
  KeySounds: []
- StartTime: 19218
  Lane: 4
  KeySounds: []
- StartTime: 19903
  Lane: 4
  KeySounds: []
- StartTime: 20589
  Lane: 4
  KeySounds: []
- StartTime: 21275
  Lane: 4
  KeySounds: []
- StartTime: 21960
  Lane: 4
  KeySounds: []
- StartTime: 22303
  Lane: 4
  KeySounds: []
- StartTime: 22989
  Lane: 4
  KeySounds: []
- StartTime: 23675
  Lane: 4
  KeySounds: []
- StartTime: 24360
  Lane: 4
  KeySounds: []
- StartTime: 25046
  Lane: 4
  KeySounds: []
- StartTime: 25732
  Lane: 4
  KeySounds: []
- StartTime: 26418
  Lane: 4
  KeySounds: []
- StartTime: 27103
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