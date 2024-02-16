import json

data = '''
- StartTime: 9617
  Lane: 3
  KeySounds: []
- StartTime: 9917
  Lane: 4
  KeySounds: []
- StartTime: 10217
  Lane: 4
  KeySounds: []
- StartTime: 10517
  Lane: 4
  KeySounds: []
- StartTime: 10817
  Lane: 3
  KeySounds: []
- StartTime: 11117
  Lane: 4
  KeySounds: []
- StartTime: 11117
  Lane: 1
  KeySounds: []
- StartTime: 11267
  Lane: 4
  KeySounds: []
- StartTime: 11417
  Lane: 4
  KeySounds: []
- StartTime: 11717
  Lane: 4
  KeySounds: []
- StartTime: 11717
  Lane: 1
  KeySounds: []
- StartTime: 12017
  Lane: 3
  KeySounds: []
- StartTime: 12317
  Lane: 4
  KeySounds: []
- StartTime: 12617
  Lane: 4
  KeySounds: []
- StartTime: 12917
  Lane: 4
  KeySounds: []
- StartTime: 13217
  Lane: 3
  KeySounds: []
- StartTime: 13517
  Lane: 4
  KeySounds: []
- StartTime: 13517
  Lane: 1
  KeySounds: []
- StartTime: 13667
  Lane: 4
  KeySounds: []
- StartTime: 13817
  Lane: 4
  KeySounds: []
- StartTime: 14117
  Lane: 4
  KeySounds: []
- StartTime: 14117
  Lane: 1
  KeySounds: []
- StartTime: 14417
  Lane: 3
  KeySounds: []
- StartTime: 14717
  Lane: 4
  KeySounds: []
- StartTime: 15017
  Lane: 4
  KeySounds: []
- StartTime: 15317
  Lane: 4
  KeySounds: []
- StartTime: 15617
  Lane: 3
  KeySounds: []
- StartTime: 15917
  Lane: 4
  KeySounds: []
- StartTime: 15917
  Lane: 1
  KeySounds: []
- StartTime: 16067
  Lane: 4
  KeySounds: []
- StartTime: 16217
  Lane: 4
  KeySounds: []
- StartTime: 16517
  Lane: 4
  KeySounds: []
- StartTime: 16517
  Lane: 1
  KeySounds: []
- StartTime: 16817
  Lane: 3
  KeySounds: []
- StartTime: 17117
  Lane: 4
  KeySounds: []
- StartTime: 17417
  Lane: 4
  KeySounds: []
- StartTime: 17717
  Lane: 4
  KeySounds: []
- StartTime: 18017
  Lane: 3
  KeySounds: []
- StartTime: 20417
  Lane: 1
  KeySounds: []
- StartTime: 20717
  Lane: 4
  KeySounds: []
- StartTime: 21017
  Lane: 4
  KeySounds: []
- StartTime: 21317
  Lane: 4
  KeySounds: []
- StartTime: 21617
  Lane: 1
  KeySounds: []
- StartTime: 21917
  Lane: 4
  KeySounds: []
- StartTime: 21917
  Lane: 3
  KeySounds: []
- StartTime: 22067
  Lane: 4
  KeySounds: []
- StartTime: 22217
  Lane: 4
  KeySounds: []
- StartTime: 22517
  Lane: 4
  KeySounds: []
- StartTime: 22517
  Lane: 3
  KeySounds: []
- StartTime: 22817
  Lane: 1
  KeySounds: []
- StartTime: 23117
  Lane: 4
  KeySounds: []
- StartTime: 23417
  Lane: 4
  KeySounds: []
- StartTime: 23717
  Lane: 4
  KeySounds: []
- StartTime: 24017
  Lane: 1
  KeySounds: []
- StartTime: 24317
  Lane: 4
  KeySounds: []
- StartTime: 24317
  Lane: 3
  KeySounds: []
- StartTime: 24467
  Lane: 4
  KeySounds: []
- StartTime: 24617
  Lane: 4
  KeySounds: []
- StartTime: 24917
  Lane: 4
  KeySounds: []
- StartTime: 24917
  Lane: 3
  KeySounds: []
- StartTime: 25217
  Lane: 1
  KeySounds: []
- StartTime: 25517
  Lane: 4
  KeySounds: []
- StartTime: 25817
  Lane: 4
  KeySounds: []
- StartTime: 26117
  Lane: 4
  KeySounds: []
- StartTime: 26417
  Lane: 1
  KeySounds: []
- StartTime: 26717
  Lane: 4
  KeySounds: []
- StartTime: 26717
  Lane: 3
  KeySounds: []
- StartTime: 26867
  Lane: 4
  KeySounds: []
- StartTime: 27017
  Lane: 4
  KeySounds: []
- StartTime: 27317
  Lane: 4
  KeySounds: []
- StartTime: 27317
  Lane: 3
  KeySounds: []
- StartTime: 27392
  Lane: 7
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
  Lane: 7
  KeySounds: []
- StartTime: 30017
  Lane: 4
  KeySounds: []
- StartTime: 30017
  Lane: 5
  KeySounds: []
- StartTime: 30317
  Lane: 4
  KeySounds: []
- StartTime: 30617
  Lane: 4
  KeySounds: []
- StartTime: 30917
  Lane: 4
  KeySounds: []
- StartTime: 31217
  Lane: 4
  KeySounds: []
- StartTime: 31217
  Lane: 5
  KeySounds: []
- StartTime: 31517
  Lane: 4
  KeySounds: []
- StartTime: 31517
  Lane: 7
  KeySounds: []
- StartTime: 31667
  Lane: 4
  KeySounds: []
- StartTime: 31817
  Lane: 4
  KeySounds: []
- StartTime: 32117
  Lane: 4
  KeySounds: []
- StartTime: 32117
  Lane: 7
  KeySounds: []
- StartTime: 32417
  Lane: 4
  KeySounds: []
- StartTime: 32417
  Lane: 5
  KeySounds: []
- StartTime: 32717
  Lane: 4
  KeySounds: []
- StartTime: 33017
  Lane: 4
  KeySounds: []
- StartTime: 33317
  Lane: 4
  KeySounds: []
- StartTime: 33617
  Lane: 4
  KeySounds: []
- StartTime: 33617
  Lane: 5
  KeySounds: []
- StartTime: 33917
  Lane: 4
  KeySounds: []
- StartTime: 33917
  Lane: 7
  KeySounds: []
- StartTime: 34067
  Lane: 4
  KeySounds: []
- StartTime: 34217
  Lane: 4
  KeySounds: []
- StartTime: 34517
  Lane: 4
  KeySounds: []
- StartTime: 34517
  Lane: 7
  KeySounds: []
- StartTime: 34817
  Lane: 4
  KeySounds: []
- StartTime: 34817
  Lane: 5
  KeySounds: []
- StartTime: 35117
  Lane: 4
  KeySounds: []
- StartTime: 35417
  Lane: 4
  KeySounds: []
- StartTime: 35717
  Lane: 4
  KeySounds: []
- StartTime: 36017
  Lane: 4
  KeySounds: []
- StartTime: 36017
  Lane: 5
  KeySounds: []
- StartTime: 36317
  Lane: 4
  KeySounds: []
- StartTime: 36317
  Lane: 7
  KeySounds: []
- StartTime: 36467
  Lane: 4
  KeySounds: []
- StartTime: 36617
  Lane: 4
  KeySounds: []
- StartTime: 36917
  Lane: 4
  KeySounds: []
- StartTime: 36917
  Lane: 7
  KeySounds: []
- StartTime: 37217
  Lane: 4
  KeySounds: []
- StartTime: 37217
  Lane: 3
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
- StartTime: 39617
  Lane: 4
  KeySounds: []
- StartTime: 39617
  Lane: 3
  KeySounds: []
- StartTime: 39692
  Lane: 1
  KeySounds: []
- StartTime: 39917
  Lane: 4
  KeySounds: []
- StartTime: 40067
  Lane: 4
  KeySounds: []
- StartTime: 40217
  Lane: 4
  KeySounds: []
- StartTime: 40517
  Lane: 4
  KeySounds: []
- StartTime: 40667
  Lane: 4
  KeySounds: []
- StartTime: 40817
  Lane: 4
  KeySounds: []
- StartTime: 41117
  Lane: 4
  KeySounds: []
- StartTime: 41267
  Lane: 4
  KeySounds: []
- StartTime: 41417
  Lane: 4
  KeySounds: []
- StartTime: 41717
  Lane: 4
  KeySounds: []
- StartTime: 41942
  Lane: 1
  KeySounds: []
- StartTime: 42017
  Lane: 4
  KeySounds: []
- StartTime: 42017
  Lane: 3
  KeySounds: []
- StartTime: 42317
  Lane: 4
  KeySounds: []
- StartTime: 42617
  Lane: 4
  KeySounds: []
- StartTime: 42917
  Lane: 4
  KeySounds: []
- StartTime: 43067
  Lane: 4
  KeySounds: []
- StartTime: 43217
  Lane: 4
  KeySounds: []
- StartTime: 43517
  Lane: 4
  KeySounds: []
- StartTime: 43592
  Lane: 4
  KeySounds: []
- StartTime: 43667
  Lane: 4
  KeySounds: []
- StartTime: 43742
  Lane: 4
  KeySounds: []
- StartTime: 43817
  Lane: 4
  KeySounds: []
- StartTime: 44117
  Lane: 4
  KeySounds: []
- StartTime: 44267
  Lane: 4
  KeySounds: []
- StartTime: 44417
  Lane: 4
  KeySounds: []
- StartTime: 44417
  Lane: 3
  KeySounds: []
- StartTime: 44492
  Lane: 1
  KeySounds: []
- StartTime: 44717
  Lane: 4
  KeySounds: []
- StartTime: 44867
  Lane: 4
  KeySounds: []
- StartTime: 45017
  Lane: 4
  KeySounds: []
- StartTime: 45317
  Lane: 4
  KeySounds: []
- StartTime: 45467
  Lane: 4
  KeySounds: []
- StartTime: 45617
  Lane: 4
  KeySounds: []
- StartTime: 45917
  Lane: 4
  KeySounds: []
- StartTime: 46067
  Lane: 4
  KeySounds: []
- StartTime: 46217
  Lane: 4
  KeySounds: []
- StartTime: 46517
  Lane: 4
  KeySounds: []
- StartTime: 46817
  Lane: 4
  KeySounds: []
- StartTime: 46817
  Lane: 1
  KeySounds: []
- StartTime: 46892
  Lane: 3
  KeySounds: []
- StartTime: 47117
  Lane: 4
  KeySounds: []
- StartTime: 47417
  Lane: 4
  KeySounds: []
- StartTime: 47717
  Lane: 4
  KeySounds: []
- StartTime: 47867
  Lane: 4
  KeySounds: []
- StartTime: 48017
  Lane: 4
  KeySounds: []
- StartTime: 48317
  Lane: 4
  KeySounds: []
- StartTime: 48392
  Lane: 4
  KeySounds: []
- StartTime: 48467
  Lane: 4
  KeySounds: []
- StartTime: 48542
  Lane: 4
  KeySounds: []
- StartTime: 48617
  Lane: 4
  KeySounds: []
- StartTime: 48917
  Lane: 4
  KeySounds: []
- StartTime: 49067
  Lane: 4
  KeySounds: []
- StartTime: 49217
  Lane: 3
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
        print("location of note:"+  str(result_array.index(46217)))
      result_array.clear()