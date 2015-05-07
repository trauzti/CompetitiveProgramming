from datastructures.stack import stack


def run():
    print "stack TEST STARTING"
    s = stack()
    i = 0
    for j in xrange(0,1000):
        s.push(j)

    val = 999
    while val >= 0:
        x = s.pop()
        assert x == val
        val -= 1
    assert s.empty()
    print "stack TEST COMPLETED"

if __name__ == "__main__":
    run()
