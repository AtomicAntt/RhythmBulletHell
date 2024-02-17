import json

data = '''
- StartTime: 17
  Lane: 4
  KeySounds: []
- StartTime: 17
  Lane: 7
  KeySounds: []
- StartTime: 1217
  Lane: 4
  KeySounds: []
- StartTime: 1217
  Lane: 7
  KeySounds: []
- StartTime: 2417
  Lane: 4
  KeySounds: []
- StartTime: 2417
  Lane: 5
  KeySounds: []
- StartTime: 3617
  Lane: 4
  KeySounds: []
- StartTime: 3617
  Lane: 5
  KeySounds: []
- StartTime: 4817
  Lane: 4
  KeySounds: []
- StartTime: 4817
  Lane: 7
  KeySounds: []
- StartTime: 6017
  Lane: 4
  KeySounds: []
- StartTime: 6017
  Lane: 7
  KeySounds: []
- StartTime: 7217
  Lane: 4
  KeySounds: []
- StartTime: 7217
  Lane: 5
  KeySounds: []
- StartTime: 8417
  Lane: 4
  KeySounds: []
- StartTime: 8417
  Lane: 5
  KeySounds: []
- StartTime: 9617
  Lane: 4
  KeySounds: []
- StartTime: 9617
  Lane: 7
  KeySounds: []
- StartTime: 10817
  Lane: 4
  KeySounds: []
- StartTime: 10817
  Lane: 7
  KeySounds: []
- StartTime: 12017
  Lane: 4
  KeySounds: []
- StartTime: 12017
  Lane: 5
  KeySounds: []
- StartTime: 13217
  Lane: 4
  KeySounds: []
- StartTime: 13217
  Lane: 5
  KeySounds: []
- StartTime: 14417
  Lane: 4
  KeySounds: []
- StartTime: 14417
  Lane: 7
  KeySounds: []
- StartTime: 15617
  Lane: 4
  KeySounds: []
- StartTime: 15617
  Lane: 7
  KeySounds: []
- StartTime: 16817
  Lane: 4
  KeySounds: []
- StartTime: 16817
  Lane: 5
  KeySounds: []
- StartTime: 18017
  Lane: 4
  KeySounds: []
- StartTime: 18017
  Lane: 5
  KeySounds: []
- StartTime: 18092
  Lane: 6
  KeySounds: []
- StartTime: 19217
  Lane: 4
  KeySounds: []
- StartTime: 19217
  Lane: 6
  KeySounds: []
- StartTime: 19817
  Lane: 4
  KeySounds: []
- StartTime: 19892
  Lane: 4
  KeySounds: []
- StartTime: 19967
  Lane: 4
  KeySounds: []
- StartTime: 20042
  Lane: 4
  KeySounds: []
- StartTime: 20117
  Lane: 4
  KeySounds: []
- StartTime: 20192
  Lane: 4
  KeySounds: []
- StartTime: 20267
  Lane: 4
  KeySounds: []
- StartTime: 20342
  Lane: 4
  KeySounds: []
- StartTime: 20417
  Lane: 4
  KeySounds: []
- StartTime: 20492
  Lane: 7
  KeySounds: []
- StartTime: 20717
  Lane: 4
  KeySounds: []
- StartTime: 21017
  Lane: 7
  KeySounds: []
- StartTime: 21017
  Lane: 4
  KeySounds: []
- StartTime: 21092
  Lane: 6
  KeySounds: []
- StartTime: 21317
  Lane: 4
  KeySounds: []
- StartTime: 21617
  Lane: 4
  KeySounds: []
- StartTime: 21617
  Lane: 6
  KeySounds: []
- StartTime: 21692
  Lane: 5
  KeySounds: []
- StartTime: 21917
  Lane: 4
  KeySounds: []
- StartTime: 22217
  Lane: 4
  KeySounds: []
- StartTime: 22217
  Lane: 5
  KeySounds: []
- StartTime: 22292
  Lane: 6
  KeySounds: []
- StartTime: 22517
  Lane: 4
  KeySounds: []
- StartTime: 22817
  Lane: 4
  KeySounds: []
- StartTime: 22817
  Lane: 6
  KeySounds: []
- StartTime: 22892
  Lane: 7
  KeySounds: []
- StartTime: 23117
  Lane: 4
  KeySounds: []
- StartTime: 23417
  Lane: 4
  KeySounds: []
- StartTime: 23417
  Lane: 7
  KeySounds: []
- StartTime: 23492
  Lane: 6
  KeySounds: []
- StartTime: 23717
  Lane: 4
  KeySounds: []
- StartTime: 24017
  Lane: 4
  KeySounds: []
- StartTime: 24017
  Lane: 6
  KeySounds: []
- StartTime: 24092
  Lane: 5
  KeySounds: []
- StartTime: 24317
  Lane: 4
  KeySounds: []
- StartTime: 24617
  Lane: 4
  KeySounds: []
- StartTime: 24617
  Lane: 5
  KeySounds: []
- StartTime: 24692
  Lane: 6
  KeySounds: []
- StartTime: 24917
  Lane: 4
  KeySounds: []
- StartTime: 25217
  Lane: 4
  KeySounds: []
- StartTime: 25217
  Lane: 6
  KeySounds: []
- StartTime: 25292
  Lane: 7
  KeySounds: []
- StartTime: 25517
  Lane: 4
  KeySounds: []
- StartTime: 25817
  Lane: 4
  KeySounds: []
- StartTime: 25817
  Lane: 7
  KeySounds: []
- StartTime: 25892
  Lane: 6
  KeySounds: []
- StartTime: 26117
  Lane: 4
  KeySounds: []
- StartTime: 26417
  Lane: 4
  KeySounds: []
- StartTime: 26417
  Lane: 6
  KeySounds: []
- StartTime: 26717
  Lane: 4
  KeySounds: []
- StartTime: 27017
  Lane: 4
  KeySounds: []
- StartTime: 27317
  Lane: 4
  KeySounds: []
- StartTime: 27392
  Lane: 2
  KeySounds: []
- StartTime: 27617
  Lane: 4
  KeySounds: []
- StartTime: 27917
  Lane: 4
  KeySounds: []
- StartTime: 28217
  Lane: 4
  KeySounds: []
- StartTime: 28517
  Lane: 4
  KeySounds: []
- StartTime: 28817
  Lane: 4
  KeySounds: []
- StartTime: 29117
  Lane: 4
  KeySounds: []
- StartTime: 29417
  Lane: 4
  KeySounds: []
- StartTime: 29717
  Lane: 4
  KeySounds: []
- StartTime: 29942
  Lane: 2
  KeySounds: []
- StartTime: 30017
  Lane: 4
  KeySounds: []
- StartTime: 30017
  Lane: 3
  KeySounds: []
- StartTime: 30317
  Lane: 4
  KeySounds: []
- StartTime: 30542
  Lane: 3
  KeySounds: []
- StartTime: 30617
  Lane: 4
  KeySounds: []
- StartTime: 30617
  Lane: 2
  KeySounds: []
- StartTime: 30917
  Lane: 4
  KeySounds: []
- StartTime: 31142
  Lane: 2
  KeySounds: []
- StartTime: 31217
  Lane: 4
  KeySounds: []
- StartTime: 31217
  Lane: 1
  KeySounds: []
- StartTime: 31517
  Lane: 4
  KeySounds: []
- StartTime: 31742
  Lane: 1
  KeySounds: []
- StartTime: 31817
  Lane: 4
  KeySounds: []
- StartTime: 31817
  Lane: 2
  KeySounds: []
- StartTime: 32117
  Lane: 4
  KeySounds: []
- StartTime: 32342
  Lane: 2
  KeySounds: []
- StartTime: 32417
  Lane: 4
  KeySounds: []
- StartTime: 32417
  Lane: 3
  KeySounds: []
- StartTime: 32717
  Lane: 4
  KeySounds: []
- StartTime: 32942
  Lane: 3
  KeySounds: []
- StartTime: 33017
  Lane: 4
  KeySounds: []
- StartTime: 33017
  Lane: 2
  KeySounds: []
- StartTime: 33317
  Lane: 4
  KeySounds: []
- StartTime: 33542
  Lane: 2
  KeySounds: []
- StartTime: 33617
  Lane: 4
  KeySounds: []
- StartTime: 33617
  Lane: 1
  KeySounds: []
- StartTime: 33917
  Lane: 4
  KeySounds: []
- StartTime: 34142
  Lane: 1
  KeySounds: []
- StartTime: 34217
  Lane: 4
  KeySounds: []
- StartTime: 34217
  Lane: 2
  KeySounds: []
- StartTime: 34517
  Lane: 4
  KeySounds: []
- StartTime: 34742
  Lane: 2
  KeySounds: []
- StartTime: 34817
  Lane: 4
  KeySounds: []
- StartTime: 34817
  Lane: 3
  KeySounds: []
- StartTime: 35117
  Lane: 4
  KeySounds: []
- StartTime: 35342
  Lane: 3
  KeySounds: []
- StartTime: 35417
  Lane: 4
  KeySounds: []
- StartTime: 35417
  Lane: 2
  KeySounds: []
- StartTime: 35717
  Lane: 4
  KeySounds: []
- StartTime: 35942
  Lane: 2
  KeySounds: []
- StartTime: 36017
  Lane: 4
  KeySounds: []
- StartTime: 36317
  Lane: 4
  KeySounds: []
- StartTime: 36617
  Lane: 4
  KeySounds: []
- StartTime: 36917
  Lane: 4
  KeySounds: []
- StartTime: 37217
  Lane: 4
  KeySounds: []
- StartTime: 37217
  Lane: 6
  KeySounds: []
- StartTime: 37517
  Lane: 4
  KeySounds: []
- StartTime: 37817
  Lane: 4
  KeySounds: []
- StartTime: 38117
  Lane: 4
  KeySounds: []
- StartTime: 38417
  Lane: 4
  KeySounds: []
- StartTime: 38717
  Lane: 4
  KeySounds: []
- StartTime: 39017
  Lane: 4
  KeySounds: []
- StartTime: 39317
  Lane: 4
  KeySounds: []
- StartTime: 39467
  Lane: 4
  KeySounds: []
- StartTime: 39617
  Lane: 4
  KeySounds: []
- StartTime: 39617
  Lane: 6
  KeySounds: []
- StartTime: 39692
  Lane: 7
  KeySounds: []
- StartTime: 40217
  Lane: 4
  KeySounds: []
- StartTime: 40217
  Lane: 7
  KeySounds: []
- StartTime: 40292
  Lane: 6
  KeySounds: []
- StartTime: 40817
  Lane: 4
  KeySounds: []
- StartTime: 40817
  Lane: 6
  KeySounds: []
- StartTime: 40892
  Lane: 5
  KeySounds: []
- StartTime: 41417
  Lane: 4
  KeySounds: []
- StartTime: 41417
  Lane: 5
  KeySounds: []
- StartTime: 41492
  Lane: 6
  KeySounds: []
- StartTime: 42017
  Lane: 4
  KeySounds: []
- StartTime: 42017
  Lane: 6
  KeySounds: []
- StartTime: 42092
  Lane: 7
  KeySounds: []
- StartTime: 42617
  Lane: 4
  KeySounds: []
- StartTime: 42617
  Lane: 7
  KeySounds: []
- StartTime: 42692
  Lane: 6
  KeySounds: []
- StartTime: 43217
  Lane: 4
  KeySounds: []
- StartTime: 43217
  Lane: 6
  KeySounds: []
- StartTime: 43292
  Lane: 5
  KeySounds: []
- StartTime: 43817
  Lane: 4
  KeySounds: []
- StartTime: 43817
  Lane: 5
  KeySounds: []
- StartTime: 43892
  Lane: 6
  KeySounds: []
- StartTime: 44342
  Lane: 6
  KeySounds: []
- StartTime: 44417
  Lane: 4
  KeySounds: []
- StartTime: 44417
  Lane: 7
  KeySounds: []
- StartTime: 44942
  Lane: 7
  KeySounds: []
- StartTime: 45017
  Lane: 4
  KeySounds: []
- StartTime: 45017
  Lane: 6
  KeySounds: []
- StartTime: 45542
  Lane: 6
  KeySounds: []
- StartTime: 45617
  Lane: 4
  KeySounds: []
- StartTime: 45617
  Lane: 5
  KeySounds: []
- StartTime: 46142
  Lane: 5
  KeySounds: []
- StartTime: 46217
  Lane: 4
  KeySounds: []
- StartTime: 46217
  Lane: 6
  KeySounds: []
- StartTime: 46742
  Lane: 6
  KeySounds: []
- StartTime: 46817
  Lane: 4
  KeySounds: []
- StartTime: 46817
  Lane: 7
  KeySounds: []
- StartTime: 47342
  Lane: 7
  KeySounds: []
- StartTime: 47417
  Lane: 4
  KeySounds: []
- StartTime: 47417
  Lane: 6
  KeySounds: []
- StartTime: 47942
  Lane: 6
  KeySounds: []
- StartTime: 48017
  Lane: 4
  KeySounds: []
- StartTime: 48017
  Lane: 5
  KeySounds: []
- StartTime: 48542
  Lane: 5
  KeySounds: []
- StartTime: 48617
  Lane: 4
  KeySounds: []
- StartTime: 48617
  Lane: 6
  KeySounds: []
- StartTime: 49142
  Lane: 6
  KeySounds: []
- StartTime: 49217
  Lane: 4
  KeySounds: []
- StartTime: 50417
  Lane: 4
  KeySounds: []
- StartTime: 50417
  Lane: 7
  KeySounds: []
- StartTime: 51617
  Lane: 4
  KeySounds: []
- StartTime: 51617
  Lane: 7
  KeySounds: []
- StartTime: 52817
  Lane: 4
  KeySounds: []
- StartTime: 52817
  Lane: 5
  KeySounds: []
- StartTime: 54017
  Lane: 4
  KeySounds: []
- StartTime: 54017
  Lane: 5
  KeySounds: []
- StartTime: 55217
  Lane: 4
  KeySounds: []
- StartTime: 55217
  Lane: 7
  KeySounds: []
- StartTime: 56417
  Lane: 4
  KeySounds: []
- StartTime: 56417
  Lane: 7
  KeySounds: []
- StartTime: 57617
  Lane: 4
  KeySounds: []
- StartTime: 57617
  Lane: 5
  KeySounds: []
- StartTime: 58817
  Lane: 4
  KeySounds: []
- StartTime: 58817
  Lane: 5
  KeySounds: []
- StartTime: 60017
  Lane: 4
  KeySounds: []
- StartTime: 60017
  Lane: 7
  KeySounds: []
- StartTime: 61217
  Lane: 4
  KeySounds: []
- StartTime: 61217
  Lane: 7
  KeySounds: []
- StartTime: 62417
  Lane: 4
  KeySounds: []
- StartTime: 62417
  Lane: 5
  KeySounds: []
- StartTime: 63617
  Lane: 4
  KeySounds: []
- StartTime: 63617
  Lane: 5
  KeySounds: []
- StartTime: 64817
  Lane: 4
  KeySounds: []
- StartTime: 64817
  Lane: 7
  KeySounds: []
- StartTime: 66017
  Lane: 4
  KeySounds: []
- StartTime: 66017
  Lane: 7
  KeySounds: []
- StartTime: 66092
  Lane: 6
  KeySounds: []
- StartTime: 66617
  Lane: 6
  KeySounds: []
- StartTime: 67217
  Lane: 4
  KeySounds: []
- StartTime: 68417
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
      # if (j == (4-1)):
      #   print("location of note:"+  str(result_array.index(47717)))
      result_array.clear()