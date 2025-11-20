import java.util.*;
class EnumIterAdp implements Iterator<Object> 
{
    private Enumeration<?> en;

    public EnumIterAdp(Enumeration<?> en) 
    {
        this.en = en;
    }
    
    public boolean hasNext() 
    {
        return en.hasMoreElements();
    }
    
    public Object next() 
    {
        return en.nextElement();
    }
    
    public void remove() 
    {
        throw new UnsupportedOperationException();
    }
}

public class Enumeration5
{
    public static void main(String[] args) 
    {
        Vector<String> v = new Vector<>();
        v.add("Java");
        v.add("Python");
        v.add("C++");

        Enumeration<String> e = v.elements();

        Iterator<Object> it = new EnumIterAdp(e);

        System.out.println("Using Adapter:");
        while (it.hasNext()) 
        {
            System.out.println(it.next());
        }
    }
}

