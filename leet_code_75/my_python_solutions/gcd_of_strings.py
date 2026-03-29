def gcdOfStrings(str1, str2):
    # get the string lengths of each string
    str1_length = len(str1)
    str2_length = len(str2)

    # if theyre the same length
    if str1_length == str2_length:
        # and if theyre the same string, return either or
        if str1 == str2:
            return str1
        # else return the empty string
        else:
            return ''

    # set the final gcd to the empty string
    final_gcd_string = ''

    # if str 1 is smaller
    if str1_length < str2_length:
        # step 1, check if gcd matches with str 2
        # initialize the gcd to be empty
        gcd_string = ''
        # for each index in str 1
        for i in range(str1_length):
            # initialize the concatenated string to be empty
            concatenated_string = ''
            # concatenate the i-th character to the gcd string
            gcd_string += str1[i]
            # for every possible concatentation of gcd upto (str2 length // index + 1)
            for j in range((str2_length // (i + 1))):
                # concatenate gcd to concatenated string
                concatenated_string += gcd_string
            # get the length of the gcd string
            gcd_string_length = len(gcd_string)
            # if the string is a match, and perfectly divides str1 and str2, set the final gcd to the current gcd
            if (concatenated_string == str2) and (str1_length % gcd_string_length == 0) and (str2_length % gcd_string_length == 0):
                final_gcd_string = gcd_string

        # step 2, check if gcd matches with str 1
        # if its the empty string, or if it matches with the str1, return the final gcd
        if final_gcd_string == '' or final_gcd_string == str1:
            return final_gcd_string
        # else check to see if its own cocatenation matches with str 1
        else:
            # get the length of the final gcd string
            final_gcd_string_length = len(final_gcd_string)

            concatenated_string = ''
            # concatenate the final gcd to itself up to (str1 length // final gcd string length)
            for i in range(str1_length // final_gcd_string_length):
                concatenated_string += final_gcd_string 
            # if the concatenation matches with str1, return the final gcd string
            if (concatenated_string == str1):
                return final_gcd_string
            # else return the empty string
            else:
                return ''
    # else str 2 is smaller
    else:
        # step 1, check if gcd matches with str 1
        # initialize the gcd to be empty
        gcd_string = ''
        # for each index in str 2
        for i in range(str2_length):
            # initialize the concatenated string to be empty
            concatenated_string = ''
            # concatenate the i-th character to the gcd string
            gcd_string += str2[i]
            # for every possible concatentation of gcd upto (str1 length // index + 1)
            for j in range((str1_length // (i + 1))):
                # concatenate gcd to concatenated string
                concatenated_string += gcd_string
            # get the length of the gcd string
            gcd_string_length = len(gcd_string)
            # if the string is a match, and perfectly divides str1 and str2, set the final gcd to the current gcd
            if (concatenated_string == str1) and (str1_length % gcd_string_length == 0) and (str2_length % gcd_string_length == 0):
                final_gcd_string = gcd_string

        # step 2, check if gcd matches with str 2
        # if its the empty string, or if it matches with the str2, return the final gcd
        if final_gcd_string == '' or final_gcd_string == str2:
            return final_gcd_string
            # else check to see if its own cocatenation matches with str 2
        else:
            # get the length of the final gcd string
            final_gcd_string_length = len(final_gcd_string)

            concatenated_string = ''
            # concatenate the final gcd to itself up to (str2 length // final gcd string length)
            for i in range(str2_length // final_gcd_string_length):
                concatenated_string += final_gcd_string 
            # if the concatenation matches with str2, return the final gcd string
            if (concatenated_string == str2):
                return final_gcd_string
            # else return the empty string
            else:
                return ''


str1 = 'ABCABC'
str2 = 'ABC'
print("String 1: " + str1 + " String 2: " + str2)
print("------------------------")
print("Result: ABC " + 'Expected: ' + gcdOfStrings(str1, str2) + '\n')

str1 = 'ABABAB'
str2 = 'ABAB'
print("String 1: " + str1 + " String 2: " + str2)
print("------------------------")
print("Result: AB " + 'Expected: ' + gcdOfStrings(str1, str2) + '\n')

str1 = 'ALEX'
str2 = 'ARIAS'
print("String 1: " + str1 + " String 2: " + str2)
print("------------------------")
print("Result: '' " + 'Expected: ' + gcdOfStrings(str1, str2) + '\n')

str1 = 'AAAAAB'
str2 = 'AAA'
print("String 1: " + str1 + " String 2: " + str2)
print("------------------------")
print("Result: '' " + 'Expected: ' + gcdOfStrings(str1, str2) + '\n')
