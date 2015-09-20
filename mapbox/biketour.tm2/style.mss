@water: #ddeeff;
@land: #ffffdd;
@line: #226688;

@sans: 'Source Sans Pro Regular';
@sans_italic: 'Source Sans Pro Italic';
@sans_bold: 'Source Sans Pro Semibold';

/* Water bodies */
Map { 
  background-color: @water;
}

#land-border-country[zoom>1] {
  line-width:1;
  line-color:#fff;
  line-join:round;
}


#country-name {
  text-name: '';
  text-face-name: @sans_bold;
  text-fill: #6161b9;
  text-size: 16;
  
  [ADM0_A3='CHE'] { text-name: [NAME]; }
  [ADM0_A3='ITA'] { text-name: [NAME]; }
  [ADM0_A3='SVN'] { text-name: [NAME]; }
  [ADM0_A3='HRV'] { text-name: [NAME]; }
  [ADM0_A3='ALB'] { text-name: [NAME]; }
  [ADM0_A3='BIH'] { text-name: [NAME]; }
  [ADM0_A3='MNE'] { text-name: [NAME]; }
  [ADM0_A3='GRC'] { text-name: [NAME]; }
  
  [ADM0_A3='GRC'] {
  text-dy: -18;
  text-dx: -23;
  }
  [ADM0_A3='ALB'] {
  text-dy: -2;
  text-dx: 1;
  }
}

@white: #F0F8FF; /* blue-tinted, for Antarctica */
@red: #fdaf6b;
@orange: #fdc663;
@yellow: #fae364;
@green: #d3e46f;
@turquoise: #aadb78;
@blue: #a3cec5;
@purple: #ceb5cf;
@pink: #f3c1d3;
@f00: #f00;

/* Coastlines */
#country::land-glow-inner[zoom>=0] { 
  line-color:@line;
  line-join:round;
  line-width:1;
}


#country[zoom>=0] {
  polygon-fill:#fff ;
  [ADM0_A3='CHE'] { polygon-fill:@blue; }
  [ADM0_A3='ITA'] { polygon-fill:@green; }
  [ADM0_A3='SVN'] { polygon-fill:@purple; }
  [ADM0_A3='HRV'] { polygon-fill:@yellow; }
  [ADM0_A3='ALB'] { polygon-fill:@purple; }
  [ADM0_A3='BIH'] { polygon-fill:@blue; }
  [ADM0_A3='MNE'] { polygon-fill:@pink; }
  [ADM0_A3='GRC'] { polygon-fill:@red; }
  
}

/* Useful/significant lines */
#geo-lines[DISPLAY!='International Date Line - Pre 1995 alignment'] {
  line-color:@line;
  line-dasharray:6,2;
  [zoom=0] { line-width:0.2; }
  [zoom=1] { line-width:0.4; }
  [zoom=2] { line-width:0.6; }
  [zoom=3] { line-width:0.8; }
  [zoom>3] { line-width:1; }
}

