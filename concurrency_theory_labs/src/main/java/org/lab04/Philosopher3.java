package org.lab04;

// 3. Rozwiązanie asymetryczne. Filozofowie są ponumerowani. Filozof z parzystym numerem najpierw podnosi prawy widelec,
//    filozof z nieparzystym numerem najpierw podnosi lewy widelec.

public class Philosopher3 extends Philosopher {
    public Philosopher3(Fork leftFork, Fork rightFork, WaitTimer timer) {
        super(leftFork, rightFork, timer);
    }

    @Override
    public void run() {
        long acquisitionTime;
        long waitingTime = 0;
        long waitingCount = 0;
        while (!Thread.currentThread().isInterrupted()) {
            long startTime = System.nanoTime();

            if (this.id % 2 == 1){
                this.printLeftForkLifting();
                synchronized (leftFork) {
                    this.printRightForkLifting();
                    synchronized (rightFork) {
                        acquisitionTime = System.nanoTime();
                    }
                }
            }
            else {
                this.printRightForkLifting();
                synchronized (rightFork) {
                    this.printLeftForkLifting();
                    synchronized (leftFork) {
                        acquisitionTime = System.nanoTime();
                    }
                }
            }
            waitingTime += acquisitionTime - startTime;
            waitingCount++;
        }
        timer.addTime(this.id, waitingTime, waitingCount);
    }
}
