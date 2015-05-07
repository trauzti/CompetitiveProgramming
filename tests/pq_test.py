from datastructures.pq import pq


def run():
    print "pq TEST STARTING"
    q = pq()
    i = 0
    LIMIT = 1000
    for j in xrange(0,LIMIT+1):
        q.push(j)

    for j in xrange(0, LIMIT+1):
        x = q.pop()
        assert x == j
    assert q.empty()
    print "pq TEST COMPLETED"

if __name__ == "__main__":
    run()
