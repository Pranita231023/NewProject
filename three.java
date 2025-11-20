import java.util.*;

class WeatherStation extends Observable 
{
    float temp, humidity, pressure;

    void setMeasurements(float t, float h, float p) 
    {
        temp = t; humidity = h; pressure = p;
        setChanged();
        notifyObservers();
    }

    float getTemperature() { return temp; }
    float getHumidity() { return humidity; }
    float getPressure() { return pressure; }
}

class Display implements Observer {
    public void update(Observable o, Object arg) {
        WeatherStation w = (WeatherStation) o;
        System.out.println("Temp: " + w.getTemperature() +
            " Humidity: " + w.getHumidity() +
            " Pressure: " + w.getPressure());
    }
}

public class three {
    public static void main(String[] args) {
        WeatherStation ws = new WeatherStation();
        ws.addObserver(new Display());
        ws.setMeasurements(30.5f, 65.2f, 1013f);
        ws.setMeasurements(28.4f, 70.1f, 1010f);
    }
}
