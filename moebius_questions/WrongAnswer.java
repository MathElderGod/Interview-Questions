/**
   QUESTION 5: Wrong Result
   ----------------

   The following program produces inconsistent results. It should always output
   this: ``` counter is 20000
   ``` Please correct the program. ```
*/

public class WrongAnswer {
    private int counter = 0;

    public static void main(String[] args) {
        new WrongAnswer().run();
    }

    private void run() {
        try {
            Thread t1 = new Thread(this::incrementToOnHundred);
            Thread t2 = new Thread(this::incrementToOnHundred);
            t1.start();
            t2.start();
            t1.join();
            t2.join();
            System.out.println("counter is " + counter);
        } catch (InterruptedException e) {
            System.err.println("fatal error, unexpected interrupt exception");
            System.exit(2);
        }
    }

    private void incrementToOnHundred() {
        for (int i = 0; i < 10000; i++) {
            doSomeFakeWork();
        }
    }

    private synchronized void doSomeFakeWork() {
        counter++;
    }
}




/**
 * Answer: 
 *
 * The issue with this program arises from race conditions. The counter variable is shared between two threads, 
 * and without synchronization, both threads attempt to increment counter simultaneously. This causes inconsistent 
 * results because the threads are not properly coordinated and might overwrite each other’s updates.
 * In a multi-threaded program, when threads share resources like the counter variable, synchronization 
 * ensures that only one thread can modify the counter at a time, preventing unexpected behavior caused by concurrent updates.
 * 
 * To fix the issue, I used the synchronized keyword on the doSomeFakeWork method. This guarantees 
 * that only one thread can execute this method at a time, ensuring that counter is correctly incremented and always ends up at the expected value.
 *
 * Solution: By adding the synchronized keyword, it ensures that the counter is safely incremented by each thread in turn, eliminating race conditions and providing consistent results.
 * 
 * cite: https://www.geeksforgeeks.org/synchronization-in-java/
 *      
 *
 * Funny enough, it looks like the problem was ripped right from my citation. 
 */
