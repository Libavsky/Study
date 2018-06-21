<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:msxsl="urn:schemas-microsoft-com:xslt" exclude-result-prefixes="msxsl" xmlns:cs="urn:cs" xmlns:typy="http://www.example.org/typy">
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
                <xsl:value-of select="count(/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Łódź'])"/>
              </liczba_samochodow>
              <średnia_cena_wypożyczenia>
                <xsl:value-of select="concat(format-number((sum(/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Łódź']/following-sibling::typy:cena_wypożyczenia_za_1_dzien) div count(/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Łódź'])),'####.00'),' ',/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Łódź']/following-sibling::typy:cena_wypożyczenia_za_1_dzien/@waluta)"/>
              </średnia_cena_wypożyczenia>
              <średni_przebieg>
                <xsl:value-of select="concat(format-number((sum(/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Łódź']/preceding-sibling::typy:przebieg) div count(/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Łódź'])),'##########'),' ', /typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Łódź']/preceding-sibling::typy:przebieg/@jednostka)"/>
              </średni_przebieg>
              <średni_wiek>
                <xsl:value-of select="format-number((sum(/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Łódź']/preceding-sibling::typy:rok_produkcji) div count(/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Łódź'])),'####')"/>
              </średni_wiek>
            </miasto>
            <miasto>
              <nazwa>Warszawa</nazwa>
              <liczba_samochodow>
                <xsl:value-of select="count(/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Warszawa'])"/>
              </liczba_samochodow>
              <średnia_cena_wypożyczenia>
                <xsl:value-of select="concat(format-number((sum(/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Warszawa']/following-sibling::typy:cena_wypożyczenia_za_1_dzien) div count(/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Warszawa'])),'####.00'),' ',/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Warszawa']/following-sibling::typy:cena_wypożyczenia_za_1_dzien/@waluta)"/>
              </średnia_cena_wypożyczenia>
              <średni_przebieg>
                <xsl:value-of select="concat(format-number((sum(/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Warszawa']/preceding-sibling::typy:przebieg) div count(/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Warszawa'])),'##########'),' ', /typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Warszawa']/preceding-sibling::typy:przebieg/@jednostka)"/>
              </średni_przebieg>
              <średni_wiek>
                <xsl:value-of select="format-number((sum(/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Warszawa']/preceding-sibling::typy:rok_produkcji) div count(/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Warszawa'])),'####')"/>
              </średni_wiek>
            </miasto>
            <miasto>
              <nazwa>Wrocław</nazwa>
              <liczba_samochodow>
                <xsl:value-of select="count(/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Wrocław'])"/>
              </liczba_samochodow>
              <średnia_cena_wypożyczenia>
                <xsl:value-of select="concat(format-number((sum(/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Wrocław']/following-sibling::typy:cena_wypożyczenia_za_1_dzien) div count(/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Wrocław'])),'####.00'),' ',/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Wrocław']/following-sibling::typy:cena_wypożyczenia_za_1_dzien/@waluta)"/>
              </średnia_cena_wypożyczenia>
              <średni_przebieg>
                <xsl:value-of select="concat(format-number((sum(/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Wrocław']/preceding-sibling::typy:przebieg) div count(/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Wrocław'])),'##########'),' ', /typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Wrocław']/preceding-sibling::typy:przebieg/@jednostka)"/>
              </średni_przebieg>
              <średni_wiek>
                <xsl:value-of select="format-number((sum(/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Wrocław']/preceding-sibling::typy:rok_produkcji) div count(/typy:wypożyczalnia/typy:samochody/typy:samochód/typy:miasto[@miasto = 'Wrocław'])),'####')"/>
              </średni_wiek>
            </miasto>
          </miasta>
        </statystyki>
        <wypożyczenia>
          <xsl:apply-templates select="/typy:wypożyczalnia/typy:usługi/typy:wypożyczenia"/>
        </wypożyczenia>
        <autorzy>
          <xsl:apply-templates select="/typy:wypożyczalnia/typy:opis/typy:autorzy"/>
        </autorzy>
        <data_raportu>
          <xsl:value-of  select="cs:datenow()"/>
        </data_raportu>
      </xsl:element>
    </xsl:template>
  
  <xsl:template match="/typy:wypożyczalnia/typy:usługi/typy:wypożyczenia">
      <xsl:apply-templates select="typy:wypożyczenie"/>
  </xsl:template>
  
  <xsl:template match="/typy:wypożyczalnia/typy:usługi/typy:wypożyczenia/typy:wypożyczenie">
    <xsl:variable name="id_samochodu" select="@id_samochodu"/>
    <xsl:variable name="nazwa_samochodu" select="/typy:wypożyczalnia/typy:samochody/typy:samochód[@id = $id_samochodu]/typy:nazwa"/>
    <xsl:variable name="id_pracownika" select="@id_pracownika"/>
    <xsl:variable name="pracownik" select="/typy:wypożyczalnia/typy:usługi/typy:pracownicy/typy:pracownik[@id = $id_pracownika]"/>
    <wypożyczenie>
      <samochod>
        <xsl:value-of select="concat($nazwa_samochodu/typy:marka, ' ', $nazwa_samochodu/typy:model)"/>
      </samochod>
      <pracownik>
        <xsl:value-of select="concat($pracownik/typy:imie, ' ', $pracownik/typy:nazwisko)"/>
      </pracownik>
      <data_wypożyczenia>
        <xsl:value-of select="typy:data_wypożyczenia"/>
      </data_wypożyczenia>
      <data_zwrotu>
        <xsl:value-of select="typy:data_zwrotu"/>
      </data_zwrotu>
      <wypożyczający>
        <xsl:value-of select="concat(typy:wypożyczający/@imie, ' ' , typy:wypożyczający/@nazwisko)"/>
      </wypożyczający>
    </wypożyczenie>
  </xsl:template>
  
  <xsl:template match="/typy:wypożyczalnia/typy:opis/typy:autorzy">
    <xsl:for-each select="typy:autor">
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
