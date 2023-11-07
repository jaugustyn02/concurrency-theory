package org.lab04;

import java.util.Arrays;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Semaphore;
import java.util.concurrent.TimeUnit;


public class FivePhilosophersProblem {
    public static void main(String[] args) throws InterruptedException {
        int[] N = new int[]{10, 25, 100}; // num of threads
        int R = 3; // num of runs per test
        int t = 5; // running time in seconds

        Fork[] Forks = new Fork[Arrays.stream(N).max().getAsInt()];
        for (int i=0; i<Arrays.stream(N).max().getAsInt(); i++)
            Forks[i] = new Fork();

        for (Philosopher.PhilosopherType type: Philosopher.PhilosopherType.values()) {
            if (type == Philosopher.PhilosopherType.LEFT_RIGHT || type == Philosopher.PhilosopherType.STOCHASTIC)
                continue;
            for (int numOfPhilosophers : N) {
                for (int r = 0; r < R; r++) {
                    UniquePhilosopherNumbers.resetID();
                    WaitTimer timer = new WaitTimer(numOfPhilosophers, type);
                    Semaphore semaphore = new Semaphore(numOfPhilosophers - 1); // needed for philosophers 5 and 6

                    ExecutorService executor = Executors.newFixedThreadPool(numOfPhilosophers);

                    for (int i = 0; i < numOfPhilosophers; i++) {
                        Philosopher philosopher = Philosopher.philosopherGenerator(
                                type, Forks[i], Forks[(i + 1) % numOfPhilosophers], timer, semaphore
                        );
                        executor.execute(philosopher);
                    }

                    try {
                        Thread.sleep(t * 1000); // Threads running time - 5 sec
                    } catch (InterruptedException e) {
                        throw new RuntimeException(e);
                    }

                    executor.shutdownNow();
                    boolean finished = executor.awaitTermination(10, TimeUnit.SECONDS);

                    timer.printTimes();
                    timer.saveTimeMeasurementsAsCSV("src/main/results_lab04/" + type + "_" + numOfPhilosophers + ".csv", r > 0);
                }
            }
        }
    }
}
