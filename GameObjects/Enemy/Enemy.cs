using Godot;
using System;
using System.Linq;

public class Enemy : Node2D
{
    public enum States {MIRROR, IDLE}

    public enum ShootingSelection {NORMAL, SHOTGUN, STACK, SPIRAL, CIRCLE, HOMINGCIRCLE}

    [Export]
    public int[] songPositions; // This is every time the enemy fires
    public int songPosIndex = 0; // This is the index position that the composer.cs looks for

    [Export]
    public int[] songPositions1;
    [Export]
    public int[] songPositions2;
    [Export]
    public int[] songPositions3;
    [Export]
    public int[] songPositions4;
    [Export]
    public int[] songPositions5;
    [Export]
    public int[] songPositions6;

    public SongPosition indexSongPos1 = new SongPosition(), indexSongPos2 = new SongPosition(), indexSongPos3 = new SongPosition(), indexSongPos4 = new SongPosition(), indexSongPos5 = new SongPosition(), indexSongPos6 = new SongPosition();

    [Export]
    public int[] switchToSpiralIndex = {-1};

    public void CheckSwitchToSpiralIndex(int posIndex)
    {
        if (switchToSpiralIndex.Length <= 0)
        {
            return;
        }

        if (switchToSpiralIndex.Contains(posIndex))
        {
            spiraling = true;
            shootingSelection = ShootingSelection.SPIRAL;
        }
    }

    public class SongPosition
    {
        public int Index = 0;
    }

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

    [Export]
    public ShootingSelection shootingSelection = ShootingSelection.NORMAL;

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
    public void ShootAssigned()
    {
        switch (shootingSelection)
        {
            case ShootingSelection.NORMAL:
                Shoot();
                break;
            case ShootingSelection.SHOTGUN:
                ShootShotgun();
                break;
            case ShootingSelection.STACK:
                ShootStack();
                break;
            case ShootingSelection.SPIRAL:
                ShootSpiral();
                break;
            case ShootingSelection.CIRCLE:
                ShootCircle();
                break;
            case ShootingSelection.HOMINGCIRCLE:
                ShootHomingCircle();
                break;
        }
    }

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

            projectile.SetNonDirectional();

            
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

            projectile.SetDirectional();
            
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

    // Even song positions move to odd song positions, so index 0 goes to index 1, index 2 goes to index 3
    public void CheckAndMovePositions(int songPosition)
    {
        // First, lets see if this song position is in any of the arrays...
        int positionAt = -1;
        int[][] allPositionsArrays = { songPositions1, songPositions2, songPositions3, songPositions4, songPositions5, songPositions6 };
        SongPosition[] allIndexArrays = {indexSongPos1, indexSongPos2, indexSongPos3, indexSongPos4, indexSongPos5, indexSongPos6};
        int[] positionsArray = allPositionsArrays[0];// initialize just to avoid error
        int positionNumber = -1; // The position2d node's group

        for (int i = 0; i < allPositionsArrays.Length; i++)
        {
            // complex but for each array, look at their corresponding index and that value is the target position we want to hit
            int targetSongPosition = -1; 
            // VALID INDEX? also, this is some code that is getting somewhere lol
            // Only explanation is that we see if the length of the positions array we looking at right now is not as big as the corresponding index, has to be less or it goes too far
            if (allIndexArrays[i].Index < allPositionsArrays[i].Length)
            {
                targetSongPosition = allPositionsArrays[i][allIndexArrays[i].Index];
            }
            // GD.Print(targetSongPosition);
            if (songPosition >= targetSongPosition && targetSongPosition != -1) // Song position in any of the array and even?
            {
                    // GD.Print(targetSongPosition);
                    positionAt = allIndexArrays[i].Index + 1; // Index at the same array that the next song position is located
                    positionNumber = i+1;
                    allIndexArrays[i].Index = allIndexArrays[i].Index + 2; // So next time, the next note is a starting position
                    GD.Print(allIndexArrays[i].Index);
                    positionsArray = allPositionsArrays[i]; // And we also need this information to know the final destination, which is the next value (assume there will always be)
                    break;
            }
        }

        if (positionAt != -1)
        {
            GD.Print("Attempting to tween: " + songPosition);
            GD.Print("Attempting to tween for this seconds: " + (float) (positionsArray[positionAt] - positionsArray[positionAt-1])/1000);

            SceneTreeTween tween = GetTree().CreateTween();
            EnemyPosition enemyPosition = GetTree().GetNodesInGroup(positionNumber.ToString())[0] as EnemyPosition;

            GD.Print("TO THIS POSITION: " + enemyPosition.GlobalPosition);

            tween.TweenProperty(this, "position", enemyPosition.GlobalPosition, (float) (positionsArray[positionAt] - positionsArray[positionAt-1])/1000);
        }
        

        




        // if (songPositions1.Contains(songPosition))
        // {
        //     if (Array.IndexOf(songPositions1, songPosition) % 2 == 0) // check if even
        //     {
        //         positionAt = 1;
        //         positionsArray = songPositions1;
        //     }
        // }
        // else if (songPositions2.Contains(songPosition))
        // {
        //     if (Array.IndexOf(songPositions2, songPosition) % 2 == 0) // check if even
        //     {
        //         positionAt = 2;
        //         positionsArray = songPositions2;
        //     }
        // }
        // else if (songPositions3.Contains(songPosition))
        // {
        //     if (Array.IndexOf(songPositions3, songPosition) % 2 == 0) // check if even
        //     {
        //         positionAt = 3;
        //         positionsArray = songPositions3;
        //     }
        // }
        // else if (songPositions4.Contains(songPosition))
        // {
        //     if (Array.IndexOf(songPositions4, songPosition) % 2 == 0) // check if even
        //     {
        //         positionAt = 4;
        //         positionsArray = songPositions4;
        //     }
        // }
        // else if (songPositions5.Contains(songPosition))
        // {
        //     if (Array.IndexOf(songPositions5, songPosition) % 2 == 0) // check if even
        //     {
        //         positionAt = 5;
        //         positionsArray = songPositions5;
        //     }
        // }
        // else if (songPositions6.Contains(songPosition))
        // {
        //     if (Array.IndexOf(songPositions6, songPosition) % 2 == 0) // check if even
        //     {
        //         positionAt = 6;
        //         positionsArray = songPositions6;
        //     }
        // }
    }


}
