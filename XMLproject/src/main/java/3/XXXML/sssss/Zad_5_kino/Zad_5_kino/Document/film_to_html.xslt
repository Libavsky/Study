<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns="http://www.w3.org/1999/xhtml">
  <xsl:output method="xml" indent="yes" version="1.0" encoding="utf-8" doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"/>

  <xsl:template match="/">
    <html>
        <head>
          <title>Dane z xml</title>
        </head>
      <body style="background-color: grey;">
        
        <div>
          <h1 id="repertuar">Statystki filmów po gatunkach</h1>
          <a href="#stats">Statystyki</a>
          <a href="#filmy_w_kinie">Seanse w kinach</a>
          <a href="#autorzy">Autorzy</a>
        </div>
        <div class="stats">
          <h3 id="stats">Gatunki filmowe</h3>
          <table border="1" style="background-color: red;">
            <tr>
              <th align="center">Gatunek</th>
              <th align="center">Liczebność gatunku</th>
              <th align="center">Średni box office</th>
              <th align="center">Średnia ocena</th>
              <th align="center">Średni wiek najmłodszego widza</th>
            </tr>
            <xsl:for-each select="/repertuar/statystyki/gatunki/gatunek">
              <tr>
                <td align="center">
                  <xsl:value-of select="nazwa"/>
                </td>
                <td align="center">
                  <xsl:value-of select="liczba_gatunku"/>
                </td>
                <td align="center">
                  <xsl:value-of select="średnia_box_office"/>
                </td>
                <td align="center">
                  <xsl:value-of select="średnia_ocena"/>
                </td>
                <td align="center">
                  <xsl:value-of select="średni_wiek_od"/>
                </td>
              </tr>
            </xsl:for-each>
          </table>
          <a href="#repertuar">Do góry</a>
        </div>

        <div class="filmy_w_kinie">
          <h3 id="filmy_w_kinie">Seanse filmów w kinach</h3>
          <table border="1" style="background-color: green;">
            <tr>
              <th>Film</th>
              <th>Kino</th>
              <th>Data seansu</th>
            </tr>
            <xsl:for-each select="/repertuar/filmy_w_kinie/seans">
              <tr>
                <td>
                  <xsl:value-of select="film"/>
                </td>
                <td>
                  <xsl:value-of select="kino"/>
                </td>
                <td>
                  <xsl:value-of select="data_seansu"/>
                </td>
              </tr>
            </xsl:for-each>
          </table>
          <a href="#repertuar">Do góry</a>
        </div>

        <div class="autorzy">
          <h3 id="autorzy">Autorzy</h3>
          <xsl:for-each select="/repertuar/autorzy/autor">
            <p>
              <xsl:value-of select="."/>
            </p>
          </xsl:for-each>
          <a href="#repertuar">Do góry</a>
        </div>
        <p>
          Raport wygenerowano: 
          <xsl:value-of select="/repertuar/data_raportu"/>
        </p>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
