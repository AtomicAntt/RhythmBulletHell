using Godot;
using System;

public class Projectile : Area2D
{
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
}
