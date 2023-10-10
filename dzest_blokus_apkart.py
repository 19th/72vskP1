# MakeCode https://makecode.com/_UDmAYyekRg9Y

def clear(size):
    # koordinātes norāda kastes diagonāles malas no kurai līdz kurai visus blokus aizvietot ar gaisu 
    blocks.fill(AIR, pos(-1 * size, 0, -1 * size), pos(size, size, size), FillOperation.DESTROY)

# izmantot ierakstot čatā "clear 5" vai "clear 15" utt
player.on_chat("clear", clear)
