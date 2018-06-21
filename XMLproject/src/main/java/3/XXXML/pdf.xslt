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
            <xsl:apply-templates select="/repertuar/autorzy/autor"/>
            <xsl:apply-templates select="/repertuar/data_raportu"/>
          </fo:block>
        </fo:static-content>
        <fo:flow flow-name="xsl-region-body">
          <fo:block font-weight="bold" text-align="center" font-size="large" font-family="Arial">
            <xsl:text>Statystyki gatunków filmowych</xsl:text>
          </fo:block>
          <xsl:apply-templates select="/repertuar/statystyki/gatunki/gatunek"/>
          <fo:block font-weight="bold" text-align="center" font-size="large" font-family="Arial" margin-bottom="20mm" margin-top="80mm" line-height="20mm">
            <xsl:text>Filmy w kinach</xsl:text>
          </fo:block>
          <fo:table margin-left="5mm" margin-right="5mm" margin-bottom="5mm" margin-top="5mm" table-layout="fixed" width="200mm" >
            <fo:table-column column-width="proportional-column-width(3)"/>
            <fo:table-column column-width="proportional-column-width(1)"/>
            <fo:table-column column-width="proportional-column-width(1)"/>
            <fo:table-header>
              <fo:table-row>
                <fo:table-cell text-align="center">
                  <fo:block font-weight="bold">Film</fo:block>
                </fo:table-cell>
                <fo:table-cell text-align="center">
                  <fo:block font-weight="bold">Kino</fo:block>
                </fo:table-cell>
                <fo:table-cell text-align="center">
                  <fo:block font-weight="bold">Data seansu</fo:block>
                </fo:table-cell>
              </fo:table-row>
            </fo:table-header>
            <fo:table-body>
              <xsl:apply-templates select="/repertuar/filmy_w_kinie/seans"/>
            </fo:table-body>
          </fo:table>
        </fo:flow>
      </fo:page-sequence>
    </fo:root>
  </xsl:template>
  
  <xsl:template match="/repertuar/statystyki/gatunki/gatunek">
    <fo:block border-color="black" border-width="0.6mm" border-style="solid" margin-top="5mm" margin-bottom="5mm" margin-left="5mm" margin-right="5mm" font-family="Arial">
      <fo:list-block>
      <fo:list-item>
          <fo:list-item-label>
            <fo:block>Gatunek:</fo:block>
          </fo:list-item-label>
          <fo:list-item-body>
            <fo:block margin-left="140mm">
              <xsl:value-of select="nazwa"/>
            </fo:block>
          </fo:list-item-body>
        </fo:list-item>
        <fo:list-item>
          <fo:list-item-label>
            <fo:block>Liczba filmów danego gatunku:</fo:block>
          </fo:list-item-label>
          <fo:list-item-body>
            <fo:block margin-left="140mm">
              <xsl:value-of select="liczba_gatunku"/>
            </fo:block>
          </fo:list-item-body>
        </fo:list-item>
        <fo:list-item>
          <fo:list-item-label>
            <fo:block>Średni box office:</fo:block>
          </fo:list-item-label>
          <fo:list-item-body>
            <fo:block margin-left="140mm">
              <xsl:value-of select="średnia_box_office"/>
            </fo:block>
          </fo:list-item-body>
        </fo:list-item>
        <fo:list-item>
          <fo:list-item-label>
            <fo:block>Średnia ocena:</fo:block>
          </fo:list-item-label>
          <fo:list-item-body>
            <fo:block margin-left="140mm">
              <xsl:value-of select="średnia_ocena"/>
            </fo:block>
          </fo:list-item-body>
        </fo:list-item>
        <fo:list-item>
          <fo:list-item-label>
            <fo:block>Średnia kategoria wiekowa:</fo:block>
          </fo:list-item-label>
          <fo:list-item-body>
            <fo:block margin-left="140mm">
              <xsl:value-of select="średni_wiek_od"/>
            </fo:block>
          </fo:list-item-body>
        </fo:list-item>
      </fo:list-block>
    </fo:block>
   
  </xsl:template>
  

  <xsl:template match="/repertuar/filmy_w_kinie/seans">
      <fo:table-row line-height="7mm" border-color="black" border-width="0.6mm" border-style="solid" margin-top="2mm" margin-bottom="2mm" margin-left="2mm" margin-right="2mm" font-family="Arial">
        <fo:table-cell>
          <fo:block>
            <xsl:value-of select="film" />
          </fo:block>
        </fo:table-cell>
        <fo:table-cell>
          <fo:block>
            <xsl:value-of select="kino" />
          </fo:block>
        </fo:table-cell>
        <fo:table-cell>
          <fo:block>
            <xsl:value-of select="data_seansu" />
          </fo:block>
        </fo:table-cell>
      </fo:table-row>
  </xsl:template>

  <xsl:template match="/repertuar/autorzy/autor">
    <fo:block font-family="Arial">
      <xsl:value-of select="concat(imie,' ',nazwisko)" />
    </fo:block>
  </xsl:template>

  <xsl:template match="/repertuar/data_raportu">
    <fo:block text-align="right" font-family="Arial">
      <xsl:value-of select="concat('Data wygenerowania: ',.)" />
    </fo:block>
  </xsl:template>
</xsl:stylesheet>