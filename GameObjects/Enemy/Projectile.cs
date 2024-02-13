using Godot;
using System;

public class Projectile : Area2D
{
    [Export]
    public int damage = 20;

    public float maxSpeed = 230;
    public float speed;

    // Homing use only variables
    [Export]
    public bool homing = false;
    Vector2 acceleration = Vector2.Zero;
    Vector2 velocity = Vector2.Zero;
    public int steerForce = 2;
    private Player player;

    // ---------

    



    

    // private Vector2 forwardVector;

    public override void _Ready()
    {
        speed = maxSpeed;

        player = GetTree().GetNodesInGroup("Player")[0] as Player;

        if (homing)
        {
            velocity = GlobalPosition.DirectionTo(player.GlobalPosition) * speed;
        }
    }
    

    // Homing

    public Vector2 Seek()
    {
        Vector2 steer = Vector2.Zero;
        if (IsInstanceValid(player))
        {
            Vector2 desired = (player.GlobalPosition - GlobalPosition).Normalized() * speed;
            steer = (desired-velocity).Normalized() * steerForce;
        }
        return steer;
    }

    // If homing, use these variables to track time
    private float _homingTime = 0.0f;
    private float _homingDuration = 1.0f;

    public override void _PhysicsProcess(float delta)
    {
        if (_homingTime < _homingDuration)
        {
            _homingTime += delta;
        }

        // After homing duration passes, you can move normally again
        if (!homing || _homingTime >= _homingDuration)
        {
            Position += Transform.x * speed * delta;
        }
        else
        {
            acceleration += Seek();
            velocity += acceleration * delta;
            velocity = velocity.LimitLength(speed);
            Rotation = velocity.Angle();
            Position += velocity * delta;
        }
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
