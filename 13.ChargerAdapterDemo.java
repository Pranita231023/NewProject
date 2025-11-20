// Volt class
class Volt 
{
    private int volts;

    Volt(int v) 
    {
        volts = v;
    }

    int getVolts() 
    {
        return volts;
    }
}

// Socket (Adaptee)
class Socket 
{
    Volt getVolt() 
    {
        return new Volt(120); // default household voltage
    }
}

// Adapter Interface
interface ChargerAdapter 
{
    Volt get3Volt();
    Volt get12Volt();
    Volt get120Volt();
}

// Class Adapter (using inheritance)
class AdapterClass extends Socket implements ChargerAdapter 
{

    // simple converter method
    private Volt convert(Volt v, int div) 
    {
        return new Volt(v.getVolts() / div);
    }

    public Volt get3Volt() 
    {
        return convert(getVolt(), 40); // 120V → 3V
    }

    public Volt get12Volt() 
    {
        return convert(getVolt(), 10); // 120V → 12V
    }

    public Volt get120Volt() 
    {
        return getVolt(); // direct 120V from socket
    }
}

// Test
public class ChargerAdapterDemo
{
    public static void main(String[] args) 
    {

        ChargerAdapter adapter = new AdapterClass();

        System.out.println("3V   : " + adapter.get3Volt().getVolts());
        System.out.println("12V  : " + adapter.get12Volt().getVolts());
        System.out.println("120V : " + adapter.get120Volt().getVolts());
    }
}
