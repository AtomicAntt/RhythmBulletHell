using Godot;
using System;

public class Player : KinematicBody2D
{
    public enum States {NORMAL, DASH, HURT, DEAD};

    public States state = States.NORMAL;

    [Export]
    public int speed = 300;
    public Vector2 velocity = Vector2.Zero;

    // CHILD VARIABLES

    private AnimatedSprite _animatedSprite;

    public override void _Ready()
    {
        _animatedSprite = GetNode<AnimatedSprite>("AnimatedSprite");
    }

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

    public override void _PhysicsProcess(float delta)
    {
        // if (state != States.DEAD)
        // {
        //     GetInput();
        // }

        switch (state)
        {
            case States.NORMAL:
                // Looks like a lot but its just getting the direction string from the inputs and then playing the correct direction according to the input.
                _animatedSprite.Play(ReturnDirectionString(GetInput()));
                break;
            case States.DASH:
                break;
            case States.HURT:
                break;
            case States.DEAD:
                break;
        }

        velocity = MoveAndSlide(velocity);
    }

}
