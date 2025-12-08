#! /usr/bin/awk --exec
BEGIN {
    FS = ""
}

NR==1 {
    # Part One
    #   simply count the splitters encountered by beams paths
    splitters = 0

    # Part Two
    #   pathcounts accumulate the number of paths for each columns
    #   after the first line pathcounts is filled with 0 except at the S column where there is 1 path
    for (col = 0; col < NF; col++) {
        pathcounts[col] = 0
    }
    pathcounts[index($0, "S")] = 1
}

NR>1 {
    for (col = 0; col < NF; col++) {
        if ($col == "^") {
            count = pathcounts[col]

            # Part One
            #   +1 if a beam arrives at this splitter
            if (count != 0)
                splitters += 1

            # Part Two
            #   after a splitter, the count at the splitter column becomes 0
            #   and the counts at left and at right are increased by the count of paths ending at the splitter
            pathcounts[col] = 0
            pathcounts[col-1] += count
            pathcounts[col+1] += count
        }
    }
}

END {
    print "Part One: " splitters
    for (col in pathcounts) {
        sum += pathcounts[col]
    }
    print "Part Two: " sum
}
