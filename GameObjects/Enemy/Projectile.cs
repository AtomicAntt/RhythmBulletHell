using Godot;
using System;

public class Projectile : Area2D
{
    [Export]
    public int damage = 20;

    public float speed = 300;

    private Vector2 forwardVector;

    public override void _Ready()
    {
        forwardVector = new Vector2(0, 1).Rotated(Rotation);
    }

    public override void _PhysicsProcess(float delta)
    {
        Position += forwardVector * speed * delta;
    }

    public void _on_Projectile_area_entered(Area2D area)
    {
        if (area.IsInGroup("PlayerHitbox"))
        {
            Player player = GetTree().GetNodesInGroup("Player")[0] as Player;
            player.Hurt(damage);
            QueueFree();
        }
    }
}
