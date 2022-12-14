#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Modificado a partir de:

# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(5, 2))
for label in ax.get_xaxis().get_ticklabels():
    label.set_fontweight("bold")

plt.tight_layout()
# plt.savefig("bold-ticklabel.pdf")
plt.show()