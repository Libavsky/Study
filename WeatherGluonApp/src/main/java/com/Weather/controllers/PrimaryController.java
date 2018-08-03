package com.Weather.controllers;

import com.Weather.models.Citys;
import com.Weather.services.CityServices;
import com.Weather.services.WeatherApiService;
import com.gluonhq.particle.application.ParticleApplication;
import com.gluonhq.particle.state.StateManager;
import com.gluonhq.particle.view.ViewManager;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.ResourceBundle;

import javafx.fxml.FXML;
import javafx.scene.control.*;

import javax.inject.Inject;

import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.input.MouseEvent;
import org.controlsfx.control.action.Action;
import org.controlsfx.control.action.ActionMap;
import org.controlsfx.control.action.ActionProxy;

public class PrimaryController {

    @Inject ParticleApplication app;
    
    @Inject private ViewManager viewManager;

    @Inject private StateManager stateManager;

    private CityServices cityServices = new CityServices();

    private WeatherApiService weatherApiService = new WeatherApiService();

    private boolean first = true;
    
    @FXML
    private Label label;
    
    @FXML
    private Button button;
    
    @FXML
    private ResourceBundle resources;

    @FXML
    private TableView<Citys> citytable;

    @FXML
    private TableColumn<Citys, String> name;

    @FXML
    private TableColumn<Citys, String> country;

    @FXML
    private TextArea CurrentWeather;
    
    private Action actionSignin;

    private Action actionLoadCitys;
    
    public void initialize() throws FileNotFoundException {
        ActionMap.register(this);
        actionSignin =  ActionMap.action("signin");
        actionLoadCitys = ActionMap.action("load");

        button.setOnAction(e -> viewManager.switchView("secondary"));



    }
    
    public void postInit() {
        if (first) {
            stateManager.setPersistenceMode(StateManager.PersistenceMode.USER);
            addUser(stateManager.getProperty("UserName").orElse("").toString());
            first = false;
        }
        app.getParticle().getToolBarActions().add(0, actionSignin);
        app.getParticle().getToolBarActions().add(1, actionLoadCitys);
    }
    
    public void dispose() {
        app.getParticle().getToolBarActions().remove(actionSignin);
        app.getParticle().getToolBarActions().remove(actionLoadCitys);
    }
    
    public void addUser(String userName) {
        label.setText(resources.getString("label.text") + (userName.isEmpty() ? "" :  ", " + userName) + "!");
        stateManager.setProperty("UserName", userName);
    }

    @ActionProxy(text="Sign In")
    private void signin() {
        TextInputDialog input = new TextInputDialog(stateManager.getProperty("UserName").orElse("").toString());
        input.setTitle("User name");
        input.setHeaderText(null);
        input.setContentText("Input your name:");
        input.showAndWait().ifPresent(this::addUser);
    }

    @ActionProxy(text="Load Citys")
    private void load() throws FileNotFoundException, UnsupportedEncodingException {

        cityServices.ReadCitysFromJson();
        name.setCellValueFactory(new PropertyValueFactory<Citys, String>("name"));
        country.setCellValueFactory(new PropertyValueFactory<Citys, String>("country"));
        citytable.setItems(cityServices.getAllCities());
        //cityServices.PrintCityInfo();
    }

    @FXML
    void selected(MouseEvent event) throws IOException {
        Citys selectedCity = citytable.getSelectionModel().getSelectedItem();
        CurrentWeather.setText(weatherApiService.GetCurrentWeatherInNiceFormat(weatherApiService.GetCurrentWeather(selectedCity.getName(),selectedCity.getCountry())));

    }

    
}