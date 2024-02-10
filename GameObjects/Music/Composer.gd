extends AudioStreamPlayer

var bpm = 175
var songPos = 0.0
var secPerBeat

var previousSongPos = 0

var songPositions = [18, 360, 703, 1046, 1389, 1732, 2075, 2418, 2760, 3103, 3446, 3789, 4132, 4475, 4818, 4989, 5160, 5503, 5846, 6189, 6532, 6875, 7218, 7560, 7903, 8246, 8589, 8932, 9275, 9618, 9960, 10303, 10475, 10646, 11332, 12018, 12703, 13389, 14075, 14760, 15446, 16132]

var songPosIndex = 0

func _ready():
	secPerBeat = 60.0/bpm

func _process(delta):
	songPos = get_playback_position() + AudioServer.get_time_since_last_mix()
	songPos -= AudioServer.get_output_latency();
	songPos *= 1000;
	songPos = int(songPos);
	
	if playing and songPos >= songPositions[songPosIndex]:
		print(str(songPosIndex) + ": " + str(songPos) + ", So difference in accuracy is " + str((songPos - songPositions[songPosIndex])))
		songPosIndex += 1

#    public override void _Process(float delta)
#    {
#        songPos = GetPlaybackPosition() + AudioServer.GetTimeSinceLastMix();
#        songPos -= AudioServer.GetOutputLatency();
#        songPos *= 1000;
#        songPos = (int) songPos;
#        if (Playing && songPos >= songPositions[songPosIndex])
#        {
#            GD.Print(songPosIndex + ": " + songPos + ", So difference in accuracy is " + (songPos - songPositions[songPosIndex]));
#            songPosIndex += 1;
#        }
#    }
#
#    public void ReportBeat()
#    {
#        // if (songPos % 100 == 0 && songPos != 0)
#        // {
#        //     GD.Print(songPos);
#        // }
#    }
