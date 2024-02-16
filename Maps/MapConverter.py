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
- StartTime: 50400
  Lane: 4
  KeySounds: []
- StartTime: 50475
  Lane: 4
  KeySounds: []
- StartTime: 50550
  Lane: 4
  KeySounds: []
- StartTime: 50625
  Lane: 4
  KeySounds: []
- StartTime: 50700
  Lane: 4
  KeySounds: []
- StartTime: 50775
  Lane: 4
  KeySounds: []
- StartTime: 50850
  Lane: 4
  KeySounds: []
- StartTime: 50925
  Lane: 4
  KeySounds: []
- StartTime: 51000
  Lane: 4
  KeySounds: []
- StartTime: 51075
  Lane: 4
  KeySounds: []
- StartTime: 51150
  Lane: 4
  KeySounds: []
- StartTime: 51225
  Lane: 4
  KeySounds: []
- StartTime: 51300
  Lane: 4
  KeySounds: []
- StartTime: 51375
  Lane: 4
  KeySounds: []
- StartTime: 51450
  Lane: 4
  KeySounds: []
- StartTime: 51525
  Lane: 4
  KeySounds: []
- StartTime: 51600
  Lane: 4
  KeySounds: []
- StartTime: 51675
  Lane: 4
  KeySounds: []
- StartTime: 51750
  Lane: 4
  KeySounds: []
- StartTime: 51825
  Lane: 4
  KeySounds: []
- StartTime: 51900
  Lane: 4
  KeySounds: []
- StartTime: 51975
  Lane: 4
  KeySounds: []
- StartTime: 52050
  Lane: 4
  KeySounds: []
- StartTime: 52125
  Lane: 4
  KeySounds: []
- StartTime: 52200
  Lane: 4
  KeySounds: []
- StartTime: 52275
  Lane: 4
  KeySounds: []
- StartTime: 52350
  Lane: 4
  KeySounds: []
- StartTime: 52425
  Lane: 4
  KeySounds: []
- StartTime: 52500
  Lane: 4
  KeySounds: []
- StartTime: 52575
  Lane: 4
  KeySounds: []
- StartTime: 52650
  Lane: 4
  KeySounds: []
- StartTime: 52725
  Lane: 4
  KeySounds: []
- StartTime: 52800
  Lane: 1
  KeySounds: []
- StartTime: 52800
  Lane: 4
  KeySounds: []
- StartTime: 52875
  Lane: 4
  KeySounds: []
- StartTime: 52950
  Lane: 4
  KeySounds: []
- StartTime: 53025
  Lane: 4
  KeySounds: []
- StartTime: 53100
  Lane: 4
  KeySounds: []
- StartTime: 53175
  Lane: 4
  KeySounds: []
- StartTime: 53250
  Lane: 4
  KeySounds: []
- StartTime: 53325
  Lane: 4
  KeySounds: []
- StartTime: 53400
  Lane: 4
  KeySounds: []
- StartTime: 53475
  Lane: 4
  KeySounds: []
- StartTime: 53550
  Lane: 4
  KeySounds: []
- StartTime: 53625
  Lane: 4
  KeySounds: []
- StartTime: 53625
  Lane: 1
  KeySounds: []
- StartTime: 53700
  Lane: 4
  KeySounds: []
- StartTime: 53700
  Lane: 3
  KeySounds: []
- StartTime: 53775
  Lane: 4
  KeySounds: []
- StartTime: 53850
  Lane: 4
  KeySounds: []
- StartTime: 53925
  Lane: 4
  KeySounds: []
- StartTime: 54000
  Lane: 4
  KeySounds: []
- StartTime: 54075
  Lane: 4
  KeySounds: []
- StartTime: 54150
  Lane: 4
  KeySounds: []
- StartTime: 54225
  Lane: 4
  KeySounds: []
- StartTime: 54300
  Lane: 4
  KeySounds: []
- StartTime: 54375
  Lane: 4
  KeySounds: []
- StartTime: 54450
  Lane: 4
  KeySounds: []
- StartTime: 54525
  Lane: 4
  KeySounds: []
- StartTime: 54600
  Lane: 4
  KeySounds: []
- StartTime: 54675
  Lane: 4
  KeySounds: []
- StartTime: 54750
  Lane: 4
  KeySounds: []
- StartTime: 54825
  Lane: 4
  KeySounds: []
- StartTime: 54900
  Lane: 4
  KeySounds: []
- StartTime: 54975
  Lane: 4
  KeySounds: []
- StartTime: 55050
  Lane: 4
  KeySounds: []
- StartTime: 55125
  Lane: 4
  KeySounds: []
- StartTime: 55200
  Lane: 4
  KeySounds: []
- StartTime: 55200
  Lane: 3
  KeySounds: []
- StartTime: 55275
  Lane: 4
  KeySounds: []
- StartTime: 55350
  Lane: 4
  KeySounds: []
- StartTime: 55425
  Lane: 4
  KeySounds: []
- StartTime: 55500
  Lane: 4
  KeySounds: []
- StartTime: 55575
  Lane: 4
  KeySounds: []
- StartTime: 55650
  Lane: 4
  KeySounds: []
- StartTime: 55725
  Lane: 4
  KeySounds: []
- StartTime: 55800
  Lane: 4
  KeySounds: []
- StartTime: 55875
  Lane: 4
  KeySounds: []
- StartTime: 55950
  Lane: 4
  KeySounds: []
- StartTime: 56025
  Lane: 4
  KeySounds: []
- StartTime: 56100
  Lane: 4
  KeySounds: []
- StartTime: 56175
  Lane: 4
  KeySounds: []
- StartTime: 56250
  Lane: 4
  KeySounds: []
- StartTime: 56325
  Lane: 4
  KeySounds: []
- StartTime: 56400
  Lane: 4
  KeySounds: []
- StartTime: 56475
  Lane: 4
  KeySounds: []
- StartTime: 56550
  Lane: 4
  KeySounds: []
- StartTime: 56625
  Lane: 4
  KeySounds: []
- StartTime: 56700
  Lane: 4
  KeySounds: []
- StartTime: 56775
  Lane: 4
  KeySounds: []
- StartTime: 56850
  Lane: 4
  KeySounds: []
- StartTime: 56925
  Lane: 4
  KeySounds: []
- StartTime: 57000
  Lane: 4
  KeySounds: []
- StartTime: 57075
  Lane: 4
  KeySounds: []
- StartTime: 57150
  Lane: 4
  KeySounds: []
- StartTime: 57225
  Lane: 4
  KeySounds: []
- StartTime: 57300
  Lane: 4
  KeySounds: []
- StartTime: 57375
  Lane: 4
  KeySounds: []
- StartTime: 57450
  Lane: 4
  KeySounds: []
- StartTime: 57525
  Lane: 4
  KeySounds: []
- StartTime: 57600
  Lane: 4
  KeySounds: []
- StartTime: 57600
  Lane: 1
  KeySounds: []
- StartTime: 57675
  Lane: 4
  KeySounds: []
- StartTime: 57750
  Lane: 4
  KeySounds: []
- StartTime: 57825
  Lane: 4
  KeySounds: []
- StartTime: 57900
  Lane: 4
  KeySounds: []
- StartTime: 57975
  Lane: 4
  KeySounds: []
- StartTime: 58050
  Lane: 4
  KeySounds: []
- StartTime: 58125
  Lane: 4
  KeySounds: []
- StartTime: 58200
  Lane: 4
  KeySounds: []
- StartTime: 58275
  Lane: 4
  KeySounds: []
- StartTime: 58350
  Lane: 4
  KeySounds: []
- StartTime: 58425
  Lane: 4
  KeySounds: []
- StartTime: 58500
  Lane: 4
  KeySounds: []
- StartTime: 58575
  Lane: 4
  KeySounds: []
- StartTime: 58650
  Lane: 4
  KeySounds: []
- StartTime: 58725
  Lane: 4
  KeySounds: []
- StartTime: 58800
  Lane: 4
  KeySounds: []
- StartTime: 58875
  Lane: 4
  KeySounds: []
- StartTime: 58950
  Lane: 4
  KeySounds: []
- StartTime: 59025
  Lane: 4
  KeySounds: []
- StartTime: 59100
  Lane: 4
  KeySounds: []
- StartTime: 59175
  Lane: 4
  KeySounds: []
- StartTime: 59250
  Lane: 4
  KeySounds: []
- StartTime: 59325
  Lane: 4
  KeySounds: []
- StartTime: 59400
  Lane: 4
  KeySounds: []
- StartTime: 59475
  Lane: 4
  KeySounds: []
- StartTime: 59550
  Lane: 4
  KeySounds: []
- StartTime: 59625
  Lane: 4
  KeySounds: []
- StartTime: 59700
  Lane: 4
  KeySounds: []
- StartTime: 59775
  Lane: 4
  KeySounds: []
- StartTime: 59850
  Lane: 4
  KeySounds: []
- StartTime: 59925
  Lane: 4
  KeySounds: []
- StartTime: 59925
  Lane: 1
  KeySounds: []
- StartTime: 60000
  Lane: 4
  KeySounds: []
- StartTime: 60000
  Lane: 3
  KeySounds: []
- StartTime: 60075
  Lane: 4
  KeySounds: []
- StartTime: 60150
  Lane: 4
  KeySounds: []
- StartTime: 60225
  Lane: 4
  KeySounds: []
- StartTime: 60300
  Lane: 4
  KeySounds: []
- StartTime: 60375
  Lane: 4
  KeySounds: []
- StartTime: 60450
  Lane: 4
  KeySounds: []
- StartTime: 60525
  Lane: 4
  KeySounds: []
- StartTime: 60600
  Lane: 4
  KeySounds: []
- StartTime: 60675
  Lane: 4
  KeySounds: []
- StartTime: 60750
  Lane: 4
  KeySounds: []
- StartTime: 60825
  Lane: 4
  KeySounds: []
- StartTime: 60900
  Lane: 4
  KeySounds: []
- StartTime: 60975
  Lane: 4
  KeySounds: []
- StartTime: 61050
  Lane: 4
  KeySounds: []
- StartTime: 61125
  Lane: 4
  KeySounds: []
- StartTime: 61200
  Lane: 4
  KeySounds: []
- StartTime: 61200
  Lane: 3
  KeySounds: []
- StartTime: 61275
  Lane: 4
  KeySounds: []
- StartTime: 61275
  Lane: 1
  KeySounds: []
- StartTime: 61350
  Lane: 4
  KeySounds: []
- StartTime: 61425
  Lane: 4
  KeySounds: []
- StartTime: 61500
  Lane: 4
  KeySounds: []
- StartTime: 61575
  Lane: 4
  KeySounds: []
- StartTime: 61650
  Lane: 4
  KeySounds: []
- StartTime: 61725
  Lane: 4
  KeySounds: []
- StartTime: 61800
  Lane: 4
  KeySounds: []
- StartTime: 61875
  Lane: 4
  KeySounds: []
- StartTime: 61950
  Lane: 4
  KeySounds: []
- StartTime: 62025
  Lane: 4
  KeySounds: []
- StartTime: 62100
  Lane: 4
  KeySounds: []
- StartTime: 62175
  Lane: 4
  KeySounds: []
- StartTime: 62250
  Lane: 4
  KeySounds: []
- StartTime: 62325
  Lane: 4
  KeySounds: []
- StartTime: 62400
  Lane: 4
  KeySounds: []
- StartTime: 62400
  Lane: 1
  KeySounds: []
- StartTime: 62475
  Lane: 4
  KeySounds: []
- StartTime: 62550
  Lane: 4
  KeySounds: []
- StartTime: 62625
  Lane: 4
  KeySounds: []
- StartTime: 62700
  Lane: 4
  KeySounds: []
- StartTime: 62775
  Lane: 4
  KeySounds: []
- StartTime: 62850
  Lane: 4
  KeySounds: []
- StartTime: 62925
  Lane: 4
  KeySounds: []
- StartTime: 63000
  Lane: 4
  KeySounds: []
- StartTime: 63075
  Lane: 4
  KeySounds: []
- StartTime: 63150
  Lane: 4
  KeySounds: []
- StartTime: 63225
  Lane: 4
  KeySounds: []
- StartTime: 63300
  Lane: 4
  KeySounds: []
- StartTime: 63375
  Lane: 4
  KeySounds: []
- StartTime: 63450
  Lane: 4
  KeySounds: []
- StartTime: 63525
  Lane: 4
  KeySounds: []
- StartTime: 63600
  Lane: 4
  KeySounds: []
- StartTime: 63675
  Lane: 4
  KeySounds: []
- StartTime: 63750
  Lane: 4
  KeySounds: []
- StartTime: 63825
  Lane: 4
  KeySounds: []
- StartTime: 63900
  Lane: 4
  KeySounds: []
- StartTime: 63975
  Lane: 4
  KeySounds: []
- StartTime: 64050
  Lane: 4
  KeySounds: []
- StartTime: 64125
  Lane: 4
  KeySounds: []
- StartTime: 64200
  Lane: 4
  KeySounds: []
- StartTime: 64275
  Lane: 4
  KeySounds: []
- StartTime: 64350
  Lane: 4
  KeySounds: []
- StartTime: 64425
  Lane: 4
  KeySounds: []
- StartTime: 64500
  Lane: 4
  KeySounds: []
- StartTime: 64575
  Lane: 4
  KeySounds: []
- StartTime: 64650
  Lane: 4
  KeySounds: []
- StartTime: 64725
  Lane: 4
  KeySounds: []
- StartTime: 64800
  Lane: 4
  KeySounds: []
- StartTime: 64800
  Lane: 3
  KeySounds: []
- StartTime: 64875
  Lane: 4
  KeySounds: []
- StartTime: 64950
  Lane: 4
  KeySounds: []
- StartTime: 65025
  Lane: 4
  KeySounds: []
- StartTime: 65100
  Lane: 4
  KeySounds: []
- StartTime: 65175
  Lane: 4
  KeySounds: []
- StartTime: 65250
  Lane: 4
  KeySounds: []
- StartTime: 65325
  Lane: 4
  KeySounds: []
- StartTime: 65400
  Lane: 4
  KeySounds: []
- StartTime: 65475
  Lane: 4
  KeySounds: []
- StartTime: 65550
  Lane: 4
  KeySounds: []
- StartTime: 65625
  Lane: 4
  KeySounds: []
- StartTime: 65700
  Lane: 4
  KeySounds: []
- StartTime: 65775
  Lane: 4
  KeySounds: []
- StartTime: 65850
  Lane: 4
  KeySounds: []
- StartTime: 65925
  Lane: 3
  KeySounds: []
- StartTime: 65925
  Lane: 4
  KeySounds: []
- StartTime: 66000
  Lane: 1
  KeySounds: []
- StartTime: 66000
  Lane: 4
  KeySounds: []
- StartTime: 66075
  Lane: 4
  KeySounds: []
- StartTime: 66150
  Lane: 4
  KeySounds: []
- StartTime: 66225
  Lane: 4
  KeySounds: []
- StartTime: 66300
  Lane: 4
  KeySounds: []
- StartTime: 66375
  Lane: 4
  KeySounds: []
- StartTime: 66450
  Lane: 4
  KeySounds: []
- StartTime: 66525
  Lane: 4
  KeySounds: []
- StartTime: 66600
  Lane: 4
  KeySounds: []
- StartTime: 66675
  Lane: 4
  KeySounds: []
- StartTime: 66750
  Lane: 4
  KeySounds: []
- StartTime: 66825
  Lane: 4
  KeySounds: []
- StartTime: 66900
  Lane: 4
  KeySounds: []
- StartTime: 66975
  Lane: 4
  KeySounds: []
- StartTime: 67050
  Lane: 4
  KeySounds: []
- StartTime: 67125
  Lane: 4
  KeySounds: []
- StartTime: 67200
  Lane: 1
  KeySounds: []
- StartTime: 67200
  Lane: 4
  KeySounds: []
- StartTime: 67275
  Lane: 4
  KeySounds: []
- StartTime: 67350
  Lane: 4
  KeySounds: []
- StartTime: 67425
  Lane: 4
  KeySounds: []
- StartTime: 67500
  Lane: 4
  KeySounds: []
- StartTime: 67575
  Lane: 4
  KeySounds: []
- StartTime: 67650
  Lane: 4
  KeySounds: []
- StartTime: 67725
  Lane: 4
  KeySounds: []
- StartTime: 67800
  Lane: 4
  KeySounds: []
- StartTime: 67875
  Lane: 4
  KeySounds: []
- StartTime: 67950
  Lane: 4
  KeySounds: []
- StartTime: 68025
  Lane: 4
  KeySounds: []
- StartTime: 68100
  Lane: 4
  KeySounds: []
- StartTime: 68175
  Lane: 4
  KeySounds: []
- StartTime: 68250
  Lane: 4
  KeySounds: []
- StartTime: 68325
  Lane: 4
  KeySounds: []
- StartTime: 68400
  Lane: 4
  KeySounds: []
- StartTime: 68475
  Lane: 4
  KeySounds: []
- StartTime: 68550
  Lane: 4
  KeySounds: []
- StartTime: 68625
  Lane: 4
  KeySounds: []
- StartTime: 68700
  Lane: 4
  KeySounds: []
- StartTime: 68775
  Lane: 4
  KeySounds: []
- StartTime: 68850
  Lane: 4
  KeySounds: []
- StartTime: 68925
  Lane: 4
  KeySounds: []
- StartTime: 69000
  Lane: 4
  KeySounds: []
- StartTime: 69075
  Lane: 4
  KeySounds: []
- StartTime: 69150
  Lane: 4
  KeySounds: []
- StartTime: 69225
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