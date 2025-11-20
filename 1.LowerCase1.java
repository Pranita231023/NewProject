import java.io.*;

class LowerCaseInputStream extends FilterInputStream 
{
    LowerCaseInputStream(InputStream in) { super(in); }
    public int read() throws IOException 
    {
        int c = super.read();
        return (c == -1) ? -1 : Character.toLowerCase(c);
    }
}

public class LowerCase1{
    public static void main(String[] args) throws Exception 
    {
        System.out.print("Enter text: ");
        InputStream in = new LowerCaseInputStream(System.in);
        int ch;
        while ((ch = in.read()) != -1)
            System.out.print((char) ch);
    }
}
