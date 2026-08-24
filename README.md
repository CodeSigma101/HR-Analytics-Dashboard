# Achievo for Naivas - HR Analytics Dashboard
#### App Link: https://hr-analytics-dashboard-awf4rpedxfnatr7ylrses9.streamlit.app/

This is a dashboard built for Achievo Limited to manage staff for Naivas Supermarket.

Think of it like a control room where you can see everything happening in all Naivas stores from one screen.

## What is this dashboard for?

Naivas has over 113 stores across Kenya and over 9,000 staff. Achievo helps Naivas hire and manage some of these staff, like:
- Loss Control Officers (security)
- Cleaners and Hygiene Auditors
- Cashiers and Shelf Attendants
- Supervisors

Before this dashboard, all this information was in Excel sheets. This dashboard puts it in one place with charts and numbers.

## What can you see in the dashboard?

The dashboard has 6 tabs. Each tab shows different information:

### 1. Store Overview
This is the first screen you see. It shows:
- How many staff are in each county
- Which stores have the most problems (incidents)
- How many staff are in each store

Example: If you select Kiambu County, you will only see the 8 stores in Kiambu and the 1,070 staff who work there.

### 2. HR and Payroll
This shows money and people:
- How many staff are active (still working) vs exited (left)
- Total salary paid per month (payroll)
- How many staff left the job (attrition)
- Salary distribution - how many people earn 20k, 30k, 40k etc.

Realistic figures:
- A Cleaner earns KES 18,000 to 25,000
- A Loss Control Officer earns KES 30,000 to 45,000
- A Supervisor earns KES 45,000 to 75,000
- One branch has 70 to 250 staff, average is 150 staff

### 3. Recruitment
This shows how Achievo hires people:
Applicants (2,250 people apply) -> Screened (1,125) -> Vetted (810) -> Trained (720) -> Deployed (648 staff sent to stores)

It also tracks Time to Fill - how many days it takes to fill an empty position. Naivas wants this to be less than 14 days.

### 4. Loss Prevention
Naivas loses money through theft and damage. This is called shrinkage.

This tab shows:
- Which stores lose the most money
- How much money is lost per store
- Number of incidents (theft cases)

Example: Naivas Nyali Centre might have KES 120,000 loss this month. Without Achievo officers, it would be 2.8 times higher.

### 5. Hygiene
Naivas needs to be clean. Auditors give each store a hygiene score from 0% to 100%.

Target is >90%. This tab shows:
- Hygiene score per county
- Which counties are cleanest
- Stores below 90% need attention

### 6. Value & ROI (Return on Investment)
This is the most important tab for the boss.

It answers: Why should Naivas pay Achievo?

It shows:
- **Money saved from theft prevention:** Example: KES 2.1M saved in Kiambu County alone
- **Money saved on HR costs:** Achievo charges KES 5,200 per staff to manage them. If Naivas did it themselves, it would cost KES 8,500 per staff. So Naivas saves 37%.
- **Before vs After Achievo:** Before Achievo, it took 28 days to hire someone. After Achievo, it takes 9.5 days. Before Achievo, hygiene was 76%. After Achievo, it is 91%.
- **SLA Compliance:** SLA means Service Level Agreement - a promise. Achievo promised 98% of positions will be filled in under 14 days. They achieved 98.7%.

Total ROI is 342% - meaning for every 1 KES Naivas pays Achievo, they get back 3.4 KES in savings.

## How does the filtering work?

At the left side of the screen, there are filters:

1. **Select County:** Choose one or more counties. Example: Kiambu, Nairobi, Mombasa.
2. **Select Store:** Once you pick a county, the store list changes to show only stores in that county. If you pick Kiambu, you will see only 8 Kiambu stores: Kiambu Mall, Spur Mall Ruiru, Juja City Mall, etc.
3. **Select Department:** HR, Hygiene, Loss Prevention, Operations.

Everything in the dashboard updates automatically when you change the filter.

Example:
- Pick County = Kiambu
- The dashboard now shows: 1,070 staff, 8 stores, KES 32M payroll, and all charts show only Kiambu data.
- Pick County = Nairobi
- Now it shows 2,280 staff, 15 stores, KES 68M payroll, Nairobi only.

## Real Naivas Stores Used

We are using real Naivas branch names, not fake names:

**Nairobi (15 stores):** CBD Ronald Ngala, Westgate, The Greenhouse, Prestige Plaza, Mountain Mall, Greenspan Donholm, Eastgate, Ciata Ridgeways, Development House, Buruburu, Umoja, Kasarani Mwiki, Embakasi, Utawala Mihango, South B

**Kiambu (8 stores):** Kiambu Mall, Spur Mall Ruiru, Juja City Mall, Gachie Westbay Mall, Ruaka, Limuru Kijabe, Kinoo, TRM Roysambu

**Nakuru (7 stores):** Midtown Kenyatta Ave, Highway Milimani, Naivasha Main, Naivasha Self Service, Gilgil, Molo, Kabati

**Mombasa (5 stores):** Nyali Centre, Likoni Mall, Bamburi Mwembeni, Mombasa CBD Digo Road, Mtwapa

**Kisumu (5 stores):** Simba Club Hall (largest Naivas in Kenya - 250 staff), Mega City Mall, Kisumu CBD, Lake Basin Mall, United Mall

**Uasin Gishu (5 stores):** Zion Mall Eldoret, Eldoret Town Oginga Odinga, Eldoret Highway, Kapsoya, Elgon View

## How to Run the Dashboard

You need Python installed.

1. Install required tools:

2. Make sure you have two files in the same folder:
- dash.py (the main code)
- style.css (the colors and design - Naivas Red #E30613, Naivas Navy #0A1931)

3. Run the dashboard:

4. It will open in your browser at http://localhost:8501

## How to Use Your Own Data

If you have a real Excel file from Naivas with staff data, you can upload it:

Click "Upload Weekly HR Data" on the left side and upload your CSV or Excel file.

Your file should have these columns:
EmployeeID, Store, County, Role, Department, HireDate, Status, Salary, Incidents, ValueOfLoss, Attendance, HygieneScore, TimeToFill

If you don't upload anything, the dashboard creates demo data automatically with realistic figures (150 staff per branch average).

## Who Built This?

Built for Achievo Limited
Client: Naivas Supermarket
Purpose: To show Naivas how Achievo adds value and to manage daily HR operations

Total staff managed in this demo: 6,500+ across 45 stores in 6 counties (real total is 113 stores)
