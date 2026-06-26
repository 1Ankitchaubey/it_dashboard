import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime
import io

# ── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="IT Support Dashboard",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Dark Theme CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

/* Full dark background */
.stApp { background-color: #0a0f1e; }
.main  { background-color: #0a0f1e; }
.block-container { padding-top: 1.2rem; padding-bottom: 2rem; }

/* Dark sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #060b18 0%, #0d1428 100%);
    border-right: 1px solid #1e2d4a;
}
[data-testid="stSidebar"] * { color: #c9d8f0 !important; }
[data-testid="stSidebar"] h2 { color: #60a5fa !important; font-size: 1.1rem !important; }
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stMultiSelect label,
[data-testid="stSidebar"] .stDateInput label { color: #7b93b8 !important; font-size: 0.75rem !important; }
[data-testid="stSidebar"] hr { border-color: #1e2d4a !important; }

/* Multiselect tags */
[data-testid="stMultiSelect"] span[data-baseweb="tag"] {
    background: #1e3a5f !important; color: #93c5fd !important;
}

/* Input fields dark */
[data-testid="stTextInput"] input,
[data-testid="stDateInput"] input {
    background: #0d1428 !important; color: #e2e8f0 !important;
    border-color: #1e3a5f !important;
}

/* Radio buttons */
[data-testid="stRadio"] label { color: #94a3b8 !important; font-size: 0.82rem !important; }
[data-testid="stRadio"] div[data-checked="true"] label { color: #60a5fa !important; }

/* Slider */
[data-testid="stSlider"] { color: #60a5fa; }

/* KPI Cards */
.kpi-card {
    background: linear-gradient(135deg, #0d1428 0%, #111827 100%);
    border-radius: 14px;
    padding: 1.2rem 1.4rem;
    border: 1px solid #1e2d4a;
    border-left: 4px solid;
    height: 100%;
    box-shadow: 0 4px 24px rgba(0,0,0,0.4);
}
.kpi-card.blue   { border-left-color: #3b82f6; }
.kpi-card.green  { border-left-color: #10b981; }
.kpi-card.orange { border-left-color: #f59e0b; }
.kpi-card.red    { border-left-color: #ef4444; }
.kpi-card.purple { border-left-color: #a855f7; }
.kpi-card.teal   { border-left-color: #06b6d4; }

.kpi-icon  { font-size: 1.4rem; margin-bottom: 0.4rem; }
.kpi-label { font-size: 0.7rem; font-weight: 600; color: #4a6080; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 0.2rem; }
.kpi-value { font-size: 1.9rem; font-weight: 800; color: #f1f5f9; line-height: 1.1; }
.kpi-sub   { font-size: 0.75rem; color: #4a6080; margin-top: 0.25rem; }

/* Section headers */
.sec-title {
    font-size: 0.85rem; font-weight: 700; color: #60a5fa;
    text-transform: uppercase; letter-spacing: 0.1em;
    margin-bottom: 0.6rem; padding-bottom: 0.4rem;
    border-bottom: 1px solid #1e2d4a;
}

/* Chart card */
.chart-card {
    background: linear-gradient(135deg, #0d1428 0%, #0f172a 100%);
    border-radius: 14px;
    padding: 1.2rem 1.2rem 0.6rem;
    border: 1px solid #1e2d4a;
    margin-bottom: 1rem;
    box-shadow: 0 4px 24px rgba(0,0,0,0.3);
}

/* Header */
.dash-header {
    background: linear-gradient(135deg, #060b18 0%, #0d1f3c 50%, #0a1628 100%);
    padding: 1.4rem 2rem;
    border-radius: 16px;
    margin-bottom: 1.4rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border: 1px solid #1e3a5f;
    box-shadow: 0 8px 32px rgba(0,0,0,0.5);
}
.dash-title { font-size: 1.5rem; font-weight: 800; color: #f1f5f9; margin: 0; letter-spacing: -0.02em; }
.dash-sub   { font-size: 0.82rem; color: #4a6080; margin: 0.2rem 0 0; }
.dash-badge {
    background: rgba(59,130,246,0.15);
    color: #60a5fa;
    padding: 0.4rem 1rem;
    border-radius: 20px;
    font-size: 0.78rem;
    font-weight: 600;
    border: 1px solid rgba(59,130,246,0.25);
}

/* Expander */
[data-testid="stExpander"] {
    background: #0d1428 !important;
    border: 1px solid #1e2d4a !important;
    border-radius: 12px !important;
}
[data-testid="stExpander"] summary { color: #93c5fd !important; }

/* Dataframe */
[data-testid="stDataFrame"] { background: #0d1428 !important; }

/* Download button */
[data-testid="stDownloadButton"] button {
    background: #1e3a5f !important; color: #93c5fd !important;
    border: 1px solid #2d4f7a !important; border-radius: 8px !important;
}

/* Upload */
[data-testid="stFileUploader"] {
    border: 2px dashed #1e3a5f !important;
    border-radius: 12px !important;
    background: #060d1a !important;
}
[data-testid="stFileUploader"] * { color: #60a5fa !important; }

/* Scrollbar */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: #0a0f1e; }
::-webkit-scrollbar-thumb { background: #1e3a5f; border-radius: 3px; }
</style>
""", unsafe_allow_html=True)


# ── Dark Plotly Template ───────────────────────────────────────────────────────
DARK_BG    = '#0d1428'
GRID_COLOR = '#1a2640'
TEXT_COLOR = '#94a3b8'
TITLE_COLOR = '#e2e8f0'

PALETTE = ['#3b82f6','#10b981','#f59e0b','#ef4444','#a855f7',
           '#06b6d4','#f97316','#ec4899','#84cc16','#14b8a6']

def dark_chart(fig, title='', height=320):
    fig.update_layout(
        title=dict(text=f"<b>{title}</b>", font=dict(size=12.5, color=TITLE_COLOR, family='Inter'), x=0, pad=dict(l=2)),
        height=height,
        margin=dict(l=8, r=8, t=44 if title else 8, b=8),
        paper_bgcolor=DARK_BG,
        plot_bgcolor=DARK_BG,
        font=dict(family='Inter', color=TEXT_COLOR, size=11),
        legend=dict(font=dict(size=10, color=TEXT_COLOR), bgcolor='rgba(0,0,0,0)',
                    orientation='h', yanchor='bottom', y=1.01, xanchor='right', x=1),
        xaxis=dict(gridcolor=GRID_COLOR, linecolor=GRID_COLOR, tickfont=dict(color=TEXT_COLOR, size=10)),
        yaxis=dict(gridcolor=GRID_COLOR, linecolor=GRID_COLOR, tickfont=dict(color=TEXT_COLOR, size=10)),
        coloraxis=dict(colorbar=dict(tickfont=dict(color=TEXT_COLOR))),
    )
    return fig


# ── Data Cleaning ──────────────────────────────────────────────────────────────
def clean_data(df):
    df.columns = df.columns.str.strip()
    df = df.dropna(how='all')
    df = df[df['S.NO'].notna()]

    # Call Type normalize
    def norm_call(v):
        if pd.isna(v): return 'Unknown'
        v = str(v).strip().lower()
        if ('hardware' in v and 'software' in v) or ('software' in v and 'hardware' in v):
            return 'Hardware & Software'
        if 'hardware' in v or 'harware' in v: return 'Hardware'
        if 'software' in v or 'softare' in v: return 'Software'
        if 'network' in v: return 'Network'
        return str(v).strip().title()
    df['CALL TYPE'] = df['CALL TYPE'].apply(norm_call)

    # Remarks normalize
    def norm_remark(v):
        if pd.isna(v): return 'Unknown'
        v = str(v).strip().lower()
        if 'resolve' in v or 'done' in v: return 'Resolved'
        if 'pending' in v: return 'Pending'
        if 'process' in v or 'progress' in v: return 'In Process'
        return 'Resolved'
    df['REMARKS'] = df['REMARKS'].apply(norm_remark)

    # Engineer normalize
    eng_map = {
        'ankit kumar': 'Ankit Kumar', 'ankit chaubey': 'Ankit Chaubey',
        'jai kaushik': 'Jai Kaushik', 'rajni kant singh': 'Rajni Kant Singh',
        'rajanikant sir': 'Rajni Kant Singh', 'aatif khan': 'Aatif Khan',
        'md. aatif khan khan': 'Aatif Khan', 'deepa singh': 'Deepa Singh',
        'sandeep yadav': 'Sandeep Yadav', 'abhishek pathak': 'Abhishek Pathak',
        'abhishek sir': 'Abhishek Pathak', 'salim khan': 'Salim Khan',
        'suraj': 'Suraj', 'rakesh kadyan sir': 'Rakesh Kadyan',
        'ankit kumar with canon support team member': 'Ankit Kumar',
    }
    df['Engineer Name'] = df['Engineer Name'].apply(
        lambda v: eng_map.get(str(v).strip().lower(), str(v).strip().title()) if pd.notna(v) else 'Unknown'
    )

    # Device normalize
    def norm_device(v):
        if pd.isna(v): return 'Unknown'
        v = str(v).strip().lower()
        if 'desktop' in v or 'dekstop' in v: return 'Desktop'
        if 'laptop' in v: return 'Laptop'
        if 'server' in v: return 'Server'
        if 'network' in v: return 'Network'
        if 'switch' in v or 'swtich' in v: return 'Switch'
        if 'printer' in v: return 'Printer'
        if 'mobile' in v or 'iphone' in v: return 'Mobile'
        return str(v).strip().title()
    df['Desktop/Laptop'] = df['Desktop/Laptop'].apply(norm_device)

    # Date parse — handles both '16-10-2025' and '2025-11-01 00:00:00' formats
    def parse_date(v):
        if pd.isna(v): return pd.NaT
        v = str(v).strip().split(' ')[0]   # strip time part if present
        for fmt in ['%d-%m-%Y', '%Y-%m-%d', '%d/%m/%Y', '%m/%d/%Y']:
            try: return pd.to_datetime(v, format=fmt)
            except: pass
        try: return pd.to_datetime(float(v), unit='D', origin='1899-12-30')
        except: return pd.NaT
    df['DATE'] = df['DATE'].apply(parse_date)
    df = df[df['DATE'].notna()]
    df['Month']    = df['DATE'].dt.strftime('%b %Y')
    df['MonthNum'] = df['DATE'].dt.to_period('M')
    df['Week']     = df['DATE'].dt.to_period('W').apply(lambda x: str(x.start_time.date()))
    df['Day']      = df['DATE'].dt.date

    # Duration in minutes from HH:MM:SS strings
    def calc_dur(start, end):
        try:
            s = pd.to_datetime(str(start).strip(), format='%H:%M:%S')
            e = pd.to_datetime(str(end).strip(), format='%H:%M:%S')
            diff = (e - s).total_seconds() / 60
            if diff < 0: diff += 24 * 60
            return round(diff, 1) if 0 < diff <= 480 else None
        except:
            return None
    df['Duration_Min'] = df.apply(lambda r: calc_dur(r['START TIME'], r['END TIME']), axis=1)

    # Location fill
    df['LOCATION'] = df['LOCATION'].fillna('Unknown').str.strip()
    df['DEPT']     = df['DEPT'].fillna('Unknown').str.strip()

    return df


@st.cache_data(show_spinner=False)
def load_excel(file_bytes):
    df_raw = pd.read_excel(io.BytesIO(file_bytes), dtype=str)
    return clean_data(df_raw)


# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🖥️ IT Support Dashboard")
    st.markdown("---")
    st.markdown("### 📂 Upload Data")
    uploaded = st.file_uploader("Drop Excel file here", type=['xlsx','xls'], label_visibility='collapsed')
    st.markdown("---")

    if uploaded:
        file_bytes  = uploaded.read()
        df_full     = load_excel(file_bytes)

        st.markdown("### 🔍 Filters")
        all_locs = sorted(df_full['LOCATION'].dropna().unique().tolist())
        sel_loc  = st.multiselect("📍 Location", all_locs, default=all_locs)

        all_engs = sorted(df_full['Engineer Name'].dropna().unique().tolist())
        sel_eng  = st.multiselect("👨‍💻 Engineer", all_engs, default=all_engs)

        all_types = sorted(df_full['CALL TYPE'].dropna().unique().tolist())
        sel_type  = st.multiselect("🔧 Call Type", all_types, default=all_types)

        all_rem = sorted(df_full['REMARKS'].dropna().unique().tolist())
        sel_rem = st.multiselect("✅ Status", all_rem, default=all_rem)

        min_d = df_full['DATE'].min().date()
        max_d = df_full['DATE'].max().date()
        date_range = st.date_input("📅 Date Range", value=(min_d, max_d), min_value=min_d, max_value=max_d)

        # Apply filters
        df = df_full.copy()
        if sel_loc:  df = df[df['LOCATION'].isin(sel_loc)]
        if sel_eng:  df = df[df['Engineer Name'].isin(sel_eng)]
        if sel_type: df = df[df['CALL TYPE'].isin(sel_type)]
        if sel_rem:  df = df[df['REMARKS'].isin(sel_rem)]
        if len(date_range) == 2:
            df = df[(df['DATE'].dt.date >= date_range[0]) & (df['DATE'].dt.date <= date_range[1])]

        st.markdown("---")
        st.markdown(f"<div style='color:#4a6080;font-size:0.78rem'>📊 Showing <b style='color:#3b82f6'>{len(df):,}</b> of <b style='color:#60a5fa'>{len(df_full):,}</b> records</div>", unsafe_allow_html=True)
    else:
        df = None


# ── Header ─────────────────────────────────────────────────────────────────────
now_str = datetime.now().strftime("%d %b %Y  %I:%M %p")
st.markdown(f"""
<div class="dash-header">
    <div>
        <p class="dash-title">🖥️ IT Support Operations Dashboard</p>
        <p class="dash-sub">Daily Call Report — Real-time Interactive Analytics</p>
    </div>
    <div style="text-align:right">
        <span class="dash-badge">🕐 {now_str}</span>
    </div>
</div>
""", unsafe_allow_html=True)


# ── Upload Prompt ──────────────────────────────────────────────────────────────
if df is None:
    st.markdown("""
    <div style="background:linear-gradient(135deg,#0d1428,#0f172a);border-radius:16px;
    padding:3.5rem 2rem;text-align:center;border:1px solid #1e2d4a;box-shadow:0 8px 32px rgba(0,0,0,0.5);">
        <div style="font-size:3.5rem">📤</div>
        <h2 style="color:#f1f5f9;margin:1rem 0 0.5rem;font-weight:800">Upload your Excel file to begin</h2>
        <p style="color:#4a6080;font-size:0.95rem">Use the sidebar on the left to upload your Daily Call Report.<br>
        All charts and KPIs will auto-update instantly.</p>
        <br>
        <div style="display:flex;justify-content:center;gap:1.5rem;flex-wrap:wrap;">
            <div style="background:#0a1628;padding:1rem 1.5rem;border-radius:12px;color:#3b82f6;font-weight:600;font-size:0.82rem;border:1px solid #1e3a5f">📊 10+ Interactive Charts</div>
            <div style="background:#0a1628;padding:1rem 1.5rem;border-radius:12px;color:#10b981;font-weight:600;font-size:0.82rem;border:1px solid #1e3a5f">🔍 Smart Filters</div>
            <div style="background:#0a1628;padding:1rem 1.5rem;border-radius:12px;color:#f59e0b;font-weight:600;font-size:0.82rem;border:1px solid #1e3a5f">📈 Live KPI Cards</div>
            <div style="background:#0a1628;padding:1rem 1.5rem;border-radius:12px;color:#a855f7;font-weight:600;font-size:0.82rem;border:1px solid #1e3a5f">⚡ Problem & Solution Log</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.stop()


# ── KPIs ───────────────────────────────────────────────────────────────────────
total     = len(df)
resolved  = (df['REMARKS'] == 'Resolved').sum()
res_pct   = resolved / total * 100 if total else 0
pending   = (df['REMARKS'] == 'Pending').sum()
avg_dur   = df['Duration_Min'].dropna().mean()
top_eng   = df['Engineer Name'].value_counts().idxmax() if total else 'N/A'
top_eng_n = df['Engineer Name'].value_counts().max() if total else 0
hw_calls  = (df['CALL TYPE'] == 'Hardware').sum()
sw_calls  = (df['CALL TYPE'] == 'Software').sum()

c1,c2,c3,c4,c5,c6 = st.columns(6)
cards = [
    (c1, "blue",   "🗂️", "Total Calls",       f"{total:,}",          f"{df['DATE'].min().strftime('%d %b')} – {df['DATE'].max().strftime('%d %b %Y')}"),
    (c2, "green",  "✅", "Resolved",           f"{res_pct:.1f}%",     f"{resolved:,} calls resolved"),
    (c3, "red",    "⏳", "Pending / Open",     f"{pending:,}",        "Needs attention"),
    (c4, "orange", "⏱️", "Avg Resolution",    f"{avg_dur:.0f} min",  "Per call average"),
    (c5, "purple", "👨‍💻", "Top Engineer",      top_eng.split()[0],   f"{top_eng_n} calls handled"),
    (c6, "teal",   "🔧", "SW vs HW",          f"{sw_calls} / {hw_calls}", "Software / Hardware"),
]
for col, color, icon, label, val, sub in cards:
    with col:
        st.markdown(f"""
        <div class="kpi-card {color}">
            <div class="kpi-icon">{icon}</div>
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{val}</div>
            <div class="kpi-sub">{sub}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ── Row 1: Trend + Call Type ───────────────────────────────────────────────────
col_a, col_b = st.columns([3, 1])

with col_a:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">📈 Call Volume Trend</div>', unsafe_allow_html=True)
    tg = st.radio("", ["Daily","Weekly","Monthly"], horizontal=True, key='trend_grp', label_visibility='collapsed')

    if tg == "Daily":
        trend = df.groupby('Day').size().reset_index(name='Calls')
        trend['Day'] = pd.to_datetime(trend['Day'])
        fig_t = px.area(trend, x='Day', y='Calls', color_discrete_sequence=['#3b82f6'])
        fig_t.update_traces(fill='tozeroy', fillcolor='rgba(59,130,246,0.12)', line=dict(width=2))
    elif tg == "Weekly":
        trend = df.groupby('Week').size().reset_index(name='Calls')
        fig_t = px.bar(trend, x='Week', y='Calls', color_discrete_sequence=['#3b82f6'])
    else:
        trend = df.groupby('Month').size().reset_index(name='Calls')
        fig_t = px.bar(trend, x='Month', y='Calls', color='Calls', color_continuous_scale='Blues')

    fig_t = dark_chart(fig_t, height=270)
    st.plotly_chart(fig_t, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_b:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">🔧 Call Type</div>', unsafe_allow_html=True)
    ct = df['CALL TYPE'].value_counts().reset_index()
    ct.columns = ['Type','Count']
    fig_pie = px.pie(ct, names='Type', values='Count',
                     color_discrete_sequence=PALETTE, hole=0.6)
    fig_pie.update_traces(textposition='outside', textinfo='percent+label',
                          textfont=dict(size=9.5, color='#94a3b8'))
    fig_pie = dark_chart(fig_pie, height=270)
    fig_pie.update_layout(showlegend=False)
    st.plotly_chart(fig_pie, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ── Row 2: Engineer + Location ─────────────────────────────────────────────────
col_c, col_d = st.columns(2)

with col_c:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">👨‍💻 Engineer Performance</div>', unsafe_allow_html=True)

    eng = df.groupby('Engineer Name').agg(
        Total=('S.NO','count'),
        Resolved=('REMARKS', lambda x: (x=='Resolved').sum()),
        Pending=('REMARKS',  lambda x: (x=='Pending').sum()),
    ).reset_index()
    eng['Resolved %'] = (eng['Resolved'] / eng['Total'] * 100).round(1)
    eng['Pending %']  = (eng['Pending']  / eng['Total'] * 100).round(1)

    # Call type breakdown per engineer
    eng_ct = df.groupby(['Engineer Name','CALL TYPE']).size().reset_index(name='Count')

    chart_view = st.radio("View", ["Bar (Vertical)", "Bar (Horizontal)", "Donut", "Call Type Breakdown"],
                          horizontal=True, key='eng_view', label_visibility='collapsed')

    if chart_view == "Bar (Vertical)":
        eng_v = eng.sort_values('Total', ascending=False)
        fig_eng = go.Figure()
        fig_eng.add_trace(go.Bar(x=eng_v['Engineer Name'], y=eng_v['Total'],
                                 name='Total', marker_color='#1e3a5f',
                                 marker_line_color='#3b82f6', marker_line_width=1))
        fig_eng.add_trace(go.Bar(x=eng_v['Engineer Name'], y=eng_v['Resolved'],
                                 name='Resolved', marker_color='#10b981', opacity=0.9))
        fig_eng.add_trace(go.Bar(x=eng_v['Engineer Name'], y=eng_v['Pending'],
                                 name='Pending', marker_color='#ef4444', opacity=0.9))
        fig_eng = dark_chart(fig_eng, height=340)
        fig_eng.update_layout(barmode='overlay', xaxis=dict(tickangle=-25))
        st.plotly_chart(fig_eng, use_container_width=True)

    elif chart_view == "Bar (Horizontal)":
        eng_h = eng.sort_values('Total', ascending=True)
        fig_eng = go.Figure()
        fig_eng.add_trace(go.Bar(y=eng_h['Engineer Name'], x=eng_h['Total'],
                                 name='Total', orientation='h',
                                 marker_color='#1e3a5f', marker_line_color='#3b82f6', marker_line_width=1))
        fig_eng.add_trace(go.Bar(y=eng_h['Engineer Name'], x=eng_h['Resolved'],
                                 name='Resolved', orientation='h', marker_color='#10b981', opacity=0.9))
        fig_eng.add_trace(go.Bar(y=eng_h['Engineer Name'], x=eng_h['Pending'],
                                 name='Pending', orientation='h', marker_color='#ef4444', opacity=0.9))
        fig_eng = dark_chart(fig_eng, height=340)
        fig_eng.update_layout(barmode='overlay')
        st.plotly_chart(fig_eng, use_container_width=True)

    elif chart_view == "Donut":
        fig_eng = px.pie(eng, names='Engineer Name', values='Total',
                         color_discrete_sequence=PALETTE, hole=0.55)
        fig_eng.update_traces(textposition='outside', textinfo='percent+label',
                              textfont=dict(size=9, color='#94a3b8'))
        fig_eng = dark_chart(fig_eng, height=340)
        fig_eng.update_layout(showlegend=False)
        st.plotly_chart(fig_eng, use_container_width=True)

    else:  # Call Type Breakdown
        fig_eng = px.bar(eng_ct, x='Engineer Name', y='Count', color='CALL TYPE',
                         color_discrete_sequence=PALETTE, barmode='stack',
                         text='Count')
        fig_eng = dark_chart(fig_eng, height=340)
        fig_eng.update_traces(textposition='inside', textfont=dict(size=9))
        fig_eng.update_layout(xaxis=dict(tickangle=-25))
        st.plotly_chart(fig_eng, use_container_width=True)

    # Resolved % table below chart
    st.markdown("<div style='margin-top:0.5rem'>", unsafe_allow_html=True)
    eng_disp = eng[['Engineer Name','Total','Resolved','Pending','Resolved %']].sort_values('Total', ascending=False).reset_index(drop=True)
    eng_disp['Resolved %'] = eng_disp['Resolved %'].apply(lambda x: f"{x:.1f}%")
    st.dataframe(eng_disp, use_container_width=True, height=160,
                 column_config={"Resolved %": st.column_config.TextColumn("✅ Resolved %")})
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_d:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">📍 Calls by Location & Type</div>', unsafe_allow_html=True)
    loc = df.groupby(['LOCATION','CALL TYPE']).size().reset_index(name='Count')
    fig_loc = px.bar(loc, x='LOCATION', y='Count', color='CALL TYPE',
                     color_discrete_sequence=PALETTE, barmode='stack')
    fig_loc = dark_chart(fig_loc, height=320)
    st.plotly_chart(fig_loc, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ── Row 3: Heatmap + Status + Device ──────────────────────────────────────────
col_e, col_f, col_g = st.columns([2,1,1])

with col_e:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">🏢 Department × Engineer Heatmap</div>', unsafe_allow_html=True)
    top_depts = df['DEPT'].value_counts().head(12).index
    pivot = df[df['DEPT'].isin(top_depts)].groupby(['DEPT','Engineer Name']).size().unstack(fill_value=0)
    fig_h = px.imshow(pivot, color_continuous_scale='Blues', aspect='auto',
                      labels=dict(color="Calls"))
    fig_h = dark_chart(fig_h, height=320)
    fig_h.update_layout(
        xaxis=dict(tickfont=dict(size=9), tickangle=-30),
        yaxis=dict(tickfont=dict(size=9)),
        coloraxis_showscale=False
    )
    st.plotly_chart(fig_h, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_f:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">✅ Resolution Status</div>', unsafe_allow_html=True)
    rem = df['REMARKS'].value_counts().reset_index()
    rem.columns = ['Status','Count']
    cmap = {'Resolved':'#10b981','Pending':'#ef4444','In Process':'#f59e0b','Unknown':'#4a6080'}
    colors = [cmap.get(s,'#3b82f6') for s in rem['Status']]
    fig_rem = px.pie(rem, names='Status', values='Count', color_discrete_sequence=colors, hole=0.62)
    fig_rem.update_traces(textposition='outside', textinfo='percent+label', textfont=dict(size=9.5, color='#94a3b8'))
    fig_rem = dark_chart(fig_rem, height=280)
    fig_rem.update_layout(showlegend=False)
    st.plotly_chart(fig_rem, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_g:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">💻 Device Type</div>', unsafe_allow_html=True)
    dev = df['Desktop/Laptop'].value_counts().reset_index()
    dev.columns = ['Device','Count']
    fig_dev = px.bar(dev, x='Device', y='Count', color='Device', color_discrete_sequence=PALETTE)
    fig_dev = dark_chart(fig_dev, height=280)
    fig_dev.update_layout(showlegend=False, xaxis=dict(tickangle=-20))
    st.plotly_chart(fig_dev, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ── Row 4: Top Departments + Duration ─────────────────────────────────────────
col_h, col_i = st.columns(2)

with col_h:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">🏢 Top Departments by Call Volume</div>', unsafe_allow_html=True)
    top_n = st.slider("Show top N", 5, 25, 15, key='topn')
    dept  = df['DEPT'].value_counts().head(top_n).reset_index()
    dept.columns = ['Department','Calls']
    fig_dept = px.bar(dept, x='Calls', y='Department', orientation='h',
                      color='Calls', color_continuous_scale='Blues')
    fig_dept = dark_chart(fig_dept, height=max(280, top_n*22))
    fig_dept.update_layout(coloraxis_showscale=False, yaxis=dict(autorange='reversed'))
    st.plotly_chart(fig_dept, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_i:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">⏱️ Avg Resolution Time per Engineer (min)</div>', unsafe_allow_html=True)
    dur = df.groupby('Engineer Name')['Duration_Min'].mean().dropna().reset_index()
    dur.columns = ['Engineer','Avg Min']
    dur = dur.sort_values('Avg Min', ascending=True)
    fig_dur = px.bar(dur, x='Avg Min', y='Engineer', orientation='h',
                     color='Avg Min', color_continuous_scale='RdYlGn_r')
    fig_dur = dark_chart(fig_dur, height=max(280, len(dur)*28))
    fig_dur.update_layout(coloraxis_showscale=False)
    st.plotly_chart(fig_dur, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ── Row 5: Location Resolution Rate ───────────────────────────────────────────
st.markdown('<div class="chart-card">', unsafe_allow_html=True)
st.markdown('<div class="sec-title">📍 Resolution Rate by Location</div>', unsafe_allow_html=True)
loc_res = df.groupby('LOCATION').apply(
    lambda x: pd.Series({'Total':len(x), 'Resolved':(x['REMARKS']=='Resolved').sum()})
).reset_index()
loc_res['Resolution %'] = (loc_res['Resolved']/loc_res['Total']*100).round(1)
fig_lr = px.bar(loc_res, x='LOCATION', y='Resolution %',
                color='Resolution %', color_continuous_scale='Greens',
                text='Resolution %')
fig_lr = dark_chart(fig_lr, height=260)
fig_lr.update_traces(texttemplate='%{text:.1f}%', textposition='outside', textfont=dict(color='#94a3b8'))
fig_lr.update_layout(coloraxis_showscale=False, yaxis=dict(range=[0,115]))
st.plotly_chart(fig_lr, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)


# ── Problem & Solution Log ─────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="sec-title" style="font-size:0.95rem;border-bottom:2px solid #1e3a5f;padding-bottom:0.5rem;margin-bottom:1rem">🔎 Problem & Solution Log</div>', unsafe_allow_html=True)

# Search
search = st.text_input("🔍 Search problem / solution / user name...", placeholder="e.g. VMware, printer, Jai Kaushik...", label_visibility='collapsed')

log_df = df[['DATE','LOCATION','USER NAME','DEPT','CALL TYPE','USER DESCRIPTION','PROBLEM RESOLVED STATUS','REMARKS','Engineer Name','Duration_Min']].copy()
log_df['DATE'] = log_df['DATE'].dt.strftime('%d-%m-%Y')
log_df.columns = ['Date','Location','User','Dept','Type','🔴 Problem','🟢 Solution','Status','Engineer','⏱ Min']
log_df['⏱ Min'] = log_df['⏱ Min'].apply(lambda x: f"{x:.0f} min" if pd.notna(x) else '—')

if search:
    mask = log_df.apply(lambda row: row.astype(str).str.contains(search, case=False).any(), axis=1)
    log_df = log_df[mask]

st.markdown(f"<div style='color:#4a6080;font-size:0.78rem;margin-bottom:0.5rem'>Showing {len(log_df):,} records</div>", unsafe_allow_html=True)
st.dataframe(
    log_df.reset_index(drop=True),
    use_container_width=True,
    height=400,
    column_config={
        "🔴 Problem":  st.column_config.TextColumn(width="large"),
        "🟢 Solution": st.column_config.TextColumn(width="large"),
    }
)

# Download
csv = log_df.to_csv(index=False).encode('utf-8')
st.download_button("⬇️ Download Filtered Data as CSV", data=csv,
                   file_name='it_support_data.csv', mime='text/csv')


# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;color:#1e3a5f;font-size:0.72rem;margin-top:2rem;
padding:1rem;border-top:1px solid #1a2640;">
    IT Support Dashboard • Upload new Excel file anytime • All data stays local
</div>
""", unsafe_allow_html=True)
