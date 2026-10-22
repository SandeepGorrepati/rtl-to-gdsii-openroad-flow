# Upgrade validation - 2026-10-22

Recorded run: https://github.com/SandeepGorrepati/rtl-to-gdsii-openroad-flow/actions/runs/39756423219

Validated code commit: a43706e02d9e3273635dae2d4c2bb38f70b479dd.

- 8,200 independent Python-oracle vectors passed against RTL.
- Fresh synthesis generated a generic logic netlist.
- The same 8,200 vectors passed against the freshly synthesized netlist.
- Yosys proved all 32 output equivalence cells with zero unproven; observed log: `Equivalence successfully proven!`

Full synthesis/equivalence logs and the generated netlist are workflow artifacts. These results establish combinational RTL/netlist equivalence for this ALU, not physical implementation, PPA, or timing signoff.
