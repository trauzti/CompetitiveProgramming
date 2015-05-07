from datastructures.Stack import Stack


def run():
    print "Testing stack"
    s = Stack()
    i = 0
    for j in xrange(0,1000):
        s.push(j)

    val = 999
    while val >= 0:
        x = s.pop()
        assert x == val
        val -= 1
    assert s.size() == 0
    print "STACK TEST COMPLETED"

if __name__ == "__main__":
    run()
