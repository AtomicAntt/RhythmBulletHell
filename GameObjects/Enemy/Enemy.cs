using Godot;
using System;

public class Enemy : Node2D
{
    private Player player;

    public override void _Ready()
    {
        player = GetTree().GetNodesInGroup("Player")[0] as Player;
    }

    public override void _PhysicsProcess(float delta)
    {
        if (IsInstanceValid(player))
        {
            GlobalPosition = new Vector2(player.GlobalPosition.x, GlobalPosition.y);
        }
    }


}
