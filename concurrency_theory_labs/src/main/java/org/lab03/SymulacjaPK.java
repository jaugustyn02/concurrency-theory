package org.lab03;


import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

class UnikalneNumery {
    private static int numerId = 0;
    synchronized public static int nowyID () {
        return numerId ++;
    }
}

class Producer extends Thread {
    private final Buffer _buf;
    private final Random random = new Random();

    public Producer(Buffer buf) {
        _buf = buf;
    }

    public void run() {
        for (int i = 0; i < 100; ++i) {
            try {
                TimeUnit.MILLISECONDS.sleep(random.nextInt(100));
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
            _buf.put();
        }
    }
}

class Consumer extends Thread {
    private final Buffer _buf;
    private final Random random = new Random();

    public Consumer(Buffer buf) {
        _buf = buf;
    }

    public void run() {
        for (int i = 0; i < 100; ++i) {
            try {
                TimeUnit.MILLISECONDS.sleep(random.nextInt(100));
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
            System.out.println("Ściągam pizze o numerze: " + _buf.get());
        }
    }
}

class Buffer {
    private final int buf_size;
    private final int[] tab;
    private int next_put_index = 0;
    private int next_get_index = 0;

    public Buffer(int buf_size){
        this.buf_size = buf_size;
        tab = new int[buf_size];
        for (int i=0; i < buf_size; i++){
            tab[i] = -1;
        }
    }

    synchronized public void put() {
        while (tab[next_put_index] != -1){
            try {
                wait();
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }

        int pizzaID = UnikalneNumery.nowyID();
        tab[next_put_index] = pizzaID;
        next_put_index = (next_put_index + 1) % buf_size;
        System.out.println("Dokładam pizze o numerze: " + pizzaID);

        notify();
    }

    synchronized public int get() {

        while (tab[next_get_index] == -1) {
            try {
                wait();
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }

        int pizzaID = tab[next_get_index];
        tab[next_get_index] = -1;
        next_get_index = (next_get_index + 1) % buf_size;

        notify();
        return pizzaID;
    }
}

public class SymulacjaPK {
    public static void main(String[] args) {
        Buffer buffer = new Buffer(20);

        int numOfProducers = 2;
        int numOfConsumers = 4;

        ExecutorService executor = Executors.newFixedThreadPool(numOfProducers + numOfConsumers);

        for (int i = 0; i < numOfProducers; i++) {
            Producer producer = new Producer(buffer);
            executor.execute(producer);
        }

        for (int i = 0; i < numOfConsumers; i++) {
            Consumer consumer = new Consumer(buffer);
            executor.execute(consumer);
        }


        try {
            Thread.sleep(20000);
        } catch (InterruptedException e) {
            System.out.println("Coś poszło nie tak ze sleep()");
        }

        executor.shutdownNow();
    }
}

