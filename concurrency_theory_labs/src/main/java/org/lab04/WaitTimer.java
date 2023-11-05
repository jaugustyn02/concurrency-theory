package org.lab04;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class WaitTimer {
    private final long[] waitingTimes;
    private final long[] waitingCounts;
    private final int numOfPhilosophers;
    private final Philosopher.PhilosopherType philosophersType;

    public WaitTimer(int numOfPhilosophers, Philosopher.PhilosopherType type){
        this.numOfPhilosophers = numOfPhilosophers;
        this.waitingTimes = new long[numOfPhilosophers];
        this.waitingCounts = new long[numOfPhilosophers];
        this.philosophersType = type;
    }

    synchronized public void addTime(int philosopherID, long time, long count){
        this.waitingTimes[philosopherID] = time;
        this.waitingCounts[philosopherID] = count;
    }

    public void printTimes(){
        System.out.println("\nVARIANT: " + philosophersType);
        System.out.println("NUMBER OF THREADS: " + numOfPhilosophers);
        System.out.println("TIME (NS):");
        for (int i=0; i < numOfPhilosophers; i++){
            Long averageTime = null;
            if (waitingCounts[i] != 0)
                averageTime = waitingTimes[i] / waitingCounts[i];

            System.out.print("THREAD "+ i + ":\taverage time = " + averageTime);
            System.out.println(", count = " + waitingCounts[i] + ", time = " + waitingTimes[i]);
        }
    }

    public void saveTimeMeasurementsAsCSV(String filePath) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {
            writer.write("PhilosopherID, Average Time (ns), Count, Total Time (ns)");
            writer.newLine();

            for (int i = 0; i < waitingTimes.length; i++) {
                long time = waitingTimes[i];
                long count = waitingCounts[i];
                long averageTime = (count == 0) ? 0 : time / count;

                String line = i + ", " + averageTime + ", " + count + ", " + time;
                writer.write(line);
                writer.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}