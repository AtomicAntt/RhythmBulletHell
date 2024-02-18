import json

data = '''
- StartTime: 25662
  Lane: 4
  KeySounds: []
- StartTime: 26462
  Lane: 4
  KeySounds: []
- StartTime: 28062
  Lane: 4
  KeySounds: []
- StartTime: 28862
  Lane: 4
  KeySounds: []
- StartTime: 29662
  Lane: 4
  KeySounds: []
- StartTime: 31262
  Lane: 4
  KeySounds: []
- StartTime: 32062
  Lane: 4
  KeySounds: []
- StartTime: 32862
  Lane: 4
  KeySounds: []
- StartTime: 34462
  Lane: 4
  KeySounds: []
- StartTime: 35262
  Lane: 4
  KeySounds: []
- StartTime: 36062
  Lane: 4
  KeySounds: []
- StartTime: 36462
  Lane: 4
  KeySounds: []
- StartTime: 36662
  Lane: 4
  KeySounds: []
- StartTime: 37062
  Lane: 4
  KeySounds: []
- StartTime: 37262
  Lane: 4
  KeySounds: []
- StartTime: 37662
  Lane: 4
  KeySounds: []
- StartTime: 38062
  Lane: 4
  KeySounds: []
- StartTime: 38262
  Lane: 4
  KeySounds: []
- StartTime: 38462
  Lane: 4
  KeySounds: []
- StartTime: 39262
  Lane: 4
  KeySounds: []
- StartTime: 40862
  Lane: 4
  KeySounds: []
- StartTime: 41662
  Lane: 4
  KeySounds: []
- StartTime: 42462
  Lane: 4
  KeySounds: []
- StartTime: 44062
  Lane: 4
  KeySounds: []
- StartTime: 44862
  Lane: 4
  KeySounds: []
- StartTime: 45662
  Lane: 4
  KeySounds: []
- StartTime: 47262
  Lane: 4
  KeySounds: []
- StartTime: 48062
  Lane: 4
  KeySounds: []
- StartTime: 48862
  Lane: 4
  KeySounds: []
- StartTime: 49262
  Lane: 4
  KeySounds: []
- StartTime: 49462
  Lane: 4
  KeySounds: []
- StartTime: 49862
  Lane: 4
  KeySounds: []
- StartTime: 50062
  Lane: 4
  KeySounds: []
- StartTime: 50462
  Lane: 4
  KeySounds: []
- StartTime: 50862
  Lane: 4
  KeySounds: []
- StartTime: 51062
  Lane: 4
  KeySounds: []
- StartTime: 51262
  Lane: 4
  KeySounds: []
- StartTime: 52062
  Lane: 4
  KeySounds: []
- StartTime: 53662
  Lane: 4
  KeySounds: []
- StartTime: 54462
  Lane: 4
  KeySounds: []
- StartTime: 55262
  Lane: 4
  KeySounds: []
- StartTime: 56862
  Lane: 4
  KeySounds: []
- StartTime: 57662
  Lane: 4
  KeySounds: []
- StartTime: 58462
  Lane: 4
  KeySounds: []
- StartTime: 60062
  Lane: 4
  KeySounds: []
- StartTime: 60862
  Lane: 4
  KeySounds: []
- StartTime: 61662
  Lane: 4
  KeySounds: []
- StartTime: 62062
  Lane: 4
  KeySounds: []
- StartTime: 62262
  Lane: 4
  KeySounds: []
- StartTime: 62662
  Lane: 4
  KeySounds: []
- StartTime: 62862
  Lane: 4
  KeySounds: []
- StartTime: 63262
  Lane: 4
  KeySounds: []
- StartTime: 63662
  Lane: 4
  KeySounds: []
- StartTime: 63862
  Lane: 4
  KeySounds: []
- StartTime: 70462
  Lane: 4
  KeySounds: []
- StartTime: 76862
  Lane: 4
  KeySounds: []
- StartTime: 77662
  Lane: 4
  KeySounds: []
- StartTime: 79262
  Lane: 4
  KeySounds: []
- StartTime: 80062
  Lane: 4
  KeySounds: []
- StartTime: 80862
  Lane: 4
  KeySounds: []
- StartTime: 82462
  Lane: 4
  KeySounds: []
- StartTime: 83262
  Lane: 4
  KeySounds: []
- StartTime: 84062
  Lane: 4
  KeySounds: []
- StartTime: 85662
  Lane: 4
  KeySounds: []
- StartTime: 86462
  Lane: 4
  KeySounds: []
- StartTime: 87262
  Lane: 4
  KeySounds: []
- StartTime: 87662
  Lane: 4
  KeySounds: []
- StartTime: 87862
  Lane: 4
  KeySounds: []
- StartTime: 88262
  Lane: 4
  KeySounds: []
- StartTime: 88462
  Lane: 4
  KeySounds: []
- StartTime: 88862
  Lane: 4
  KeySounds: []
- StartTime: 89262
  Lane: 4
  KeySounds: []
- StartTime: 89462
  Lane: 4
  KeySounds: []
- StartTime: 89662
  Lane: 4
  KeySounds: []
- StartTime: 90462
  Lane: 4
  KeySounds: []
- StartTime: 92062
  Lane: 4
  KeySounds: []
- StartTime: 92862
  Lane: 4
  KeySounds: []
- StartTime: 93662
  Lane: 4
  KeySounds: []
- StartTime: 95262
  Lane: 4
  KeySounds: []
- StartTime: 96062
  Lane: 4
  KeySounds: []
- StartTime: 96862
  Lane: 4
  KeySounds: []
- StartTime: 98462
  Lane: 4
  KeySounds: []
- StartTime: 99262
  Lane: 4
  KeySounds: []
- StartTime: 100062
  Lane: 4
  KeySounds: []
- StartTime: 100462
  Lane: 4
  KeySounds: []
- StartTime: 100662
  Lane: 4
  KeySounds: []
- StartTime: 101062
  Lane: 4
  KeySounds: []
- StartTime: 101262
  Lane: 4
  KeySounds: []
- StartTime: 101662
  Lane: 4
  KeySounds: []
- StartTime: 102062
  Lane: 4
  KeySounds: []
- StartTime: 102262
  Lane: 4
  KeySounds: []
- StartTime: 102462
  Lane: 4
  KeySounds: []
- StartTime: 103262
  Lane: 4
  KeySounds: []
- StartTime: 104862
  Lane: 4
  KeySounds: []
- StartTime: 105662
  Lane: 4
  KeySounds: []
- StartTime: 106462
  Lane: 4
  KeySounds: []
- StartTime: 108062
  Lane: 4
  KeySounds: []
- StartTime: 108862
  Lane: 4
  KeySounds: []
- StartTime: 109662
  Lane: 4
  KeySounds: []
- StartTime: 111262
  Lane: 4
  KeySounds: []
- StartTime: 112062
  Lane: 4
  KeySounds: []
- StartTime: 112862
  Lane: 4
  KeySounds: []
- StartTime: 113262
  Lane: 4
  KeySounds: []
- StartTime: 113462
  Lane: 4
  KeySounds: []
- StartTime: 113862
  Lane: 4
  KeySounds: []
- StartTime: 114062
  Lane: 4
  KeySounds: []
- StartTime: 114462
  Lane: 4
  KeySounds: []
- StartTime: 114862
  Lane: 4
  KeySounds: []
- StartTime: 115062
  Lane: 4
  KeySounds: []
- StartTime: 115262
  Lane: 4
  KeySounds: []
- StartTime: 116062
  Lane: 4
  KeySounds: []
- StartTime: 117662
  Lane: 4
  KeySounds: []
- StartTime: 118462
  Lane: 4
  KeySounds: []
- StartTime: 119262
  Lane: 4
  KeySounds: []
- StartTime: 120862
  Lane: 4
  KeySounds: []
- StartTime: 121662
  Lane: 4
  KeySounds: []
- StartTime: 122462
  Lane: 4
  KeySounds: []
- StartTime: 124062
  Lane: 4
  KeySounds: []
- StartTime: 124862
  Lane: 4
  KeySounds: []
- StartTime: 125662
  Lane: 4
  KeySounds: []
- StartTime: 126062
  Lane: 4
  KeySounds: []
- StartTime: 126262
  Lane: 4
  KeySounds: []
- StartTime: 126662
  Lane: 4
  KeySounds: []
- StartTime: 126862
  Lane: 4
  KeySounds: []
- StartTime: 127262
  Lane: 4
  KeySounds: []
- StartTime: 127662
  Lane: 4
  KeySounds: []
- StartTime: 127862
  Lane: 4
  KeySounds: []
- StartTime: 128062
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
      print(len(result_array))
      # if (j == (4-1)):
      #   print("location of note:"+  str(result_array.index(20417)))
      result_array.clear()