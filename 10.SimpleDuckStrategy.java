interface FlyBehavior 
{
    void fly();
}

interface QuackBehavior 
{
    void quack();
}

class CanFly implements FlyBehavior 
{
    public void fly() 
    {
        System.out.println("I can fly high!");
    }
}

class CannotFly implements FlyBehavior 
{
    public void fly() 
    {
        System.out.println("I cannot fly.");
    }
}

class CanQuack implements QuackBehavior
{
    public void quack() 
    {
        System.out.println("Quack Quack!");
    }
}

class CannotQuack implements QuackBehavior 
{
    public void quack() 
    {
        System.out.println("I cannot quack.");
    }
}

class Duck 
{
    FlyBehavior flyBehavior;
    QuackBehavior quackBehavior;

    Duck(FlyBehavior f, QuackBehavior q) 
    {
        flyBehavior = f;
        quackBehavior = q;
    }

    void showBehavior() 
    {
        flyBehavior.fly();
        quackBehavior.quack();
    }
}

// Main class
public class SimpleDuckStrategy 
{
    public static void main(String[] args) 
    {
        System.out.println("Mallard Duck:");
        Duck mallard = new Duck(new CanFly(), new CanQuack());
        mallard.showBehavior();

        System.out.println("\nRubber Duck:");
        Duck rubber = new Duck(new CannotFly(), new CanQuack());
        rubber.showBehavior();

        System.out.println("\nWooden Duck:");
        Duck wooden = new Duck(new CannotFly(), new CannotQuack());
        wooden.showBehavior();
    }
}
