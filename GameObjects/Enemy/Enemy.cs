using Godot;
using System;

public class Enemy : Node2D
{
    public enum States {MIRROR, IDLE}

    [Export]
    public bool spiraling = false;

    [Export]
    public int radius = 90;
    [Export]
    public int rotationSpeed = 100;
    [Export]
    public int spawnPointCount = 8;

    [Export]
    public States state = States.IDLE;

    private Player player;

    public Vector2 forwardDirection;

    private Node2D _rotater;


    public void PlaceSpiralPositions(int numPositions)
    {
        float step = 2*Mathf.Pi/numPositions;

        for (int i = 0; i < numPositions; i++)
        {
            Node2D spawnPoint = new Node2D();
            Vector2 posPoint = new Vector2(radius, 0).Rotated(step*i);
            spawnPoint.Position = posPoint;
            spawnPoint.Rotation = posPoint.Angle();
            _rotater.AddChild(spawnPoint);
        }
    }

    public override void _Ready()
    {
        player = GetTree().GetNodesInGroup("Player")[0] as Player;

        _rotater = GetNode<Node2D>("Rotater");

        PlaceSpiralPositions(spawnPointCount);

        forwardDirection = new Vector2(1, 0).Rotated(Rotation);
    }

    public override void _PhysicsProcess(float delta)
    {
        if (spiraling)
        {
            float newRotation = _rotater.RotationDegrees + (rotationSpeed*delta);
            _rotater.RotationDegrees = newRotation % 360;
        }

        switch (state)
        {
            case States.MIRROR:
                if (IsInstanceValid(player))
                {
                    GlobalPosition = new Vector2(player.GlobalPosition.x, GlobalPosition.y);
                }
                break;
            case States.IDLE:
                break;
        }
    }

    // Set/stopped by the composer.cs
    public void SetIdle()
    {
        state = States.IDLE;
    }

    public void SetMirror()
    {
        state = States.MIRROR;
    }

    public void SetSpiraling()
    {
        spiraling = true;
    }

    public void StopSpiraling()
    {
        spiraling = false;
    }
    // ----------

    // Call these from composer.cs
    public void Shoot()
    {
        PackedScene scene = GD.Load<PackedScene>("res://GameObjects/Enemy/Projectile.tscn");
        Projectile projectile = scene.Instance<Projectile>();
        // projectile.direction = forwardDirection;
        projectile.GlobalPosition = GlobalPosition;
        projectile.Rotation = GlobalRotation;
        GetParent().AddChild(projectile);
    }

    public void ShootShotgun()
    {
        float[] angles = {-45, -22.5f, 0, 22.5f, 45};

        foreach(float angle in angles)
        {
            float radians = Mathf.Deg2Rad(angle);
            PackedScene scene = GD.Load<PackedScene>("res://GameObjects/Enemy/Projectile.tscn");
            Projectile projectile = scene.Instance<Projectile>();
            // projectile.direction = forwardDirection.Rotated(radians);
            projectile.Rotation = forwardDirection.Rotated(radians).Angle();
            projectile.GlobalPosition = GlobalPosition;
            GetParent().AddChild(projectile);
        }
    }

    public void ShootStack()
    {
        if (IsInstanceValid(player))
        {
                LookAt(player.GlobalPosition);
        }
        for (int i = 0; i < 3; i++)
        {
            PackedScene scene = GD.Load<PackedScene>("res://GameObjects/Enemy/Projectile.tscn");
            Projectile projectile = scene.Instance<Projectile>();

            projectile.GlobalPosition = GlobalPosition;
            projectile.Rotation = GlobalRotation;
            projectile.maxSpeed = projectile.maxSpeed - (i*60);
            GetParent().AddChild(projectile);
        }
            RotationDegrees = 0;
    }

    public void ShootSpiral()
    {
        foreach (Node2D node in _rotater.GetChildren())
        {
            PackedScene scene = GD.Load<PackedScene>("res://GameObjects/Enemy/Projectile.tscn");
            Projectile projectile = scene.Instance<Projectile>();
            projectile.Position = node.GlobalPosition;
            projectile.Rotation = node.GlobalRotation;
            GetParent().AddChild(projectile);
        }
    }

    public void ShootCircle()
    {
        if (IsInstanceValid(player))
        {
                LookAt(player.GlobalPosition);
        }

        foreach(Node2D node in _rotater.GetChildren())
        {
            PackedScene scene = GD.Load<PackedScene>("res://GameObjects/Enemy/Projectile.tscn");
            Projectile projectile = scene.Instance<Projectile>();
            
            projectile.Position = node.GlobalPosition;
            projectile.Rotation = GlobalRotation;
            GetParent().AddChild(projectile);
        }
    }

    // same as shootcircle but it homes
    public void ShootHomingCircle()
    {
        if (IsInstanceValid(player))
        {
                LookAt(player.GlobalPosition);
        }

        foreach(Node2D node in _rotater.GetChildren())
        {
            PackedScene scene = GD.Load<PackedScene>("res://GameObjects/Enemy/Projectile.tscn");
            Projectile projectile = scene.Instance<Projectile>();
            
            projectile.Position = node.GlobalPosition;
            projectile.Rotation = GlobalRotation;
            projectile.homing = true;
            GetParent().AddChild(projectile);
        }
    }


}
