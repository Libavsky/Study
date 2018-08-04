package com.Weather.services;

import com.Weather.actions.MenuActions;
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
public class CityService {


    private ObservableList<Citys> allCities;

    public CityService() {
        allCities = FXCollections.observableArrayList();
    }

    public void ReadCitysFromJson() throws FileNotFoundException, UnsupportedEncodingException {
        InputStreamReader fileReader = new InputStreamReader(new FileInputStream(MenuActions.class.getResource("/city.list.json").toExternalForm().substring(6)),"UTF-8");
        Type listType = new TypeToken<ArrayList<Citys>>(){}.getType();
        ArrayList<Citys> temp = new Gson().fromJson(fileReader, listType);
        allCities = FXCollections.observableArrayList(temp.stream().filter(e -> e.getCountry().equals("PL")).distinct().collect(Collectors.toList()));
    }

    public void PrintCityInfo()
    {
        System.out.println(allCities.get(0).getCountry());
    }

    public ObservableList<Citys> getAllCities() {
        return allCities;
    }
}



