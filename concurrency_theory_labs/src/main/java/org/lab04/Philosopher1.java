package org.lab04;

// Filozof 1 (najpierw próbuje wziąć lewy widelec, a następnie prawy)

public class Philosopher1 extends Philosopher {
    public Philosopher1(Fork leftFork, Fork rightFork) {
        super(leftFork, rightFork, null);
    }

    @Override
    public void run() {
        while (true) {
            this.printLeftForkLifting();
            synchronized (leftFork) {
                this.printRightForkLifting();
                synchronized (rightFork) {}
            }
        }
    }
}

