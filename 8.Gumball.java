public class Gumball {
    static class GumballMachine 
    {
        String state = "NoCoin";

        void insertCoin() 
        {
            if (state.equals("NoCoin")) 
                {
                System.out.println("Coin inserted");
                state = "HasCoin";
            } else {
                System.out.println("Coin already inserted");
            }
        }

        void turnCrank() 
        {
            if (state.equals("HasCoin")) 
                {
                System.out.println("Gumball released!");
                state = "NoCoin";
            } else {
                System.out.println("Insert coin first");
            }
        }
    }

    public static void main(String[] args) 
    {
        GumballMachine g = new GumballMachine();
        g.turnCrank();   // No coin
        g.insertCoin();  // Insert coin
        g.turnCrank();   // Gumball out
        g.turnCrank();   // Try again without coin
    }
}
