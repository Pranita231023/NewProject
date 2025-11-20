interface Shape
{
    void draw();
}

class Circle implements Shape
{
    public void draw()
    {
        System.out.println("Circle");
    }
}

class Square implements Shape
{
    public void draw()
    {
        System.out.println("Square");
    }
}

interface Factory
{
    Shape make(String s);
}

class ShapeFactory implements Factory
{
    public Shape make(String s)
    {
        if(s.equals("C")) return new Circle();
        return new Square();
    }
}

public class AbstractFactoryShape
{
    public static void main(String[] a)
    {
        Factory f = new ShapeFactory();
        f.make("C").draw();
        f.make("S").draw();
    }
}
