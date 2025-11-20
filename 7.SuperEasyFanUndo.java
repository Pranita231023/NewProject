import java.util.*;

public class SuperEasyFanUndo 
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);

        boolean fanOn = false;   // fan state
        String last = "";        // last action

        while (true) 
        {
            System.out.println("\n1. ON  2. OFF  3. UNDO  4. EXIT");
            System.out.print("Enter choice: ");
            int c = sc.nextInt();

            if (c == 1) 
            {
                System.out.println("Fan ON");
                fanOn = true;
                last = "ON";
            }
            else if (c == 2) 
            {
                System.out.println("Fan OFF");
                fanOn = false;
                last = "OFF";
            }
            else if (c == 3) 
            {
                if (last.equals("")) 
                {
                    System.out.println("Nothing to undo");
                } 
                else if (last.equals("ON")) 
                {
                    System.out.println("Undo: Turn Fan OFF");
                    fanOn = false;
                    last = "";
                } 
                else if (last.equals("OFF")) 
                {
                    System.out.println("Undo: Turn Fan ON");
                    fanOn = true;
                    last = "";
                }
            }
            else if (c == 4) 
            {
                System.out.println("Exit...");
                break;
            }
            else 
            {
                System.out.println("Invalid choice!");
            }
        }

        sc.close();
    }
}
