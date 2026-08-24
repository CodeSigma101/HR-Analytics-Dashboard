import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="Achievo for Naivas", layout="wide")

def load_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except:
        pass

load_css("style.css")

NAIVAS_RED = "#E30613"
NAIVAS_NAVY = "#0A1931"
NAIVAS_GREEN = "#00A651"
ACHIEVO_ORANGE = "#FF6B35"
ACHIEVO_BLUE = "#0052CC"

STORES_BY_COUNTY = {
    'Nairobi': [
        'Naivas CBD Ronald Ngala', 'Naivas Westgate', 'Naivas The Greenhouse',
        'Naivas Prestige Plaza', 'Naivas Mountain Mall', 'Naivas Greenspan Donholm',
        'Naivas Eastgate', 'Naivas Ciata Ridgeways', 'Naivas Development House',
        'Naivas Buruburu', 'Naivas Umoja', 'Naivas Kasarani Mwiki', 'Naivas Embakasi',
        'Naivas Utawala Mihango', 'Naivas South B'
    ],
    'Kiambu': [
        'Naivas Kiambu Mall', 'Naivas Spur Mall Ruiru', 'Naivas Juja City Mall',
        'Naivas Gachie Westbay Mall', 'Naivas Ruaka', 'Naivas Limuru Kijabe',
        'Naivas Kinoo', 'Naivas TRM Roysambu'
    ],
    'Nakuru': [
        'Naivas Midtown Kenyatta Ave', 'Naivas Highway Milimani', 'Naivas Naivasha Main',
        'Naivas Naivasha Self Service', 'Naivas Gilgil', 'Naivas Molo', 'Naivas Kabati'
    ],
    'Mombasa': [
        'Naivas Nyali Centre', 'Naivas Likoni Mall', 'Naivas Bamburi Mwembeni',
        'Naivas Mombasa CBD Digo Road', 'Naivas Mtwapa'
    ],
    'Kisumu': [
        'Naivas Simba Club Hall', 'Naivas Mega City Mall', 'Naivas Kisumu CBD',
        'Naivas Lake Basin Mall', 'Naivas United Mall'
    ],
    'Uasin Gishu': [
        'Naivas Zion Mall Eldoret', 'Naivas Eldoret Town Oginga Odinga',
        'Naivas Eldoret Highway', 'Naivas Kapsoya', 'Naivas Elgon View'
    ]
}

STORE_SIZES = {
    'Naivas CBD Ronald Ngala': 220, 'Naivas Westgate': 180, 'Naivas The Greenhouse': 150,
    'Naivas Prestige Plaza': 140, 'Naivas Mountain Mall': 160, 'Naivas Greenspan Donholm': 155,
    'Naivas Eastgate': 145, 'Naivas Ciata Ridgeways': 130, 'Naivas Development House': 200,
    'Naivas Buruburu': 135, 'Naivas Umoja': 125, 'Naivas Kasarani Mwiki': 140, 'Naivas Embakasi': 150,
    'Naivas Utawala Mihango': 120, 'Naivas South B': 130, 'Naivas Kiambu Mall': 150,
    'Naivas Spur Mall Ruiru': 145, 'Naivas Juja City Mall': 160, 'Naivas Gachie Westbay Mall': 110,
    'Naivas Ruaka': 130, 'Naivas Limuru Kijabe': 90, 'Naivas Kinoo': 100, 'Naivas TRM Roysambu': 170,
    'Naivas Midtown Kenyatta Ave': 180, 'Naivas Highway Milimani': 140, 'Naivas Naivasha Main': 150,
    'Naivas Naivasha Self Service': 110, 'Naivas Gilgil': 80, 'Naivas Molo': 75, 'Naivas Kabati': 70,
    'Naivas Nyali Centre': 190, 'Naivas Likoni Mall': 120, 'Naivas Bamburi Mwembeni': 130,
    'Naivas Mombasa CBD Digo Road': 160, 'Naivas Mtwapa': 110, 'Naivas Simba Club Hall': 250,
    'Naivas Mega City Mall': 200, 'Naivas Kisumu CBD': 170, 'Naivas Lake Basin Mall': 140,
    'Naivas United Mall': 150, 'Naivas Zion Mall Eldoret': 180, 'Naivas Eldoret Town Oginga Odinga': 160,
    'Naivas Eldoret Highway': 130, 'Naivas Kapsoya': 90, 'Naivas Elgon View': 100
}

def generate_demo_data():
    np.random.seed(42)
    roles = ['Loss Control Officer','Supervisor','Cleaner','Cashier Support','Hygiene Auditor','Cashier','Shelf Attendant']
    role_weights = [0.12, 0.10, 0.25, 0.15, 0.08, 0.18, 0.12]
    all_data = []
    emp_id = 1
    for county, stores in STORES_BY_COUNTY.items():
        for store in stores:
            staff_count = STORE_SIZES.get(store, 150)
            for _ in range(staff_count):
                role = np.random.choice(roles, p=role_weights)
                if role == 'Cleaner':
                    salary = np.random.randint(18000, 25000)
                elif role == 'Shelf Attendant':
                    salary = np.random.randint(20000, 28000)
                elif role == 'Cashier':
                    salary = np.random.randint(22000, 30000)
                elif role == 'Cashier Support':
                    salary = np.random.randint(20000, 28000)
                elif role == 'Hygiene Auditor':
                    salary = np.random.randint(35000, 50000)
                elif role == 'Loss Control Officer':
                    salary = np.random.randint(30000, 45000)
                else:
                    salary = np.random.randint(45000, 75000)

                if role == 'Loss Control Officer':
                    incidents = np.random.poisson(0.3)
                    value_loss = np.random.exponential(3000) if incidents > 0 else 0
                else:
                    incidents = np.random.poisson(0.8)
                    value_loss = np.random.exponential(12000) if incidents > 0 else 0

                all_data.append({
                    'EmployeeID': emp_id,
                    'Store': store,
                    'County': county,
                    'Role': role,
                    'Department': 'Loss Prevention' if role == 'Loss Control Officer' else ('Hygiene' if role in ['Cleaner','Hygiene Auditor'] else ('HR' if role == 'Supervisor' else 'Operations')),
                    'HireDate': pd.Timestamp('2023-01-01') + pd.Timedelta(days=np.random.randint(0,900)),
                    'Status': np.random.choice(['Active','Exited'], p=[0.93,0.07]),
                    'Salary': salary,
                    'Incidents': incidents,
                    'ValueOfLoss': int(value_loss),
                    'Attendance': np.random.uniform(88, 99.5),
                    'HygieneScore': np.random.uniform(82, 98),
                    'TimeToFill': np.random.randint(5, 16)
                })
                emp_id += 1
    df = pd.DataFrame(all_data)
    df['TenureDays'] = (pd.Timestamp.now() - df['HireDate']).dt.days
    return df

def load_data(uploaded_file=None):
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            st.sidebar.success(f"Loaded {len(df)} records")
            return df
        except Exception as e:
            st.sidebar.error(f"Error: {e}")
    df = generate_demo_data()
    st.sidebar.info("Using demo data: 150 avg staff per branch.")
    return df

# SIDEBAR
st.sidebar.markdown("<h2 style='color:#E30613;'>Achievo for Naivas</h2>", unsafe_allow_html=True)
st.sidebar.caption("Retail Ops Command Center | 6,500+ Staff")
uploaded_file = st.sidebar.file_uploader("Upload Weekly HR Data", type=['csv','xlsx'])
if st.sidebar.button("Use Demo Data", use_container_width=True):
    uploaded_file = None

df = load_data(uploaded_file)
st.sidebar.divider()
st.sidebar.header("Filters")

county_opts = sorted(STORES_BY_COUNTY.keys())
county_f = st.sidebar.multiselect("Select County", county_opts, default=[], placeholder="All Counties")
if len(county_f)==0:
    county_f = county_opts

filtered_stores_by_county = []
for c in county_f:
    filtered_stores_by_county.extend(STORES_BY_COUNTY[c])

store_opts = sorted(filtered_stores_by_county)
store_f = st.sidebar.multiselect("Select Store", store_opts, default=[], placeholder=f"All {len(store_opts)} Stores in {', '.join(county_f)}")
dept_opts = sorted(df['Department'].unique().tolist())
dept_f = st.sidebar.multiselect("Select Department", dept_opts, default=[], placeholder="All Departments")

if len(store_f)==0:
    store_f = store_opts
if len(dept_f)==0:
    dept_f = dept_opts

df_filtered = df[df['Store'].isin(store_f) & df['County'].isin(county_f) & df['Department'].isin(dept_f)]

st.sidebar.divider()
st.sidebar.markdown('<div style="background:#FFE5E5; padding:8px; border-radius:6px; margin-bottom:6px;"><b>Naivas SLA:</b> 98% filled in <14 days</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div style="background:#E6F0FF; padding:8px; border-radius:6px;"><b>Target:</b> <5 incidents | >90% Hygiene</div>', unsafe_allow_html=True)
st.sidebar.metric("Filtered Staff", f"{len(df_filtered):,} staff")
st.sidebar.metric("Filtered Stores", f"{len(store_f)} stores")

# MAIN
st.markdown('<h1>Achievo <span style="color:#E30613;">for Naivas</span></h1>', unsafe_allow_html=True)
st.caption(f"Managing {len(df_filtered):,} Staff across {len(store_f)} Stores in {', '.join(county_f)} | Avg 150 staff per branch | Updated: {datetime.now().strftime('%d %b %Y %H:%M')}")
st.markdown(f"<div style='background:#F8F9FA; padding:12px; border-radius:8px; border-left:4px solid #E30613; margin-bottom:16px;'><b>Current View:</b> {', '.join(county_f)} | {len(store_f)} stores | {len(df_filtered):,} staff | Payroll KES {df_filtered['Salary'].sum()/1000000:.1f}M</div>", unsafe_allow_html=True)

total_payroll = df_filtered['Salary'].sum()
avg_hygiene = df_filtered['HygieneScore'].mean()
total_loss = df_filtered['ValueOfLoss'].sum()
avg_fill = df_filtered['TimeToFill'].mean()

c1,c2,c3,c4 = st.columns(4)
c1.metric("Total Staff (Filtered)", f"{len(df_filtered):,}", f"{len(store_f)} stores x ~150")
c2.metric("Monthly Payroll", f"KES {total_payroll/1000000:.1f}M", f"Avg KES {total_payroll/max(len(df_filtered),1):,.0f}/staff")
c3.metric("Avg Time to Fill", f"{avg_fill:.1f} days", "SLA: <14 days", delta_color="inverse")
c4.metric("Hygiene Audit Avg", f"{avg_hygiene:.1f}%", "Target: >90%")

c5,c6,c7,c8 = st.columns(4)
c5.metric("Total Shrinkage", f"KES {total_loss:,.0f}", f"{total_loss/max(len(df_filtered),1):,.0f} per staff")
c6.metric("Active Staff", f"{len(df_filtered[df_filtered['Status']=='Active']):,}", f"{len(df_filtered[df_filtered['Status']=='Active'])/max(len(df_filtered),1)*100:.1f}% active")
c7.metric("Loss Prevention Officers", f"{len(df_filtered[df_filtered['Role']=='Loss Control Officer'])}", "12% of staff")
c8.metric("Avg Attendance", f"{df_filtered['Attendance'].mean():.1f}%", "Target: >95%")

st.divider()

tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["Store Overview","HR and Payroll","Recruitment","Loss Prevention","Hygiene","Value & ROI"])

with tab1:
    col1,col2 = st.columns(2)
    with col1:
        county_perf = df_filtered.groupby('County', as_index=False)['Attendance'].mean()
        fig = px.bar(county_perf, x='County', y='Attendance', title=f"Avg Attendance - {', '.join(county_f)}")
        fig.update_traces(marker_color=NAIVAS_RED)
        fig.update_layout(plot_bgcolor='white', paper_bgcolor='white', font_color=NAIVAS_NAVY)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        store_perf = df_filtered.groupby('Store', as_index=False)['Incidents'].sum().sort_values('Incidents', ascending=False).head(8)
        fig2 = px.bar(store_perf, x='Incidents', y='Store', orientation='h', title=f"Top Stores by Incidents - {', '.join(county_f)}")
        fig2.update_traces(marker_color=NAIVAS_RED)
        fig2.update_layout(plot_bgcolor='white', paper_bgcolor='white', font_color=NAIVAS_NAVY)
        st.plotly_chart(fig2, use_container_width=True)
    st.subheader(f"Store Breakdown for {', '.join(county_f)} - Realistic Staffing")
    breakdown = df_filtered.groupby(['County','Store']).agg(Staff_Count=('EmployeeID','count'), Avg_Salary=('Salary','mean'), Total_Payroll=('Salary','sum')).reset_index()
    breakdown['Total_Payroll'] = breakdown['Total_Payroll'].apply(lambda x: f"KES {x:,.0f}")
    breakdown['Avg_Salary'] = breakdown['Avg_Salary'].apply(lambda x: f"KES {x:,.0f}")
    st.dataframe(breakdown, use_container_width=True)

with tab2:
    k1,k2,k3,k4 = st.columns(4)
    k1.metric("Active Staff", f"{len(df_filtered[df_filtered['Status']=='Active']):,}")
    k2.metric("Monthly Payroll", f"KES {df_filtered['Salary'].sum()/1000000:.1f}M")
    k3.metric("Attrition", f"{len(df_filtered[df_filtered['Status']=='Exited'])/max(len(df_filtered),1):.1%}")
    k4.metric("Avg Tenure", f"{df_filtered['TenureDays'].mean():.0f} days")
    colA,colB = st.columns(2)
    with colA:
        st.plotly_chart(px.pie(df_filtered, names='Department', title=f"Staff by Department - {', '.join(county_f)}", color_discrete_sequence=[NAIVAS_RED, NAIVAS_NAVY, ACHIEVO_ORANGE, NAIVAS_GREEN]), use_container_width=True)
    with colB:
        st.plotly_chart(px.histogram(df_filtered, x='Salary', nbins=20, title=f"Salary Distribution - {', '.join(county_f)}", color_discrete_sequence=[NAIVAS_RED]), use_container_width=True)

with tab3:
    st.subheader(f"Recruitment for {', '.join(county_f)}")
    funnel = pd.DataFrame({'Stage':['Applicants','Screened','Vetted','Trained','Deployed'], 'Count':[2250,1125,810,720,648]})
    fig = go.Figure(go.Funnel(y=funnel['Stage'], x=funnel['Count'], marker={"color":[NAIVAS_RED, ACHIEVO_ORANGE, NAIVAS_NAVY, NAIVAS_GREEN, ACHIEVO_BLUE]}))
    fig.update_layout(plot_bgcolor='white', paper_bgcolor='white', font_color=NAIVAS_NAVY, title="Recruitment Funnel")
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.subheader(f"Loss Prevention - {', '.join(county_f)}")
    loss = df_filtered.groupby('Store', as_index=False)['ValueOfLoss'].sum().sort_values('ValueOfLoss', ascending=False).head(10)
    fig = px.bar(loss, x='ValueOfLoss', y='Store', orientation='h', title=f"Top 10 Stores by Value of Loss - {', '.join(county_f)}")
    fig.update_traces(marker_color=NAIVAS_RED)
    fig.update_layout(plot_bgcolor='white', paper_bgcolor='white', font_color=NAIVAS_NAVY)
    st.plotly_chart(fig, use_container_width=True)

with tab5:
    st.subheader(f"Hygiene - {', '.join(county_f)}")
    fig = px.box(df_filtered, x='County', y='HygieneScore', color='County', title=f"Hygiene Score by County - Filtered View")
    fig.update_layout(plot_bgcolor='white', paper_bgcolor='white', font_color=NAIVAS_NAVY)
    st.plotly_chart(fig, use_container_width=True)

with tab6:
    st.markdown("<h2 style='color:#E30613;'>Value Delivered by Achievo to Naivas</h2>", unsafe_allow_html=True)
    st.caption(f"ROI Analysis for {', '.join(county_f)} | {len(store_f)} stores | {len(df_filtered):,} staff")

    total_payroll = df_filtered['Salary'].sum()
    total_loss = df_filtered['ValueOfLoss'].sum()
    estimated_loss_without_achievo = total_loss * 2.8
    saved_loss = estimated_loss_without_achievo - total_loss
    in_house_cost_per_staff = 8500
    achievo_cost_per_staff = 5200
    monthly_saving_hr = (in_house_cost_per_staff - achievo_cost_per_staff) * len(df_filtered)
    payroll_accuracy = 99.8
    ghost_saving = len(df_filtered) * 0.02 * 25000

    r1c1, r1c2, r1c3, r1c4 = st.columns(4)
    r1c1.metric("Total Savings (Shrinkage Prevented)", f"KES {saved_loss/1000000:.2f}M", f"{len(store_f)} stores")
    r1c2.metric("HR Cost Savings / Month", f"KES {monthly_saving_hr/1000000:.2f}M", "37% cheaper than in-house")
    r1c3.metric("SLA Compliance", "98.7%", "Target 98%")
    r1c4.metric("Payroll Accuracy", f"{payroll_accuracy}%", "0 ghost workers")

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Before Achievo vs After Achievo")
        before_after = pd.DataFrame({
            'Metric': ['Avg Monthly Shrinkage', 'Time to Fill Vacancy', 'Hygiene Audit Score', 'Payroll Errors', 'Attrition Rate'],
            'Before Achievo': [f"KES {estimated_loss_without_achievo:,.0f}", "28 days", "76%", "12 per month", "18%"],
            'After Achievo': [f"KES {total_loss:,.0f}", f"{avg_fill:.1f} days", f"{avg_hygiene:.1f}%", "1 per month", f"{len(df_filtered[df_filtered['Status']=='Exited'])/max(len(df_filtered),1)*100:.1f}%"],
            'Improvement': [f"-{(1-total_loss/max(estimated_loss_without_achievo,1))*100:.1f}% loss", f"-{28-avg_fill:.1f} days faster", f"+{avg_hygiene-76:.1f}%", "-91% errors", "-10% attrition"]
        })
        st.dataframe(before_after, use_container_width=True, hide_index=True)

    with col2:
        roi_data = pd.DataFrame({
            'Category': ['Shrinkage Saved', 'HR Cost Saved', 'Ghost Worker Eliminated', 'Overtime Reduced'],
            'Value KES': [saved_loss, monthly_saving_hr, ghost_saving, len(df_filtered)*800]
        })
        fig = px.bar(roi_data, x='Category', y='Value KES', title=f"Monthly Value Delivered - {', '.join(county_f)}", color='Category', color_discrete_sequence=[NAIVAS_RED, ACHIEVO_ORANGE, NAIVAS_GREEN, NAIVAS_NAVY])
        fig.update_layout(plot_bgcolor='white', paper_bgcolor='white', showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("In-House vs Achievo Cost Comparison")
        cost_comp = pd.DataFrame({
            'Service': ['Recruitment per hire', 'Monthly HR Mgmt per staff', 'Payroll Compliance', 'Loss Control per store'],
            'In-House Cost': ['KES 18,500', 'KES 8,500', 'KES 2,500 + penalties', 'KES 85,000'],
            'Achievo Cost': ['KES 9,200', 'KES 5,200', 'KES 1,200 (100% compliant)', 'KES 52,000'],
            'Saving': ['50% cheaper', '39% cheaper', '52% + no penalties', '39% cheaper']
        })
        st.dataframe(cost_comp, use_container_width=True, hide_index=True)

    with col4:
        st.subheader("SLA Performance")
        fig = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = 98.7,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Overall SLA Compliance %"},
            delta = {'reference': 98, 'increasing': {'color': NAIVAS_GREEN}},
            gauge = {'axis': {'range': [None, 100]}, 'bar': {'color': NAIVAS_RED}, 'steps': [{'range': [0, 90], 'color': "#FFE5E5"}, {'range': [90, 98], 'color': "#FFF4E0"}, {'range': [98, 100], 'color': "#E6F5E6"}]}
        ))
        st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.markdown(f"""
    <div style='background:#0A1931; color:white; padding:20px; border-radius:10px;'>
        <h3 style='color:white; margin-top:0;'>Executive Summary for {', '.join(county_f)}</h3>
        <p>Achievo manages <b>{len(df_filtered):,} staff</b> across <b>{len(store_f)} stores</b> in {', '.join(county_f)} with <b>KES {total_payroll/1000000:.1f}M monthly payroll</b>.
        In this region alone, Achievo prevents <b>KES {saved_loss:,.0f} in shrinkage monthly</b> and saves <b>KES {monthly_saving_hr:,.0f} in HR costs</b>.
        Total monthly value delivered: <b style='color:#00A651;'>KES {(saved_loss+monthly_saving_hr)/1000000:.2f}M</b>. ROI: <b>342%</b></p>
    </div>
    """, unsafe_allow_html=True)