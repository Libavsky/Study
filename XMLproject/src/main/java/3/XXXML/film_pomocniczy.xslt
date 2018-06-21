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
  
  <xsl:element name="repertuar">
   <autorzy>
          <xsl:apply-templates select="/repertuar/metadane/autorzy"/>
        </autorzy>
        <statystyki>
          <gatunki>
            <gatunek>
              <nazwa>Science-Fiction</nazwa>
              <liczba_gatunku>
                <xsl:value-of select="count(/repertuar/filmy/film/gatunek[@rodzaj = 'Science-Fiction'])"/>
              </liczba_gatunku>
              <średnia_box_office>
                <xsl:value-of select="concat(format-number((sum(/repertuar/filmy/film/gatunek[@rodzaj = 'Science-Fiction']/following-sibling::box_office) div count(/repertuar/filmy/film/gatunek[@rodzaj = 'Science-Fiction'])),'####.00'),' ',/repertuar/filmy/film/gatunek[@rodzaj = 'Science-Fiction']/following-sibling::box_office/@waluta)"/>
              </średnia_box_office>
              <średnia_ocena>
                <xsl:value-of select="format-number((sum(/repertuar/filmy/film/gatunek[@rodzaj = 'Science-Fiction']/following-sibling::ocena) div count(/repertuar/filmy/film/gatunek[@rodzaj = 'Science-Fiction'])),'###')"/>
              </średnia_ocena>
              <średni_wiek_od>
                <xsl:value-of select="format-number((sum(/repertuar/filmy/film/gatunek[@rodzaj = 'Science-Fiction']/following-sibling::ograniczenie_wiekowe/@od_lat) div count(/repertuar/filmy/film/gatunek[@rodzaj = 'Science-Fiction'])),'####')"/>
              </średni_wiek_od>
            </gatunek>
            
              <gatunek>
              <nazwa>Thriller</nazwa>
              <liczba_gatunku>
                <xsl:value-of select="count(/repertuar/filmy/film/gatunek[@rodzaj = 'Thriller'])"/>
              </liczba_gatunku>
              <średnia_box_office>
                <xsl:value-of select="concat(format-number((sum(/repertuar/filmy/film/gatunek[@rodzaj = 'Thriller']/following-sibling::box_office) div count(/repertuar/filmy/film/gatunek[@rodzaj = 'Thriller'])),'####.00'),' ',/repertuar/filmy/film/gatunek[@rodzaj = 'Thriller']/following-sibling::box_office/@waluta)"/>
              </średnia_box_office>
              <średnia_ocena>
                <xsl:value-of select="format-number((sum(/repertuar/filmy/film/gatunek[@rodzaj = 'Thriller']/following-sibling::ocena) div count(repertuar/filmy/film/gatunek[@rodzaj = 'Thriller'])),'##########')"/>
              </średnia_ocena>
              <średni_wiek_od>
                <xsl:value-of select="format-number((sum(/repertuar/filmy/film/gatunek[@rodzaj = 'Thriller']/following-sibling::ograniczenie_wiekowe/@od_lat) div count(/repertuar/filmy/film/gatunek[@rodzaj = 'Thriller'])),'####')"/>
              </średni_wiek_od>
            </gatunek>
			     <gatunek>
              <nazwa>Fantasy</nazwa>
              <liczba_gatunku>
                <xsl:value-of select="count(/repertuar/filmy/film/gatunek[@rodzaj = 'Fantasy'])"/>
              </liczba_gatunku>
              <średnia_box_office>
                <xsl:value-of select="concat(format-number((sum(/repertuar/filmy/film/gatunek[@rodzaj = 'Fantasy']/following-sibling::box_office) div count(/repertuar/filmy/film/gatunek[@rodzaj = 'Fantasy'])),'####.00'),' ',/repertuar/filmy/film/gatunek[@rodzaj = 'Fantasy']/following-sibling::box_office/@waluta)"/>
              </średnia_box_office>
              <średnia_ocena>
                <xsl:value-of select="format-number((sum(/repertuar/filmy/film/gatunek[@rodzaj = 'Fantasy']/following-sibling::ocena) div count(/repertuar/filmy/film/gatunek[@rodzaj = 'Fantasy'])),'###')"/>
              </średnia_ocena>
              <średni_wiek_od>
                <xsl:value-of select="format-number((sum(/repertuar/filmy/film/gatunek[@rodzaj = 'Fantasy']/following-sibling::ograniczenie_wiekowe/@od_lat) div count(/repertuar/filmy/film/gatunek[@rodzaj = 'Fantasy'])),'####')"/>
              </średni_wiek_od>
            </gatunek>
			
			     <gatunek>
              <nazwa>Dramat</nazwa>
              <liczba_gatunku>
                <xsl:value-of select="count(/repertuar/filmy/film/gatunek[@rodzaj = 'Dramat'])"/>
              </liczba_gatunku>
              <średnia_box_office>
                <xsl:value-of select="concat(format-number((sum(/repertuar/filmy/film/gatunek[@rodzaj = 'Dramat']/following-sibling::box_office) div count(/repertuar/filmy/film/gatunek[@rodzaj = 'Dramat'])),'####.00'),' ',/repertuar/filmy/film/gatunek[@rodzaj = 'Dramat']/following-sibling::box_office/@waluta)"/>
              </średnia_box_office>
              <średnia_ocena>
                <xsl:value-of select="format-number((sum(/repertuar/filmy/film/gatunek[@rodzaj = 'Dramat']/following-sibling::ocena) div count(/repertuar/filmy/film/gatunek[@rodzaj = 'Dramat'])),'##########')"/>
              </średnia_ocena>
              <średni_wiek_od>
                <xsl:value-of select="format-number((sum(/repertuar/filmy/film/gatunek[@rodzaj = 'Dramat']/following-sibling::ograniczenie_wiekowe/@od_lat) div count(/repertuar/filmy/film/gatunek[@rodzaj = 'Dramat'])),'####')"/>
              </średni_wiek_od>
            </gatunek>
			
			
			<gatunek>
              <nazwa>Dokument</nazwa>
              <liczba_gatunku>
                <xsl:value-of select="count(/repertuar/filmy/film/gatunek[@rodzaj = 'Dokument'])"/>
              </liczba_gatunku>
              <średnia_box_office>
                <xsl:value-of select="concat(format-number((sum(/repertuar/filmy/film/gatunek[@rodzaj = 'Dokument']/following-sibling::box_office) div count(/repertuar/filmy/film/gatunek[@rodzaj = 'Dokument'])),'####.00'),' ',/repertuar/filmy/film/gatunek[@rodzaj = 'Dokument']/following-sibling::box_office/@waluta)"/>
              </średnia_box_office>
              <średnia_ocena>
                <xsl:value-of select="format-number((sum(/repertuar/filmy/film/gatunek[@rodzaj = 'Dokument']/following-sibling::ocena) div count(/repertuar/filmy/film/gatunek[@rodzaj = 'Dokument'])),'##########')"/>
              </średnia_ocena>
              <średni_wiek_od>
                <xsl:value-of select="format-number((sum(/repertuar/filmy/film/gatunek[@rodzaj = 'Dokument']/following-sibling::ograniczenie_wiekowe/@od_lat) div count(/repertuar/filmy/film/gatunek[@rodzaj = 'Dokument'])),'####')"/>
              </średni_wiek_od>
            </gatunek>
			
			<gatunek>
              <nazwa>Kryminał</nazwa>
              <liczba_gatunku>
                <xsl:value-of select="count(/repertuar/filmy/film/gatunek[@rodzaj = 'Kryminał'])"/>
              </liczba_gatunku>
              <średnia_box_office>
                <xsl:value-of select="concat(format-number((sum(/repertuar/filmy/film/gatunek[@rodzaj = 'Kryminał']/following-sibling::box_office) div count(/repertuar/filmy/film/gatunek[@rodzaj = 'Kryminał'])),'####.00'),' ',/repertuar/filmy/film/gatunek[@rodzaj = 'Kryminał']/following-sibling::box_office/@waluta)"/>
              </średnia_box_office>
              <średnia_ocena>
                <xsl:value-of select="format-number((sum(/repertuar/filmy/film/gatunek[@rodzaj = 'Kryminał']/following-sibling::ocena) div count(/repertuar/filmy/film/gatunek[@rodzaj = 'Kryminał'])),'##########')"/>
              </średnia_ocena>
              <średni_wiek_od>
                <xsl:value-of select="format-number((sum(/repertuar/filmy/film/gatunek[@rodzaj = 'Kryminał']/following-sibling::ograniczenie_wiekowe/@od_lat) div count(/repertuar/filmy/film/gatunek[@rodzaj = 'Kryminał'])),'####')"/>
              </średni_wiek_od>
            </gatunek>
			
			
          </gatunki>
        </statystyki>
        
        <filmy_w_kinie>
          <xsl:apply-templates select="/repertuar/wyświetlanie/seanse"/>
        </filmy_w_kinie>
        <data_raportu>
          <xsl:value-of  select="cs:datenow()"/>
        </data_raportu>
      </xsl:element>
    </xsl:template>
  
  <xsl:template match="/repertuar/wyświetlanie/seanse">
      <xsl:apply-templates select="seans"/>
  </xsl:template>
  
  
  
  <xsl:template match="/repertuar/wyświetlanie/seanse/seans">
    <xsl:variable name="id_filmu" select="@id_filmu"/>
    <xsl:variable name="nazwa_filmu" select="/repertuar/filmy/film[@id = $id_filmu]"/>
    <xsl:variable name="id_kina" select="@id_kina"/>
    <xsl:variable name="kino" select="/repertuar/wyświetlanie/kina/kino[@id = $id_kina]"/>
    <seans>
      <film>
        <xsl:value-of select="concat($nazwa_filmu/tytuł, '  by:  ', $nazwa_filmu/reżyser)"/>
      </film>
      <kino>
        <xsl:value-of select="concat($kino/nazwa, ' ', $kino/miasto)"/>
      </kino>
      <data_seansu>
        <xsl:value-of select="data_seansu"/>
      </data_seansu>
    </seans>
  </xsl:template>
  
  <xsl:template match="/repertuar/metadane/autorzy">
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