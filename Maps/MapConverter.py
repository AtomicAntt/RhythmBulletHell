import json

data = '''
- StartTime: 20417
  Lane: 4
  KeySounds: []
- StartTime: 24917
  Lane: 4
  KeySounds: []
- StartTime: 24992
  Lane: 4
  KeySounds: []
- StartTime: 25067
  Lane: 4
  KeySounds: []
- StartTime: 25217
  Lane: 4
  KeySounds: []
- StartTime: 30017
  Lane: 4
  KeySounds: []
- StartTime: 34517
  Lane: 4
  KeySounds: []
- StartTime: 34667
  Lane: 4
  KeySounds: []
- StartTime: 34817
  Lane: 4
  KeySounds: []
- StartTime: 38417
  Lane: 4
  KeySounds: []
- StartTime: 39017
  Lane: 4
  KeySounds: []
- StartTime: 39467
  Lane: 4
  KeySounds: []
- StartTime: 39617
  Lane: 4
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
- StartTime: 40742
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
- StartTime: 42017
  Lane: 4
  KeySounds: []
- StartTime: 42317
  Lane: 4
  KeySounds: []
- StartTime: 42392
  Lane: 4
  KeySounds: []
- StartTime: 42467
  Lane: 4
  KeySounds: []
- StartTime: 42542
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
- StartTime: 45542
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
- StartTime: 47117
  Lane: 4
  KeySounds: []
- StartTime: 47192
  Lane: 4
  KeySounds: []
- StartTime: 47267
  Lane: 4
  KeySounds: []
- StartTime: 47342
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
        print("location of note:"+  str(result_array.index(47717)))
      result_array.clear()