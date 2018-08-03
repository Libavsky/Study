package com.Weather.services;
import net.aksingh.owmjapis.CurrentWeather;
import net.aksingh.owmjapis.OpenWeatherMap;

import java.io.IOException;

/**
 * Created by Bot on 2018-08-02.
 */
public class WeatherApiService {

    private OpenWeatherMap owm = new OpenWeatherMap("a36ef0192d7c9182efc40269d2b45761");


    public CurrentWeather GetCurrentWeather(String cityName, String countryCode) throws IOException {
        return owm.currentWeatherByCityName(cityName,countryCode);
    }

    public String GetCurrentWeatherInNiceFormat(CurrentWeather currentWeather)
    {
        String returnX="";
        if (currentWeather.hasWeatherInstance()) {
            returnX+="In general: "+currentWeather.getWeatherInstance(0).getWeatherName()+"   "+currentWeather.getWeatherInstance(0).getWeatherDescription()+"\n";
        }
        if (currentWeather.hasMainInstance()) {
            if (currentWeather.getMainInstance().hasTemperature()) {
                returnX+=(currentWeather.getMainInstance().getTemperature())+" \u00b0C\n";
            }
            if (currentWeather.getMainInstance().hasPressure()) {
                returnX+=(currentWeather.getMainInstance().getPressure())+" hPa\n";
            }
            if (currentWeather.getMainInstance().hasHumidity()) {
                returnX+=(currentWeather.getMainInstance().getHumidity())+" % Humidity\n";
            }
        }
        if (currentWeather.hasCloudsInstance()) {
            returnX+=(currentWeather.getCloudsInstance().getPercentageOfClouds())+" % Cloudiness\n";
        }
        if(currentWeather.hasWindInstance()){
            if(currentWeather.getWindInstance().hasWindSpeed()){
                returnX+=(currentWeather.getWindInstance().getWindSpeed())+" m/s wind";
            }
            else return returnX;
            if(currentWeather.getWindInstance().hasWindDegree()){
                returnX+=" from Azimuth: "+(currentWeather.getWindInstance().getWindDegree())+"\u00b0";
            }

        }
        return returnX;
    }
}
