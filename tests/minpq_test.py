from datastructures.priorityqueue import minpriorityqueue


def run():
    print "minpriorityqueue TEST STARTING"
    pq = minpriorityqueue()

    pq.push((100, 10))
    pq.push((1, 5))
    pq.push((4, 1000))
    rank, key = pq.pop()
    assert rank == 1
    assert key == 5

    rank, key = pq.pop()
    assert rank == 4
    assert key == 1000

    rank, key = pq.pop()
    assert rank == 100
    assert key == 10

    assert pq.empty()

    print "minpriorityqueue TEST COMPLETED"

if __name__ == "__main__":
    run()
