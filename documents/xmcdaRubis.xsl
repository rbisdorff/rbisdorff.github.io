<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xmcda="http://www.decision-deck.org/UMCDA-ML-1.0">
  
<!-- 
XMCDA 1.0 Rubis XSLT tranformation to HTML, RB 2008
$Revision: 1.2 $
The ressource comes with ABSOLUTELY NO WARRANTY 
to the extent permitted by the applicable law.
This is free software, and you are welcome to 
redistribute it if it remains free software. 
Copyright (C) 2008 DECISION DECK Project
-->


 <!-- Main start of the transform -->
  
<xsl:template match="/" >
 <html>
  <head><title>D2-Decision-Deck UMCDA-ML-1.0 application</title></head>
  <body>
    <h1><font color="#0000bb">D2-Decision-Deck UMCDA-ML application</font></h1>

    <xsl:apply-templates  select="xmcda:XMCDA" />
    <br/>
    <h2>Content</h2>
    <ul>
      <li><a href="#choice">Choice Recommendation</a></li>
      <li><a href="#graph">Outranking digraph</a></li>
      <li><a href="#actions">Potential decision actions</a></li>
      <li><a href="#performance">Performance table</a></li>
      <li><a href="#criteria">Family of criteria</a></li>
      <li><a href="#outranking">Outranking relation</a></li>	
      <li><a href="#vetos">Veto situations</a></li>	
      <li><a href="#notice">Notice</a></li>	
    </ul>
    <hr />
    <h2><a name="notice"><font color="#bb0000">Notice</font></a></h2>
    <p>Bisdorff R., Meyer P., Roubens M., <b>Rubis</b>: A new methodology for the choice decision problem. 4OR, 
      <em>A Quarterly Journal of Operational Research</em>, Springer (2008), forthcoming.
    <a href="http://sma.uni.lu/bisdorff/documents/HyperKernels.pdf">PDF preprint version</a>.</p>
   <p>Online documentation: <a href="http://sma.uni.lu/d2cms">Decision Deck Project</a><br/>
          <b>Default XSL Transformation to HTML</b><br/>
          <a href="http://ernst-schroeder.uni.lu/UMCDA-ML-1.0/doc/umcda-ml-1.0.xsd.html">XMCDA 1.0 Schema</a> P. Meyer and R.Bisdorff 2008 $Revision: 1.2 $
          Copyright (C) 2008 DECISION DECK Project</p>
   </body>
  </html>
</xsl:template>
 

 <!--  generic description layout: must fit all element description !!! -->
  
  <xsl:template match="description[type='root']">
     <xsl:apply-templates />
    <h3>Content</h3>
    <ul>
      <li><a href="#choice">Choice Recommendation</a></li>
      <li><a href="#graph">Outranking digraph</a></li>
      <li><a href="#actions">Potential decision actions</a></li>
      <li><a href="#performance">Performance table</a></li>
      <li><a href="#criteria">Family of criteria</a></li>
      <li><a href="#outranking">Outranking relation</a></li>	
      <li><a href="#vetos">Veto situations</a></li>	
      <li><a href="#notice">Notice</a></li>	
    </ul>
  </xsl:template>
  
  <xsl:template match="description" mode="bipolar">
     <xsl:apply-templates select="."/>
  </xsl:template>
 
  <xsl:template match="description" mode="veto">
     <xsl:apply-templates select="."/>
  </xsl:template>
  
  <xsl:template match="title">
    <h2><font color="#bb0000"><xsl:value-of select="text()"/></font></h2>
  </xsl:template>
  
  <xsl:template match="subTitle">
    <h3><font color="#0000bb"><xsl:value-of select="text()"/></font></h3>
  </xsl:template>
  
  <xsl:template match="id">
    Identifier: <font color="#0000bb"><xsl:value-of select="text()" /></font><br/>
  </xsl:template>
  
  <xsl:template match="approach">
    Approach: <font color="#0000bb"><xsl:value-of select="text()" /></font><br/>
  </xsl:template>
  
  <xsl:template match="methodology">
    Methodology: <font color="#0000bb"><xsl:value-of select="text()" /></font><br/>
  </xsl:template>
  
  <xsl:template match="problematique">
    Problematique: <font color="#0000bb"><xsl:value-of select="text()" /></font><br/>
  </xsl:template>
  
  <xsl:template match="shortName">
    Short name: <xsl:value-of select="text()" /><br/>
  </xsl:template>
  
  <xsl:template match="name">
    Name: <font color="#0000bb"><xsl:value-of select="text()" /></font><br/>
  </xsl:template>
  
  <xsl:template match="comment">
    Comment: <em><xsl:value-of select="text()" /></em><br/>
  </xsl:template>
  
  <xsl:template match="author">
    Author: <xsl:apply-templates/><br/>
  </xsl:template>
  
  <xsl:template match="user">
    User: <xsl:apply-templates/><br/>
  </xsl:template>
  
  <xsl:template match="type">
 <!--    <tr><th align="left">Type: </th><td><xsl:apply-templates/></td></tr> -->
  </xsl:template>
  
  <xsl:template match="version">
    Version: <xsl:apply-templates/><br/>
  </xsl:template>
  
  <xsl:template match="abstract">
    Abstract: <em><xsl:value-of select="text()" /></em><br/>
  </xsl:template>
  
  <xsl:template match="keywords">
    Key Words: <xsl:value-of select="text()" /><br/>
  </xsl:template>
  
  <xsl:template match="bibliography">
    Bibliography : <xsl:value-of select="text()" /><br/>
  </xsl:template>
  
  <xsl:template match="dateTime">
    Date: <xsl:value-of select="text()" /><br/>
  </xsl:template>
  
<!-- Method Data -->
<xsl:template match="methodData">
   <xsl:apply-templates/>
</xsl:template>
 
 <xsl:template match="parameters">
   <br/>
 <table cellpadding="1" border="1">
   <tr><th bgcolor="#9acd32">Parameter</th><th bgcolor="#9acd32">Value</th></tr>
   <xsl:apply-templates/>
   </table>
</xsl:template>
 
 <xsl:template match="parameter">
   <tr><td bgcolor="#FFF79B"><xsl:value-of select="name"/></td><td><xsl:value-of select="value"/></td></tr>
</xsl:template>

<xsl:template match="alternatives">
  <a name="alternatives"/>
   <xsl:apply-templates  select="description"/>
   <table border="1">
      <tr bgcolor="#9acd32">
        <th>#</th>
        <th>Identifyer</th>
        <th>Name</th>
        <th>Comment</th>
      </tr>
   <xsl:for-each select="alternative">
       <tr><td><xsl:number format="1"/></td>
         <th bgcolor="#FFF79B"><xsl:value-of select="@id"/></th>
           <td><xsl:value-of select="description/name"/></td>
           <td><xsl:value-of select="description/comment"/></td>
	</tr>
   </xsl:for-each>
   </table>
</xsl:template>
   
  <xsl:template match="valuedBinaryRelation">
    <h2><a name="graph"><font color="#bb0000">Significantly Concordant Outranking Graph</font></a></h2>
    <p>(<i><b> Black arrows</b> indicate outranking situations supported by a criteria coalition 
      of positive significance, i.e. gathering more than 50&#37; of the global criteria significance weights.
      <b>Empty arrow heads</b> indicate an indeterminate outranking situation.</i>)</p>
    <xsl:variable name="tiret" select=" '-' " />
    <xsl:variable name="dot" select=" '.' " />
    <xsl:variable name="name" select ="/xmcda:XMCDA/description/id" />
    <xsl:variable name="path" select=" 'http://ernst-schroeder.uni.lu/rubisServer/Images/rubisGraph-' " />
    <xsl:variable name="extension" select=" '.png' " />	
    <div style="text-align: left;">	
      <img src="{concat($path,substring-after($name,$tiret),$extension)}"  />
    </div> 
    
    
    <a name="outranking"/>
    <xsl:choose>
      <xsl:when test="valuationDomain/valuationType='bipolar'">
        <xsl:apply-templates mode="bipolar"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:apply-templates/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
 
  <xsl:template match="valuedBinaryRelation[description/type='Vetoes']" >
         <a name="vetos" />
        <xsl:apply-templates mode="veto"/>
  </xsl:template>
  
  <xsl:template match="valuationDomain" mode="bipolar">
       <xsl:apply-templates select="description"/>
       <xsl:variable name="median" select="minimum + (maximum - minimum) div 2"></xsl:variable>
       <table cellpadding="1" border="1">
         <tr><td bgcolor="#FFF79B">Maximum</td><td bgcolor="#ddffdd" align="right"><xsl:value-of select="maximum"/></td></tr>
         <tr><td bgcolor="#FFF79B">Median</td><td bgcolor="#dddddd"  align="right"><xsl:value-of select="$median" /></td></tr>
         <tr><td bgcolor="#FFF79B">Minimum</td><td bgcolor="#ffddff"  align="right"><xsl:value-of select="minimum"/></td></tr>
       </table>
    
  </xsl:template>
   
  <xsl:template match="valuationDomain">
       <xsl:apply-templates select="description"/>
        <table cellpadding="1" border="1">
         <tr><td bgcolor="#FFF79B">Minimum</td><td align="right"><xsl:value-of select="minimum"/></td></tr>
         <tr><td bgcolor="#FFF79B">Maximum</td><td align="right"><xsl:value-of select="maximum"/></td></tr>
        </table>
  </xsl:template>
 
  <xsl:template match="arcs" mode="veto">
       <xsl:variable name="Veto" select='.' />
       <xsl:apply-templates select="description"/>
    <p>(The <b>concordance degree</b> of an outranking statement (an arc) results from the 
      difference between the significance (the sum of weights) of the coalition of criteria 
      in favour and the significance of the coalition of criteria in disfavour of this statement.)</p>
       <ol>
        <xsl:for-each select="$Veto/arc">
           <li>Veto against <b><xsl:value-of select="from/alternativeID"/> outranks
            <xsl:value-of select="to/alternativeID"/> </b> (
          <xsl:value-of select="description/comment"/>)
           <table border="1">
             <tr bgcolor="#9acd32"><th>criterion</th><th>performance difference</th><th>status</th><th>characteristic</th></tr>
             <xsl:for-each select="values">
               <tr>
                 <th bgcolor="#FFF79B" align="center"><xsl:value-of select="description/id"/></th>
                 <td align="center"><xsl:value-of select="value[description/name='performanceDifference']/real"/></td>
                 <td><xsl:value-of select="description/comment"/></td>
                 <td align="center"><xsl:value-of select="value[description/name='vetoCharacteristic']/real"/></td>
               </tr>
             </xsl:for-each>
             </table><br/>
           </li>
        </xsl:for-each>
         </ol>
  </xsl:template>
   
  <xsl:template match="arcs">
    <xsl:variable name="currentArcs" select="."/>
    <xsl:apply-templates select="description"/>

    <table border="1">
      <tr bgcolor="#9acd32">
        <th>relation</th>
        <xsl:for-each select="/xmcda:XMCDA/alternatives[description/type='alternatives']/alternative">
          <th bgcolor="#FFF79B"><xsl:value-of select="@id"/></th>
        </xsl:for-each>
      </tr>
      
      <xsl:for-each select="/xmcda:XMCDA/alternatives[description/type='alternatives']/alternative">
                   <xsl:variable name="currentRow" select='@id' />
       <tr>
        <th bgcolor="#FFF79B"><xsl:value-of select="$currentRow"/></th>
        <xsl:for-each select="/xmcda:XMCDA/alternatives[description/type='alternatives']/alternative">
          <xsl:variable name="currentColumn" select='@id' />
          <xsl:for-each select="$currentArcs/arc[from/.=$currentRow]">
            <xsl:variable name="currentArc" select="."></xsl:variable>
            <xsl:call-template name="currentValue" >
              <xsl:with-param name="currentRow" select="$currentRow" />   
              <xsl:with-param name="currentColumn" select="$currentColumn"/>                  
              <xsl:with-param name="currentArc" select="$currentArc" />
             </xsl:call-template>
           </xsl:for-each>
        </xsl:for-each>
      </tr>
      </xsl:for-each>
    </table>
  </xsl:template>
 
  <xsl:template match="arcs" mode="bipolar">
    <xsl:variable name="currentArcs" select="."/>
    <xsl:apply-templates select="description"/>
    <table border="1">
      <tr bgcolor="#9acd32">
        <th><xsl:value-of select="parent::node()/description/name"/></th>
        <xsl:for-each select="/xmcda:XMCDA/alternatives[description/type='alternatives']/alternative">
          <th bgcolor="#FFF79B"><xsl:value-of select="@id"/></th>
        </xsl:for-each>
      </tr>
      
        <xsl:variable name="Min" select="parent::node()/valuationDomain/minimum"/>
        <xsl:variable name="Max" select="parent::node()/valuationDomain/maximum"/>
        <xsl:variable name="Med" select="$Min + ($Max - $Min) div 2"/>

      
      <xsl:for-each select="/xmcda:XMCDA/alternatives[description/type='alternatives']/alternative">
        <xsl:variable name="currentRow" select='@id' />
        <tr>
          <th bgcolor="#FFF79B"><xsl:value-of select="$currentRow"/></th>
          <xsl:for-each select="/xmcda:XMCDA/alternatives[description/type='alternatives']/alternative">
            <xsl:variable name="currentColumn" select='@id' />
            <xsl:for-each select="$currentArcs/arc[from/.=$currentRow]">
              <xsl:variable name="currentArc" select="."/>
              <xsl:call-template name="currentBipolarValue" >
                <xsl:with-param name="currentRow" select="$currentRow" />   
                <xsl:with-param name="currentColumn" select="$currentColumn"/>                  
                <xsl:with-param name="currentArc" select="$currentArc" />
                  <xsl:with-param name="Med" select="$Med" /> 
              </xsl:call-template>
            </xsl:for-each>
          </xsl:for-each>
        </tr>
      </xsl:for-each>
    </table>
  </xsl:template>
  
 
  <xsl:template name="currentValue" match="arc">
    <xsl:param name="currentRow"/>
    <xsl:param name="currentColumn"/>
    <xsl:param name="currentArc"/>
    <xsl:if test="$currentArc/from/.=$currentRow">
      <xsl:if test="$currentArc/to/.=$currentColumn">
        <td align="right" ><xsl:value-of select="./value"/></td>
      </xsl:if>
    </xsl:if>
  </xsl:template>
  
  <xsl:template name="currentBipolarValue" match="arc">
    <xsl:param name="currentRow"/>
    <xsl:param name="currentColumn"/>
    <xsl:param name="currentArc"/>
      <xsl:param name="Med"/>
    <xsl:if test="$currentArc/from/.=$currentRow">
      <xsl:if test="$currentArc/to/.=$currentColumn">
        <xsl:variable name="arcValue" select="$currentArc/value"></xsl:variable>
        <xsl:choose>
          <xsl:when test="$arcValue &gt; $Med">
            <td bgcolor="#ddffdd" align="right" >
              <xsl:value-of select="$arcValue"/></td>
          </xsl:when>
          <xsl:when test="$arcValue &lt; $Med">
            <td bgcolor="#ffddff"  align="right">
              <xsl:value-of select="$arcValue"/></td>
          </xsl:when>
          <xsl:otherwise>
            <td bgcolor="#dddddd" align="right" >
              <xsl:value-of select="$arcValue"/></td>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:if>
    </xsl:if>
  </xsl:template>

<!-- presentation of the criteria -->
  
<xsl:template match="criteria">
  <a name="criteria"/>
  <xsl:apply-templates  select="description"/>
   <table border="1">
     <tr bgcolor="#9acd32">
        <th rowspan="2">#</th>
        <th rowspan="2">Identifyer</th>
        <th rowspan="2">Name</th>
        <th rowspan="2">Comment</th>
        <th rowspan="2">Weight</th>
	<th colspan="3">Scale</th>
	<th colspan="5">Thresholds</th>
     </tr>
     <tr bgcolor="#9acd32">
       <th>direction</th>
       <th>min</th>
       <th>max</th>
       <th>indifference</th>
       <th>weak preference</th>
       <th>preference</th>
       <th>weak veto</th>
       <th>veto</th>
      </tr>
     <xsl:for-each select="criterion">
       <tr>
         <td align="center"><xsl:number format="1"/></td>
         <th bgcolor="#FFF79B"><xsl:value-of select="@id"/></th>
	   <td><xsl:value-of select="description/name"/></td>
	   <td><xsl:value-of select="description/comment"/></td>        
         <td align="center"><xsl:value-of select="significance/."/></td>
	   <td align="center"><xsl:value-of select="criterionFunction/scale/quantitative/preferenceDirection"/></td>
         <td align="center"><xsl:value-of select="criterionFunction/scale/quantitative/min/."/></td>
         <td align="center"><xsl:value-of select="criterionFunction/scale/quantitative/max/."/></td>
         <td align="center"><xsl:apply-templates select="criterionFunction/thresholds/threshold[type='ind']"/></td>
         <td align="center"><xsl:apply-templates select="criterionFunction/thresholds/threshold[type='weakPreference']"/></td>
         <td align="center"><xsl:apply-templates select="criterionFunction/thresholds/threshold[type='pref']"/></td>
         <td align="center"><xsl:apply-templates select="criterionFunction/thresholds/threshold[type='weakVeto']"/></td>
         <td align="center"><xsl:apply-templates select="criterionFunction/thresholds/threshold[type='veto']"/></td></tr>
     </xsl:for-each>
   </table>
</xsl:template>

<xsl:template match="function[constant]">
  <!--<xsl:if test="descendant::*name()= 'linear'">integer<xsl:value-of select="."/></xsl:if>
  <xsl:value-of select="."/> -->
  <xsl:apply-templates/>
</xsl:template>

<xsl:template match="value[integer]">
  <xsl:value-of select="format-number(.,'#')" />
</xsl:template>

<xsl:template match="value[real]">
  <xsl:value-of select="format-number(.,'#.##')"/>
</xsl:template>

  <xsl:template match="value[rational]">
  <xsl:value-of select="//numerator" /> <xsl.text>/</xsl.text><xsl:value-of select="//denominator"/>
</xsl:template>


<xsl:template match="function[linear]">
  <xsl:value-of select="linear/intercept/."/> + <xsl:value-of select="linear/slope/."/>x
</xsl:template>



  <!-- Controlling the presentation of the performance table -->
  <xsl:key name="currentAlternative" match="/xmcda:XMCDA/alternatives/alternative" use='.'  />
  
  <xsl:variable name="allAlternatives" 
    select="/xmcda:XMCDA/alternatives/alternative[
    generate-id() = 
    generate-id(key('currentAlternative',.)[1] 
    )
    ]" />  
  
  
<xsl:template match="performanceTable">
  <a name="performance" />
   <xsl:variable name="currentTable" select="."></xsl:variable>
    <xsl:apply-templates  select="description"/>
    <table border="1">
      <tr bgcolor="#9acd32">
        <th>criterion</th>
        <xsl:for-each select="/xmcda:XMCDA/alternatives[description/type='alternatives']/alternative">
	  <th bgcolor="#FFF79B"><xsl:value-of select="@id"/></th>
        </xsl:for-each>
      </tr>
      <xsl:apply-templates select="$currentTable/criterionEvaluations"/> 
    </table>
</xsl:template>

<xsl:template match="criterionEvaluations">
  <tr>
    <th bgcolor="#FFF79B"><xsl:value-of select="criterionID"/></th>
    <xsl:variable name="currentCriterion" select="."></xsl:variable>
    <xsl:for-each select="key('currentAlternative', $allAlternatives)">
      <xsl:variable name="currentAlternative" select="./@id"></xsl:variable>
       <xsl:call-template name="performanceRow">
         <xsl:with-param name="currentCriterion" select="$currentCriterion">
         </xsl:with-param>
         <xsl:with-param name="currentAlternative" select="$currentAlternative"></xsl:with-param>
       </xsl:call-template>
      </xsl:for-each>
  </tr>
</xsl:template>

<xsl:template name="performanceRow">
      <xsl:param name="currentCriterion"></xsl:param>
      <xsl:param name="currentAlternative"></xsl:param>
      <xsl:variable name="currentPerformance" select="$currentCriterion/evaluation[alternativeID=$currentAlternative]"></xsl:variable>
     <td align="right"><xsl:apply-templates select="$currentPerformance/value"/></td>
</xsl:template>

<!-- <xsl:template match="comment"> -->
  <!-- no comments -->
<!-- </xsl:template> -->
<xsl:template match="XMCDA/alternatives/description">
  <!-- no comments -->
</xsl:template>

<xsl:template match="choices">
    <a name="choice"></a>
   <xsl:apply-templates  select="description"/>
   <table border="1">
      <tr bgcolor="#9acd32">
        <th>#</th>
        <th>Choice set</th>
        <th>Determinateness</th>
        <th>Outrankingness</th>
        <th>Outrankedness</th>
        <th>Comment</th>
      </tr>
   <xsl:for-each select="choice">
       <tr><td><xsl:number format="1"/></td>
         <th bgcolor="#FFF79B">{
           <xsl:for-each select="alternativeID">
             <xsl:value-of select="."/>,
           </xsl:for-each>}
           </th>
           <td align="center"><xsl:value-of select="qualities/parameter[name='determinateness']/value"/></td>
           <td align="center"><xsl:value-of select="qualities/parameter[name='outranking']/value"/></td>
         <td align="center"><xsl:value-of select="qualities/parameter[name='outranked']/value"/></td>
         <td><xsl:value-of select="description/comment"/></td>
	</tr>
   </xsl:for-each>
   </table>
</xsl:template>
 

</xsl:stylesheet>
