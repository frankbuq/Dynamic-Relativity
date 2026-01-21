# Dynamic Relativity (DR)
**A Covariant Theory of Motion-Dependent Metric Scaling**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Research](https://img.shields.io/badge/Status-Academic_Preprint-blue.svg)](./paper/)

## 🌌 Overview
Dynamic Relativity is a proposed extension of General Relativity that abandons the "Rigid Measure Hypothesis." It posits that the stiffness of the spacetime metric is not a constant, but a dynamic variable governed by the **Total Stress Invariant** of the potential gradient.

This repository contains the **verification suite** for the theory, including the Python scripts used to analyze Gaia DR3 data, simulate Retarded Potentials, and verify the Earth Flyby Anomaly.

**Key Results:**
* **Dark Matter:** Derives the Baryonic Tully-Fisher Relation ($M \propto v^4$) from first geometric principles.
* **Dark Energy:** Identifies $\Lambda$ as the repulsive back-reaction of the superluminal Hubble horizon.
* **Flyby Anomaly:** Predicts a $\Delta V$ of **3.78 mm/s** for the Galileo I flyby (Observed: 3.92 mm/s).
* **Gaia Verification:** Detects a predicted "Saturation Horizon" in Red Dwarf binaries at **2,500 AU**.

## 📂 Repository Structure
* `paper/`: The complete LaTeX manuscript (v15.0 Maximalist Edition).
* `src/`: The Python code used to generate all figures and results.
* `plots/`: The visual outputs of the verification suite.

## 🚀 Getting Started

### Prerequisites
The code relies on the standard Python scientific stack.
```bash
pip install -r requirements.txt
