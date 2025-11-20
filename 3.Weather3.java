import java.util.Observer;
import java.util.Observable;

class WeatherStation extends Observable {
    float temp, hum, press;

    void setData(float t, float h, float p) {
        temp = t;
        hum = h;
        press = p;
        setChanged();
        notifyObservers();
    }
}

class Display implements Observer {
    public void update(Observable o, Object arg) {
        WeatherStation w = (WeatherStation) o;
        System.out.println("Temp: " + w.temp +
                           " Humidity: " + w.hum +
                           " Pressure: " + w.press);
    }
}

public class weather {
    public static void main(String[] a) {
        WeatherStation ws = new WeatherStation();
        ws.addObserver(new Display());

        ws.setData(30.5f, 65.2f, 1013f);
        ws.setData(28.4f, 70.1f, 1010f);
    }
}
