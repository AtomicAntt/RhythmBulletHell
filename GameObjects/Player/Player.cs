using Godot;
using System;

public class Player : KinematicBody2D
{
    public enum States {NORMAL, DASH, IMMUNE, HURT, DEAD};

    public States state = States.NORMAL;

    [Export]
    public int speed = 300;

    [Export]
    public int dashSpeedMultiplier = 3;

    [Export]
    public int maxHealth = 100;
    [Export]
    public int health = 100;

    public Vector2 velocity = Vector2.Zero;

    // CHILD VARIABLES

    private AnimatedSprite _animatedSprite;

    public override void _Ready()
    {
        // Initialize all child variables
        _animatedSprite = GetNode<AnimatedSprite>("AnimatedSprite");
    }

    // HEALTH RELATED METHODS

    public void Hurt(int damageTaken)
    {
        if (state == States.NORMAL) // Other states like dash and hurt are immunity states
        {
            state = States.HURT;
            health -= damageTaken;

            if (health <= 0)
            {
                state = States.DEAD;
                _animatedSprite.Play("Destroyed");
            }

            GD.Print("I got " + health + " left!");
        }
    }

    // MOVEMENT RELATED METHODS

    public Vector2 GetInput()
    {
        velocity = Vector2.Zero;

        if (Input.IsActionPressed("right"))
        {
            velocity.x += 1;
        }
        if (Input.IsActionPressed("left"))
        {
            velocity.x -= 1;
        }
        if (Input.IsActionPressed("down"))
        {
            velocity.y += 1;
        }
        if (Input.IsActionPressed("up"))
        {
            velocity.y -= 1;
        }

        Vector2 velocityVector = velocity;

        velocity = velocity.Normalized() * speed;

        return velocityVector;
    }

    // Purpose of method: AnimatedSprite animations are called with string, and directions are animated
    public String ReturnDirectionString(Vector2 direction)
    {
        if (direction.x == 1 && direction.y == 0)
        {
            return "Right";
        }
        else if (direction.x == -1 && direction.y == 0)
        {
            return "Left";
        }
        else if (direction.x == 0 && direction.y == -1)
        {
            return "Up";
        }
        else if (direction.x == 0 && direction.y == 1)
        {
            return "Down";
        }
        else if (direction.x == 1 && direction.y == -1)
        {
            return "TopRight";
        }
        else if (direction.x == 1 && direction.y == 1)
        {
            return "BottomRight";
        }
        else if (direction.x == -1 && direction.y == -1)
        {
            return "TopLeft";
        }
        else if (direction.x == -1 && direction.y == 1)
        {
            return "BottomLeft";
        }

        return "Idle";
    }

    // Some variables PhysicsProcess will use
    private float _hurtTime = 0.0f; // tracker
    private const float _hurtDuration = 0.75f; // ((6 frames / 16) * 2 FPS = 0.75)

    private float _dashTime = 0.0f; // tracker
    private const float _dashDuration = 0.25f; // (3 frames / 12 FPS = 0.25)

    // These guys are after dash, to be a little bit more lenient on allowing player to escape damage and secondly serve as a no dashing period (which will exist in addition)
    private float _immunityTime = 0.0f;
    private const float _immunityDuration = 0.25f;

    // useful method for resetting times so it can be used again later

    public void ResetTimes()
    {
        _hurtTime = 0.0f;
        _dashTime = 0.0f;
        _immunityTime = 0.0f;
    }

    public override void _PhysicsProcess(float delta)
    {
        switch (state)
        {
            case States.NORMAL:
                // Looks like a lot but its just getting the direction string from the inputs and then playing the correct direction according to the input.
                // Remember, the GetInput() in this nested method is the reason why velocity changes when you press inputs.
                // _animatedSprite.Play(ReturnDirectionString(GetInput()));

                if (Math.Abs(GetInput().Length()) >= 1)
                {
                    _animatedSprite.Play("Flight");
                }
                else
                {
                    _animatedSprite.Play("Idle");
                }

                if (Input.IsActionJustPressed("dash") && Math.Abs(GetInput().Length()) >= 1) // Player presses dash button & moving
                {
                    state = States.DASH;
                }
                break;
            case States.DASH:
                if (_dashTime >= _dashDuration)
                {
                    state = States.IMMUNE;
                    ResetTimes();
                    break;
                }

                _dashTime += delta;

                if (Math.Abs(GetInput().Length()) >= 1) // This is to avoid error saying they cant play "DashIdle"
                {
                    _animatedSprite.Play("Dash"+ReturnDirectionString(GetInput()));
                }

                velocity *= dashSpeedMultiplier;
                break;
            case States.IMMUNE:
                if (_immunityTime >= _immunityDuration)
                {
                    state = States.NORMAL;
                    ResetTimes();
                }
                _immunityTime += delta;

                _animatedSprite.Play(ReturnDirectionString(GetInput()));
                break;
            case States.HURT:
                if (_hurtTime >= _hurtDuration)
                {
                    state = States.NORMAL;
                    ResetTimes();
                    break;
                }
                _hurtTime += delta;

                // _animatedSprite.Play("Hurt"+ReturnDirectionString(GetInput()));

                GetInput();
                _animatedSprite.Play("Hurt");
                break;
            case States.DEAD:
                break;
        }

        velocity = MoveAndSlide(velocity);
    }

}
