<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema"
  xmlns:tei="http://www.tei-c.org/ns/1.0" xmlns:xlink="http://www.w3.org/1999/xlink" exclude-result-prefixes="#all" version="2.0">
  <xsl:output doctype-public="-//W3C//DTD XHTML 1.0 Transitional//EN"
    doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd" encoding="UTF-8" exclude-result-prefixes="#all" indent="no"
    media-type="text/html; charset=UTF-8" method="xhtml" omit-xml-declaration="yes"/>
  <xsl:strip-space elements="*"/>
  <xsl:template exclude-result-prefixes="#all" match="/">
    <xsl:apply-templates select="tei:TEI"/>
  </xsl:template>

  <xsl:param name="doc.title" select="//tei:title[@type='codexfull']"/>

  <xsl:template exclude-result-prefixes="#all" match="/tei:TEI">
    <html lang="en" xml:lang="en">
      <head>
        <meta content="text/html; charset=UTF-8" http-equiv="Content-Type"/>
        <title>Archive of Early Middle English :: <xsl:value-of select="$doc.title"/></title>
        <link href="http://www.emesoc.org/schema/aeme-proofing.css" media="screen" rel="stylesheet" type="text/css"/>
        <link href="http://www.emesoc.org/favicon.ico" rel="shortcut icon" type="image/x-icon"/>
        <style type="text/css">
          body{
          margin:10px 10px 10px 10px;
          padding:10px;
          width: 95%;
          font-size: larger;
          }
          #content-primary .thinspace{
          letter-spacing:1px;
          }
          
          #content-primary .touched-blue{
          border-bottom:none;
          }
          
          #content-primary .touched-green{
          border-bottom:none;
          }
          
          #content-primary .touched-red{
          border-bottom:none;
          }
          
          #content-primary .underlined{
          text-decoration:none;
          }
          
          #content-primary .underlined-overlined{
          text-decoration:none;
          text-decoration:none;
          }
          
          #content-primary .underlined-red{
          text-decoration:none;
          -moz-text-decoration-color:black;
          }
          
          #content-primary .underlined-red-overlined-red{
          text-decoration:none;
          text-decoration:none;
          -moz-text-decoration-color:black;
          }
          
          #content-primary .twous{
          border-bottom:none;
          }
          
          #content-primary .wavy-underline{
          -moz-text-decoration-style:none;
          }
        </style>
        <script type="text/javascript" src="http://code.jquery.com/jquery-1.7.1.js"></script>
        <script type="text/javascript">
          $(window).load(function() {
            $.fn.replaceCharacters = function() {
              return this.each(function() {
                var html = $(this).html();
                var re1 = new RegExp("ſ", "gi");
                var re2 = new RegExp("ꝛ", "gi");
                html = html.replace(re1, "s");
                html = html.replace(re2, "r");
                $(this).html(html);
               });
             };
             // Works only if the containing TEI element is transformed to HTML p. 
             //Possibly other HTML elements need to be added.              
             $('p').replaceCharacters();
        });
        </script>
		</head>
      <body>
        <!--<a class="jump-to-content" href="#content">Jump to Content</a>-->
        <div id="content">
          <a name="content"/>
          <div id="content-primary">
            <xsl:apply-templates select="//tei:front/*"/>
            <xsl:apply-templates select="//tei:body/*"/>
<!--            <xsl:variable name="s1" select="//tei:body/*"/>
            <xsl:value-of select="replace($s1, '&#x17F;', 's')"/> -->
<!--            <xsl:variable name="s2" select="replace($s1, '&#xA75B;', 'r')"/>
            <xsl:apply-templates select="s2"/> -->
            <xsl:apply-templates select="//tei:back/*"/>
          </div>
        </div>
      </body>
    </html>
  </xsl:template>

  <!-- first elements a-z, then templates -->

  <!-- ELEMENT: ab -->
  <xsl:template exclude-result-prefixes="#all" match="tei:ab[@type]">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: abb -->
  <xsl:template exclude-result-prefixes="#all" match="tei:abbr[@type]">
    <!--<xsl:apply-templates/>-->
  </xsl:template>
  
  <!-- ELEMENT: acquisition -->
  <xsl:template exclude-result-prefixes="#all" match="tei:acquisition">
    <p>
      <xsl:apply-templates/>
    </p>
  </xsl:template>

  <!-- ELEMENT: add -->
  <xsl:template exclude-result-prefixes="#all" match="tei:add">
    <xsl:text>&#x2038;</xsl:text>
    <xsl:apply-templates/>
    <xsl:text>&#x2038;</xsl:text>
  </xsl:template>

  <!-- ELEMENT: addSpan -->
  <xsl:template exclude-result-prefixes="#all" match="tei:addSpan">
    <xsl:text> &#x2038;</xsl:text>
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: additional -->
  <xsl:template exclude-result-prefixes="#all" match="tei:additional">
    <div>
      <h3>additional</h3>
      <xsl:apply-templates/>
    </div>
  </xsl:template>

  <!-- ELEMENT: am -->
  <xsl:template exclude-result-prefixes="#all" match="tei:am">
    <!--<span class="am">
      <xsl:apply-templates/>
    </span>-->
  </xsl:template>

  <!-- ELEMENT: anchor -->
  <xsl:template exclude-result-prefixes="#all" match="tei:anchor">
    <xsl:choose>
      <xsl:when test="@type='addSpan'">
        <xsl:apply-templates/>
        <xsl:text>&#x2038; </xsl:text>
      </xsl:when>
      <xsl:when test="@type='delSpan'">
        <xsl:text> [DELSPAN ENDS] </xsl:text>
      </xsl:when>
      <xsl:otherwise>
        <xsl:apply-templates/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <!-- ELEMENT: author -->
  <xsl:template exclude-result-prefixes="#all" match="tei:author">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: back -->
  <xsl:template exclude-result-prefixes="#all" match="tei:back">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: bibl -->
  <xsl:template exclude-result-prefixes="#all" match="tei:bibl">
    <div class="hangbib1">
      <xsl:apply-templates/>
    </div>
  </xsl:template>

  <!-- ELEMENT: body -->
  <xsl:template exclude-result-prefixes="#all" match="tei:body">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: cb -->
  <xsl:template exclude-result-prefixes="#all" match="tei:cb">
    <span style="display:none;">
      <xsl:text> [</xsl:text>
      <xsl:value-of select="@n"/>
      <xsl:text>] </xsl:text>
    </span>
  </xsl:template>

  <!-- ELEMENT: change -->
  <xsl:template exclude-result-prefixes="#all" match="tei:change">
    <li>
      <xsl:value-of select="@when"/>
      <xsl:text>, </xsl:text>
      <xsl:value-of select="@who"/>
      <xsl:text>: </xsl:text>
      <xsl:apply-templates/>
    </li>
  </xsl:template>

  <!-- ELEMENT: choice -->
  <xsl:template exclude-result-prefixes="#all" match="tei:choice">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: classDecl -->
  <xsl:template exclude-result-prefixes="#all" match="tei:classDecl">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: collection -->
  <xsl:template exclude-result-prefixes="#all" match="tei:collection">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: corr -->
  <xsl:template exclude-result-prefixes="#all" match="tei:corr">
    <xsl:text>[</xsl:text>
    <xsl:apply-templates/>
    <xsl:text>]</xsl:text>
  </xsl:template>

  <!-- ELEMENT: damage -->
  <xsl:template exclude-result-prefixes="#all" match="tei:damage">
    <span style="color: purple">
      <xsl:text>[</xsl:text>
      <xsl:apply-templates/>
      <xsl:text>]</xsl:text>
    </span>
  </xsl:template>

  <!-- ELEMENT: date -->
  <xsl:template exclude-result-prefixes="#all" match="tei:date">
    <xsl:choose>
      <xsl:when test="parent::publicationStmt">
        <p>
          <xsl:apply-templates/>
        </p>
      </xsl:when>
      <xsl:otherwise>
        <xsl:apply-templates/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <!-- ELEMENT: decoDesc -->
  <xsl:template exclude-result-prefixes="#all" match="tei:decoDesc">
    <div>
      <h3>decoDesc</h3>
      <xsl:apply-templates/>
    </div>
  </xsl:template>

  <!-- ELEMENT: del -->
  <xsl:template exclude-result-prefixes="#all" match="tei:del">
    <!--<xsl:choose>
      <xsl:when test="parent::del">
        <span class="doubledel">
          <xsl:apply-templates/>
        </span>
      </xsl:when>
      <xsl:otherwise>
        <span class="del">
          <xsl:apply-templates/>
        </span>
      </xsl:otherwise>
    </xsl:choose>-->
  </xsl:template>

  <!-- ELEMENT: delSpan -->
  <xsl:template exclude-result-prefixes="#all" match="tei:delSpan">
    <xsl:text> [DELSPAN BEGINS] </xsl:text>
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: div1 -->
  <xsl:template exclude-result-prefixes="#all" match="tei:div1">
    <br/>
    <xsl:choose>
      <xsl:when test="@xml:id">
        <span class="proofID">
          <xsl:text>[</xsl:text>
          <xsl:value-of select="@xml:id"/>
          <xsl:text>] </xsl:text>
        </span>
        <xsl:apply-templates/>
      </xsl:when>
      <xsl:otherwise>
        <span style="display:none;">
          <xsl:text>no ID </xsl:text>
        </span>
        <xsl:apply-templates/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <!-- ELEMENT: div2 -->
  <xsl:template exclude-result-prefixes="#all" match="tei:div2">
    <xsl:choose>
      <xsl:when test="@xml:id">
        <span class="proofID">
          <xsl:text>[</xsl:text>
          <xsl:value-of select="@xml:id"/>
          <xsl:text>] </xsl:text>
        </span>
        <xsl:apply-templates/>
      </xsl:when>
      <xsl:otherwise>
        <span class="proofID">
          <xsl:text>no ID </xsl:text>
        </span>
        <xsl:apply-templates/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <!-- ELEMENT: div3 -->
  <xsl:template exclude-result-prefixes="#all" match="tei:div3">
    <xsl:choose>
      <xsl:when test="@xml:id">
        <span class="proofID">
          <xsl:text>[</xsl:text>
          <xsl:value-of select="@xml:id"/>
          <xsl:text>] </xsl:text>
        </span>
        <xsl:apply-templates/>
      </xsl:when>
      <xsl:otherwise>
        <span class="proofID">
          <xsl:text>no ID </xsl:text>
        </span>
        <xsl:apply-templates/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <!-- ELEMENT: edition -->
  <xsl:template exclude-result-prefixes="#all" match="tei:edition">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: encodingDesc -->
  <xsl:template exclude-result-prefixes="#all" match="tei:encodingDesc">
    <div>
      <h3>encodingDesc</h3>
      <xsl:apply-templates/>
    </div>
  </xsl:template>

  <!-- ELEMENT: ex -->
  <xsl:template exclude-result-prefixes="#all" match="tei:ex">
    <span>
      <xsl:apply-templates/>
    </span>
  </xsl:template>

  <!-- ELEMENT: facsimile -->
  <xsl:template exclude-result-prefixes="#all" match="tei:facsimile">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: fileDesc -->
  <xsl:template exclude-result-prefixes="#all" match="tei:fileDesc">
    <div>
      <h3>fileDesc</h3>
      <xsl:apply-templates/>
    </div>
  </xsl:template>

  <!-- ELEMENT: front -->
  <xsl:template exclude-result-prefixes="#all" match="tei:front">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: fw -->
  <xsl:template exclude-result-prefixes="#all" match="tei:fw">
    <div style="display:none;">
      <xsl:text>[</xsl:text>
      <xsl:apply-templates/>
      <xsl:text>]</xsl:text>
    </div>
  </xsl:template>

  <!-- ELEMENT: gap -->
  <xsl:template exclude-result-prefixes="#all" match="tei:gap">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: gb -->
  <xsl:template exclude-result-prefixes="#all" match="tei:gb">
    <span class="proofID">
      <xsl:text> [</xsl:text>
      <xsl:value-of select="@n"/>
      <xsl:text>] </xsl:text>
    </span>
  </xsl:template>

  <!-- ELEMENT: hand -->
  <xsl:template exclude-result-prefixes="#all" match="tei:hand">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: handDesc -->
  <xsl:template exclude-result-prefixes="#all" match="tei:handDesc">
    <div>
      <h3><xsl:value-of select="@hands"/> hands</h3>
      <xsl:apply-templates/>
    </div>
  </xsl:template>

  <!-- ELEMENT: handNote -->
  <xsl:template exclude-result-prefixes="#all" match="tei:handNote">
    <p>
      <xsl:value-of select="@n"/>
      <xsl:text> (</xsl:text>
      <xsl:value-of select="@scope"/>
      <xsl:text>). </xsl:text>
      <xsl:apply-templates/>
    </p>
  </xsl:template>

  <!-- ELEMENT: handShift -->
  <xsl:template exclude-result-prefixes="#all" match="tei:handShift">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: hi -->
  <xsl:template exclude-result-prefixes="#all" match="tei:hi">
    <span>
      <xsl:call-template name="align"/>
    </span>
  </xsl:template>

  <!-- ELEMENT: history -->
  <xsl:template exclude-result-prefixes="#all" match="tei:history">
    <div>
      <h3>history</h3>
      <xsl:apply-templates/>
    </div>
  </xsl:template>

  <!-- ELEMENT: idno -->
  <xsl:template exclude-result-prefixes="#all" match="tei:idno">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: keywords -->
  <xsl:template exclude-result-prefixes="#all" match="tei:keywords">
    <p>
      <span class="proofID">
        <xsl:value-of select="@scheme"/>
      </span>
      <xsl:apply-templates/>
    </p>
  </xsl:template>

  <!-- ELEMENT: l -->
  <xsl:template exclude-result-prefixes="#all" match="tei:l">
    <xsl:choose>
      <xsl:when test="@rend">
        <p>
          <xsl:attribute name="title">
            <xsl:value-of select="@xml:id"/>
          </xsl:attribute>
          <xsl:attribute name="class">
            <xsl:value-of select="@rhyme"/>
          </xsl:attribute>
          <xsl:call-template name="align"/>
        </p>
      </xsl:when>
      <xsl:otherwise>
        <p>
          <xsl:attribute name="title">
            <xsl:value-of select="@xml:id"/>
          </xsl:attribute>
          <xsl:attribute name="class">
            <xsl:value-of select="@rhyme"/>
          </xsl:attribute>
          <xsl:apply-templates/>
        </p>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <!-- ELEMENT: lb -->
  <xsl:template exclude-result-prefixes="#all" match="tei:lb">
    <xsl:choose>
      <xsl:when test="parent::tei:l"> </xsl:when>
      <xsl:otherwise>
        <br/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <!-- ELEMENT: lg -->
  <xsl:template exclude-result-prefixes="#all" match="tei:lg">
    <div class="stanza">
      <xsl:apply-templates/>
    </div>
  </xsl:template>

  <!-- ELEMENT: line -->
  <xsl:template exclude-result-prefixes="#all" match="tei:line">
    <p>
      <xsl:apply-templates/>
    </p>
  </xsl:template>

  <!-- ELEMENT: listBibl -->
  <xsl:template exclude-result-prefixes="#all" match="tei:listBibl">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: locus -->
  <xsl:template exclude-result-prefixes="#all" match="tei:locus">
    <xsl:choose>
      <xsl:when test="ancestor::msContents">
        <span class="locus">
          <xsl:apply-templates/>
        </span>
        <br/>
      </xsl:when>
      <xsl:otherwise>
        <span class="locus">
          <xsl:apply-templates/>
        </span>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <!-- ELEMENT: msContents -->
  <xsl:template exclude-result-prefixes="#all" match="tei:msContents">
    <div>
      <p style="text-indent:2em">msContents</p>
      <xsl:apply-templates/>
    </div>
  </xsl:template>

  <!-- ELEMENT: msDesc -->
  <xsl:template exclude-result-prefixes="#all" match="tei:msDesc">
    <p style="text-indent:1em">msDesc</p>
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: msIdentifier -->
  <xsl:template exclude-result-prefixes="#all" match="tei:msIdentifier">
    <xsl:choose>
      <xsl:when test="parent::msDesc">
        <p style="text-indent:3em">msIdentifier</p>
        <p>
          <xsl:apply-templates/>
        </p>
      </xsl:when>
      <xsl:otherwise>
        <span class="msID">
          <xsl:apply-templates/>
        </span>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <!-- ELEMENT: msItem -->
  <xsl:template exclude-result-prefixes="#all" match="tei:msItem">
    <p>
      <strong>
        <xsl:value-of select="@n"/>
      </strong>
      <xsl:text>. </xsl:text>
      <xsl:apply-templates/>
    </p>
  </xsl:template>

  <!-- ELEMENT: name -->
  <xsl:template exclude-result-prefixes="#all" match="tei:name">
    <NAME>
      <xsl:apply-templates/>
    </NAME>
  </xsl:template>

  <!-- ELEMENT: note -->
  <xsl:template exclude-result-prefixes="#all" match="tei:note">
<!--    <xsl:choose>
      <xsl:when test="@resp='#bioHO001'">
        <span>
          <xsl:text>[</xsl:text>
          <xsl:apply-templates/>
          <xsl:text>]</xsl:text>
        </span>
      </xsl:when>
      <xsl:otherwise>
        <xsl:text>[</xsl:text>
        <span>
          <xsl:apply-templates/>
        </span>
        <xsl:text>]</xsl:text>
      </xsl:otherwise>
    </xsl:choose> -->
  </xsl:template>

  <!-- ELEMENT: orig -->
  <xsl:template exclude-result-prefixes="#all" match="tei:orig">
    <!--<span style="display:none;">
      <xsl:apply-templates/>
    </span>-->
  </xsl:template>

  <!-- ELEMENT: origin -->
  <xsl:template exclude-result-prefixes="#all" match="tei:origin">
    <p>origin:</p>
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: p -->
  <xsl:template exclude-result-prefixes="#all" match="tei:p">
    <p>
      <xsl:apply-templates/>
    </p>
  </xsl:template>

  <!-- ELEMENT: pb -->
  <xsl:template exclude-result-prefixes="#all" match="tei:pb">
    <span style="display:none;">
      <xsl:text> [</xsl:text>
      <xsl:value-of select="@n"/>
      <xsl:text>] </xsl:text>
    </span>
  </xsl:template>

  <!-- ELEMENT: physDesc -->
  <xsl:template exclude-result-prefixes="#all" match="tei:physDesc">
    <div>
      <h3>physDesc</h3>
      <xsl:apply-templates/>
    </div>
  </xsl:template>

  <!-- ELEMENT: profileDesc -->
  <xsl:template exclude-result-prefixes="#all" match="tei:profileDesc">
    <div>
      <h3>profileDesc</h3>
      <xsl:apply-templates/>
    </div>
  </xsl:template>

  <!-- ELEMENT: provenance -->
  <xsl:template exclude-result-prefixes="#all" match="tei:provenance">
    <br/>
    <p>provenance:</p>
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: publicationStmt -->
  <xsl:template exclude-result-prefixes="#all" match="tei:publicationStmt">
    <div>
      <h3>publicationStmt</h3>
      <xsl:apply-templates/>
    </div>
  </xsl:template>

  <!-- ELEMENT: publisher -->
  <xsl:template exclude-result-prefixes="#all" match="tei:publisher">
    <p>
      <xsl:apply-templates/>
    </p>
  </xsl:template>

  <!-- ELEMENT: ref -->
  <xsl:template exclude-result-prefixes="#all" match="tei:ref">
    <xsl:choose>
      <xsl:when test="@target">
        <span class="proofID">
          <xsl:text> [</xsl:text>
          <xsl:value-of select="@type"/>
          <xsl:text>] </xsl:text>
        </span>
        <a>
          <xsl:attribute name="href">
            <xsl:value-of select="@target"/>
          </xsl:attribute>
          <xsl:apply-templates/>
        </a>
      </xsl:when>
      <xsl:otherwise>
        <xsl:apply-templates/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <!-- ELEMENT: reg -->
  <xsl:template exclude-result-prefixes="#all" match="tei:reg">
    <span>
      <xsl:text> </xsl:text>
      <xsl:apply-templates/>
      <xsl:text> </xsl:text>
    </span>
  </xsl:template>

  <!-- ELEMENT: repository -->
  <xsl:template exclude-result-prefixes="#all" match="tei:repository">
    <xsl:apply-templates/>
    <xsl:text>, </xsl:text>
  </xsl:template>

  <!-- ELEMENT: resp -->
  <xsl:template exclude-result-prefixes="#all" match="tei:resp">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: respStmt -->
  <xsl:template exclude-result-prefixes="#all" match="tei:respStmt">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: revisionDesc -->
  <xsl:template exclude-result-prefixes="#all" match="tei:revisionDesc">
    <div>
      <h3>revisionDesc</h3>
      <ul>
        <xsl:apply-templates/>
      </ul>
    </div>
  </xsl:template>

  <!-- ELEMENT: scriptDesc -->
  <xsl:template exclude-result-prefixes="#all" match="tei:scriptDesc">
    <div>
      <h3>scriptDesc</h3>
      <xsl:apply-templates/>
    </div>
  </xsl:template>

  <!-- ELEMENT: settlement -->
  <xsl:template exclude-result-prefixes="#all" match="tei:settlement">
    <xsl:apply-templates/>
    <xsl:text>, </xsl:text>
  </xsl:template>

  <!-- ELEMENT: sg -->
  <xsl:template exclude-result-prefixes="#all" match="tei:sg">
    <xsl:choose>
      <xsl:when test="@type='ln'"></xsl:when>
      <xsl:when test="text()=' '">
        <span class="sg">&#xA0;</span>
      </xsl:when>
      <xsl:otherwise>
        <span class="sg">
          <xsl:apply-templates/>
        </span>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <!-- ELEMENT: sic -->
  <xsl:template exclude-result-prefixes="#all" match="tei:sic">
    <!--<span style="display:none;">
      <xsl:apply-templates/>
    </span>-->
  </xsl:template>
  
  <!-- ELEMENT: sourceDesc -->
  <xsl:template exclude-result-prefixes="#all" match="tei:sourceDesc">
    <div>
      <h3>sourceDesc</h3>
      <xsl:apply-templates/>
    </div>
  </xsl:template>

  <!-- ELEMENT: space -->
  <xsl:template exclude-result-prefixes="#all" match="tei:space">
    <xsl:choose>
      <xsl:when test="@quantity">
        <xsl:for-each select="1 to @quantity">
          <span class="normal">
            <xsl:text>&#x2003;</xsl:text>
          </span>
        </xsl:for-each>
      </xsl:when>
      <xsl:otherwise>
        <xsl:text>&#xA0;</xsl:text>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <!-- ELEMENT: summary -->
  <xsl:template exclude-result-prefixes="#all" match="tei:summary">
    <p>
      <xsl:apply-templates/>
    </p>
  </xsl:template>

  <!-- ELEMENT: supplied -->
  <xsl:template exclude-result-prefixes="#all" match="tei:supplied">
    <span style="color: purple">
      <xsl:text>[</xsl:text>
      <xsl:apply-templates/>
      <xsl:text>]</xsl:text>
    </span>
  </xsl:template>

  <!-- ELEMENT: surface -->
  <xsl:template exclude-result-prefixes="#all" match="tei:surface">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: taxonomy -->
  <xsl:template exclude-result-prefixes="#all" match="tei:taxonomy">
    <p>
      <xsl:apply-templates/>
    </p>
  </xsl:template>

  <!-- ELEMENT: teiHeader -->
  <xsl:template exclude-result-prefixes="#all" match="tei:teiHeader">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: term -->
  <xsl:template exclude-result-prefixes="#all" match="tei:term">
    <span class="proofID">
      <xsl:apply-templates/>
    </span>
  </xsl:template>

  <!-- ELEMENT: textClass -->
  <xsl:template exclude-result-prefixes="#all" match="tei:textClass">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: title -->
  <xsl:template exclude-result-prefixes="#all" match="tei:title">
    <xsl:choose>
      <xsl:when test="@type='codexfull'">
        <h4>
          <xsl:apply-templates/>
        </h4>
      </xsl:when>
      <xsl:when test="parent::tei:bibl">
        <span class="italic">
          <xsl:apply-templates/>
        </span>
      </xsl:when>
      <xsl:otherwise>
        <xsl:apply-templates/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <!-- ELEMENT: titleStmt -->
  <xsl:template exclude-result-prefixes="#all" match="tei:titleStmt">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- ELEMENT: unclear -->
  <xsl:template exclude-result-prefixes="#all" match="tei:unclear">
    <span style="color: purple">
      <xsl:text>[</xsl:text>
      <xsl:apply-templates/>
      <xsl:text>]</xsl:text>
    </span>
  </xsl:template>

  <!-- ELEMENT: zone -->
  <xsl:template exclude-result-prefixes="#all" match="tei:zone">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- TEMPLATE: align -->
  <xsl:template exclude-result-prefixes="#all" name="align">
    <xsl:choose>
      <xsl:when test="matches(@rend, '^float[a-z]+')">
        <div>
          <xsl:attribute name="class">
            <xsl:value-of select="@rend"/>
          </xsl:attribute>
          <xsl:apply-templates/>
        </div>
      </xsl:when>
      <xsl:when test="matches(@rend, '^text-indent:\d+')">
        <xsl:attribute name="style">
          <xsl:value-of select="concat(@rend,'em')"/>
        </xsl:attribute>
        <xsl:apply-templates/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:attribute name="class">
          <xsl:value-of select="@rend"/>
        </xsl:attribute>
        <xsl:apply-templates/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

</xsl:stylesheet>
