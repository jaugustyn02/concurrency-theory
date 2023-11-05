package org.lab04;

// 2) Filozof najpierw sprawdza, czy oba widelce nie są zajęte, i jeżeli nie są, to podnosi oba na raz

public class Philosopher2 extends Philosopher {
    public Philosopher2(Fork leftFork, Fork rightFork, WaitTimer timer) {
        super(leftFork, rightFork, timer);
    }

    @Override
    public void run() {
        long startTime = System.nanoTime();
        long acquisitionTime;
        long waitingTime = 0;
        long waitingCount = 0;
        while (!Thread.currentThread().isInterrupted()) {
            if (leftFork.lock.tryLock() && rightFork.lock.tryLock()) {
                    acquisitionTime = System.nanoTime();
                    this.printBothForksLifted();

                    leftFork.lock.unlock();
                    rightFork.lock.unlock();

                    waitingTime += acquisitionTime - startTime;
                    waitingCount++;
                    startTime = System.nanoTime();
            } else {
                if (leftFork.lock.isHeldByCurrentThread()){
                    leftFork.lock.unlock();
                }
                if (rightFork.lock.isHeldByCurrentThread()){
                    rightFork.lock.unlock();
                }
            }
        }
        timer.addTime(this.id, waitingTime, waitingCount);
    }
}