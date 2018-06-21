<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:msxsl="urn:schemas-microsoft-com:xslt" exclude-result-prefixes="msxsl" xmlns:cs="urn:cs">
  <xsl:output method="xml" indent="yes"/>
  <msxsl:script language="C#" implements-prefix="cs">
    <![CDATA[
      public string datenow()
     {
        return(DateTime.Now.ToString("yyyy'-'MM'-'dd'T'HH':'mm':'ss'Z'"));
     }
     ]]>
  </msxsl:script>
  
    <xsl:template match="/">
      <xsl:element name="wypożyczalnia">
        <statystyki>
          <miasta>
            <miasto>
              <nazwa>Łódź</nazwa>
              <liczba_samochodow>
                <xsl:value-of select="count(/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Łódź'])"/>
              </liczba_samochodow>
              <średnia_cena_wypożyczenia>
                <xsl:value-of select="concat(format-number((sum(/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Łódź']/following-sibling::cena_wypożyczenia_za_1_dzien) div count(/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Łódź'])),'####.00'),' ',/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Łódź']/following-sibling::cena_wypożyczenia_za_1_dzien/@waluta)"/>
              </średnia_cena_wypożyczenia>
              <średni_przebieg>
                <xsl:value-of select="concat(format-number((sum(/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Łódź']/preceding-sibling::przebieg) div count(/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Łódź'])),'##########'),' ', /wypożyczalnia/samochody/samochód/miasto[@miasto = 'Łódź']/preceding-sibling::przebieg/@jednostka)"/>
              </średni_przebieg>
              <średni_wiek>
                <xsl:value-of select="format-number((sum(/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Łódź']/preceding-sibling::rok_produkcji) div count(/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Łódź'])),'####')"/>
              </średni_wiek>
            </miasto>
            <miasto>
              <nazwa>Warszawa</nazwa>
              <liczba_samochodow>
                <xsl:value-of select="count(/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Warszawa'])"/>
              </liczba_samochodow>
              <średnia_cena_wypożyczenia>
                <xsl:value-of select="concat(format-number((sum(/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Warszawa']/following-sibling::cena_wypożyczenia_za_1_dzien) div count(/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Warszawa'])),'####.00'),' ',/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Warszawa']/following-sibling::cena_wypożyczenia_za_1_dzien/@waluta)"/>
              </średnia_cena_wypożyczenia>
              <średni_przebieg>
                <xsl:value-of select="concat(format-number((sum(/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Warszawa']/preceding-sibling::przebieg) div count(/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Warszawa'])),'##########'),' ', /wypożyczalnia/samochody/samochód/miasto[@miasto = 'Warszawa']/preceding-sibling::przebieg/@jednostka)"/>
              </średni_przebieg>
              <średni_wiek>
                <xsl:value-of select="format-number((sum(/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Warszawa']/preceding-sibling::rok_produkcji) div count(/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Warszawa'])),'####')"/>
              </średni_wiek>
            </miasto>
            <miasto>
              <nazwa>Wrocław</nazwa>
              <liczba_samochodow>
                <xsl:value-of select="count(/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Wrocław'])"/>
              </liczba_samochodow>
              <średnia_cena_wypożyczenia>
                <xsl:value-of select="concat(format-number((sum(/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Wrocław']/following-sibling::cena_wypożyczenia_za_1_dzien) div count(/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Wrocław'])),'####.00'),' ',/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Wrocław']/following-sibling::cena_wypożyczenia_za_1_dzien/@waluta)"/>
              </średnia_cena_wypożyczenia>
              <średni_przebieg>
                <xsl:value-of select="concat(format-number((sum(/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Wrocław']/preceding-sibling::przebieg) div count(/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Wrocław'])),'##########'),' ', /wypożyczalnia/samochody/samochód/miasto[@miasto = 'Wrocław']/preceding-sibling::przebieg/@jednostka)"/>
              </średni_przebieg>
              <średni_wiek>
                <xsl:value-of select="format-number((sum(/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Wrocław']/preceding-sibling::rok_produkcji) div count(/wypożyczalnia/samochody/samochód/miasto[@miasto = 'Wrocław'])),'####')"/>
              </średni_wiek>
            </miasto>
          </miasta>
        </statystyki>
        <wypożyczenia>
          <xsl:apply-templates select="/wypożyczalnia/usługi/wypożyczenia"/>
        </wypożyczenia>
        <autorzy>
          <xsl:apply-templates select="/wypożyczalnia/opis/autorzy"/>
        </autorzy>
        <data_raportu>
          <xsl:value-of  select="cs:datenow()"/>
        </data_raportu>
      </xsl:element>
    </xsl:template>
  
  <xsl:template match="/wypożyczalnia/usługi/wypożyczenia">
      <xsl:apply-templates select="wypożyczenie"/>
  </xsl:template>
  
  <xsl:template match="/wypożyczalnia/usługi/wypożyczenia/wypożyczenie">
    <xsl:variable name="id_samochodu" select="@id_samochodu"/>
    <xsl:variable name="nazwa_samochodu" select="/wypożyczalnia/samochody/samochód[@id = $id_samochodu]/nazwa"/>
    <xsl:variable name="id_pracownika" select="@id_pracownika"/>
    <xsl:variable name="pracownik" select="/wypożyczalnia/usługi/pracownicy/pracownik[@id = $id_pracownika]"/>
    <wypożyczenie>
      <samochod>
        <xsl:value-of select="concat($nazwa_samochodu/marka, ' ', $nazwa_samochodu/model)"/>
      </samochod>
      <pracownik>
        <xsl:value-of select="concat($pracownik/imie, ' ', $pracownik/nazwisko)"/>
      </pracownik>
      <data_wypożyczenia>
        <xsl:value-of select="data_wypożyczenia"/>
      </data_wypożyczenia>
      <data_zwrotu>
        <xsl:value-of select="data_zwrotu"/>
      </data_zwrotu>
      <wypożyczający>
        <xsl:value-of select="concat(wypożyczający/@imie, ' ' , wypożyczający/@nazwisko)"/>
      </wypożyczający>
    </wypożyczenie>
  </xsl:template>
  
  <xsl:template match="/wypożyczalnia/opis/autorzy">
    <xsl:for-each select="autor">
      <xsl:sort select="@nazwisko" data-type="text"/>
      <autor>
        <imie>
          <xsl:value-of select="@imie"/>
        </imie>
        <nazwisko>
          <xsl:value-of select="@nazwisko"/>
        </nazwisko>
      </autor>
    </xsl:for-each>
  </xsl:template>
</xsl:stylesheet>
