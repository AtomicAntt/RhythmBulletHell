using Godot;
using System;

public class Signals : Node
{
    [Signal]
    public delegate void UpdateHealth(int health);
}