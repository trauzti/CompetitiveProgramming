from datastructures.Queue import Queue


def run():
    print "Testing Queue"
    q = Queue()
    i = 0
    LIMIT = 1000
    for j in xrange(0,LIMIT+1):
        q.push(j)

    for j in xrange(0, LIMIT+1):
        x = q.pop()
        assert x == j
    assert q.size() == 0
    print "QUEUE TEST COMPLETED"

if __name__ == "__main__":
    run()
