class Singleton {
    private static Singleton instance;

    private Singleton() 
    {
        System.out.println("Instance created!");
    }

    public static synchronized Singleton getInstance() 
    {
        if (instance == null)
            instance = new Singleton();
        return instance;
    }
}

public class Singleton2
{
    public static void main(String[] args) 
    {
        Runnable task = () -> {
            Singleton s = Singleton.getInstance();
            System.out.println(s);
        };

        new Thread(task).start();
        new Thread(task).start();
        new Thread(task).start();
    }
}
