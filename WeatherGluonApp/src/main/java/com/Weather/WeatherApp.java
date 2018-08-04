package com.Weather;

import com.gluonhq.particle.application.ParticleApplication;
import javafx.scene.Scene;
import static org.controlsfx.control.action.ActionMap.actions;

public class WeatherApp extends ParticleApplication {

    public WeatherApp() {
        super("OxyWeatherApp");
    }

    @Override
    public void postInit(Scene scene) {
        scene.getStylesheets().add(WeatherApp.class.getResource("style.css").toExternalForm());

        setTitle("OxyWeatherApp [UALX and X47]");
        
        getParticle().getToolBarActions().addAll(actions("---", "about", "exit"));
    }
}