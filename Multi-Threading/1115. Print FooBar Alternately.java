class FooBar {
    private int n;
    private Lock lock;
    private boolean fooDone;
    private boolean barDone;
    private Condition cv;

    public FooBar(int n) {
        this.n = n;
        this.lock = new ReentrantLock();
        this.barDone = true;
        this.fooDone = false;
        this.cv = this.lock.newCondition();
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            this.lock.lock();
        	// printFoo.run() outputs "foo". Do not change or remove this line.
            try {
                while (!barDone) {
                    cv.await();
                }

                barDone = false;
                fooDone = true;
                printFoo.run();
                cv.signalAll();
            } finally {
                this.lock.unlock();
            }
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            this.lock.lock();
        	// printBar.run() outputs "bar". Do not change or remove this line.
            try {
                while (!fooDone) {
                    cv.await();
                }

                fooDone = false;
                barDone = true;
                printBar.run();
                cv.signalAll();
            } finally {
                this.lock.unlock();
            }
        }
    }
}