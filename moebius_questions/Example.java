// QUESTION 1. Why does this code not work? How do you fix it?
import java.util.List;
import java.util.ArrayList;

public class Example {
	public List<Integer> removeBigNumbers(List<Integer> data) {
		// advanced for loop, takes the form of
		// for(dataType element : collection) {}
		// This means each Integer i is an actual value, and not an index

		// create a new list, to append elements correctly and accordingly
		List<Integer> resultList = new ArrayList<Integer>();
		for(Integer i : data) {
			// ** start orginal implementation
			// if the element is greater than ten
				// if(i > 10) {
					/**
					 * 
					 * remove(int index) or remove(Object o)
					 * Removes the element at the specified position in this list (optional operation).
					 *
					 * or
					 *
					 * Removes the first occurrence of the specified element from this list, if it is present (optional operation).
					 */
					
					// this attempts to remove either the element at index i, or the first instance of an object o
					// in the list
					// data.remove(i);
				//}
			// ** end original implementation
			// if the element is less than or equals to 10
			if(i <= 10){
				// 	add(E e)
				//
				// 	Appends the specified element to the end of this list (optional operation).
				resultList.add(i);
			}
		}
		// returns a new list that is composed of only integers greater than or equals to 10
		return resultList;
	}

	public static void main(String args[]){
		// run a test
		
		// create relevant objects 
		Example someExample = new Example();
        	List<Integer> someIntegerList = new ArrayList<Integer>();
        	List<Integer> resultList = new ArrayList<Integer>();

		// append new elements to some integer list
        	someIntegerList.add(20);
        	someIntegerList.add(28);
        	someIntegerList.add(11);
        	someIntegerList.add(10);
        	someIntegerList.add(2);
        	someIntegerList.add(11);
        	someIntegerList.add(20);
        	someIntegerList.add(28);
        	someIntegerList.add(10);
        	someIntegerList.add(1);

		// result should only contain 10, 2, 10, 1 when remove big numbers is called
        	resultList = someExample.removeBigNumbers(someIntegerList);

        	System.out.print("[ ");
        	for(Integer someInt : resultList){
                	System.out.print(someInt + " ");
        	}
        	System.out.println("]");
	}

}

// Answer: 
//
//
// resources: 	https://docs.oracle.com/javase/8/docs/api/java/util/List.html
// 		https://docs.oracle.com/javase/8/docs/api/java/util/ConcurrentModificationException.html
//
// Error Found is ConcurrentModificationException. Error Type is RuntimeException.
// This exception may be thrown by methods that have detected concurrent modification of an object when such modification is not permissible.
//
// In other words, there are elements that are actively being removed from list data, and it is being iterated over at the same time. This will
// cause unexpected behavior, as we wouldn't be iterating over the original list, but a modified version of it in every new iteration (potentially). 
//
// Best fix is to keep track of any numbers that are less than or equals to 10, and add them to a seperate new list, and return that list as whole. This would prevent
// the ConcurrentModificationException from happening altogether and implement the original solution that was intended. 

// This should be the correct revision needed to be made to fix the issue addressed above. 

/* 
  public class Example {
         public List<Integer> removeBigNumbers(List<Integer> data) {
                 List<Integer> resultList = new ArrayList<Integer>();
                 for(Integer i : data) {
                         if(i <= 10){
                                 resultList.add(i);
                         }
                 }
                 return resultList;
         }
  }

*/
