# Encryption Terms

### Getting Started
    Just clone the git or download the ZIP file
    Goto the downloaded folder
    Make a new python file

#### Use of number Encryption
`from encto import NEncryptTSK`<br>
`obj = NEncryptTSK(Key_One, Key_two)`<br>
`encryeption = obj.calc(number)`<br>
`print(encryeption)`<br>
#### Use of number Decryption
`from encto import NDecryptTSK`<br>
`obj = NDecryptTSK(Key_One, Key_two)`<br>
`decryeption = obj.calc(number)`<br>
`print(decryeption)`<br>
#### Some point to notice
`1. Key_one must be grater than Key_two`<br>
`2. Key_two - Key_one  must be grater than 2`<br>
`3. Key_two must be less than 9`<br>
`4. There are some logical error to fix that's why condition 3 comes`<br>

*****

### TODO
1. Fix the point no `3` `The Logical Error`