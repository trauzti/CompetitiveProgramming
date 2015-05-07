from datastructures.queue import queue


def run():
    print "queue TEST STARTING"
    q = queue()
    i = 0
    LIMIT = 1000
    for j in xrange(0,LIMIT+1):
        q.push(j)

    for j in xrange(0, LIMIT+1):
        x = q.pop()
        assert x == j
    assert q.empty()
    print "queue TEST COMPLETED"

if __name__ == "__main__":
    run()
