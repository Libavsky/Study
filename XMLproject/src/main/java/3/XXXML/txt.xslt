<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:msxsl="urn:schemas-microsoft-com:xslt" exclude-result-prefixes="msxsl"
>
  <xsl:output method="text"/>
	<xsl:variable name="spacje" select='"                                                                             "'/>
    <xsl:template match="/">
	  <xsl:text>Statystyki gatunków filmowych:&#xA;&#xA;</xsl:text>
      <xsl:apply-templates select="/repertuar/statystyki/gatunki/gatunek"/>
      <xsl:text>Filmy w kinie:&#xA;&#xA;</xsl:text>
      <xsl:apply-templates select="/repertuar/filmy_w_kinie/seans"/>
      <xsl:text>Autorzy:&#xA;&#xA;</xsl:text>
      <xsl:apply-templates select="/repertuar/autorzy/autor"/>
      <xsl:apply-templates select="/repertuar/data_raportu"/>
    </xsl:template>
    
    <xsl:template match="/repertuar/statystyki/gatunki/gatunek">

		<!-- <xsl:value-of select="concat(nazwa,'&#xA;')" /> -->
		
		<xsl:text>Gatunek:</xsl:text>
		<xsl:value-of select="substring($spacje,0,60 - string-length('Gatunek:'))"/>
		<xsl:value-of select="concat(nazwa,'&#xA;')" />
		
		<xsl:text>Liczba wystąpień gatunku:</xsl:text>
		<xsl:value-of select="substring($spacje,0,60 - string-length('Liczba wystąpień gatunku:'))"/>
		<xsl:value-of select="concat(liczba_gatunku,'&#xA;')" />
		
		<xsl:text>Średni box office:</xsl:text>
		<xsl:value-of select="substring($spacje,0,60 - string-length('Średni box office:'))"/>
		<xsl:value-of select="concat(średnia_box_office,'&#xA;')" />
		
		<xsl:text>Średnia ocena:</xsl:text>
		<xsl:value-of select="substring($spacje,0,60 - string-length('Średnia ocena:'))"/>
		<xsl:value-of select="concat(średnia_ocena,'&#xA;')" />
		
		<xsl:text>Średnia kategoria wiekowa:</xsl:text>
		<xsl:value-of select="substring($spacje,0,60 - string-length('Średnia kategoria wiekowa:'))"/>
		<xsl:value-of select="concat(średni_wiek_od,'&#xA;&#xA;')" />
	</xsl:template>
	
	<xsl:template match="/repertuar/filmy_w_kinie/seans">
		
		<xsl:text>Film:</xsl:text>
		<xsl:value-of select="substring($spacje,0,60 - string-length('Film:'))"/>
		<xsl:value-of select="concat(film,'&#xA;')" />
		
		<xsl:text>Kino:</xsl:text>
		<xsl:value-of select="substring($spacje,0,60 - string-length('Kino:'))"/>
		<xsl:value-of select="concat(kino,'&#xA;')" />
		
		<xsl:text>Data seansu:</xsl:text>
		<xsl:value-of select="substring($spacje,0,60 - string-length('Data seansu:'))"/>
		<xsl:value-of select="concat(data_seansu,'&#xA;&#xA;')" />
		

	</xsl:template>
    
    <xsl:template match="/repertuar/autorzy/autor">
		
		<xsl:text>Imie:</xsl:text>
		<xsl:value-of select="substring($spacje,0,60 - string-length('Imie:'))"/>
		<xsl:value-of select="concat(imie,'&#xA;')" />
		
		<xsl:text>Nazwisko:</xsl:text>
		<xsl:value-of select="substring($spacje,0,60 - string-length('Nazwisko:'))"/>
		<xsl:value-of select="concat(nazwisko,'&#xA;&#xA;')" />
				

	</xsl:template>
	
	<xsl:template match="/repertuar/data_raportu">
		
		<xsl:text>Data utworzenia raportu:</xsl:text>
		<xsl:value-of select="substring($spacje,0,60 - string-length('Data utworzenia raportu:'))"/>
		<xsl:value-of select="concat(.,'&#xA;')" />
		
	</xsl:template>
    
    
    
</xsl:stylesheet>