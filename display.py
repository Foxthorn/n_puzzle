def print_puz(puz):
    for line in puz:
        print line
    print '\n'


def print_output(path, maxim, close, i, select, num_moves):
    path.reverse()
    for node in path:
        for line in node:
            print line
        print "\n"

    print 'Total number of states ever selected in the "opened" set: ', select
    print "Maximum number of states ever represented in memory at the same time during the search: ", maxim
    print "Maximum nodes held in open list: ", i
    print "Total nodes added to closed list: ", close
    print "Number of moves required to transition from the initial state to the final state," \
          " according to the search: ", num_moves - 1
