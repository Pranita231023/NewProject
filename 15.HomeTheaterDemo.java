// Subsystem 1
class TV {
    void on() 
    { 
        System.out.println("TV ON"); 
    }
    void off() 
    { 
        System.out.println("TV OFF"); 
    }
}

// Subsystem 2
class DVDPlayer
 {
    void on() 
    { 
        System.out.println("DVD Player ON"); 
    }
    void play() 
    { 
        System.out.println("Playing Movie"); 
    }
    void off() 
    { 
        System.out.println("DVD Player OFF"); 
    }
}

// Facade
class HomeTheaterFacade {
    TV tv;
    DVDPlayer dvd;

    HomeTheaterFacade(TV tv, DVDPlayer dvd) {
        this.tv = tv;
        this.dvd = dvd;
    }

    void watchMovie() {
        System.out.println("\nStart Movie");
        tv.on();
        dvd.on();
        dvd.play();
    }

    void stopMovie() {
        System.out.println("\nStop Movie");
        tv.off();
        dvd.off();
    }
}

// Client
public class HomeTheaterDemo{
    public static void main(String[] args) {

        HomeTheaterFacade home = new HomeTheaterFacade(
            new TV(), new DVDPlayer()
        );

        home.watchMovie();
        home.stopMovie();
    }
}
