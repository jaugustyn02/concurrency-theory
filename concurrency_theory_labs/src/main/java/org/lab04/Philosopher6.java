package org.lab04;

// Filozof 6

import java.util.concurrent.Semaphore;

public class Philosopher6 extends Philosopher {
    private final Semaphore semaphore;

    public Philosopher6(Fork leftFork, Fork rightFork, WaitTimer timer, Semaphore semaphore) {
        super(leftFork, rightFork, timer);
        this.semaphore = semaphore;
    }

    @Override
    public void run() {
        long waitingTime = 0;
        long count = 0;
        while (!Thread.currentThread().isInterrupted()) {
            long startTime = System.nanoTime();
            long acquisitionTime;

            if (semaphore.tryAcquire()) {
                this.printLeftForkLifting();
                synchronized (leftFork) {
                    this.printRightForkLifting();
                    synchronized (rightFork) {
                        acquisitionTime = System.nanoTime();
                    }
                }
                semaphore.release();
            } else {
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
