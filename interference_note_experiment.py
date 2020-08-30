#!/usr/bin/env python3
# Recreation of double slit experiment from
# https://www.wolframphysics.org/bulletins/2020/08/a-short-note-on-the-double-slit-experiment-and-other-quantum-interference-effects-in-the-wolfram-model/

from src.slit_exp import SlitExp
two_slit = SlitExp((-2,2))
two_slit.run(10)
two_slit.show_distribution()
#two_slit.show_density()

three_slit = SlitExp((-1,0,1))
three_slit.run(10)
three_slit.show_distribution()
