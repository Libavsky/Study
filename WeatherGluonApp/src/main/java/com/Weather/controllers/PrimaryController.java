package com.Weather.controllers;

import com.Weather.actions.MenuActions;
import com.Weather.models.Citys;
import com.Weather.services.CityService;
import com.Weather.services.FileSavingService;
import com.Weather.services.WeatherApiService;
import com.gluonhq.particle.application.ParticleApplication;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.List;
import java.util.ResourceBundle;


import com.lynden.gmapsfx.GoogleMapView;
import com.lynden.gmapsfx.MapComponentInitializedListener;
import com.lynden.gmapsfx.javascript.event.GMapMouseEvent;
import com.lynden.gmapsfx.javascript.event.UIEventType;
import com.lynden.gmapsfx.javascript.object.*;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.Node;
import javafx.scene.control.*;

import javax.inject.Inject;

import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.GridPane;
import javafx.stage.FileChooser;
import javafx.stage.Stage;
import org.controlsfx.control.action.Action;
import org.controlsfx.control.action.ActionMap;
import org.controlsfx.control.action.ActionProxy;



public class PrimaryController implements MapComponentInitializedListener{

    @Inject ParticleApplication app;

    private CityService cityService = new CityService();

    private WeatherApiService weatherApiService = new WeatherApiService();

    private FileSavingService fileSavingService = new FileSavingService();

    @FXML
    private GridPane grid;          //Children with indexes 8-15 are ImageViews, 16-23 = Labels to fill with data

    private ObservableList<Node> gridChildren;
    
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

    @FXML
    private ChoiceBox<String> ChooseDay;

    @FXML
    private GoogleMapView Map;

    private GoogleMap map;

    private MarkerOptions markerOptions;

    private LatLong currentLatLong;

    private Action actionLoadCitys;

    private Action actionSaveData;
    
    public void initialize() {
        ActionMap.register(this);
        actionLoadCitys = ActionMap.action("load");
        actionSaveData=ActionMap.action("saveToFile");
        Map.addMapInializedListener(this);
        ChooseDay.setItems(FXCollections.observableArrayList("0","1","2","3","4","5"));
        ChooseDay.getSelectionModel().selectFirst();
        gridChildren = grid.getChildren();
        markerOptions = new MarkerOptions().visible(Boolean.TRUE);

    }
    
    public void postInit() {
        app.getParticle().getToolBarActions().add(0, actionLoadCitys);
        app.getParticle().getToolBarActions().add(1, actionSaveData);
    }
    
    public void dispose() {
        app.getParticle().getToolBarActions().remove(actionLoadCitys);
        app.getParticle().getToolBarActions().remove(actionSaveData);
    }

    @ActionProxy(text="Save to file")
    private void saveToFile() {

        if(currentLatLong==null){
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("Alert");
            alert.setHeaderText("Data needed");
            alert.setContentText("Gather some data by selecting a city or clicking somewhere on the map");
            alert.showAndWait();
            return;
        }

        FileChooser fileChooser = new FileChooser();

        FileChooser.ExtensionFilter extFilter = new FileChooser.ExtensionFilter("TXT files (*.txt)", "*.txt");
        FileChooser.ExtensionFilter jsonFilter = new FileChooser.ExtensionFilter("JSON files (*.json)", "*.json");
        FileChooser.ExtensionFilter csvFilter = new FileChooser.ExtensionFilter("CSV files (*.csv)", "*.csv");
        FileChooser.ExtensionFilter xmlFilter = new FileChooser.ExtensionFilter("XML files (*.xml)", "*.xml");
        fileChooser.getExtensionFilters().add(extFilter);
        fileChooser.getExtensionFilters().add(jsonFilter);
        fileChooser.getExtensionFilters().add(csvFilter);
        fileChooser.getExtensionFilters().add(xmlFilter);

        File file = fileChooser.showSaveDialog(new Stage());
        if(file != null){
            try {
                fileSavingService.Save(file,fileChooser.getSelectedExtensionFilter(),weatherApiService.GetListOfForecasts(
                        weatherApiService.GetHourlyForecastByCoords(currentLatLong.getLatitude(),currentLatLong.getLongitude())));
            } catch (IOException e) {
                e.printStackTrace();
                ShowErrorAlert(e);
            }
        }

    }

    @ActionProxy(text="Load Cities")
    private void load() {

        try {
            cityService.ReadCitysFromJson();
            name.setCellValueFactory(new PropertyValueFactory<Citys, String>("name"));
            country.setCellValueFactory(new PropertyValueFactory<Citys, String>("country"));
            citytable.setItems(cityService.getAllCities());
        } catch (FileNotFoundException | UnsupportedEncodingException e) {
            e.printStackTrace();
            ShowErrorAlert(e);
        }


    }

    @FXML
    void selected(MouseEvent event) {
        Citys selectedCity = citytable.getSelectionModel().getSelectedItem();
        net.aksingh.owmjapis.CurrentWeather currentWeather = null;
            try {
                currentWeather = weatherApiService.GetCurrentWeatherByName(selectedCity.getName(),selectedCity.getCountry());
                CurrentWeather.setText(weatherApiService.GetCurrentWeatherInNiceFormat(weatherApiService.GetCurrentWeatherByName(selectedCity.getName(),selectedCity.getCountry())));
                currentLatLong = new LatLong(currentWeather.getCoordInstance().getLatitude(),currentWeather.getCoordInstance().getLongitude());
                map.setCenter(currentLatLong);
                map.clearMarkers();
                map.addMarker(new Marker(markerOptions.position(currentLatLong)));

            }
            catch (NullPointerException e)
            {
                ;
            } catch (IOException e) {
                e.printStackTrace();
                ShowErrorAlert(e);
            }

        try {
                List<String> icons = weatherApiService.GetIconDesigantionsList(weatherApiService.GetDataByDate(
                        weatherApiService.GetHourlyForecastByName(selectedCity.getName(),selectedCity.getCountry()),ChooseDay.getValue()));
                List<String> ForecastLabelData = weatherApiService.GetForecastDataInNiceFormat(weatherApiService.GetDataByDate(
                        weatherApiService.GetHourlyForecastByName(selectedCity.getName(),selectedCity.getCountry()),ChooseDay.getValue()));
                if(icons.isEmpty()){
                    clearImagesAndDataLabels();
                }
                else {
                    int startingPoint = (((Integer.parseInt(icons.get(icons.size() - 2))) + 1) / 3) + 7; //horrible translation to index format given at the gridpane definition
                    int endingPoint = (((Integer.parseInt(icons.get(icons.size() - 1))) + 1) / 3) + 7;
                    clearImagesAndDataLabels();
                    for (int i = startingPoint; i <= endingPoint; i++) {
                        ((ImageView) gridChildren.get(i)).setImage(new Image(icons.get(i - startingPoint)));
                    }
                    for (int j = startingPoint + 8; j <= endingPoint + 8; j++) {
                        ((Label) gridChildren.get(j)).setText(ForecastLabelData.get(j - (startingPoint+8)));
                    }
                    for (int i = endingPoint + 1; i <= 15; i++) {
                        ((ImageView) gridChildren.get(i)).setImage(null);
                    }
                    for (int i = endingPoint + 9; i <= 23; i++) {
                        ((Label) gridChildren.get(i)).setText("No Data");
                    }
                }

            } catch (IOException e) {
                e.printStackTrace();
                ShowErrorAlert(e);
            }

            catch (NullPointerException e) {
                CurrentWeather.setText("Please load city data");
            }

    }



    public void clearImagesAndDataLabels(){

        for (int j = 8;j<=15;j++){
            ((ImageView)gridChildren.get(j)).setImage(null);
        }
        for (int j = 16;j<=23;j++){
            ((Label)gridChildren.get(j)).setText("No Data");
        }
    }


    @Override
    public void mapInitialized() {
        MapOptions mapOptions = new MapOptions();

        mapOptions.center(new LatLong(52.237049, 21.017532))
                .mapType(MapTypeIdEnum.ROADMAP)
                .overviewMapControl(false)
                .panControl(false)
                .rotateControl(false)
                .scaleControl(false)
                .streetViewControl(false)
                .zoomControl(false)
                .zoom(12);

        map = Map.createMap(mapOptions);
        map.addMouseEventHandler(UIEventType.click, (GMapMouseEvent event) -> {
            currentLatLong = event.getLatLong();
            map.clearMarkers();
            markerOptions.position(currentLatLong).visible(Boolean.TRUE);

            map.addMarker(new Marker(markerOptions));
            try {
                    CurrentWeather.setText(weatherApiService.GetCurrentWeatherInNiceFormat(weatherApiService.GetCurrentWeatherByCoords(currentLatLong.getLatitude(),currentLatLong.getLongitude())));
                } catch (IOException e) {
                    e.printStackTrace();
                    ShowErrorAlert(e);
                }
            try {
                    List<String> icons = weatherApiService.GetIconDesigantionsList(weatherApiService.GetDataByDate(
                            weatherApiService.GetHourlyForecastByCoords(currentLatLong.getLatitude(),currentLatLong.getLongitude()),ChooseDay.getValue()));
                    List<String> ForecastLabelData = weatherApiService.GetForecastDataInNiceFormat(weatherApiService.GetDataByDate(
                            weatherApiService.GetHourlyForecastByCoords(currentLatLong.getLatitude(),currentLatLong.getLongitude()),ChooseDay.getValue()));
                    if(icons.isEmpty()){
                        clearImagesAndDataLabels();
                    }
                    else {
                        int startingPoint = (((Integer.parseInt(icons.get(icons.size() - 2))) + 1) / 3) + 7; //horrible translation to index format given at the gridpane definition
                        int endingPoint = (((Integer.parseInt(icons.get(icons.size() - 1))) + 1) / 3) + 7;
                        clearImagesAndDataLabels();
                        for (int i = startingPoint; i <= endingPoint; i++) {
                            ((ImageView) gridChildren.get(i)).setImage(new Image(icons.get(i - startingPoint)));
                        }
                        for (int j = startingPoint + 8; j <= endingPoint + 8; j++) {
                            ((Label) gridChildren.get(j)).setText(ForecastLabelData.get(j - (startingPoint+8)));
                        }
                        for (int i = endingPoint + 1; i <= 15; i++) {
                            ((ImageView) gridChildren.get(i)).setImage(null);
                        }
                        for (int i = endingPoint + 9; i <= 23; i++) {
                            ((Label) gridChildren.get(i)).setText("No Data");
                        }
                    }

                } catch (IOException e) {
                    e.printStackTrace();
                    ShowErrorAlert(e);
                }

        });
    }
    public void ShowErrorAlert(Exception e){
        Alert alert = new Alert(Alert.AlertType.ERROR);
        alert.setTitle("Error");
        alert.setHeaderText("Something went wrong");
        alert.setContentText("For developers"+e.getMessage());
        alert.showAndWait();
    }


}