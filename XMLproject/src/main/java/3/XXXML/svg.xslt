<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
		xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
		xmlns="http://www.w3.org/2000/svg"
		>
  <xsl:output
      method="xml"
      indent="yes"
      standalone="no"
      doctype-public="-//W3C//DTD SVG 1.1//EN"
      doctype-system="http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd"
      media-type="image/svg" />

  <xsl:template match="/">
    <svg xmlns="http://www.w3.org/2000/svg" width="1000" height="900" >
      
            <script type="text/ecmascript"> 
                <![CDATA[
                    function onMouseOverWykres(evt) 
                    {
                        var liczby = document.getElementsByClassName("liczba_gatunku");
                        for (i = 0; i < liczby.length; ++i) 
                        {
                          liczby[i].setAttribute("visibility", "visible");
                        }
                    }
                    function onMouseOutWykres(evt) 
                    {
                        var liczby = document.getElementsByClassName("liczba_gatunku");
                        for (i = 0; i < liczby.length; ++i) 
                        {
                          liczby[i].setAttribute("visibility", "hidden");
                        }
                    }
                    function onClickAutorzy(evt)
                    {
                        var autorzy = document.getElementById("autorzy");
                        var visibility = autorzy.getAttribute("visibility");
                        if(visibility==="visible")
                        {
                            autorzy.setAttribute("visibility", "hidden");
                        }
                        else
                        {
                            autorzy.setAttribute("visibility", "visible");
                        }
                    }
            ]]>
            </script>      
      
      <rect x="0" y="0" width="1000" height="900" fill="DarkGrey"/>
      <text x="80" y="30" font-size="24" fill="black" font-weight="bold">Liczba filmów danego gatunku</text>
      <g id="poleWykresu" onmouseover="onMouseOverWykres(evt)" onmouseout="onMouseOutWykres(evt)">
        <rect x="25" y="50" width="950" height="765" fill="Grey" stroke="DimGrey"/>
        <xsl:apply-templates select="/repertuar/statystyki/gatunki/gatunek"/>
      </g>
      <text x="25" y="800" font-size="24" fill="black" font-weight="bold" onclick="onClickAutorzy(evt)">Autorzy</text>
      <g id="autorzy" visibility="hidden">
        <xsl:apply-templates select="/repertuar/autorzy/autor"/>
      </g> 
    </svg>
  </xsl:template>

  <xsl:template match="/repertuar/statystyki/gatunki/gatunek">
      <xsl:variable name="postitionX" select="position()*70 + (position() - 1)*50"/>
      <xsl:variable name="height" select="liczba_gatunku * 36"/>
      <xsl:variable name="positionY" select="40 + (500 - $height)"/>
      <rect x="{$postitionX}" width="50" fill="white" stroke="black">
        <animate attributeName="height" from="0" to="{$height}" dur="5s" fill="freeze"/>
        <animate attributeName="y" from="580" to="{$positionY}" dur="5s" fill="freeze"/>
      </rect>
      <text x="{$postitionX}" y="605" font-size="16" fill="black" font-weight="bold">
        <xsl:value-of select="nazwa"/>
      </text>
      <text class="liczba_gatunku" visibility="hidden" x="{$postitionX + 20}" y="{$positionY - 5}" font-size="16" fill="black" font-weight="bold">
        <xsl:value-of select="liczba_gatunku"/>
      </text>
  </xsl:template>

  <xsl:template match="/repertuar/autorzy/autor">
    <xsl:variable name="positionY" select="760 + position()*20"/>
    <text x="150" y="{$positionY}" font-size="24" fill="black" font-style="italic">
      <xsl:value-of select="concat(imie,' ',nazwisko)"/>
    </text>
  </xsl:template>
</xsl:stylesheet>