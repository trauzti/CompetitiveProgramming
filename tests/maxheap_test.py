from datastructures.maxheap import maxheap

def run():
    print "maxheap TEST STARTING"
    arr = [5,1,2,3,5,14,2,3,5,6,1,2,3,4,5,6,9,8,10,11]
    h = maxheap()
    for x in arr:
        h.push(x)

    assert h.pop() == 14
    assert h.pop() == 11
    assert h.pop() == 10
    assert h.pop() == 9
    assert h.pop() == 8
    print "maxheap TEST COMPLETED"

if __name__ == "__main__":
    run()
