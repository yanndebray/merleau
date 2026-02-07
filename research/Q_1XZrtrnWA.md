# Beat Your Ghost - Cycling Data Analysis with MATLAB

**Source:** [https://youtu.be/Q_1XZrtrnWA](https://youtu.be/Q_1XZrtrnWA)
**Analyzed with:** ponty (merleau v0.3.1) | gemini-2.5-flash
**Cost:** $0.0226 | 144,843 prompt tokens | 1,510 response tokens

---

The video is a tutorial on how to analyze bicycle ride data to improve performance, focusing on comparing current rides with past "ghost" rides.

## Breakdown

### 1. Introduction (0:00-0:16)
The presenter introduces the topic, explaining that he wants to analyze his cycling performance over the summer in New England. The title "Beat Your Ghost" suggests a comparison with previous best performances.

### 2. Data Export (0:16-0:42)
- A map animation shows a bicycle route, indicating a cycling session.
- The presenter states he will export data from his smartwatch using Garmin and Strava apps.
- The goal is to "Improve performance over time."

### 3. Environment Setup (0:42-1:21)
- The presenter points to a GitHub repository where the code is available.
- He mentions the need to set up a Python environment in MATLAB Online, referencing a blog post about installing `pip` and `uv` in MATLAB Online. This implies the use of Python libraries within a MATLAB environment for data processing.

### 4. Data Cleaning & Derivation (1:21-2:38)
- The presenter opens a MATLAB Live Script titled "Cycling part 2."
- He briefly shows the table of contents and then jumps to the "Analysis" section, specifically "Clean & derive signals (once per ride)."
- He displays a timetable `TT` containing raw data (timestamp, latitude, longitude, distance, speed, altitude).
- The `prepRide(T)` function is used to process the raw data, including resampling to 1 Hz, smoothing altitude, and computing grade, acceleration, and moving time.
- He notes that he only stopped once during this particular ride.
- He plots "enhanced_altitude" and "alt_smooth" to show the altitude profile of the ride, noting it's a relatively flat road.
- A plot of "Grade" (road slope as a percentage) is displayed, confirming that the grades are small, so they won't significantly impact performance analysis for this ride.

### 5. Baseline Metrics (2:38-3:09)
- The presenter moves to "Baseline metrics (what matters for improvement)."
- He runs `baselineStats(TT)` to compute metrics like total distance, elevation gain, moving time, percentage stopped, speed percentiles (P50, P90), and Vertical Ascent Speed (VAM).
- A box chart is generated showing speed distribution across different grades (percentages), further illustrating the relatively flat terrain.

### 6. Power Estimation (3:09-4:22)
- The next section is "Power (no power meter? estimate it!)."
- He explains that a physics-based model can estimate power based on aerodynamic drag, rolling resistance, gravity, and inertia.
- The `estPower(TT)` function is used to calculate estimated power.
- A plot shows the "Estimated cycling power output from physics" in Watts over the ride duration.
- He introduces additional metrics derived from estimated power: Normalized Power (NP), FTP estimate (Functional Threshold Power), Intensity Factor (IF), and Training Stress Score (TSS). These are displayed in a struct `M`.

### 7. Power-Duration & Rolling Bests (4:22-5:33)
- The presenter explains the concept of a "power-duration curve," which plots maximum average power sustained for various durations (e.g., 5s sprint, 20min threshold). This helps identify physiological strengths and weaknesses.
- The `powerDuration(P)` function is used to compute these rolling averages.
- A table `pd` shows the best power (Watts) for different durations (5s, 15s, 30s, 1min, 2min, 5min, 10min, 20min).
- A log-log plot of the "Power-Duration Curve" is displayed, illustrating the relationship between duration and maximum sustainable power.

### 8. Route-Matched Comparison - "Your Ghost" (5:33-7:59)
- This section focuses on comparing two rides on the same route. He loads a previous ride (`df1` or `TT1`) from June 2025 and compares it to the current ride (`TT`) from September 2025.
- The `compareRides(TT, TT1)` function aligns the rides by distance and calculates the "time lead" (how much time one ride is ahead or behind the other at any given point).
- A "Time Lead vs Distance (colored by Grade)" plot is generated. The vertical lines in the plot indicate significant time differences, which the presenter explains are due to stops.
- He interprets the plot, highlighting that most of the time gap isn't from riding slower, but from stops. He also notes a steady loss of time between stops, suggesting a general pace difference. Grade coloring shows losses across all terrain.
- A bar chart "Time Lost/Gained by Grade Bin" visually represents where time was lost or gained across different road grades. He notes he loses most time on flats.
- The "Pacing & fatigue diagnostics" section introduces "decoupling," which measures the correlation between speed and estimated power. A large positive decoupling indicates fatigue, meaning the rider produces the same watts but doesn't maintain speed. The calculated decoupling for this ride is slightly negative, meaning it is not correlating much.
- Finally, he analyzes "Stops/slow coasts." He shows that for the newer ride (end of September), he stopped only once, while for the previous ride (end of June), he stopped 5 times for a total of 5.3 minutes and had 17.8 minutes of coasting.
- A `geoscatter` plot shows the "Stop locations" on the map for the June ride, explaining that he often stopped when using MATLAB Mobile to set up recordings.
- A pie chart titled "Ride time distribution" visually breaks down the time spent pedaling, coasting, and stopped during a ride.

### 9. Conclusion (7:59-8:12)
The presenter concludes by thanking the viewer, encouraging sharing and subscribing, and signing off.

## Summary

The video demonstrates a practical application of data analysis using MATLAB to track and improve cycling performance by comparing rides, estimating power, and diagnosing pacing and fatigue, with a particular focus on identifying time losses due to stops and other factors.
