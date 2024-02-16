using Godot;
using System;
using System.Data;

public class Main : Control
{
    // ---------- Game states to track the player is currently playing the game ----------

    public enum GameStates {ACTIVE, INACTIVE, PAUSED};

    public GameStates gameState = GameStates.INACTIVE;

    // ---------- Initialized audio node variables ----------

    // SFX
    public AudioStreamPlayer mouseHoverSound;
    public AudioStreamPlayer clickPlaySound;
    public AudioStreamPlayer quitSound;
    public AudioStreamPlayer clickSettingsSound;

    // Music
    public AudioStreamPlayer mainMenuMusic;
    public AudioStreamPlayer inGameMusic;

    // ---------- Variables for loading/unloading the game levels ----------

    private Node2D _levels; // Initialized child node

    private Node2D _levelInstance; // Current Node2D scene that will be under _levels

    // ----------- Initialized menu references that may need to be shown or hidden ----------

    private Control _mainMenu;
    private Control _settings;

    private Panel _settingsPanel;
    private ColorRect _settingsBackground;

    // ---------- Initialized Game UI references ----------

    public Control gameUI;
    public Control pauseUI;
    public TextureProgress healthBar;
    public TextureProgress damageBar;
    public Label healthLabel;

    // ---------- Initialized Autoloads ----------

    private Saves _saves;
    private Signals _signals;

    // ---------- Methods to call on ready, which also loads saved parts of the game as the game is getting started ----------

    public void InitializeVolume()
    {
        
    }

    // ----------- Initialize all child node references ----------

    public override void _Ready()
    {
        // Initialize all child node references
        mouseHoverSound = GetNode<AudioStreamPlayer>("SFX/MouseHoverSound");
        clickPlaySound = GetNode<AudioStreamPlayer>("SFX/ClickPlaySound");
        quitSound = GetNode<AudioStreamPlayer>("SFX/QuitSound");
        clickSettingsSound = GetNode<AudioStreamPlayer>("SFX/ClickSettingsSound");

        mainMenuMusic = GetNode<AudioStreamPlayer>("Music/MainMenuMusic");
        inGameMusic = GetNode<AudioStreamPlayer>("Music/InGameMusic");

        _levels = GetNode<Node2D>("Levels");

        _mainMenu = GetNode<Control>("MainMenu");
        _settings = GetNode<Control>("Settings");

        _settingsPanel = GetNode<Panel>("Settings/SettingsPanel");
        _settingsBackground = GetNode<ColorRect>("Settings/SettingsBackground");

        gameUI = GetNode<Control>("Levels/CanvasLayer/GameUI");
        pauseUI = GetNode<Control>("Levels/CanvasLayer/PauseUI");
        healthBar = GetNode<TextureProgress>("Levels/CanvasLayer/GameUI/VBoxContainer/HealthBar");
        damageBar = GetNode<TextureProgress>("Levels/CanvasLayer/GameUI/VBoxContainer/HealthBar/DamageBar");
        healthLabel = GetNode<Label>("Levels/CanvasLayer/GameUI/VBoxContainer/HealthLabel");

        // Initialize needed autoloads
        _saves = GetNode<Saves>("/root/Saves");
        _signals = GetNode<Signals>("/root/Signals");

        _signals.Connect("UpdateHealth", this, "SetHealth");

        // Load values like settings that were set.
        _saves.LoadGame();

        // Play music after loading to allow it to play at the volume setting the user saved.
        mainMenuMusic.Play();
    }

    // ---------- GAME UI HANDLING ----------

    public void SetHealth(int value)
    {
        healthBar.Value = value;

        SceneTreeTween tween = GetTree().CreateTween();
        tween.TweenProperty(damageBar, "value", (float)value, 0.5f);

        healthLabel.Text = value + "/100";
    }

    // ---------- Methods to handle loading and unloading levels ----------

    public void UnloadLevel()
    {
        if (IsInstanceValid(_levelInstance))
        {
            _levelInstance.QueueFree();
        }
    }

    public void LoadLevel(String levelName)
    {
        // First, remove menus and any current levels that are running
        UnloadLevel();
        _mainMenu.Visible = false;

        // This assumes that the level scene is in a folder called 'Levels' that is under res://
        String levelPath = "res://Levels/" + levelName + ".tscn";
        PackedScene levelResource = GD.Load<PackedScene>(levelPath);

        if (levelResource != null)
        {
            _levelInstance = levelResource.Instance<Node2D>();
            _levels.AddChild(_levelInstance);
        }
    }

	// ---------- Methods to handle tween animations ----------

    // ---------- BUTTON SIGNAL METHODS ----------

    // Signal used on all menu buttons to indicate that the mouse is hovering over a button by playing a sound.
    public void _on_Button_mouse_entered()
    {
        mouseHoverSound.Play();
    }

    public void _on_StartButton_pressed()
    {
        LoadLevel("Level3");
        gameUI.Visible = true;
        mainMenuMusic.Stop();
        clickPlaySound.Play();
        gameState = GameStates.ACTIVE;
    }

    public void _on_QuitButton_pressed()
    {
        quitSound.Play();

        GetTree().Quit();
    }

    public void _on_SettingsButton_pressed()
    {
        _settings.Visible = true;
        
        clickSettingsSound.Play();
    }

    public void _on_SettingsBackButton_pressed()
    {
        _settings.Visible = false;

        quitSound.Play();
    }

    // ---------- VOLUME SLIDER SIGNAL METHODS ----------

    public void _on_VolumeSlider_value_changed(float value, String audioBusName, String labelName)
    {
        int busIndex = AudioServer.GetBusIndex(audioBusName);
        AudioServer.SetBusVolumeDb(busIndex, GD.Linear2Db(value));

        // So.. the labels will be in a group that is the same name as the audio bus name assigned for the volume slider with label at the end
        // Also, the reason why the HSliders also have group names that are the same as the audio bus name is so the save autoload can figure out where it is.
        foreach (Label label in GetTree().GetNodesInGroup(audioBusName + " Label"))
        {
            label.Text = labelName + ": " + (value * 100) + "%";
        }

        // Save it so next time you open the game you get the same volume
        _saves.SaveGame();
    }

    // ---------- FULLSCREEN BUTTON SIGNAL METHOD ----------

    public void _on_FullscreenButton_toggled(bool buttonPressed)
    {
        OS.WindowFullscreen = buttonPressed;
    }

    // ---------- INPUT SIGNAL METHOD ----------

    // If you click and settings is up, if it was outside of the settings window, it will close it
    public override void _Input(InputEvent @event)
    {
        if (@event is InputEventMouseButton && _settings.Visible)
        {
            Vector2 mousePos = GetGlobalMousePosition();

            Rect2 uiBoundingBox = _settingsPanel.GetRect();

            if (!uiBoundingBox.HasPoint(mousePos))
            {
                _settings.Visible = false;

                quitSound.Play();
            }
        }

        // Lets leave it up to the actual pause menu to deal with it
        // if (@event.IsActionPressed("pause"))
        // {
        //     TogglePause();
        // }
    }

    // ---------- PAUSING/UNPAUSING ----------

    // public void TogglePause()
    // {
    //     if (gameState == GameStates.ACTIVE)
    //     {
    //         pauseUI.Visible = true;
    //         gameState = GameStates.PAUSED;
    //         GetTree().Paused = true;

    //         foreach (Composer composerNode in GetTree().GetNodesInGroup("GameMusic"))
    //         {
    //             composerNode.StreamPaused = true;
    //         }
    //     }
    //     else if (gameState == GameStates.PAUSED)
    //     {
    //         pauseUI.Visible = false;
    //         gameState = GameStates.ACTIVE;
    //         GetTree().Paused = false;

    //         foreach (Composer composerNode in GetTree().GetNodesInGroup("GameMusic"))
    //         {
    //             composerNode.StreamPaused = false;
    //         }
    //     }
    // }
}
