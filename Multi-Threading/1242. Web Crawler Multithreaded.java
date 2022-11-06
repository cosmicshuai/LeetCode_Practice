/**
 * // This is the HtmlParser's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface HtmlParser {
 *     public List<String> getUrls(String url) {}
 * }
 */

class Solution {
    public List<String> crawl(String startUrl, HtmlParser htmlParser) {
        List<String> res = new ArrayList<String>();
        Deque<String> queue = new LinkedBlockingDeque<String>();
        Set<String> visited = new HashSet<String>();
        Deque<Future> tasks = new ArrayDeque<Future>();
        queue.offer(startUrl);
        String host = getHostName(startUrl);
        ExecutorService es = Executors.newFixedThreadPool(5, r -> {
            Thread t = new Thread(r);
            t.setDaemon(true);
            return t;
        });

        while(true) {
            String url = queue.poll();
            if (url != null) {
                if(getHostName(url).equals(host) && !visited.contains(url)) {
                    res.add(url);
                    visited.add(url);
                    tasks.add(es.submit(() -> {
                        List<String> urls = htmlParser.getUrls(url);
                        for (String u: urls) {
                            queue.offer(u);
                        }
                    }));
                }
            } else {
                if (!tasks.isEmpty()) {
                    Future curTask = tasks.poll();
                    try {
                        curTask.get();
                    } catch (InterruptedException | ExecutionException e) {}
                } else {
                    break;
                }
            }
        }

        return res; 
    }

    private String getHostName(String url) {
        url = url.substring(7);
        String[] parts = url.split("/");
        return parts[0];
    }
}