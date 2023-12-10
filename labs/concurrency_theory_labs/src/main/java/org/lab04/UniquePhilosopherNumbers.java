package org.lab04;

public class UniquePhilosopherNumbers {
    private static int nextID = 0;

    synchronized public static int getID() {
        return nextID++;
    }

    synchronized public static void resetID() {
        nextID = 0;
    }
}
