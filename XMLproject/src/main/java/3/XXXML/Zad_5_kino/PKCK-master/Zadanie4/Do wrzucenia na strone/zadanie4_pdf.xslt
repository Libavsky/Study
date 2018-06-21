<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format"
    xmlns:msxsl="urn:schemas-microsoft-com:xslt" exclude-result-prefixes="msxsl"
>
  <xsl:output method="xml"/>
  
  <xsl:template match="/">
    <fo:root language="PL">
      <fo:layout-master-set>
        <fo:simple-page-master master-name="Raport" page-height="297mm" page-width="210mm" margin-top="5mm" margin-bottom="5mm" margin-left="5mm" margin-right="5mm">
          <fo:region-body margin-top="10mm" margin-bottom="10mm"/>
          <fo:region-after region-name="xsl-region-after" extent="20mm"/>
        </fo:simple-page-master>
      </fo:layout-master-set>
      <fo:page-sequence master-reference="Raport">
        <fo:static-content flow-name="xsl-region-after">
          <fo:block>
            <xsl:apply-templates select="/wypożyczalnia/autorzy/autor"/>
            <xsl:apply-templates select="/wypożyczalnia/data_raportu"/>
          </fo:block>
        </fo:static-content>
        <fo:flow flow-name="xsl-region-body">
          <fo:block font-weight="bold" text-align="center" font-size="large">
            <xsl:text>Statysyki miast</xsl:text>
          </fo:block>
          <xsl:apply-templates select="/wypożyczalnia/statystyki/miasta/miasto"/>
          <fo:block font-weight="bold" text-align="center" font-size="large" margin-bottom="100mm" margin-top="100mm" line-height="20mm">
            <xsl:text>Wypozyczenia</xsl:text>
          </fo:block>
          <fo:table margin-left="50mm" margin-right="50mm" margin-bottom="10mm" margin-top="10mm" table-layout="fixed" width="200mm" >
            <fo:table-column column-width="proportional-column-width(1)"/>
            <fo:table-column column-width="proportional-column-width(1)"/>
            <fo:table-column column-width="proportional-column-width(1)"/>
            <fo:table-column column-width="proportional-column-width(1)"/>
            <fo:table-column column-width="proportional-column-width(1)"/>
            <fo:table-header>
              <fo:table-row>
                <fo:table-cell text-align="center">
                  <fo:block font-weight="bold">Samochod</fo:block>
                </fo:table-cell>
                <fo:table-cell text-align="center">
                  <fo:block font-weight="bold">Pracownik</fo:block>
                </fo:table-cell>
                <fo:table-cell text-align="center">
                  <fo:block font-weight="bold">Data Wypozyczenia</fo:block>
                </fo:table-cell>
                <fo:table-cell text-align="center">
                  <fo:block font-weight="bold">Data Zwrotu</fo:block>
                </fo:table-cell>
                <fo:table-cell text-align="center">
                  <fo:block font-weight="bold">Wypozyczajacy</fo:block>
                </fo:table-cell>
              </fo:table-row>
            </fo:table-header>
            <fo:table-body>
              <xsl:apply-templates select="/wypożyczalnia/wypożyczenia/wypożyczenie"/>
            </fo:table-body>
          </fo:table>
        </fo:flow>
      </fo:page-sequence>
    </fo:root>
    
    <!--
    <xsl:text>Autorzy:&#xA;&#xA;</xsl:text>
    <xsl:apply-templates select="/wypożyczalnia/autorzy/autor"/>
    -->
  </xsl:template>

  <xsl:template match="/wypożyczalnia/statystyki/miasta/miasto">
    <fo:block border-color="black" border-width="0.6mm" border-style="solid" margin-top="5mm" margin-bottom="5mm" margin-left="5mm" margin-right="5mm">
      <fo:block>
        <xsl:value-of select="nazwa"/>
      </fo:block>
      <fo:list-block>
        <fo:list-item>
          <fo:list-item-label>
            <fo:block>Liczba samochodow:</fo:block>
          </fo:list-item-label>
          <fo:list-item-body>
            <fo:block margin-left="150mm">
              <xsl:value-of select="liczba_samochodow"/>
            </fo:block>
          </fo:list-item-body>
        </fo:list-item>
        <fo:list-item>
          <fo:list-item-label>
            <fo:block>Srednia cena wypozyczenia:</fo:block>
          </fo:list-item-label>
          <fo:list-item-body>
            <fo:block margin-left="150mm">
              <xsl:value-of select="średnia_cena_wypożyczenia"/>
            </fo:block>
          </fo:list-item-body>
        </fo:list-item>
        <fo:list-item>
          <fo:list-item-label>
            <fo:block>Sredni przebieg:</fo:block>
          </fo:list-item-label>
          <fo:list-item-body>
            <fo:block margin-left="150mm">
              <xsl:value-of select="średni_przebieg"/>
            </fo:block>
          </fo:list-item-body>
        </fo:list-item>
        <fo:list-item>
          <fo:list-item-label>
            <fo:block>Sredni wiek:</fo:block>
          </fo:list-item-label>
          <fo:list-item-body>
            <fo:block margin-left="150mm">
              <xsl:value-of select="średni_wiek"/>
            </fo:block>
          </fo:list-item-body>
        </fo:list-item>
      </fo:list-block>
    </fo:block>
   
  </xsl:template>
  

  <xsl:template match="/wypożyczalnia/wypożyczenia/wypożyczenie">
      <fo:table-row line-height="20mm" border-color="black" border-width="0.6mm" border-style="solid" margin-top="5mm" margin-bottom="5mm" margin-left="5mm" margin-right="5mm">
        <fo:table-cell>
          <fo:block>
            <xsl:value-of select="samochod" />
          </fo:block>
        </fo:table-cell>
        <fo:table-cell>
          <fo:block>
            <xsl:value-of select="pracownik" />
          </fo:block>
        </fo:table-cell>
        <fo:table-cell>
          <fo:block>
            <xsl:value-of select="data_wypożyczenia" />
          </fo:block>
        </fo:table-cell>
        <fo:table-cell>
          <fo:block>
            <xsl:value-of select="data_zwrotu" />
          </fo:block>
        </fo:table-cell>
        <fo:table-cell>
          <fo:block>
            <xsl:value-of select="wypożyczający" />
          </fo:block>
        </fo:table-cell>
      </fo:table-row>
  </xsl:template>

  <xsl:template match="/wypożyczalnia/autorzy/autor">
    <fo:block>
      <xsl:value-of select="concat(imie,' ',nazwisko)" />
    </fo:block>
  </xsl:template>

  <xsl:template match="/wypożyczalnia/data_raportu">
    <fo:block text-align="right">
      <xsl:value-of select="concat('Data wygenerowania: ',.)" />
    </fo:block>
  </xsl:template>
</xsl:stylesheet>
