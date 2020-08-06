import cellpylib as cpl


cellular_automaton = cpl.init_random2d(600, 600)


# evolve the cellular automaton for 60 time steps
cellular_automaton = cpl.evolve2d(
    cellular_automaton,
    timesteps=60,
    neighbourhood='Moore',
    apply_rule=cpl.game_of_life_rule,
)

cpl.plot2d_animate(cellular_automaton)
