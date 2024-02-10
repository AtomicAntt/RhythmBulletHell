using Godot;
using System;
using System.Linq;

public class Composer : AudioStreamPlayer
{
    [Export]
    public double bpm = 175;
    public double songPos = 0.0;

    private double secPerBeat; // 60.0 / bpm

    // private int previousSongPos = 0;

    public int[] songPositions = {18, 360, 703, 1046, 1389, 1732, 2075, 2418, 2760, 3103, 3446, 3789, 4132, 4475, 4818, 4989, 5160, 5503, 5846, 6189, 6532, 6875, 7218, 7560, 7903, 8246, 8589, 8932, 9275, 9618, 9960, 10303, 10475, 10646, 11332, 12018, 
    12703, 13389, 14075, 14760, 15446, 16132};

    public int totalAccuracy = 0;

    public int songPosIndex = 0;

    public override void _Ready()
    {
        secPerBeat = 60.0 / bpm;
    }

    public override void _Process(float delta)
    {
        songPos = GetPlaybackPosition() + AudioServer.GetTimeSinceLastMix();
        songPos -= AudioServer.GetOutputLatency();
        songPos *= 1000;
        songPos = (int) songPos;
        if (Playing && songPos >= songPositions[songPosIndex])
        {
            GD.Print(songPosIndex + ": " + songPos + ", So difference in accuracy is " + (songPos - songPositions[songPosIndex]));
            GD.Print("so mean accuracy is " + (totalAccuracy / (songPosIndex+1)));
            songPosIndex += 1;
            totalAccuracy += totalAccuracy / (songPosIndex+1);
        }
    }

    public void _on_Timer_timeout()
    {
        Play();
    }

    public void ReportBeat()
    {
        // if (songPos % 100 == 0 && songPos != 0)
        // {
        //     GD.Print(songPos);
        // }
    }
}
