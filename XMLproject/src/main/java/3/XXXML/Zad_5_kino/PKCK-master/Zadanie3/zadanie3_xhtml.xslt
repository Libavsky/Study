<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns="http://www.w3.org/1999/xhtml">
  <xsl:output method="xml" indent="yes" version="1.0" encoding="utf-8" doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"/>

  <xsl:template match="/">
    <html>
        <head>
          <title>Raport</title>
        </head>
      <body>
        
        <div>
          <h1 id="wypozyczalnia">Wypożyczalnia</h1>
          <a href="#stats">Statystyki</a>
          <a href="#wypozyczenia">Wypożyczenia</a>
          <a href="#autorzy">Autorzy</a>
        </div>
        <div class="stats">
          <h3 id="stats">Statystki Miast</h3>
          <table>
            <tr>
              <th>Miasto</th>
              <th>Liczba samochodów</th>
              <th>Średnia cena wypożyczenia</th>
              <th>Średni przebieg</th>
              <th>Przeciętny rocznik</th>
            </tr>
            <xsl:for-each select="/wypożyczalnia/statystyki/miasta/miasto">
              <tr>
                <td>
                  <xsl:value-of select="nazwa"/>
                </td>
                <td>
                  <xsl:value-of select="liczba_samochodow"/>
                </td>
                <td>
                  <xsl:value-of select="średnia_cena_wypożyczenia"/>
                </td>
                <td>
                  <xsl:value-of select="średni_przebieg"/>
                </td>
                <td>
                  <xsl:value-of select="średni_wiek"/>
                </td>
              </tr>
            </xsl:for-each>
          </table>
          <a href="#wypozyczalnia">Do góry</a>
        </div>

        <div class="wypożyczenia">
          <h3 id="wypozyczenia">Aktualne wypożyczenia</h3>
          <table>
            <tr>
              <th>Samochód</th>
              <th>Pracownik</th>
              <th>Data Wypożyczenia</th>
              <th>Data Zwrotu</th>
              <th>Wypożyczający</th>
            </tr>
            <xsl:for-each select="/wypożyczalnia/wypożyczenia/wypożyczenie">
              <tr>
                <td>
                  <xsl:value-of select="samochod"/>
                </td>
                <td>
                  <xsl:value-of select="pracownik"/>
                </td>
                <td>
                  <xsl:value-of select="data_wypożyczenia"/>
                </td>
                <td>
                  <xsl:value-of select="data_zwrotu"/>
                </td>
                <td>
                  <xsl:value-of select="wypożyczający"/>
                </td>
              </tr>
            </xsl:for-each>
          </table>
          <a href="#wypozyczalnia">Do góry</a>
        </div>

        <div class="autorzy">
          <h3 id="autorzy">Autorzy</h3>
          <xsl:for-each select="/wypożyczalnia/autorzy/autor">
            <p>
              <xsl:value-of select="."/>
            </p>
          </xsl:for-each>
          <a href="#wypozyczalnia">Do góry</a>
        </div>
        <p>
          Raport wygenerowano: 
          <xsl:value-of select="/wypożyczalnia/data_raportu"/>
        </p>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
