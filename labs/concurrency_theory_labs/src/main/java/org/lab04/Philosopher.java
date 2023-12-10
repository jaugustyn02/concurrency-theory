package org.lab04;

import java.util.concurrent.Semaphore;
import java.util.concurrent.locks.ReentrantLock;

class UniqueForkNumbers {
    private static int nextID = 0;
    synchronized public static int getID() {
        return nextID++;
    }
}

class Fork {
    public final int id = UniqueForkNumbers.getID();
    public final ReentrantLock lock = new ReentrantLock();
}

public abstract class Philosopher extends Thread {
    final protected int id;
    protected final Fork leftFork;
    protected final Fork rightFork;
    protected final WaitTimer timer;
    static boolean enablePrinting = false;
    public Philosopher(Fork leftFork, Fork rightFork, WaitTimer timer) {
        this.leftFork = leftFork;
        this.rightFork = rightFork;
        this.id = UniquePhilosopherNumbers.getID();
        this.timer = timer;
    }

    public enum PhilosopherType{
        LEFT_RIGHT,
        BOTH,
        ASYMMETRIC,
        STOCHASTIC,
        ARBITER,
        MODIFIED_ARBITER
    }

    protected void printLeftForkLifting(){
        if (enablePrinting)
            System.out.printf("[Filozof %d]: Chce podnieść lewy widelec (%d)%n", this.id, leftFork.id);
    }

    protected void printRightForkLifting(){
        if (enablePrinting)
            System.out.printf("[Filozof %d]: Chce podnieść prawy widelec (%d)%n", this.id, rightFork.id);
    }

    protected void printBothForksLifted(){
        if (enablePrinting)
            System.out.printf("[Filozof %d]: Podniosłem oba widelce (%d, %d)%n", this.id, leftFork.id, rightFork.id);
    }

    public static Philosopher philosopherGenerator(PhilosopherType type, Fork leftFork, Fork rightFork, WaitTimer timer, Semaphore semaphore){
        return switch (type){
            case LEFT_RIGHT -> new Philosopher1(leftFork, rightFork, timer);
            case BOTH -> new Philosopher2(leftFork, rightFork, timer);
            case ASYMMETRIC -> new Philosopher3(leftFork, rightFork, timer);
            case STOCHASTIC -> new Philosopher4(leftFork, rightFork, timer);
            case ARBITER -> new Philosopher5(leftFork, rightFork, timer, semaphore);
            case MODIFIED_ARBITER -> new Philosopher6(leftFork, rightFork, timer, semaphore);
        };
    }

    @Override
    public void run() {
        super.run();
    }
}

