#Homework 3: Huffman Coding

Problem Description:
The easiest way to output the huffman tree itself is to, starting at the root, dump first the left hand side then the right hand side(recursive infix traversal, i.e. Center – Left – Right). For each node you output a 0, for each leaf you output a 1 followed by the char.

Input:
第一行: how many different character(不同字元的總數)
第二行: The first character and the frequency of the character(第一個字元以及它出現的次數)
第三行: The second character and the frequency of the character(第二個字元以及它出現的次數)
字元以及次數已逗號分隔.
之後依此類推，直到等於物品總數.

Output:
For each node you output a 0, for each leaf you output a 1 followed by the char.

Example:
總共有 2 個不同字元
1. Huffman Tree 為 1 節點，left leaf A, right leaf B, output 答案為 01A1B。
2. 課本185(b)圖: 001a1d01f01c01b1e
