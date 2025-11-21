class Volt
{
    int v;

    Volt(int v)
    {
        this.v = v;
    }

    int get()
    {
        return v;
    }
}

class Socket
{
    Volt getVolt()
    {
        return new Volt(120);
    }
}

class Adapter extends Socket
{
    Volt get3()
    {
        return new Volt(getVolt().get() / 40);
    }

    Volt get12()
    {
        return new Volt(getVolt().get() / 10);
    }

    Volt get120()
    {
        return getVolt();
    }
}

public class Volt1
{
    public static void main(String[] args)
    {
        Adapter a = new Adapter();

        System.out.println(a.get3().get());
        System.out.println(a.get12().get());
        System.out.println(a.get120().get());
    }
}
