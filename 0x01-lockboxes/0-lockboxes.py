#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    x = len(boxes)
    boxes_seen = set([0])
    boxes_unseen = set(boxes[0]).difference(set([0]))
    while len(boxes_unseen) > 0:
        boxIdx = boxes_unseen.pop()
        if not boxIdx or boxIdx >= x or boxIdx < 0:
            continue
        if boxIdx not in boxes_seen:
            boxes_unseen = boxes_unseen.union(boxes[boxIdx])
            boxes_seen.add(boxIdx)
    return x == len(boxes_seen)
