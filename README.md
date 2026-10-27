# RTL synthesis and netlist-equivalence flow

![Verification](https://github.com/SandeepGorrepati/rtl-to-gdsii-openroad-flow/actions/workflows/verify.yml/badge.svg)

A reproducible free-tool flow for a 32-bit combinational ALU: independent functional simulation, fresh Yosys synthesis, gate-level simulation, and formal combinational equivalence. The repository keeps its historical RTL-to-GDSII name; completed work stops at a generic gate-level netlist. No routed GDSII, Sky130 implementation, signoff timing, area in square micrometers, or power result is claimed.

## Design

Opcodes select addition/subtraction modulo 2^32, bitwise AND/OR/XOR, one-bit logical left/right shifts, and default zero. The shift amount is fixed at one; this is not a variable barrel shifter.

## Evidence

| Stage | Observed result |
|---|---|
| Python arithmetic oracle versus RTL | 8,200 vectors passed across all eight opcode values |
| Fresh Yosys synthesis | Generic logic netlist generated in CI |
| Same independent oracle versus synthesized netlist | 8,200 vectors passed |
| Yosys combinational equivalence | All 32 output-bit equivalence cells proven; zero unproven |

Vectors include a cross-product of boundary values and 1,000 deterministic random operand pairs, each exercised under every opcode. Python integer arithmetic supplies the expected data; neither the RTL nor the gate netlist computes its own test expectation. Formal equivalence covers the combinational input space relative to the RTL specification; it does not prove that the RTL matches an external ISA specification.

## Reproduce

Install Python 3, Icarus Verilog, and Yosys. From the root:

```bash
python3 scripts/gen_vectors.py
iverilog -g2012 -s tb_oracle -o build/rtl rtl/alu.v rtl/tb_oracle.v
vvp build/rtl
mkdir -p reports
yosys -s scripts/synth.ys
iverilog -g2012 -s tb_oracle -o build/gate reports/alu_netlist.v rtl/tb_oracle.v
vvp build/gate
yosys -s scripts/equiv.ys
```

CI saves fresh synthesis/equivalence logs and the generated netlist as artifacts. A scoreboard mismatch, timeout, synthesis error, or unproven equivalence fails the workflow. The older checked-in netlist/report are historical outputs; use a fresh run's artifacts for current tool-dependent cell statistics.

## Relationship to the timing exercise

This repository's design is a **32-bit combinational ALU**, with independent
RTL/netlist simulation and combinational equivalence as its main deliverables.
The separate [`synth-sta` learning exercise](https://github.com/SandeepGorrepati/synth-sta)
uses an **8-bit registered ALU** for synthesis statistics and timing-flow exploration.
They are distinct designs, not two completed RTL-to-GDSII projects.

## Physical implementation scope

Floorplanning, placement, clock-tree synthesis, routing, extraction, and GDSII export remain future work. There is no PDK/liberty/SDC-backed timing constraint or physical signoff in this repository. Generic-cell counts are not standard-cell area or a measured PPA result.

This supporting project demonstrates synthesis reproducibility and transformation verification. It is not presented as completed RTL-to-GDSII experience. See [upgrade validation](proof/UPGRADE_VALIDATION.md).
