package org.lab05;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ReadWriteListTest {
    public static void main(String[] args) {
        final ReadWriteList list = new ReadWriteList();
        ExecutorService executor = Executors.newFixedThreadPool(3);

        executor.execute(() -> {
            for (int i = 0; i < 30; i++) {
                list.add("test");
                System.out.println("[Thread 1]: Added a value");
            }
        });

        executor.execute(() -> {
            for (int i = 0; i < 30; i++) {
                if (list.remove()) {
                    System.out.println("[Thread 2]: removed the last element");
                } else {
                    System.out.println("[Thread 2]: couldn't remove the last element");
                }
            }
        });

        executor.execute(() -> {
            for (int i = 0; i < 10; i++) {
                if (list.contains("test")) {
                    System.out.println("[Thread 3]: found the value");
                } else {
                    System.out.println("[Thread 3]: didn't find the value");
                }
            }
        });

        executor.shutdown();
    }
}
