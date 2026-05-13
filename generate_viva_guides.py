"""Generate two viva revision guides: Inventory Management & Capacity Analysis."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
)


PRIMARY = HexColor("#1f3a5f")
ACCENT = HexColor("#c0392b")
LIGHT = HexColor("#eef2f7")
RULE = HexColor("#b0bec5")


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="TitleBig", fontName="Helvetica-Bold", fontSize=22, leading=26,
        textColor=PRIMARY, spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="Subtitle", fontName="Helvetica-Oblique", fontSize=12, leading=15,
        textColor=HexColor("#555555"), spaceAfter=18,
    ))
    styles.add(ParagraphStyle(
        name="H1", fontName="Helvetica-Bold", fontSize=15, leading=19,
        textColor=PRIMARY, spaceBefore=14, spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="H2", fontName="Helvetica-Bold", fontSize=12, leading=15,
        textColor=ACCENT, spaceBefore=10, spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        name="Body", fontName="Helvetica", fontSize=10.5, leading=14,
        alignment=TA_JUSTIFY, spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="BulletItem", fontName="Helvetica", fontSize=10.5, leading=14,
        leftIndent=14, bulletIndent=2, spaceAfter=3,
    ))
    styles.add(ParagraphStyle(
        name="Formula", fontName="Courier-Bold", fontSize=10.5, leading=14,
        textColor=PRIMARY, leftIndent=10, spaceBefore=2, spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        name="QA_Q", fontName="Helvetica-Bold", fontSize=10.5, leading=13,
        textColor=PRIMARY, spaceBefore=6, spaceAfter=2,
    ))
    styles.add(ParagraphStyle(
        name="QA_A", fontName="Helvetica", fontSize=10.5, leading=13,
        leftIndent=12, spaceAfter=4,
    ))
    return styles


def bullets(items, style):
    return [Paragraph(f"&bull;&nbsp;&nbsp;{it}", style) for it in items]


def info_box(text, styles):
    p = Paragraph(text, ParagraphStyle(
        name="Box", parent=styles["Body"], fontSize=10, leading=13,
        leftIndent=6, rightIndent=6, spaceBefore=4, spaceAfter=8,
    ))
    tbl = Table([[p]], colWidths=[16 * cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
        ("BOX", (0, 0), (-1, -1), 0.5, RULE),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return tbl


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(PRIMARY)
    canvas.rect(0, A4[1] - 1.2 * cm, A4[0], 1.2 * cm, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("Helvetica-Bold", 11)
    canvas.drawString(1.5 * cm, A4[1] - 0.8 * cm, doc.title)
    canvas.setFont("Helvetica", 9)
    canvas.drawRightString(A4[0] - 1.5 * cm, A4[1] - 0.8 * cm,
                           "Operations Management - Viva Revision Guide")
    canvas.setFillColor(HexColor("#666666"))
    canvas.setFont("Helvetica", 9)
    canvas.drawString(1.5 * cm, 1 * cm, f"Page {doc.page}")
    canvas.drawRightString(A4[0] - 1.5 * cm, 1 * cm,
                           "Quick reference - not a substitute for the textbook")
    canvas.setStrokeColor(RULE)
    canvas.line(1.5 * cm, 1.3 * cm, A4[0] - 1.5 * cm, 1.3 * cm)
    canvas.restoreState()


def styled_table(data, col_widths, styles):
    data = [[Paragraph(c, styles["Body"]) for c in row] for row in data]
    tbl = Table(data, colWidths=col_widths)
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), PRIMARY),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("GRID", (0, 0), (-1, -1), 0.4, RULE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, LIGHT]),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return tbl


# ---------------------------------------------------------------------------
# INVENTORY MANAGEMENT
# ---------------------------------------------------------------------------

def inventory_story(styles):
    s = []
    s.append(Paragraph("Inventory Management", styles["TitleBig"]))
    s.append(Paragraph(
        "Viva revision guide &mdash; key concepts, formulas, and quick-fire Q&amp;A",
        styles["Subtitle"]))

    s.append(Paragraph("1. What is Inventory?", styles["H1"]))
    s.append(Paragraph(
        "Inventory is the stock of any item or resource used in an organisation. It includes "
        "raw materials, work-in-progress (WIP), finished goods, and MRO (maintenance, repair, "
        "and operating) supplies. Inventory acts as a buffer between supply and demand, "
        "smoothing operations and protecting against uncertainty.",
        styles["Body"]))

    s.append(Paragraph("Types of Inventory", styles["H2"]))
    s.extend(bullets([
        "<b>Raw materials</b> &mdash; inputs awaiting use in production.",
        "<b>Work-in-progress (WIP)</b> &mdash; partially completed goods on the shop floor.",
        "<b>Finished goods</b> &mdash; ready-to-ship products.",
        "<b>MRO</b> &mdash; consumables for maintaining operations (lubricants, spares).",
        "<b>Pipeline / in-transit</b> &mdash; goods moving between stages or locations.",
    ], styles["BulletItem"]))

    s.append(Paragraph("2. Why Hold Inventory? (Functions)", styles["H1"]))
    s.extend(bullets([
        "<b>Decoupling</b> stages of production so a stoppage in one doesn't halt others.",
        "<b>Meeting anticipated demand</b> (seasonality, promotions).",
        "<b>Buffering uncertainty</b> in demand and supply (safety stock).",
        "<b>Economies of scale</b> via bulk purchasing and longer production runs (cycle stock).",
        "<b>Hedging</b> against price increases or currency fluctuations.",
        "<b>Pipeline inventory</b> for goods in transit.",
    ], styles["BulletItem"]))

    s.append(Paragraph("3. Inventory Costs &mdash; The Trade-off", styles["H1"]))
    s.append(info_box(
        "<b>Core idea:</b> inventory decisions balance the cost of <i>ordering / setting up</i> "
        "against the cost of <i>holding</i> stock, while keeping stockouts acceptably low. "
        "All EOQ-family models are variations on this trade-off.",
        styles))
    s.extend(bullets([
        "<b>Holding (carrying) cost &mdash; H</b>: storage, insurance, obsolescence, capital "
        "tied up. Usually 20&ndash;40% of unit cost per year.",
        "<b>Ordering / setup cost &mdash; S</b>: paperwork, transport, inspection, machine setup.",
        "<b>Purchase / item cost</b>: unit price (relevant under quantity discounts).",
        "<b>Stockout (shortage) cost</b>: lost sales, backorders, loss of goodwill.",
    ], styles["BulletItem"]))

    s.append(Paragraph("4. ABC Analysis (Pareto Classification)", styles["H1"]))
    s.append(Paragraph(
        "A selective control technique that classifies items by annual rupee usage so that "
        "managerial attention is focused where it matters most.",
        styles["Body"]))
    s.append(styled_table([
        ["Class", "% of items", "% of annual value", "Control"],
        ["A", "~10&ndash;20%", "~70&ndash;80%", "Tight: frequent review, accurate records"],
        ["B", "~30%", "~15&ndash;25%", "Moderate: periodic review"],
        ["C", "~50&ndash;60%", "~5&ndash;10%", "Simple: bulk orders, two-bin system"],
    ], [1.8 * cm, 3 * cm, 3.5 * cm, 7.7 * cm], styles))

    s.append(Paragraph("5. Economic Order Quantity (EOQ)", styles["H1"]))
    s.append(Paragraph(
        "EOQ gives the order quantity that minimises total annual inventory cost. Assumes "
        "constant demand, constant lead time, no stockouts, and no quantity discounts.",
        styles["Body"]))
    s.append(Paragraph("Key Formulas", styles["H2"]))
    s.append(Paragraph("EOQ  =  &radic;( 2 &times; D &times; S / H )", styles["Formula"]))
    s.append(Paragraph("Number of orders per year  =  D / EOQ", styles["Formula"]))
    s.append(Paragraph("Time between orders (T)    =  EOQ / D  (in years)", styles["Formula"]))
    s.append(Paragraph("Total annual cost  =  (D/Q)&times;S  +  (Q/2)&times;H  +  D&times;P",
                       styles["Formula"]))
    s.append(Paragraph(
        "Where D = annual demand, S = cost per order, H = holding cost per unit per year, "
        "P = unit price.",
        styles["Body"]))

    s.append(Paragraph("6. Reorder Point (ROP) &amp; Safety Stock", styles["H1"]))
    s.append(Paragraph("ROP  =  d &times; L  +  Safety Stock", styles["Formula"]))
    s.append(Paragraph("Safety Stock  =  Z &times; &sigma;<sub>dLT</sub>", styles["Formula"]))
    s.append(Paragraph(
        "d = average daily demand, L = lead time in days, Z = service-level factor "
        "(e.g. 1.65 for 95%, 2.33 for 99%), &sigma;<sub>dLT</sub> = std. deviation of demand "
        "during lead time. Higher service level &rArr; more safety stock &rArr; higher cost.",
        styles["Body"]))

    s.append(Paragraph("7. Inventory Control Systems", styles["H1"]))
    s.extend(bullets([
        "<b>Continuous (Q) system / Fixed-order-quantity</b>: order a fixed quantity (EOQ) "
        "whenever stock falls to ROP. Requires perpetual monitoring.",
        "<b>Periodic (P) system / Fixed-time-period</b>: review stock at fixed intervals and "
        "order up to a target level. Simpler but needs higher safety stock.",
        "<b>Two-bin system</b>: a visual reorder trigger &mdash; reorder when first bin empties.",
        "<b>VED analysis</b>: Vital, Essential, Desirable &mdash; used for spare parts.",
        "<b>FSN analysis</b>: Fast-moving, Slow-moving, Non-moving items.",
        "<b>HML analysis</b>: classification by unit price (High, Medium, Low).",
    ], styles["BulletItem"]))

    s.append(Paragraph("8. Modern Approaches", styles["H1"]))
    s.extend(bullets([
        "<b>Just-In-Time (JIT)</b>: receive goods only as needed; minimises inventory but "
        "demands reliable suppliers and stable demand.",
        "<b>Vendor-Managed Inventory (VMI)</b>: supplier monitors and replenishes buyer's stock.",
        "<b>Material Requirements Planning (MRP)</b>: computes dependent demand from a master "
        "production schedule and bill of materials.",
        "<b>ERP systems (e.g. SAP)</b>: integrate inventory with finance, sales, production.",
        "<b>RFID &amp; barcoding</b>: real-time visibility and accuracy.",
    ], styles["BulletItem"]))

    s.append(Paragraph("9. Key Performance Indicators", styles["H1"]))
    s.append(Paragraph("Inventory turnover  =  COGS / Average inventory", styles["Formula"]))
    s.append(Paragraph("Days of supply  =  365 / Inventory turnover", styles["Formula"]))
    s.append(Paragraph("Fill rate  =  Units shipped on time / Units ordered", styles["Formula"]))
    s.append(Paragraph("Other KPIs: stockout rate, carrying cost %, shrinkage rate, GMROI.",
                       styles["Body"]))

    s.append(PageBreak())
    s.append(Paragraph("10. Quick-Fire Viva Q&amp;A", styles["H1"]))

    qa = [
        ("What is the main objective of inventory management?",
         "To make items available when needed at the lowest total cost &mdash; balancing customer "
         "service against holding, ordering and stockout costs."),
        ("State the assumptions of the basic EOQ model.",
         "Constant demand; constant lead time; entire order received at once; no stockouts; "
         "no quantity discounts; only ordering and holding costs vary with quantity."),
        ("Why does EOQ occur where ordering cost equals holding cost?",
         "Because total cost = ordering + holding, and ordering cost decreases while holding "
         "cost increases with Q; the sum is minimum where the two curves intersect."),
        ("Difference between independent and dependent demand?",
         "Independent demand comes from the market (finished goods) and is forecast. "
         "Dependent demand is derived from independent demand via BOM (e.g. components), "
         "and is computed using MRP."),
        ("What is safety stock and what does it depend on?",
         "Extra stock held to protect against variability in demand or lead time. Depends on "
         "demand variability, lead-time variability, and the desired service level."),
        ("What is service level?",
         "The probability of not stocking out during the lead time, e.g. 95% means a 5% chance "
         "of a stockout per replenishment cycle."),
        ("Why is ABC analysis useful?",
         "It focuses managerial control on the few items that account for most of the value "
         "&mdash; tight control on A items, lighter control on C items."),
        ("Limitations of EOQ?",
         "Real demand is rarely constant; lead times vary; quantity discounts are common; "
         "capacity and shelf-life constraints are ignored."),
        ("What is JIT and what does it require?",
         "Just-In-Time aims for near-zero inventory by receiving inputs just as they are "
         "needed. Requires reliable suppliers, short setup times, quality at source, and "
         "stable schedules."),
        ("How is inventory turnover interpreted?",
         "Higher turnover means inventory is sold and replenished more frequently &mdash; often "
         "good, but excessively high turnover can indicate stockout risk."),
        ("What is the bullwhip effect?",
         "Amplification of demand variability as orders move upstream in a supply chain, "
         "caused by forecast updating, batching, price fluctuations and rationing."),
        ("Difference between Q-system and P-system?",
         "Q: fixed quantity ordered at variable times when stock hits ROP. "
         "P: variable quantity ordered at fixed time intervals, up to a target level."),
        ("How would you reduce inventory in a cafe / small business context?",
         "Improve demand forecasting, shorten supplier lead times, adopt FIFO, classify items "
         "(ABC / FSN), reduce SKUs, and use a simple two-bin or par-stock reorder system."),
    ]
    for q, a in qa:
        s.append(Paragraph(f"Q. {q}", styles["QA_Q"]))
        s.append(Paragraph(f"A. {a}", styles["QA_A"]))

    s.append(Paragraph("One-Minute Recap", styles["H1"]))
    s.append(info_box(
        "Inventory exists to <b>decouple</b> stages and <b>buffer uncertainty</b>. We classify "
        "items via <b>ABC</b>, decide order size using <b>EOQ</b>, decide <i>when</i> to order "
        "using <b>ROP = dL + safety stock</b>, and monitor performance through "
        "<b>turnover, fill rate and days of supply</b>. Modern systems &mdash; JIT, VMI, MRP, ERP "
        "&mdash; tighten this loop. The eternal trade-off is <b>holding vs ordering vs stockout</b> "
        "cost.",
        styles))
    return s


# ---------------------------------------------------------------------------
# CAPACITY ANALYSIS
# ---------------------------------------------------------------------------

def capacity_story(styles):
    s = []
    s.append(Paragraph("Capacity Analysis", styles["TitleBig"]))
    s.append(Paragraph(
        "Viva revision guide &mdash; key concepts, formulas, and quick-fire Q&amp;A",
        styles["Subtitle"]))

    s.append(Paragraph("1. What is Capacity?", styles["H1"]))
    s.append(Paragraph(
        "Capacity is the maximum rate of output of a process or facility over a given period. "
        "It is measured either in terms of <i>output</i> (units per hour) or <i>inputs</i> "
        "(machine-hours, labour-hours, seats, beds). Capacity decisions are long-term, "
        "capital-intensive, and difficult to reverse &mdash; they set the upper limit on what "
        "operations can deliver.",
        styles["Body"]))

    s.append(Paragraph("2. Types of Capacity", styles["H1"]))
    s.extend(bullets([
        "<b>Design capacity</b>: the maximum theoretical output under ideal conditions.",
        "<b>Effective capacity</b>: maximum possible output given product mix, scheduling "
        "difficulties, maintenance, quality factors and breaks.",
        "<b>Actual output</b>: what is really produced &mdash; always &le; effective capacity.",
        "<b>Rated / sustainable capacity</b>: realistic long-run output the firm can sustain.",
    ], styles["BulletItem"]))

    s.append(Paragraph("3. Key Measures &mdash; Efficiency &amp; Utilisation", styles["H1"]))
    s.append(Paragraph("Utilisation  =  Actual output / Design capacity", styles["Formula"]))
    s.append(Paragraph("Efficiency   =  Actual output / Effective capacity", styles["Formula"]))
    s.append(Paragraph("Expected output = Effective capacity &times; Efficiency", styles["Formula"]))
    s.append(info_box(
        "<b>Mnemonic:</b> Utilisation compares to the <i>dream</i> (design); Efficiency "
        "compares to the <i>realistic plan</i> (effective). Utilisation is always &le; "
        "Efficiency.",
        styles))

    s.append(Paragraph("4. Determinants of Effective Capacity", styles["H1"]))
    s.extend(bullets([
        "<b>Facilities</b>: size, layout, location, climate control.",
        "<b>Product / service</b>: design, standardisation, mix.",
        "<b>Process</b>: technology, automation, quality issues.",
        "<b>Human factors</b>: skills, motivation, training, absenteeism.",
        "<b>Policy</b>: shifts, overtime, work hours.",
        "<b>Operational</b>: scheduling, inventory, balancing of work.",
        "<b>Supply chain</b>: reliable suppliers, distribution.",
        "<b>External</b>: regulation, unions, pollution control.",
    ], styles["BulletItem"]))

    s.append(Paragraph("5. Capacity Planning Horizons", styles["H1"]))
    s.append(styled_table([
        ["Horizon", "Time frame", "Decisions"],
        ["Long-term", "&gt; 1 year", "Add plant, new technology, expansion"],
        ["Medium-term", "6&ndash;18 months", "Hiring, sub-contracting, additional shifts"],
        ["Short-term", "Daily &ndash; weekly", "Overtime, schedule changes, work transfers"],
    ], [3 * cm, 3 * cm, 10 * cm], styles))

    s.append(Paragraph("6. Capacity Strategies", styles["H1"]))
    s.extend(bullets([
        "<b>Lead strategy</b>: add capacity in anticipation of demand &mdash; captures market, "
        "but risks idle capacity.",
        "<b>Lag strategy</b>: add capacity only after demand is proven &mdash; conservative, "
        "but risks lost sales / dissatisfied customers.",
        "<b>Match (tracking) strategy</b>: add capacity in small increments to follow demand.",
        "<b>Capacity cushion</b> = 100% &minus; Utilisation. Higher cushion suits volatile "
        "demand; lower cushion suits stable, capital-intensive industries.",
    ], styles["BulletItem"]))

    s.append(Paragraph("7. Bottleneck Analysis &amp; Theory of Constraints", styles["H1"]))
    s.append(Paragraph(
        "The <b>bottleneck</b> is the resource with the lowest capacity in a process &mdash; it "
        "dictates the throughput of the entire system. Improving non-bottleneck resources does "
        "<i>not</i> increase output. Goldratt's <b>Theory of Constraints (TOC)</b> formalises "
        "this insight.",
        styles["Body"]))
    s.append(Paragraph("Five Focusing Steps of TOC", styles["H2"]))
    s.extend(bullets([
        "<b>Identify</b> the system's constraint.",
        "<b>Exploit</b> the constraint (squeeze maximum output from it).",
        "<b>Subordinate</b> everything else to the constraint.",
        "<b>Elevate</b> the constraint (add capacity if needed).",
        "<b>Repeat</b> &mdash; once broken, a new constraint will appear; do not let inertia "
        "set in.",
    ], styles["BulletItem"]))
    s.append(Paragraph("Throughput  =  min(capacity of each stage)", styles["Formula"]))
    s.append(Paragraph("Cycle time  =  1 / Throughput rate", styles["Formula"]))

    s.append(Paragraph("8. Break-Even Analysis", styles["H1"]))
    s.append(Paragraph(
        "Used to find the volume at which total revenue equals total cost &mdash; a key input "
        "to capacity sizing.",
        styles["Body"]))
    s.append(Paragraph("Break-even (units)  Q*  =  FC / (P &minus; VC)", styles["Formula"]))
    s.append(Paragraph("Break-even (revenue) =  FC / (1 &minus; VC/P)", styles["Formula"]))
    s.append(Paragraph("Profit  =  Q &times; (P &minus; VC) &minus; FC", styles["Formula"]))
    s.append(Paragraph(
        "FC = fixed cost, VC = variable cost per unit, P = price per unit. Larger capacity "
        "raises FC but typically lowers VC &mdash; the choice depends on expected volume.",
        styles["Body"]))

    s.append(Paragraph("9. Decision Tools", styles["H1"]))
    s.extend(bullets([
        "<b>Decision trees</b>: structure capacity choices under uncertainty using "
        "Expected Monetary Value (EMV).",
        "<b>Waiting-line (queuing) analysis</b>: size service capacity to balance customer "
        "wait against staffing cost.",
        "<b>Simulation</b>: model variability where formulas don't apply.",
        "<b>Linear programming</b>: allocate limited capacity across products to maximise profit.",
        "<b>Learning curves</b>: forecast capacity gains from experience.",
    ], styles["BulletItem"]))

    s.append(Paragraph("10. Economies &amp; Diseconomies of Scale", styles["H1"]))
    s.extend(bullets([
        "<b>Economies of scale</b>: average cost falls as output rises &mdash; fixed costs "
        "spread, bulk discounts, specialisation.",
        "<b>Diseconomies of scale</b>: average cost rises beyond a point &mdash; coordination "
        "overhead, complexity, fatigue, distribution costs.",
        "Each plant has an optimal operating level; <b>best operating level</b> is the volume "
        "at which average unit cost is minimised.",
    ], styles["BulletItem"]))

    s.append(PageBreak())
    s.append(Paragraph("11. Worked Mini-Example", styles["H1"]))
    s.append(info_box(
        "A bakery has a design capacity of 1,000 loaves/day. Effective capacity is 800 "
        "loaves/day after allowing for cleaning and changeover. Actual output is 720 loaves/day."
        "<br/><br/>"
        "<b>Utilisation</b> = 720 / 1000 = <b>72%</b><br/>"
        "<b>Efficiency</b>  = 720 / 800  = <b>90%</b><br/><br/>"
        "If demand rises to 900 loaves/day, the bakery cannot meet it within effective "
        "capacity &mdash; options: overtime (short-term), extra shift (medium-term), or new "
        "oven (long-term).",
        styles))

    s.append(Paragraph("12. Quick-Fire Viva Q&amp;A", styles["H1"]))
    qa = [
        ("Define capacity.",
         "The maximum rate of output a process or facility can achieve over a given time, "
         "expressed in units of output or input."),
        ("Difference between design and effective capacity?",
         "Design is the ideal-conditions maximum. Effective capacity is what is realistically "
         "achievable given product mix, scheduling, maintenance and quality losses."),
        ("Why is utilisation always &le; efficiency?",
         "Because design capacity &ge; effective capacity, and both ratios use actual output "
         "in the numerator. So dividing by the larger denominator gives a smaller fraction."),
        ("What is a bottleneck and why does it matter?",
         "The lowest-capacity stage in a process &mdash; it caps the throughput of the entire "
         "system, so improvements elsewhere have no effect on output."),
        ("What is a capacity cushion?",
         "The amount of capacity in excess of expected demand, i.e. 100% &minus; utilisation. "
         "Used as a buffer against demand or supply variability."),
        ("When would you choose a lead strategy over a lag strategy?",
         "When growth is rapid and predictable, the cost of lost sales is high, or being "
         "first to market is strategically important."),
        ("Explain the Theory of Constraints in one line.",
         "A system's output is governed by its weakest link; focus improvement on the "
         "constraint and subordinate everything else to it."),
        ("How do you do break-even capacity analysis?",
         "Compute Q* = FC / (P &minus; VC) for each capacity alternative; pick the option whose "
         "break-even volume sits comfortably below expected demand."),
        ("What are economies and diseconomies of scale?",
         "Economies: average cost falls as scale grows (fixed-cost spreading, bulk buying). "
         "Diseconomies: beyond an optimal point, coordination and complexity push average "
         "cost back up."),
        ("How does product mix affect capacity?",
         "Different products have different processing times. A richer mix or more setups "
         "reduces effective capacity even though design capacity is unchanged."),
        ("What is the role of forecasting in capacity planning?",
         "Capacity is committed long before demand is realised &mdash; forecasts of volume, mix "
         "and growth drive the size, timing and type of capacity added."),
        ("How would you analyse capacity for a cafe?",
         "Identify the bottleneck (counter / espresso machine / seating), measure throughput "
         "per hour, calculate utilisation during peak vs off-peak, and use queuing analysis "
         "to size staff and equipment for the peak demand."),
        ("Why is capacity decision strategic?",
         "It commits large capital, is hard to reverse, sets a ceiling on revenue, affects "
         "cost structure and competitive position."),
    ]
    for q, a in qa:
        s.append(Paragraph(f"Q. {q}", styles["QA_Q"]))
        s.append(Paragraph(f"A. {a}", styles["QA_A"]))

    s.append(Paragraph("One-Minute Recap", styles["H1"]))
    s.append(info_box(
        "Capacity = max output. We distinguish <b>design</b> vs <b>effective</b> vs <b>actual</b>, "
        "and measure performance via <b>utilisation</b> and <b>efficiency</b>. Capacity is "
        "planned across <b>long, medium and short</b> horizons, using <b>lead, lag or match</b> "
        "strategies. Throughput is set by the <b>bottleneck</b> &mdash; the Theory of Constraints "
        "says: identify, exploit, subordinate, elevate, repeat. <b>Break-even analysis, decision "
        "trees and queuing models</b> support the choice. Watch out for the curve of "
        "<b>economies vs diseconomies</b> of scale.",
        styles))
    return s


def build_pdf(filename, title, story_fn):
    doc = SimpleDocTemplate(
        filename, pagesize=A4,
        leftMargin=1.8 * cm, rightMargin=1.8 * cm,
        topMargin=1.8 * cm, bottomMargin=1.6 * cm,
        title=title, author="Operations Management Project",
    )
    doc.title = title
    styles = build_styles()
    doc.build(story_fn(styles), onFirstPage=header_footer, onLaterPages=header_footer)
    print(f"  wrote {filename}")


if __name__ == "__main__":
    build_pdf("Inventory_Management_Viva_Guide.pdf",
              "Inventory Management", inventory_story)
    build_pdf("Capacity_Analysis_Viva_Guide.pdf",
              "Capacity Analysis", capacity_story)
    print("Done.")
