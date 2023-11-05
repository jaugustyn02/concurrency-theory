package org.lab04;

// 5. Rozwiązanie z arbitrem. Zewnętrzny arbiter (lokaj, kelner) pilnuje, aby jednocześnie co najwyżej czterech
//    (w ogólnym przypadku N-1) filozofów konkurowało o widelce. Każdy podnosi najpierw lewy a potem prawy widelec.
//    Jeśli naraz wszyscy filozofowie będą chcieli jeść, arbiter powstrzymuje jednego z nich aż do czasu, gdy któryś z
//    filozofów skończy jeść.

import java.util.concurrent.Semaphore;

public class Philosopher5 extends Philosopher {
    private final Semaphore semaphore;

    public Philosopher5(Fork leftFork, Fork rightFork, WaitTimer timer, Semaphore semaphore) {
        super(leftFork, rightFork, timer);
        this.semaphore = semaphore;
    }

    @Override
    public void run() {
        long waitingTime = 0;
        long count = 0;
        try {
            while (!Thread.currentThread().isInterrupted()) {
                long startTime = System.nanoTime();
                long acquisitionTime;

                semaphore.acquire();
                this.printLeftForkLifting();
                synchronized (leftFork) {
                    this.printRightForkLifting();
                    synchronized (rightFork) {
                        acquisitionTime = System.nanoTime();
                    }
                }
                semaphore.release();

                waitingTime += acquisitionTime - startTime;
                count++;
            }
        }
        catch (InterruptedException ignored) {
            timer.addTime(this.id, waitingTime, count);
        }
        finally {
            timer.addTime(this.id, waitingTime, count);
        }
    }
}
