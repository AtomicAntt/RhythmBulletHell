import json

data = '''
- StartTime: 9900
  Lane: 4
  KeySounds: []
- StartTime: 10350
  Lane: 4
  KeySounds: []
- StartTime: 11100
  Lane: 4
  KeySounds: []
- StartTime: 11550
  Lane: 4
  KeySounds: []
- StartTime: 12300
  Lane: 4
  KeySounds: []
- StartTime: 12750
  Lane: 4
  KeySounds: []
- StartTime: 13500
  Lane: 4
  KeySounds: []
- StartTime: 13950
  Lane: 4
  KeySounds: []
- StartTime: 14700
  Lane: 4
  KeySounds: []
- StartTime: 15150
  Lane: 4
  KeySounds: []
- StartTime: 15900
  Lane: 4
  KeySounds: []
- StartTime: 16350
  Lane: 4
  KeySounds: []
- StartTime: 17100
  Lane: 4
  KeySounds: []
- StartTime: 17550
  Lane: 4
  KeySounds: []
- StartTime: 18300
  Lane: 4
  KeySounds: []
- StartTime: 18450
  Lane: 4
  KeySounds: []
- StartTime: 18600
  Lane: 4
  KeySounds: []
- StartTime: 18750
  Lane: 4
  KeySounds: []
- StartTime: 19200
  Lane: 4
  KeySounds: []
- StartTime: 19500
  Lane: 4
  KeySounds: []
- StartTime: 19800
  Lane: 4
  KeySounds: []
- StartTime: 21600
  Lane: 4
  KeySounds: []
- StartTime: 21900
  Lane: 4
  KeySounds: []
- StartTime: 22200
  Lane: 4
  KeySounds: []
- StartTime: 24000
  Lane: 4
  KeySounds: []
- StartTime: 24300
  Lane: 4
  KeySounds: []
- StartTime: 24600
  Lane: 4
  KeySounds: []
- StartTime: 25950
  Lane: 4
  KeySounds: []
- StartTime: 26100
  Lane: 4
  KeySounds: []
- StartTime: 26400
  Lane: 4
  KeySounds: []
- StartTime: 26700
  Lane: 4
  KeySounds: []
- StartTime: 27000
  Lane: 4
  KeySounds: []
- StartTime: 28800
  Lane: 4
  KeySounds: []
- StartTime: 29100
  Lane: 4
  KeySounds: []
- StartTime: 29400
  Lane: 4
  KeySounds: []
- StartTime: 30000
  Lane: 4
  KeySounds: []
- StartTime: 30450
  Lane: 4
  KeySounds: []
- StartTime: 30900
  Lane: 4
  KeySounds: []
- StartTime: 31200
  Lane: 4
  KeySounds: []
- StartTime: 31500
  Lane: 4
  KeySounds: []
- StartTime: 31800
  Lane: 4
  KeySounds: []
- StartTime: 32400
  Lane: 4
  KeySounds: []
- StartTime: 33000
  Lane: 4
  KeySounds: []
- StartTime: 33600
  Lane: 4
  KeySounds: []
- StartTime: 34050
  Lane: 4
  KeySounds: []
- StartTime: 34500
  Lane: 4
  KeySounds: []
- StartTime: 36000
  Lane: 4
  KeySounds: []
- StartTime: 36450
  Lane: 4
  KeySounds: []
- StartTime: 36900
  Lane: 4
  KeySounds: []
- StartTime: 41400
  Lane: 4
  KeySounds: []
- StartTime: 42300
  Lane: 4
  KeySounds: []
- StartTime: 43800
  Lane: 4
  KeySounds: []
- StartTime: 44700
  Lane: 4
  KeySounds: []
- StartTime: 46200
  Lane: 4
  KeySounds: []
- StartTime: 47100
  Lane: 4
  KeySounds: []
- StartTime: 48600
  Lane: 4
  KeySounds: []
- StartTime: 49500
  Lane: 4
  KeySounds: []
- StartTime: 50700
  Lane: 4
  KeySounds: []
- StartTime: 51150
  Lane: 4
  KeySounds: []
- StartTime: 51900
  Lane: 4
  KeySounds: []
- StartTime: 52350
  Lane: 4
  KeySounds: []
- StartTime: 53100
  Lane: 4
  KeySounds: []
- StartTime: 53550
  Lane: 4
  KeySounds: []
- StartTime: 54300
  Lane: 4
  KeySounds: []
- StartTime: 54750
  Lane: 4
  KeySounds: []
- StartTime: 55500
  Lane: 4
  KeySounds: []
- StartTime: 55950
  Lane: 4
  KeySounds: []
- StartTime: 56700
  Lane: 4
  KeySounds: []
- StartTime: 57150
  Lane: 4
  KeySounds: []
- StartTime: 57900
  Lane: 4
  KeySounds: []
- StartTime: 58350
  Lane: 4
  KeySounds: []
- StartTime: 59100
  Lane: 4
  KeySounds: []
- StartTime: 59250
  Lane: 4
  KeySounds: []
- StartTime: 59550
  Lane: 4
  KeySounds: []
- StartTime: 60300
  Lane: 4
  KeySounds: []
- StartTime: 60750
  Lane: 4
  KeySounds: []
- StartTime: 61500
  Lane: 4
  KeySounds: []
- StartTime: 61950
  Lane: 4
  KeySounds: []
- StartTime: 62700
  Lane: 4
  KeySounds: []
- StartTime: 63150
  Lane: 4
  KeySounds: []
- StartTime: 63900
  Lane: 4
  KeySounds: []
- StartTime: 64350
  Lane: 4
  KeySounds: []
- StartTime: 65100
  Lane: 4
  KeySounds: []
- StartTime: 65550
  Lane: 4
  KeySounds: []
- StartTime: 66300
  Lane: 4
  KeySounds: []
- StartTime: 66750
  Lane: 4
  KeySounds: []
- StartTime: 67500
  Lane: 4
  KeySounds: []
- StartTime: 67950
  Lane: 4
  KeySounds: []
- StartTime: 68700
  Lane: 4
  KeySounds: []
- StartTime: 68850
  Lane: 4
  KeySounds: []
- StartTime: 69150
  Lane: 4
  KeySounds: []
- StartTime: 69600
  Lane: 4
  KeySounds: []
- StartTime: 69900
  Lane: 4
  KeySounds: []
- StartTime: 70200
  Lane: 4
  KeySounds: []
- StartTime: 71400
  Lane: 4
  KeySounds: []
- StartTime: 72000
  Lane: 4
  KeySounds: []
- StartTime: 72300
  Lane: 4
  KeySounds: []
- StartTime: 72600
  Lane: 4
  KeySounds: []
- StartTime: 73050
  Lane: 4
  KeySounds: []
- StartTime: 73200
  Lane: 4
  KeySounds: []
- StartTime: 74400
  Lane: 4
  KeySounds: []
- StartTime: 74700
  Lane: 4
  KeySounds: []
- StartTime: 75000
  Lane: 4
  KeySounds: []
- StartTime: 76200
  Lane: 4
  KeySounds: []
- StartTime: 76800
  Lane: 4
  KeySounds: []
- StartTime: 77100
  Lane: 4
  KeySounds: []
- StartTime: 77400
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
      if (j == (4-1)):
        print("location of note:"+  str(result_array.index(50400)))
      result_array.clear()