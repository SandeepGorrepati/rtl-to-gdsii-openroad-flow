# Implemented flow notes

The verified flow is Python oracle -> RTL simulation -> Yosys generic synthesis -> gate-level simulation -> combinational equivalence. Commands and evidence are documented in README.md and proof/UPGRADE_VALIDATION.md.

Physical implementation stages are not executed here. Do not attribute generic-cell counts to Sky130, infer PPA, or describe existing screenshots as routed layout evidence. A physical-flow extension requires PDK setup, constraints, implementation scripts, generated layout, and timing/DRC evidence.
