package org.lab05;

import java.util.concurrent.locks.ReentrantReadWriteLock;

class Node {
    Object value;
    Node next, prev;
    ReentrantReadWriteLock lock;

    public Node(Object value) {
        this.value = value;
        this.lock = new ReentrantReadWriteLock();
    }
}

public class ReadWriteList {
    private final Node sentinel = new Node(null);
    static final int MAX_SIZE = 15;
    private int size = 0;

    public boolean contains(Object o) {
        sentinel.lock.readLock().lock();
        if (sentinel.next == null){
            sentinel.lock.readLock().unlock();
            return false;
        }
        sentinel.next.lock.readLock().lock();
        Node current = sentinel.next;
        sentinel.lock.readLock().unlock();

        while (true) {
            if (current.value.equals(o)){
                current.lock.readLock().unlock();
                return true;
            }
            if (current.next == null){
                current.lock.readLock().unlock();
                return false;
            }

            current.next.lock.readLock().lock();
            current = current.next;
            current.prev.lock.readLock().unlock();
        }
    }

    public void add(Object o) {
        if (size >= MAX_SIZE) return;

        Node newNode = new Node(o);
        newNode.lock.writeLock().lock();

        sentinel.lock.writeLock().lock();
        Node current = sentinel;
        while (current.next != null){
            current.next.lock.writeLock().lock();
            current = current.next;
            current.prev.lock.writeLock().unlock();
        }
        current.next = newNode;
        newNode.prev = current;
        current.lock.writeLock().unlock();
        newNode.lock.writeLock().unlock();
        size++;
    }

    public boolean remove() {
        sentinel.lock.writeLock().lock();
        if (sentinel.next == null){
            sentinel.lock.writeLock().unlock();
            return false;
        }

        Node current = sentinel;
        while (current.next.next != null){
            current.next.lock.writeLock().lock();
            current = current.next;
            current.prev.lock.writeLock().unlock();
        }

        current.next = null;
        current.lock.writeLock().unlock();
        size--;
        return true;
    }
}
