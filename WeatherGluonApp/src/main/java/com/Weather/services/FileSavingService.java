package com.Weather.services;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import com.thoughtworks.xstream.XStream;
import javafx.stage.FileChooser;
import net.aksingh.owmjapis.HourlyForecast;

import java.io.*;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by Bot on 2018-08-04.
 */
public class FileSavingService {

    public void Save(File file, FileChooser.ExtensionFilter filter, List<HourlyForecast.Forecast> forecasts) throws IOException {
        switch (filter.getExtensions().get(0)){
            case "*.txt":
                saveToTxt(file, forecasts);
                break;
            case "*.json":
                saveToJson(file, forecasts);
                break;
            case "*.xml":
                saveToXml(file, forecasts);
                break;
            case "*.csv":
                saveToCsv(file, forecasts);
                break;
        }
    }

    private void saveToCsv(File file, List<HourlyForecast.Forecast> forecasts) throws IOException {
        List<String> listToSave = new ArrayList<>();
        for (HourlyForecast.Forecast forecast:forecasts
                ) {
            listToSave.add(forecast.getRawResponse());
        }
        OutputStreamWriter outputStreamWriter = new OutputStreamWriter(new FileOutputStream(file),"UTF-8");
        outputStreamWriter.write(String.join(",",listToSave));
        outputStreamWriter.close();
    }

    private void saveToXml(File file, List<HourlyForecast.Forecast> forecasts) throws IOException {
        class forecastsList{
            List<HourlyForecast.Forecast> forecasts;

            public forecastsList(List<HourlyForecast.Forecast> forecasts) {
                this.forecasts = forecasts;
            }
        }
        forecastsList list = new forecastsList(forecasts);
        XStream xstream = new XStream();
        xstream.alias("forecast", HourlyForecast.Forecast.class);
        xstream.alias("forecasts", forecastsList.class);
        xstream.addImplicitCollection(forecastsList.class, "forecasts");

        String xml = xstream.toXML(list);
        OutputStreamWriter outputStreamWriter = new OutputStreamWriter(new FileOutputStream(file),"UTF-8");
        outputStreamWriter.write(xml);
        outputStreamWriter.close();

    }

    private void saveToJson(File file, List<HourlyForecast.Forecast> forecasts) throws IOException {
        OutputStreamWriter outputStreamWriter = new OutputStreamWriter(new FileOutputStream(file),"UTF-8");
        String gson = new Gson().toJson(forecasts);
        outputStreamWriter.write(gson);
        outputStreamWriter.close();
    }

    private void saveToTxt(File file, List<HourlyForecast.Forecast> forecasts) throws IOException {
        String toBeSaved = "";
        for (HourlyForecast.Forecast forecast:forecasts
             ) {
            toBeSaved+=forecast.getRawResponse();
        }
        OutputStreamWriter outputStreamWriter = new OutputStreamWriter(new FileOutputStream(file),"UTF-8");
        outputStreamWriter.write(toBeSaved);
        outputStreamWriter.close();

    }

}
