# GIKAFE Cafeteria: Operations Management Project

**Course:** MS-492 Operations Management · **Term:** Spring 2026
**Institute:** GIK Institute of Engineering Sciences & Technology, Topi
**Instructor:** Dr. Muhammad Suhaib
**Textbook:** Heizer & Render: *Operations Management*, 12e

An integrated operations study of the GIKAFE main counter during the 12:00–14:00
peak lunch window. We applied three classical OM tools: **forecasting,
inventory control, and queueing analysis**, to diagnose long queues, occasional
stockouts, and the absence of any formal ordering policy.

---

## 1. The Problem

GIKAFE serves roughly **500 students** during a two-hour lunch window through a
**single service counter**. On-site observation revealed:

- Visible **6–8 person queues** at the peak.
- **Stockouts** on popular items before 14:00.
- **No demand forecasting** and **no formal inventory policy** in place.

**System boundary:** GIKAFE main counter only · 12:00–14:00 · 16 menu items ·
1 service line. Kitchen prep, breakfast, and dinner are out of scope.

## 2. Methodology

| # | Tool | Chapter | Purpose |
|---|---|---|---|
| 1 | **Forecasting** (SMA · WMA · Exponential Smoothing) | Heizer Ch. 4 | Predict daily demand for the top 5 items; compare via MAPE |
| 2 | **Inventory** (ABC · EOQ · ROP) | Heizer Ch. 12 | Classify 16 items by annual value; size optimal order quantities |
| 3 | **Queueing** (M/M/1) | Heizer Ch. D | Diagnose server utilisation and waiting time at the peak |

## 3. Data Collection

- **3 observation days** (Fri / Sat / Sun), 12:00–14:00 each.
- **51 timed observations** of arrivals and service durations.
- **511 customers** counted at the Friday peak.
- **Two-observer protocol:** one on stopwatch, one on tally + queue length.
- End-of-day totals **cross-checked** with the GIKAFE supervisor.
- Forecast actuals validated against a self-observed Monday 11-May trading day
  (sale invoice retained as proof of presence).

## 4. Key Results

**Forecasting:** Weighted Moving Average (WMA) gave the lowest mean MAPE
(~1.5% across the top 5 items) and was adopted as the daily ordering signal.

**Inventory:** EOQ and ROP for the Class-A items (lead time L = 1 day,
holding cost H = 15% of unit price, safety stock SS = 0.5 × mean daily demand,
313 working days/yr):

| Item | Annual D (units) | EOQ | ROP | Orders / yr |
|---|---:|---:|---:|---:|
| Chicken Biryani | 13,876 | 481 | 66 | 28.8 |
| Chicken Karhai + Rice | 9,286 | 273 | 45 | 34.0 |
| Daal Chawal | 13,876 | 430 | 66 | 32.3 |
| Chicken Tikka | 7,616 | 319 | 36 | 23.9 |
| Chicken Burger | 5,321 | 206 | 26 | 25.8 |
| Tea / Chai | 15,859 | 531 | 76 | 29.9 |

**Queueing (M/M/1):** λ = 4.06 cust/min at the full peak, μ = 1.03 cust/min,
giving **ρ = 3.92**: well above 1. A single server is mathematically
incapable of clearing the peak arrival rate, which explains the observed
6–8 person queues.

## 5. Recommendations

To restore ρ < 1 and stabilise the system:

1. **Increase μ:** add a second server or a dedicated Tea/Naan batch station;
   pre-pack Class-A items during 12:00–14:00.
2. **Decrease λ:** stagger class-break timings, or push QR-menu pre-orders to
   spread arrivals across a wider window.
3. **Pilot at off-peak:** validate the changes during 11:30 or 13:30 windows
   before scaling to full peak.

Pair these with **WMA-driven daily ordering** and **ROP-triggered replenishment
on Class-A items** for a complete operating policy.

## 6. Repository Contents

| File | Description |
|---|---|
| `OM_Project_Report.pdf` | Full written report submitted for evaluation (a hardcopy was also submitted to Sir) |
| `GIKAFE_OM_Project_Final.pptx` | 11-slide presentation deck |
| `Appendix_GIKAFE_Final.xlsx` | Raw observations, forecast workings, EOQ / ROP calculations, queueing model |
| `Inventory_Management_Viva_Guide.pdf` | Quick-revision viva guide: concepts, formulas, Q&A |
| `Capacity_Analysis_Viva_Guide.pdf` | Quick-revision viva guide: concepts, formulas, Q&A |
| `generate_viva_guides.py` | Python (reportlab) script that builds the two viva PDFs |

### Regenerating the viva guides

```bash
pip install reportlab
python generate_viva_guides.py
```

## 7. Authors

- **Ahmed Musharaf**: Reg# 2022067
- **Umar Mushtaq Mughal**: Reg# 2022602

---

> _Good luck with the viva!_ 🙂
