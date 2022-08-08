<?xml version='1.0' encoding='us-ascii'?>
<algebra>
  <basicAlgebra>
    <algName>m5</algName>
    <desc>the diamond of 5</desc>
    <cardinality>7</cardinality>
    <operations>
      <op>
        <opSymbol>
          <opName>join</opName>
          <arity>2</arity>
        </opSymbol>
        <opTable>
          <intArray>

          <row r="[0]">0,1,2,3,4,5,6</row>
			<row r="[1]">1,1,4,4,4,4,4</row>
			<row r="[2]">2,4,2,4,4,4,4</row>
			<row r="[3]">3,4,4,3,4,4,4</row>
			<row r="[4]">4,4,4,4,4,4,4</row>
			<row r="[5]">5,4,4,4,4,5,4</row>
			<row r="[6]">6,4,4,4,4,4,6</row>
			</intArray>
        </opTable>
      </op>
      <op>
        <opSymbol>
          <opName>meet</opName>
          <arity>2</arity>
        </opSymbol>
        <opTable>
          <intArray>
           
          <row r="[0]">0,4,4,4,4,4,0</row>
			<row r="[1]">4,1,4,4,4,4,1</row>
			<row r="[2]">4,4,2,4,4,4,2</row>
			<row r="[3]">4,4,4,3,4,4,3</row>
			<row r="[4]">4,4,4,4,4,4,4</row>
			<row r="[5]">4,4,4,4,4,5,5</row>
			<row r="[6]">0,1,2,3,4,5,6</row>
			</intArray>
        </opTable>
      </op>
    </operations>
  </basicAlgebra>
</algebra>