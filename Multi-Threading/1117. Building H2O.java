class H2O {
    private Semaphore sh;
    private Semaphore so;
    private int nh;

    public H2O() {
        sh = new Semaphore(0);
        so = new Semaphore(1);
        nh = 0;
    }

    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
		sh.acquire();
        // releaseHydrogen.run() outputs "H". Do not change or remove this line.
        releaseHydrogen.run();
        nh += 1;
        if (nh == 1) {
            sh.release();
        }

        if (nh == 2) {
            so.release();
        }

    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        
        // releaseOxygen.run() outputs "O". Do not change or remove this line.
        so.acquire();
		releaseOxygen.run();
        nh = 0;
        sh.release();
    }
}