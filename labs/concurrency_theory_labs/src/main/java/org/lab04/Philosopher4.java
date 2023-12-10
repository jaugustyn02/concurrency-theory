package org.lab04;

// 4. Rozwiązanie stochastyczne. Każdy filozof rzuca monetą tuż przed podniesieniem widelców i w ten sposób decyduje,
//    który najpierw podnieść - lewy czy prawy (z prawdopodobieństwem 1 nie dojdzie do zagłodzenia).

import java.util.Random;

public class Philosopher4 extends Philosopher {
    private final Random random = new Random();
    public Philosopher4(Fork leftFork, Fork rightFork, WaitTimer timer) {
        super(leftFork, rightFork, timer);
    }

    @Override
    public void run() {
        long waitingTime = 0;
        long count = 0;
        boolean coinToss; // 0 - heads, 1 - tails
        while (!Thread.currentThread().isInterrupted()) {
            long startTime = System.nanoTime();
            long acquisitionTime;

            coinToss = random.nextBoolean();
            if (coinToss){
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
            count++;
        }
        timer.addTime(this.id, waitingTime, count);
    }
}
