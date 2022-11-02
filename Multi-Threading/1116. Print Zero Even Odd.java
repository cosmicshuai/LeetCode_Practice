class ZeroEvenOdd {
    private int n;
    private Lock lock;
    private Condition cv0;
    private Condition cv1;
    private Condition cv2;
    private boolean zeroDone;
    private boolean oddDone;
    private boolean evenDone;
    
    public ZeroEvenOdd(int n) {
        this.n = n;
        this.lock = new ReentrantLock();
        this.zeroDone = false;
        this.oddDone = false;
        this.evenDone = true;
        this.cv0 = lock.newCondition();
        this.cv1 = lock.newCondition();
        this.cv2 = lock.newCondition();
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void zero(IntConsumer printNumber) throws InterruptedException {
        for(int i = 0; i < this.n; i++){    
            this.lock.lock();
            try {
                while (zeroDone) {
                    cv0.await();
                }

                printNumber.accept(0);
                zeroDone = true;
                if (oddDone) {
                    cv2.signal();
                } else {
                    cv1.signal();
                }
            } finally {
                this.lock.unlock();
            }
        }
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        for(int i = 1; i <= this.n; i++){
            if (i % 2 == 0) {
                continue;
            }

            this.lock.lock();
            try {
                while (!zeroDone || !evenDone) {
                    cv1.await();
                }

                printNumber.accept(i);
                oddDone = true;
                evenDone = false;
                zeroDone = false;
                cv0.signal();
            } finally {
                this.lock.unlock();
            }
        }
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        for(int i = 1; i <= this.n; i++){
            if (i % 2 != 0) {
                continue;
            }
            this.lock.lock();
            try {
                while (!zeroDone || !oddDone) {
                    cv2.await();
                }

                printNumber.accept(i);
                oddDone = false;
                evenDone = true;
                zeroDone = false;
                cv0.signal();
            } finally {
                this.lock.unlock();
            }
        }
    }
}