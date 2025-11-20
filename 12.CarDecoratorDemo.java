interface Car 
{
    void assemble();
}

public class CarDecoratorDemo 
{
    public static void main(String[] args) 
    {
        Car basic = new Car() 
        {
            public void assemble() 
            {
                System.out.println("Basic Car");
            }
        };

        Car sports = new Car() 
        {
            public void assemble() 
            {
                basic.assemble();
                System.out.println("Adding Sports Car features");
            }
        };

        Car luxury = new Car() 
        {
            public void assemble() 
            {
                basic.assemble();
                System.out.println("Adding Luxury Car features");
            }
        };

        Car sportsLuxury = new Car() 
        {
            public void assemble() 
            {
                luxury.assemble();
                System.out.println("Adding Sports Car features");
            }
        };

        System.out.println("Sports Car:");
        sports.assemble();

        System.out.println("\nLuxury Car:");
        luxury.assemble();

        System.out.println("\nSports Luxury Car:");
        sportsLuxury.assemble();
    }
}
