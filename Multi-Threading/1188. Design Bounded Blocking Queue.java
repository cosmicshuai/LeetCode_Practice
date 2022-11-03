class BoundedBlockingQueue {
    private Deque<Integer> dq;
    private int capacity;
    private int size;
    private Lock lock;
    private Condition enqueCV;
    private Condition dequeCV;
    public BoundedBlockingQueue(int capacity) {
        this.dq = new LinkedList<Integer>();
        this.capacity = capacity;
        this.size = 0;
        this.lock = new ReentrantLock();
        this.enqueCV = this.lock.newCondition();
        this.dequeCV = this.lock.newCondition();
    }
    
    public void enqueue(int element) throws InterruptedException {
        this.lock.lock();
        try{
            while (this.size == capacity) {
                enqueCV.await();
            }

            this.dq.offerFirst(element);
            this.size++;
            dequeCV.signal();
        } finally {
            this.lock.unlock();
        }
    }
    
    public int dequeue() throws InterruptedException {
        this.lock.lock();
        int ans = 0;
        try{
            while (this.size == 0) {
                dequeCV.await();
            }

            ans = this.dq.removeLast();
            this.size--;
            enqueCV.signal();
        } finally {
            this.lock.unlock();
        }

        return ans;
    }
    
    public int size() {
        return this.size;
    }
}