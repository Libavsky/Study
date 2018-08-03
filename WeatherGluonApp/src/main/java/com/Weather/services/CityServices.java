package com.Weather.services;

import com.Weather.models.Citys;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;

import java.io.*;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.stream.Collectors;

/**
 * Created by Bot on 2018-08-02.
 */
public class CityServices {

    private ObservableList<Citys> allCities;

    public void ReadCitysFromJson() throws FileNotFoundException, UnsupportedEncodingException {
        InputStreamReader fileReader = new InputStreamReader(new FileInputStream("E:\\projekty\\repomine2\\z\\WeatherGluonApp\\src\\main\\resources\\city.list.json"),"UTF-8");
        Type listType = new TypeToken<ArrayList<Citys>>(){}.getType();
        ArrayList<Citys> temp = new Gson().fromJson(fileReader, listType);
        allCities = FXCollections.observableArrayList(temp.stream().filter(e -> e.getCountry().equals("PL")).distinct().collect(Collectors.toList()));
        //allCities = new Gson().fromJson(fileReader,ArrayList<Citys>.class);
    }

    public void PrintCityInfo()
    {
        System.out.println(allCities.get(0).getCountry());
    }

    public ObservableList<Citys> getAllCities() {
        return allCities;
    }
}



