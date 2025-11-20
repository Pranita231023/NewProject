import java.util.*;

interface Observer 
{
    void update(int n);
}

class Subject 
{
    List<Observer> list = new ArrayList<>();

    void add(Observer o) 
    {
        list.add(o);
    }

    void setNumber(int n) 
    {
        for (Observer ob : list)
        {
            ob.update(n);
        }
    }
}

class HexObserver implements Observer 
{
    public void update(int n) 
    {
        System.out.println("Hex: " + Integer.toHexString(n));
    }
}

class OctObserver implements Observer 
{
    public void update(int n) 
    {
        System.out.println("Oct: " + Integer.toOctalString(n));
    }
}

class BinObserver implements Observer 
{
    public void update(int n) 
    {
        System.out.println("Bin: " + Integer.toBinaryString(n));
    }
}

public class ObserverDesignDemo

{
    public static void main(String[] a) 
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number: ");
        int n = sc.nextInt();

        Subject s = new Subject();
        s.add(new HexObserver());
        s.add(new OctObserver());
        s.add(new BinObserver());

        s.setNumber(n);
    }
}
