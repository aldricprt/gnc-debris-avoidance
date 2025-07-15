# Experiment log: Kalman filter parameter exploration

**Date:** 2025-06-24
**Author:** Aldric Parent

## Objective
Explore and visualize the impact of different Kalman filter parameters (P, Q, R, initial state) on the estimation of a CubeSat's altitude in LEO, using simulated noisy measurements.

## Scenarios tested
- Smooth (high R, low Q)
- Reactive (low R, high Q)
- Bad init (wrong pos, high P)
- Rigid model (very low Q)
- Noisy sensor (very high R)
- Precise sensor (very low R)

## Method
- Simulated a realistic LEO altitude profile with sinusoidal perturbation.
- Added Gaussian noise to measurements (σ = 5 km).
- Ran the Kalman filter for each scenario, plotted results on a single figure.

## Results
- See `images/kalman_scenarios.png` for a comparative plot.
- Key observations:
    - High R (measurement noise): smoother but less reactive estimation.
    - High Q (process noise): more reactive, follows measurements closely.
    - High P (initial uncertainty): fast convergence even with bad initial state.
    - Low Q: rigid estimation, slow to adapt to real changes.
    - High R: ignores noisy measurements, slow adaptation.
    - Low R: follows measurements, more noise in estimation.

## Analysis
- The Kalman filter's performance is highly sensitive to the choice of Q, R, and P.
- A realistic initial velocity is crucial to avoid large initial jumps.
- The best trade-off depends on the sensor quality and the expected dynamics.

## Next steps
- Extend to 2D/3D orbits.
- Integrate with a controller for debris avoidance.
- Test on real or more complex simulated data.

---

*This log is part of the `kalman-scenarios-visualization` branch and documents the main findings for future reference and for showcasing the engineering approach.*
