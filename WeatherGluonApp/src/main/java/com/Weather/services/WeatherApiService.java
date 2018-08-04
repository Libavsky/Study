package com.Weather.services;
import net.aksingh.owmjapis.CurrentWeather;
import net.aksingh.owmjapis.HourlyForecast;
import net.aksingh.owmjapis.OpenWeatherMap;

import java.io.IOException;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

/**
 * Created by Bot on 2018-08-02.
 */
public class WeatherApiService {

    private OpenWeatherMap owm = new OpenWeatherMap("a36ef0192d7c9182efc40269d2b45761");


    public CurrentWeather GetCurrentWeatherByName(String cityName, String countryCode) throws IOException {
        return owm.currentWeatherByCityName(cityName,countryCode);
    }
    public CurrentWeather GetCurrentWeatherByCoords(double lat, double lon) throws IOException {
        return owm.currentWeatherByCoordinates(((float) lat),(float)lon);
    }

    public HourlyForecast GetHourlyForecastByName(String cityName, String countryCode) throws IOException {
        return owm.hourlyForecastByCityName(cityName,countryCode);
    }

    public HourlyForecast GetHourlyForecastByCoords(double lat, double lon) throws IOException {
        return owm.hourlyForecastByCoordinates(((float) lat),(float)lon);
    }

    public List<HourlyForecast.Forecast> GetListOfForecasts(HourlyForecast hourlyForecast)
    {
        List<HourlyForecast.Forecast> returnList = new ArrayList<>();
        for(int i =0;i<40;i++)
        {
            try{returnList.add(hourlyForecast.getForecastInstance(i));}
            catch (IndexOutOfBoundsException e){
                break;
            }
        }
        return returnList;
    }

    public List<HourlyForecast.Forecast> GetDataByDate(HourlyForecast hourlyForecast, String numOfDays){
        Integer x = Integer.parseInt(numOfDays);
        return  GetListOfForecasts(hourlyForecast).stream().filter(
                e -> LocalDateTime.ofInstant(e.getDateTime().toInstant(),ZoneId.systemDefault()).getDayOfYear()==LocalDateTime.now().getDayOfYear()+x).collect(Collectors.toList());
    }

    public List<String> GetForecastDataInNiceFormat(List<HourlyForecast.Forecast> forecasts){
        List<String> returnList = new ArrayList<>();
        if(forecasts.isEmpty()){return returnList;}
        for (HourlyForecast.Forecast forecast:forecasts
                ) {
            String result = "";
            if (forecast.hasMainInstance()) {
                if (forecast.getMainInstance().hasTemperature()) {
                    result+=(forecast.getMainInstance().getTemperature())+" \u00b0F\n";
                }
                if (forecast.getMainInstance().hasPressure()) {
                    result+=(forecast.getMainInstance().getPressure())+" hPa\n";
                }
                if (forecast.getMainInstance().hasHumidity()) {
                    result+=(forecast.getMainInstance().getHumidity())+" % Humidity\n";
                }
            }
            if (forecast.hasCloudsInstance()) {
                result+=(forecast.getCloudsInstance().getPercentageOfClouds())+" % Cloudiness\n";
            }
            if(forecast.hasWindInstance()){
                if(forecast.getWindInstance().hasWindSpeed()){
                    result+=(forecast.getWindInstance().getWindSpeed())+" m/s wind";
                }
                if(forecast.getWindInstance().hasWindDegree() && !Float.isNaN(forecast.getWindInstance().getWindDegree())){
                    result+=" from Azimuth: "+(forecast.getWindInstance().getWindDegree())+"\u00b0";
                }

            }
            returnList.add(result);
        }
        returnList.add(String.valueOf(LocalDateTime.ofInstant(forecasts.get(0).getDateTime().toInstant(),ZoneId.systemDefault()).getHour()));
        returnList.add(String.valueOf(LocalDateTime.ofInstant(forecasts.get(forecasts.size()-1).getDateTime().toInstant(),ZoneId.systemDefault()).getHour()));
        return returnList;
    }

    public List<String> GetIconDesigantionsList(List<HourlyForecast.Forecast> forecasts){
        List<String> returnList = new ArrayList<>();
        if(forecasts.isEmpty()){return returnList;}
        for (HourlyForecast.Forecast forecast:forecasts
                ) {
            returnList.add("http://openweathermap.org/img/w/"+forecast.getWeatherInstance(0).getWeatherIconName()+".png");
        }
        returnList.add(String.valueOf(LocalDateTime.ofInstant(forecasts.get(0).getDateTime().toInstant(),ZoneId.systemDefault()).getHour()));
        returnList.add(String.valueOf(LocalDateTime.ofInstant(forecasts.get(forecasts.size()-1).getDateTime().toInstant(),ZoneId.systemDefault()).getHour()));
        return returnList;
    }

    public String GetCurrentWeatherInNiceFormat(CurrentWeather currentWeather)
    {
        String returnX="";
        if (currentWeather.hasWeatherInstance()) {
            returnX+="In general: "+currentWeather.getWeatherInstance(0).getWeatherName()+"   "+currentWeather.getWeatherInstance(0).getWeatherDescription()+"\n";
        }
        if (currentWeather.hasMainInstance()) {
            if (currentWeather.getMainInstance().hasTemperature()) {
                returnX+=(currentWeather.getMainInstance().getTemperature())+" \u00b0F\n";
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
            if(currentWeather.getWindInstance().hasWindDegree()&& !Float.isNaN(currentWeather.getWindInstance().getWindDegree())){
                returnX+=" from Azimuth: "+(currentWeather.getWindInstance().getWindDegree())+"\u00b0";
            }

        }
        return returnX;
    }
}
