interface Command 
{
    void execute();
}

class Light 
{
    void on() 
    { 
    System.out.println("Light is ON"); 
    }
}

class LightOnCommand implements Command 
{
    Light light;
    LightOnCommand(Light light) 
    { 
        this.light = light; 
    }

    public void execute() 
    {
        light.on();
    }
}

class RemoteControl
{
    Command command;

    void setCommand(Command command) 
    {
        this.command = command;
    }

    void pressButton() 
    {
        command.execute();
    }
}

public class SimpleCommandDemo 
{
    public static void main(String[] args) 
    {

        Light light = new Light();
        Command lightOn = new LightOnCommand(light);

        RemoteControl remote = new RemoteControl();
        remote.setCommand(lightOn);
        remote.pressButton();
    }
}
