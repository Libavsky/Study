<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:msxsl="urn:schemas-microsoft-com:xslt" exclude-result-prefixes="msxsl"
>
  <xsl:output method="text"/>

    <xsl:template match="/">
      <xsl:text>Statysyki miast:&#xA;&#xA;</xsl:text>
      <xsl:apply-templates select="/wypożyczalnia/statystyki/miasta/miasto"/>
      <xsl:text>Wypożyczenia:&#xA;&#xA;</xsl:text>
      <xsl:apply-templates select="/wypożyczalnia/wypożyczenia/wypożyczenie"/>
      <xsl:text>Autorzy:&#xA;&#xA;</xsl:text>
      <xsl:apply-templates select="/wypożyczalnia/autorzy/autor"/>
      <xsl:apply-templates select="/wypożyczalnia/data_raportu"/>
    </xsl:template>

  <xsl:template match="/wypożyczalnia/statystyki/miasta/miasto">

    <xsl:value-of select="concat(nazwa,'&#xA;')" />
    
    <xsl:text>Liczba samochodów:</xsl:text>
    <xsl:call-template name="wyswietlSpacje">
      <xsl:with-param name="ilosc" select="30 - string-length('Liczba samochodów:')"/>
    </xsl:call-template>
    <xsl:value-of select="concat(liczba_samochodow,'&#xA;')" />
    
    <xsl:text>Średnia cena wypożyczenia</xsl:text>
    <xsl:call-template name="wyswietlSpacje">
      <xsl:with-param name="ilosc" select="30 - string-length('Średnia cena wypożyczenia')"/>
    </xsl:call-template>
    <xsl:value-of select="concat(średnia_cena_wypożyczenia,'&#xA;')" />
    
    <xsl:text>Średni przebieg:</xsl:text>
    <xsl:call-template name="wyswietlSpacje">
      <xsl:with-param name="ilosc" select="30 - string-length('Średni przebieg:')"/>
    </xsl:call-template>
    <xsl:value-of select="concat(średnia_cena_wypożyczenia,'&#xA;')" />
    
    <xsl:text>Średni wiek:</xsl:text>
    <xsl:call-template name="wyswietlSpacje">
      <xsl:with-param name="ilosc" select="30 - string-length('Średni wiek:')"/>
    </xsl:call-template>
    <xsl:value-of select="concat(średni_wiek,'&#xA;&#xA;')" />
  </xsl:template>

  <xsl:template match="/wypożyczalnia/wypożyczenia/wypożyczenie">
    
    <xsl:text>Samochód:</xsl:text>
    <xsl:call-template name="wyswietlSpacje">
      <xsl:with-param name="ilosc" select="30 - string-length('Samochód:')"/>
    </xsl:call-template>
    <xsl:value-of select="concat(samochod,'&#xA;')" />
    
    <xsl:text>Pracownik:</xsl:text>
    <xsl:call-template name="wyswietlSpacje">
      <xsl:with-param name="ilosc" select="30 - string-length('Pracownik:')"/>
    </xsl:call-template>
    <xsl:value-of select="concat(pracownik,'&#xA;')" />
    
    <xsl:text>Data wypożyczenia:</xsl:text>
    <xsl:call-template name="wyswietlSpacje">
      <xsl:with-param name="ilosc" select="30 - string-length('Data wypożyczenia:')"/>
    </xsl:call-template>
    <xsl:value-of select="concat(data_wypożyczenia,'&#xA;')" />
    
    <xsl:text>Data zwrotu:</xsl:text>
    <xsl:call-template name="wyswietlSpacje">
      <xsl:with-param name="ilosc" select="30 - string-length('Data zwrotu:')"/>
    </xsl:call-template>
    <xsl:value-of select="concat(data_zwrotu,'&#xA;')" />

    <xsl:text>Wypożyczający:</xsl:text>
    <xsl:call-template name="wyswietlSpacje">
      <xsl:with-param name="ilosc" select="30 - string-length('Wypożyczający:')"/>
    </xsl:call-template>
    <xsl:value-of select="concat(wypożyczający,'&#xA;&#xA;')" />
  </xsl:template>

  <xsl:template match="/wypożyczalnia/autorzy/autor">
    <xsl:text>Imie:</xsl:text>
    <xsl:call-template name="wyswietlSpacje">
      <xsl:with-param name="ilosc" select="30 - string-length('Imie:')"/>
    </xsl:call-template>
    <xsl:value-of select="concat(imie,'&#xA;')" />

    <xsl:text>Nazwisko:</xsl:text>
    <xsl:call-template name="wyswietlSpacje">
      <xsl:with-param name="ilosc" select="30 - string-length('Nazwisko:')"/>
    </xsl:call-template>
    <xsl:value-of select="concat(nazwisko,'&#xA;&#xA;')" />
  </xsl:template>

  <xsl:template match="/wypożyczalnia/data_raportu">
    <xsl:text>Data Raportu:</xsl:text>
    <xsl:call-template name="wyswietlSpacje">
      <xsl:with-param name="ilosc" select="30 - string-length('Data Raportu:')"/>
    </xsl:call-template>
    <xsl:value-of select="concat(.,'&#xA;')" />
  </xsl:template>

  <xsl:template name="wyswietlSpacje" >
    <xsl:param name="ilosc"/>
    <xsl:if test="$ilosc > 0">
      <xsl:text> </xsl:text>
      <xsl:call-template name="wyswietlSpacje">
        <xsl:with-param name="ilosc" select="$ilosc - 1"/>
      </xsl:call-template>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
