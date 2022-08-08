<?xml version='1.0' encoding='us-ascii'?>
<algebra>
  <basicAlgebra>
    <algName>m8</algName>
    <desc>M_8 with 3 as the greatest.</desc>
    <cardinality>10</cardinality>
    <operations>
      <op>
        <opSymbol>
          <opName>join</opName>
          <arity>2</arity>
        </opSymbol>
        <opTable>
          <intArray>

          <row r="[0]">0,1,2,3,4,5,6,7,8,9</row>
			<row r="[1]">1,1,3,3,3,3,3,3,3,3</row>
			<row r="[2]">2,3,2,3,3,3,3,3,3,3</row>
			<row r="[3]">3,3,3,3,3,3,3,3,3,3</row>
			<row r="[4]">4,3,3,3,4,3,3,3,3,3</row>
			<row r="[5]">5,3,3,3,3,5,3,3,3,3</row>
			<row r="[6]">6,3,3,3,3,3,6,3,3,3</row>
			<row r="[7]">7,3,3,3,3,3,3,7,3,3</row>
			<row r="[8]">8,3,3,3,3,3,3,3,8,3</row>
			<row r="[9]">9,3,3,3,3,3,3,3,3,9</row>
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
           
          <row r="[0]">0,3,3,3,3,3,3,3,3,0</row>
			<row r="[1]">3,1,3,3,3,3,3,3,3,1</row>
			<row r="[2]">3,3,2,3,3,3,3,3,3,2</row>
			<row r="[3]">3,3,3,3,3,3,3,3,3,3</row>
			<row r="[4]">3,3,3,3,4,3,3,3,3,4</row>
			<row r="[5]">3,3,3,3,3,5,3,3,3,5</row>
			<row r="[6]">3,3,3,3,3,3,6,3,3,6</row>
			<row r="[7]">3,3,3,3,3,3,3,7,3,7</row>
			<row r="[8]">3,3,3,3,3,3,3,3,8,8</row>
			<row r="[9]">0,1,2,3,4,5,6,7,8,9</row>
			</intArray>
        </opTable>
      </op>
    </operations>
  </basicAlgebra>
</algebra>