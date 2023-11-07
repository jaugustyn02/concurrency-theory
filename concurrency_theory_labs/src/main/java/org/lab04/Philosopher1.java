package org.lab04;

// 1. Rozwiązanie naiwne (z możliwością blokady). Każdy filozof czeka, aż wolny będzie lewy widelec, a następnie go
//    podnosi (zajmuje), następnie podobnie postępuje z prawym widelcem.

public class Philosopher1 extends Philosopher {
    public Philosopher1(Fork leftFork, Fork rightFork, WaitTimer timer) {
        super(leftFork, rightFork, timer);
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

