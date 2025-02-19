/**
QUESTION 4: Debugging
----------------

```

package com.moesol.hr.bugs;
*/

public class Bug1 {
    private Integer rating;

    // define the default constructor
    public Bug1(){}
    // define another constructor that take in a parameter
    public Bug1(int rating){
	// set the objects rating to the passed in rating
	this.rating = rating;
    }

    public int rating() {
	// if the rating is null
	if(this.rating == null){
	    //simply return zero
	    return 0;
	} else {
	    // else return this rating
	    return this.rating;
	}
    }

    public static void main(String[] args) {
        System.out.println("rating:" +
            new Bug1().rating());
	// should print: rating:0
    }
}

/**
```

The program above throws a `NullPointerException` with this stack trace:

```
Exception in thread "main" java.lang.NullPointerException
    at com.moesol.hr.bugs.Bug1.rating(Bug1.java:7)
    at com.moesol.hr.bugs.Bug1.main(Bug1.java:12)
```

What is happening? How can it be fixed?


Answer:

        Well there appears to be a variety of issues. To begin, the default value that
        the wrapper class Integer gives in its void paramater constructor will always be
        null. Thus rating itself was never defined, only declared. As a result, it has no
        actual value and is null. When accessing this data, by using Bug1().rating(), it will
        return a null reference of the private instance variable rating. the rating() function
        explicity states that it will return an integer reference/value. This is obviously not the case since it is null.
        the easiest fix is to have a sanity check in rating, that ensures null access is avoided. we check if this.rating is null, and
        if it is, we will return 0. else we will return the actual rating.

	This is the error.
	Exception in thread "main" java.lang.NullPointerException: Cannot invoke "java.lang.Integer.intValue()" because "this.rating" is null
        at Bug1.rating(Bug1.java:14)
        at Bug1.main(Bug1.java:19)


	I have implemented the fix above. and thus, simply get a rating of zero. another thing that can be done is specifying a more in depth constructor,
	that forces the user to provide an actual integer value, and setting rating to the rating provided in the constructor. the sanity check can be left
	untouched, and thus will be a more significant fix. 
*/
