# Dynamic Relativity (DR)
**A Covariant Theory of Motion-Dependent Metric Scaling**

[ DOI: 10.5281/zenodo.18325668 ]

https://doi.org/10.5281/zenodo.18325668

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status: Research](https://img.shields.io/badge/Status-Academic_Preprint-blue.svg)](./paper/)
[![Python](https://img.shields.io/badge/Python-3.14.2%2B-green)](https://www.python.org/)

## 🌌 Overview
**Dynamic Relativity (DR)** is a proposed extension of General Relativity that abandons the "Rigid Measure Hypothesis." It posits that the stiffness of the spacetime metric is not a universal constant ($c^4/8\pi G$), but a dynamic variable governed by the **Total Stress Invariant** of the potential gradient.

By introducing a scalar field $\mu$ that saturates in high-stress environments and relaxes in low-stress environments, DR unifies the phenomenology of the "Dark Sector" with local anomalies in a single, parameter-free geometric framework.

This repository contains the **verification suite** for the theory, including the Python scripts used to analyze Gaia DR3 data, simulate Retarded Potentials, and verify the Earth Flyby Anomaly.

## 🔑 Key Results & Verification

### 1. The Red Dwarf Saturation Horizon (Gaia DR3)
* **The Prediction:** The transition from Newtonian to Galactic dynamics depends on the central mass ($r_{sat} \propto \sqrt{M}$). For Red Dwarf binaries ($0.8 M_{\odot}$), this horizon should shift inward to **2,500 AU** (vs. 4,000 AU for the Sun).
* **The Result:** A "Sniper Analysis" of 6,832 wide binaries in Gaia DR3 reveals a decisive departure from Newtonian dynamics beginning exactly in the **1,709–2,576 AU** bin.
* *See `src/analyze_gaia_binary.py`*

### 2. Strong-Field Vacuum Relaxation (LIGO)
* **The Prediction:** In the ringdown phase of a black hole merger, as the wave amplitude decays below the critical acceleration $a_0$, the local vacuum "relaxes," causing the damping time to increase ($\tau \to \tau(t)$).
* **The Result:** A residual analysis of **GW150914** reveals a positive relaxation parameter of $\alpha = +0.12$, reducing the residual error by **9.2%** compared to standard GR and eliminating systematic autocorrelation.
* *See `src/ligo_residual_analysis.py`*

### 3. The Earth Flyby Anomaly
* **The Prediction:** Spacecraft flybys exhibit a velocity boost due to the "Conformal Asymmetry" between the saturated bow shock (ingress) and the relaxed wake (egress).
* **The Result:** Integrating the conformal gradient along the Galileo I trajectory yields a predicted $\Delta V$ of **3.78 mm/s** (Observed: $3.92 \pm 0.3$ mm/s).
* *See `src/verify_flyby_anomaly.py`*

### 4. Dark Energy & Cosmology
* **The Mechanism:** At the cosmological horizon ($v > c$), the gradient norm becomes imaginary due to the Lorentzian signature. This inverts the metric coupling, turning gravity into repulsion.
* **The Result:** "Dark Energy" is identified as the repulsive back-reaction of the superluminal Hubble horizon, solving the Fine Tuning problem.

