interface Command 
{
    void execute();
}

class Light 
{
    void on() 
    {
        System.out.println("Light ON");
    }

    void off() 
    {
        System.out.println("Light OFF");
    }
}

class LightOn implements Command
{
    Light l;

    LightOn(Light l) 
    {
        this.l = l;
    }

    public void execute() 
    {
        l.on();
    }
}

class LightOff implements Command
{
    Light l;

    LightOff(Light l) 
    {
        this.l = l;
    }

    public void execute() 
    {
        l.off();
    }
}

class Remote
{
    Command c;

    void set(Command c) 
    {
        this.c = c;
    }

    void press() 
    {
        c.execute();
    }
}

public class RemoteTest1
{
    public static void main(String[] args)
    {
        Light light = new Light();
        Remote remote = new Remote();

        remote.set(new LightOn(light));
        remote.press();

        remote.set(new LightOff(light));
        remote.press();
    }
}
