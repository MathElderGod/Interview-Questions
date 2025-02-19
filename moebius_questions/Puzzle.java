/**
BONUS: Programming Puzzle Bonus!
----------------

A string of ASCII text has been encrypted using the following algorithm:

* Use the bytes "MOEBIUS" as the key.
* Working one byte at a time, xor the next byte of data with the next byte in
  the key.
* When the end of the key is reached, wrap around to the first byte again.
* Base-64 encode the data.

For example, the text "Simple is better than complex." encrypts to
"HiYoMiUwcyQ8ZSAsIScoPWU2ITQ9bSwqLzk5NjVh". The key is repeated as follows
while XOR-ing bytes:

```
Simple is better than complex.
MOEBIUSMOEBIUSMOEBIUSMOEBIUSMO
```

Write a program to reverse this process and decrypt the following message. Use
any programming language you like. Provide both your program and the decrypted
message.

```
DiArJTs0JzgjJDYgOj0+Y2U7JiBzPiApNCwxczknIGIrOj04PGUzPDAgOSYqLGhfWW1vZW
JpdXNtb2ViaXVzbW9lYml1c21vZWJpdXNtb2ViaXVzY2hibEN1c21vZWJpe3RqYWViaXVz
bWFlYml1c21vZWhucnltb2VicwoPYhB/Yml1c21hT2JpdXNtb38dFXoMd29lYhYJe2IQZW
Jnb31nEBltFn9zbW9/YmYJc3dvZWxue2ljaGtIaXV9amhreGl6D211ZWJpe3xkE2ViaXJp
amVlbRV1eW11ZWJue31qYWViZGhpInV4b0N1aRITah1zcn13dX9saXVzbWhlaG5yeW1vZW
JjdXRjaGpsbnUMEWdqHW57dHdoa2VDdWltYBlic3Vpd3V/eGl1c21vbx0Vegxnb2ViaXV+
cG8qYnR4c21gbB5pdXNtaE9iaXJ9Y2hlYm5vaXdoZWJpdXNnb2oeaX9zbW9lYmdyfGNoa2
JpdXRHb2ViaXVzbW9lYml1c21vZWJpdXljYW9iaXVzbW9lYmlvWQ==
```

 NOTE: This block uses the "MIME" flavor of Base64 encoding.
 Depending upon your Base64 decoder, you may need to remove the "=" padding.

cite: docs.oracle.com/javase/8/docs/api/java/lang/String.html
      geeksforgeeks.org/program-to-find-the-xor-of-ascii-values-of-characters-in-a-string/
      https://docs.oracle.com/javase/8/docs/api/java/util/Base64.html

*/

import java.util.Base64;
public class Puzzle {

	// private constant variables	
	private static final String ENCODING_STRING = "MOEBIUS";
	private static final int BASE_64 = 64;

	/**
	 * Encoding function, prints the encoded version of the string parameter
	 * @param someString the string to encode
	 */
	public void encode(String someString){
		// get string lengths
	        int sizeOfStringToEncode = someString.length();
		int sizeOfEncodingString = ENCODING_STRING.length();
		// start a count, will be used to circulate on MOEBIUS
	        int count = 0;
		// create an empty encoded string
		String encodedString = "";
		System.out.print("Encoded String: ");
		// iterate through each char	
		for(int i = 0; i < sizeOfStringToEncode; i++){
			// XOR each char with its corresponding char in MOEBIUS, this will ensure a repeating seed of: 
			// MOEBIUSMOEBIUSMOEBIUSMOEBIUSMOMOEBIUSMOEBIUSMOEBIUSMOEBIUSMOMOEBIUSMOEBIUSMOEBIUSMOEBIUSMO...
			char result = ( (char) ( someString.charAt(i) ^ ENCODING_STRING.charAt(count % sizeOfEncodingString)) );
			// append the encoded char to the encoded string
			encodedString += result;
			// increment the count
			count++;
		}
		// MIME base 64 encode the entire encoded string
		encodedString = Base64.getMimeEncoder().encodeToString(encodedString.getBytes());
		// print the encoded string
		System.out.println(encodedString + "\n");
	}

	/**
	 *
	 * Decoding function, prints the decoded version of the string parameter
         * @param someEncodedString the string to decode
	 *
	 *
	 */
	public void decode(String someEncodedString){
		// MIME base 64 decode the encoded string
		byte[] decodedBytes = Base64.getMimeDecoder().decode(someEncodedString);
		// save the decoded string
		String decodedString = new String(decodedBytes);
		// string lengths
		int sizeOfStringToDecode = decodedString.length();
		int sizeOfDecodingString = ENCODING_STRING.length();
                // start a count, will be used to circulate on MOEBIUS
		int count = 0;
		// create a new and empty final decoded string
		String finalDecodedString = "";
		// iterate through each char
		for(int i = 0; i < sizeOfStringToDecode; i++){
			// XOR each char with its corresponding char in MOEBIUS, this will ensure a repeating seed of:
                        // MOEBIUSMOEBIUSMOEBIUSMOEBIUSMOMOEBIUSMOEBIUSMOEBIUSMOEBIUSMOMOEBIUSMOEBIUSMOEBIUSMOEBIUSMO...
			char result = ( (char) ( decodedString.charAt(i) ^ ENCODING_STRING.charAt(count % sizeOfDecodingString)));
			// append the decoded char to the final decoded string
			finalDecodedString += result;
			// increment the count	
			count++;
		}
		// print the decoded string
		System.out.println(finalDecodedString);
	}

	public static void main(String args[]){
		// simple tests
		Puzzle somePuzzle = new Puzzle();
		somePuzzle.encode("Simple is better than complex.");
		String stringToDecode = "DiArJTs0JzgjJDYgOj0+Y2U7JiBzPiApNCwxczknIGIrOj04PGUzPDAgOSYqLGhfWW1vZWJpdXNtb2ViaXVzbW9lYml1c21vZWJpdXNtb2ViaXVzY2hibEN1c21vZWJpe3RqYWViaXVzbWFlYml1c21vZWhucnltb2VicwoPYhB/Yml1c21hT2JpdXNtb38dFXoMd29lYhYJe2IQZWJnb31nEBltFn9zbW9/YmYJc3dvZWxue2ljaGtIaXV9amhreGl6D211ZWJpe3xkE2ViaXJpamVlbRV1eW11ZWJue31qYWViZGhpInV4b0N1aRITah1zcn13dX9saXVzbWhlaG5yeW1vZWJjdXRjaGpsbnUMEWdqHW57dHdoa2VDdWltYBlic3Vpd3V/eGl1c21vbx0Vegxnb2ViaXV+cG8qYnR4c21gbB5pdXNtaE9iaXJ9Y2hlYm5vaXdoZWJpdXNnb2oeaX9zbW9lYmdyfGNoa2JpdXRHb2ViaXVzbW9lYml1c21vZWJpdXljYW9iaXVzbW9lYmlvWQ==";
		somePuzzle.decode(stringToDecode);

		// Decode this message for me, to whom it may concern regarding the team

		// somePuzzle.decode("CSokMGkdOj8mKyVpATYsImliHTpzOicqL2k8J20iJDtpNjwjLCAwJ3lzBG8vNzohczouKzYsMXM5IGU2KD42bS5lLyY4NiM7ZTYmdSAkISYnOzA/NG8xKig7OG02KjdpMzw/bzEqLHU8PT8qMD0gPSQ7PGI9OnMuICgyJTAnKG8xKix1Mj48IDE6ODYjO2U2JjEyNGFlC2khITgjPGIoJSM/KiYrKCE2bTstJ2k2OywhJidpITxtKyAvJjsgOT0kNix1PjRvNikgOT8+Y2UjJzFzBG81Nz11OiNvKDtpNzY+O2UnLzM8PztlNiZ1ICUgMiEoJjZtOC0jPXUabSwkLGkxPGNvESogJnMiPzUtOyEmIyYxO2k4NiwhNmIodT8iO2U2JnU+KGNlIycxcwRvMi08OTdtIyo0LHUnJSplISE0PS4qZTYmdTAiITErJyA2bSYrYj09Nm0/Ny0qMCA+YWULaSI8PyQgJmk9Mj8rZTYmdSM/KjYnJyFzIDZlICwmJ204KjAieXMsISFiAHU7Ij8gYj09MjlvKDtpJTY/KSowJDQ9LiplMCwzPygsMTFpNzw5J2UvMHU3KCssISghOiIhZSMnMXMgNmUnKDI2PyEgMTp1JyJvJi0nISEkLTA2LHUnIm88LTwnczkqJC9ndQclLispaSw8OG8kJSg8PW0pKjBpLDw4PWU2IDg2bS4rJmk2PCM8LCYsJzI5JiosZ3UabSMqLSJ1NSI9MiM7MXM5IGUqLDQhJCEiYi8nPCBvPC08e3MPKjY2aSc2Ki43Jjp5cwwjIDooOzcoPWUDOzwyPmE=");
	}
}
