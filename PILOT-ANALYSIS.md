# Pilot analysis

Fill `PILOT-FORM.csv` with participant codes and scores. Then:

```bash
python tools/analyze_pilot.py
```

Outputs:

- participant count;
- number of scored rows;
- median exit-ticket score;
- mean confidence and mean score;
- calibration gap;
- mean SUS.

Do not report percentages without the denominator. Do not generalise from five people.
