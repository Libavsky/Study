package com.Weather.models;

/**
 * Created by Bot on 2018-08-02.
 */
public class Citys {
    private Integer id;
    private String name;
    private String country;
    private Double lon;
    private Double lat;

    public Citys(Integer id, String name, String country, Double lon, Double lat) {
        this.id = id;
        this.name = name;
        this.country = country;
        this.lon = lon;
        this.lat = lat;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public Double getLon() {
        return lon;
    }

    public void setLon(Double lon) {
        this.lon = lon;
    }

    public Double getLat() {
        return lat;
    }

    public void setLat(Double lat) {
        this.lat = lat;
    }
}
