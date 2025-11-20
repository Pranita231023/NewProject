// Existing HeartModel
class HeartModel 
{
    void pump() 
    {
        System.out.println("Heart is pumping");
    }
}

// Target interface
interface BeatModel 
{
    void start();
    void stop();
}

// Adapter
class HeartAdapter implements BeatModel 
{
    HeartModel heart;

    HeartAdapter(HeartModel h) 
    {
        heart = h;
    }

    public void start() 
    {
        System.out.println("Starting beat");
        heart.pump();
    }

    public void stop() 
    {
        System.out.println("Stopping beat");
    }
}

// Test
public class HeartAdapterTest
{
    public static void main(String[] args) 
    {
        BeatModel beat = new HeartAdapter(new HeartModel());
        beat.start();
        beat.stop();
    }
}
