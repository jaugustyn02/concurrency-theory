package org.lab02;

//class JakasKlasa{
//    private int stan=0;
//    public int nieZmieniajStanu(){
//        stan++;
//        stan--;
//        return stan;
//    }
//}
//
//class WatekJK extends Thread {
//    JakasKlasa jk; int n;
//    WatekJK(JakasKlasa jk, int n){
//        this.jk = jk;
//        this.n = n;
//    }
//    public void run(){
//        int tmp=0;
//        for(int i=0; i<n; i++){
//            tmp=jk.nieZmieniajStanu();
//            if(tmp!=0) break;
//        }
//        if(tmp!=0) System.out.println(Thread.currentThread().
//                getId()+" "+tmp);
//    }
//}
//
//public class Main {
//    public static void main(String[] args) {
//        System.out.println("Start");
//        JakasKlasa jk = new JakasKlasa();
//        for(int i=0; i<100; i++){
//            WatekJK wjk = new WatekJK(jk, 1000);
//            new Thread(wjk).start();
//        }
//        System.out.println("Koniec");
//    }
//}

// 5.2
// 1.
// (a)
//class Rewol extends Thread {
//    public void run(){
//        for (int i=5; i > 0; i--){
//            System.out.println(i);
//        }
//        System.out.println("Pif! Paf!");
//    }
//}
//
//public class Main {
//    public static void main(String[] args) {
//        System.out.println("Start");
//        for (int i = 0; i < 10; i++) {
//            Rewol r = new Rewol();
//            new Thread(r).start();
//        }
//        System.out.println("Koniec");
//    }
//}

// (b)
//class RewolNum extends Thread {
//    int num;
//    RewolNum(int num){
//        this.num = num;
//    }
//    public void run(){
//        for (int i=num; i > 0; i--){
//            System.out.println(i);
//        }
//        System.out.println("Pif! Paf!");
//    }
//}
//
//public class Main {
//    public static void main(String[] args) {
//        System.out.println("Start");
//        for (int i = 0; i < 20; i++) {
//            RewolNum r = new RewolNum(3);
//            new Thread(r).start();
//        }
//        System.out.println("Koniec");
//    }
//}

// (c)
//class RewolNumOne extends Thread {
//    int num;
//    static boolean pifPafPrinted = false;
//    RewolNumOne(int num){
//        this.num = num;
//    }
//    public void run(){
//            for (int i = num; i > 0; i--) {
//                synchronized (RewolNumOne.class) {
//                    if (pifPafPrinted) {
//                        return;
//                    }
//                }
//                System.out.println(i);
//            }
//            synchronized (RewolNumOne.class) {
//                if (!pifPafPrinted) {
//                    System.out.println("Pif! Paf!");
//                    pifPafPrinted = true;
//                }
//            }
//        }
//}
//
//public class Main {
//    public static void main(String[] args) {
//        System.out.println("Start");
//        for (int i = 0; i < 100; i++) {
//            RewolNumOne r = new RewolNumOne(3);
//            new Thread(r).start();
//        }
//        System.out.println("Koniec");
//    }
//}

//2.

//class Inc{
//    private int n=0;
//
//    public void increment(){
//        n++;
//    }
//
//    public int getN(){
//        return n;
//    }
//}
//
//class Thr extends Thread {
//    Inc inc;
//    Thr(Inc inc){
//        this.inc = inc;
//    }
//    public void run(){
//        for(int i=0; i<10000; i++){
//            inc.increment();
//        }
//        System.out.println("Liczba jest równa: "+inc.getN());
//    }
//}
//
//public class Main {
//    public static void main(String[] args) {
//        System.out.println("Start");
//        Inc inc = new Inc();
//        for (int i = 0; i < 2; i++) {
//            Thr thr = new Thr(inc);
//            new Thread(thr).start();
//        }
//        System.out.println("Koniec");
//    }
//}
