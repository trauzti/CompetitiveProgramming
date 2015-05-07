from datastructures.minheap import minheap

def run():
    print "Testing MinHeap"
    arr = [5,1,2,3,5,14,2,3,5,6,1,2,3,4,5,6,9,8,10,11]
    h = minheap()
    for x in arr:
        h.push(x)

    assert h.pop() == 1
    assert h.pop() == 1
    assert h.pop() == 2
    assert h.pop() == 2
    assert h.pop() == 2
    assert h.pop() == 3
    print "MINHEAP TEST COMPLETED"

if __name__ == "__main__":
    run()
