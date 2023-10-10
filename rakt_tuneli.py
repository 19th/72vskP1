# MakeCode https://makecode.com/_h6k0RV8RrPsF

#
# Rakt tuneli 3 bloku augstumā, kamēr netiksi līdz tukšumam
#
def on_mine():
    while agent.inspect(AgentInspection.BLOCK, FORWARD) != Block.AIR:
        agent.destroy(FORWARD)
        agent.move(FORWARD, 1)
        agent.destroy(UP)
        agent.destroy(DOWN)
        agent.collect_all()
    player.say("Done mining "+ agent.get_position())

# čatā "mine"
player.on_chat("mine", on_mine)


#
# Rakt tuneli noradīta augstumā, kamēr netiksi līdz tukšumam
#
def on_dig_up(height):
    while agent.inspect(AgentInspection.BLOCK, FORWARD) != Block.AIR:
        # bloks zemē
        agent.destroy(FORWARD)
        agent.move(FORWARD, 1)
        # parējie bloki
        for x in range(height - 1):
            agent.destroy(UP)
            agent.move(UP, 1)
        # atgriezties lejā
        agent.move(DOWN, height)
    player.say("Done digging "+ agent.get_position())

# čatā "dig 5"
player.on_chat("dig", on_dig_up)
