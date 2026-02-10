"""
Shared utilities for AI Resume Skill Gap Analyzer
Common functions and styling used across multiple pages
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from typing import Dict, List

def set_custom_css():
    """Apply custom CSS styling for advanced black theme and hide Streamlit branding"""
    st.markdown("""
    <style>
        /* Advanced Black Theme Global Styles */
        .stApp {
            background: linear-gradient(135deg, #000000 0%, #0a0a0a 25%, #111111 50%, #1a1a1a 75%, #0f0f0f 100%);
            color: #ffffff;
            min-height: 100vh;
        }
        
        /* Streamlit default overrides */
        .stApp > div {
            background: transparent !important;
        }
        
        .stBlock {
            background: transparent !important;
        }
        
        .stMarkdown {
            color: #ffffff !important;
        }
        
        .stSelectbox > div > div > select {
            background: #1a1a1a !important;
            color: #ffffff !important;
            border: 1px solid #333333 !important;
            border-radius: 8px !important;
            padding: 0.5rem !important;
        }
        
        .stButton > button {
            background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 50%, #1a1a1a 100%) !important;
            color: #ffffff !important;
            border: 1px solid #444444 !important;
            font-weight: 600 !important;
            border-radius: 12px !important;
            padding: 0.75rem 1.5rem !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5) !important;
        }
        
        .stButton > button:hover {
            background: linear-gradient(135deg, #2d2d2d 0%, #3a3a3a 50%, #2d2d2d 100%) !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(255, 255, 255, 0.1) !important;
            border-color: #666666 !important;
        }
        
        .stFileUploader > div {
            background: #1a1a1a !important;
            border: 2px dashed #444444 !important;
            border-radius: 15px !important;
            padding: 2rem !important;
            transition: all 0.3s ease !important;
        }
        
        .stFileUploader > div:hover {
            border-color: #666666 !important;
            background: #2d2d2d !important;
            box-shadow: 0 8px 25px rgba(255, 255, 255, 0.05) !important;
        }
        
        .stAlert {
            background: #1a1a1a !important;
            border-left: 4px solid #666666 !important;
            color: #ffffff !important;
            border-radius: 8px !important;
        }
        
        .stSuccess {
            background: linear-gradient(135deg, #0d2d1d 0%, #1a3d2d 100%) !important;
            border-left: 4px solid #22c55e !important;
            color: #ffffff !important;
        }
        
        .stError {
            background: linear-gradient(135deg, #2d0d0d 0%, #3d1a1a 100%) !important;
            border-left: 4px solid #ef4444 !important;
            color: #ffffff !important;
        }
        
        .stInfo {
            background: linear-gradient(135deg, #0d1d2d 0%, #1a2a3d 100%) !important;
            border-left: 4px solid #3b82f6 !important;
            color: #ffffff !important;
        }
        
        /* Hide Streamlit watermarks and branding */
        .stDeployButton {
            display: none !important;
        }
        
        #MainMenu {
            visibility: hidden !important;
        }
        
        footer {
            visibility: hidden !important;
        }
        
        header {
            visibility: hidden !important;
        }
        
        .stApp > div > div > div > div > div > div > div > div:first-child {
            display: none !important;
        }
        
        /* Hide the "Made with Streamlit" footer and all Streamlit branding */
        .stApp > div > div > div > div > div > div > div > div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] > div[data-testid="stMarkdownContainer"] > div > p {
            display: none !important;
        }
        
        .stApp > div > div > div > div > div > div > div > div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] > div[data-testid="stMarkdownContainer"] > div > p > a {
            display: none !important;
        }
        
        /* Hide any remaining Streamlit branding elements */
        [data-testid="stHeader"] {
            display: none !important;
        }
        
        [data-testid="stFooter"] {
            display: none !important;
        }
        
        .stApp > div > div > div > div > div > div > div > div > div > div > div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] > div[data-testid="stMarkdownContainer"] > p {
            display: none !important;
        }
        
        /* Custom footer */
        .custom-footer {
            text-align: center;
            color: #666666;
            padding: 2rem;
            margin-top: 3rem;
            border-top: 1px solid #333333;
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
            border-radius: 15px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5);
        }
        
        .main-header {
            font-size: 3.5rem;
            font-weight: 800;
            color: #ffffff;
            text-align: center;
            margin-bottom: 1rem;
            padding: 2rem;
            background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 50%, #1a1a1a 100%);
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.8);
            text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);
            border: 1px solid #444444;
            position: relative;
            overflow: hidden;
        }
        
        .main-header::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.05), transparent);
            transition: left 0.5s ease;
        }
        
        .main-header:hover::before {
            left: 100%;
        }
        
        .hero-subtitle {
            font-size: 1.3rem;
            color: #999999;
            text-align: center;
            margin-bottom: 3rem;
            padding: 0 2rem;
            font-weight: 400;
            letter-spacing: 0.5px;
        }
        
        .sub-header {
            font-size: 2rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 1.5rem;
            padding: 1rem;
            background: linear-gradient(135deg, #2d2d2d 0%, #3a3a3a 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-shadow: 0 0 20px rgba(255, 255, 255, 0.1);
        }
        
        .metric-card {
            background: linear-gradient(135deg, #1a1a1a 0%, #0f0f0f 100%);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.6);
            border-left: 5px solid #666666;
            margin-bottom: 1.5rem;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border: 1px solid #333333;
            position: relative;
            overflow: hidden;
        }
        
        .metric-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, #666666, transparent);
            opacity: 0.3;
        }
        
        .metric-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(255, 255, 255, 0.05);
            border-color: #666666;
            border-left-color: #888888;
        }
        
        .feature-card {
            background: linear-gradient(135deg, #1a1a1a 0%, #0f0f0f 100%);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.6);
            margin-bottom: 2rem;
            text-align: center;
            transition: transform 0.3s ease;
            border: 1px solid #333333;
            position: relative;
            overflow: hidden;
        }
        
        .feature-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, #666666, transparent);
            opacity: 0.3;
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(255, 255, 255, 0.05);
            border-color: #666666;
        }
        
        .feature-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            filter: grayscale(20%);
        }
        
        .feature-title {
            font-size: 1.5rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 1rem;
        }
        
        .feature-description {
            color: #999999;
            line-height: 1.6;
            font-weight: 400;
        }
        
        .stat-item {
            background: linear-gradient(135deg, #1a1a1a 0%, #0f0f0f 100%);
            padding: 1.5rem;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.6);
            border: 1px solid #333333;
            position: relative;
            overflow: hidden;
        }
        
        .stat-item::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, #666666, transparent);
            opacity: 0.3;
        }
        
        .stat-number {
            font-size: 2.5rem;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 0.5rem;
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
        }
        
        .stat-label {
            color: #999999;
            font-weight: 600;
        }
        
        .job-role-card {
            background: linear-gradient(135deg, #1a1a1a 0%, #0f0f0f 100%);
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.6);
            margin-bottom: 1rem;
            border-left: 4px solid #666666;
            border: 1px solid #333333;
            position: relative;
            overflow: hidden;
        }
        
        .job-role-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, #666666, transparent);
            opacity: 0.3;
        }
        
        .job-role-title {
            font-size: 1.3rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 0.5rem;
        }
        
        .job-role-meta {
            display: flex;
            gap: 1rem;
            margin-bottom: 1rem;
            flex-wrap: wrap;
        }
        
        .job-role-badge {
            background: linear-gradient(135deg, #2d2d2d 0%, #3a3a3a 100%);
            color: #ffffff;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.875rem;
            font-weight: 600;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
            border: 1px solid #444444;
        }
        
        .job-role-badge:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(255, 255, 255, 0.05);
            background: linear-gradient(135deg, #3a3a3a 0%, #4a4a4a 100%);
        }
        
        .job-role-description {
            color: #999999;
            line-height: 1.6;
        }
        
        .sidebar-section {
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
            padding: 1.5rem;
            border-radius: 15px;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.6);
            border: 1px solid #333333;
        }
        
        .skill-match {
            color: #22c55e;
            font-weight: 600;
            background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .skill-missing {
            color: #ef4444;
            font-weight: 600;
            background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .proficiency-expert { 
            color: #22c55e; 
            font-weight: bold; 
            background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .proficiency-advanced { 
            color: #ffffff; 
            font-weight: bold;
            background: linear-gradient(135deg, #ffffff 0%, #cccccc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .proficiency-intermediate { 
            color: #fbbf24; 
            font-weight: bold;
            background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .proficiency-beginner { 
            color: #ef4444; 
            font-weight: bold;
            background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .proficiency-novice { 
            color: #999999; 
            font-weight: bold;
            background: linear-gradient(135deg, #999999 0%, #666666 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .recommendation-box {
            background: linear-gradient(135deg, #1a1a1a 0%, #0f0f0f 100%);
            border-left: 5px solid #666666;
            padding: 1.5rem;
            margin: 1rem 0;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.6);
            border: 1px solid #333333;
            position: relative;
            overflow: hidden;
        }
        
        .recommendation-box::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, #666666, transparent);
            opacity: 0.3;
        }
        
        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, #666666 0%, #888888 100%);
            border-radius: 10px;
        }
        
        /* Animation styles */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @keyframes slideIn {
            from { opacity: 0; transform: translateX(-20px); }
            to { opacity: 1; transform: translateX(0); }
        }
        
        @keyframes glow {
            0%, 100% { box-shadow: 0 0 5px rgba(255, 255, 255, 0.1); }
            50% { box-shadow: 0 0 20px rgba(255, 255, 255, 0.2); }
        }
        
        .animate-fade-in {
            animation: fadeIn 0.6s ease-out;
        }
        
        .animate-slide-in {
            animation: slideIn 0.8s ease-out;
        }
        
        .animate-glow {
            animation: glow 2s ease-in-out infinite;
        }
        
        /* Responsive design */
        @media (max-width: 1200px) {
            .main-header {
                font-size: 3rem;
            }
            .hero-subtitle {
                font-size: 1.2rem;
            }
        }
        
        @media (max-width: 768px) {
            .main-header {
                font-size: 2.5rem;
                padding: 1.5rem;
            }
            .hero-subtitle {
                font-size: 1.1rem;
                padding: 0 1rem;
            }
            .sub-header {
                font-size: 1.5rem;
            }
            .metric-card, .feature-card, .stat-item {
                padding: 1.5rem;
                margin-bottom: 1rem;
            }
            .feature-icon {
                font-size: 2rem;
            }
            .stat-number {
                font-size: 2rem;
            }
        }
        
        @media (max-width: 480px) {
            .main-header {
                font-size: 2rem;
                padding: 1rem;
            }
            .hero-subtitle {
                font-size: 1rem;
                padding: 0 0.5rem;
            }
            .sub-header {
                font-size: 1.3rem;
                padding: 0.5rem;
            }
            .metric-card, .feature-card, .stat-item {
                padding: 1rem;
                margin-bottom: 0.8rem;
            }
            .feature-icon {
                font-size: 1.8rem;
                margin-bottom: 0.8rem;
            }
            .feature-title {
                font-size: 1.2rem;
            }
            .feature-description {
                font-size: 0.9rem;
            }
            .stat-number {
                font-size: 1.8rem;
            }
            .stat-label {
                font-size: 0.9rem;
            }
            .job-role-card {
                padding: 1rem;
            }
            .job-role-title {
                font-size: 1.1rem;
            }
            .job-role-badge {
                font-size: 0.75rem;
                padding: 0.2rem 0.5rem;
            }
            .recommendation-box {
                padding: 1rem;
            }
        }
        
        /* Mobile-specific adjustments */
        @media (max-width: 768px) {
            .stApp {
                padding: 0.5rem !important;
            }
            
            .stMain {
                padding-left: 1rem !important;
                padding-right: 1rem !important;
            }
            
            /* Stack columns on mobile */
            .stColumns > div {
                width: 100% !important;
                margin-bottom: 1rem;
            }
            
            /* Adjust button sizes */
            .stButton > button {
                padding: 0.6rem 1rem !important;
                font-size: 0.9rem !important;
            }
            
            /* Adjust file uploader */
            .stFileUploader > div {
                padding: 1rem !important;
            }
            
            /* Adjust charts for mobile */
            .js-plotly-plot {
                width: 100% !important;
                height: auto !important;
            }
        }
        
        /* Tablet-specific adjustments */
        @media (min-width: 769px) and (max-width: 1024px) {
            .main-header {
                font-size: 2.8rem;
            }
            .hero-subtitle {
                font-size: 1.15rem;
            }
            .metric-card, .feature-card {
                padding: 1.5rem;
            }
        }
        
        /* Scrollbar styling */
        ::-webkit-scrollbar {
            width: 10px;
        }
        
        ::-webkit-scrollbar-track {
            background: #1a1a1a;
            border-radius: 5px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #666666 0%, #888888 100%);
            border-radius: 5px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, #888888 0%, #aaaaaa 100%);
        }
        
        /* Enhanced hover effects */
        .metric-card:hover {
            animation: glow 2s ease-in-out infinite;
        }
        
        .feature-card:hover {
            animation: glow 2s ease-in-out infinite;
        }
        
        /* Remove unwanted symbols and emojis */
        .feature-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            filter: grayscale(20%);
        }
        
        /* Clean text without symbols */
        .clean-text {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            font-weight: 400;
            line-height: 1.6;
        }
    </style>
    <script>
        // Hide Streamlit elements after page load
        document.addEventListener('DOMContentLoaded', function() {
            // Hide any remaining Streamlit branding
            const elementsToHide = [
                '[data-testid="stHeader"]',
                '[data-testid="stFooter"]',
                '.stDeployButton',
                '#MainMenu',
                'footer',
                'header'
            ];
            
            elementsToHide.forEach(selector => {
                const elements = document.querySelectorAll(selector);
                elements.forEach(el => {
                    el.style.display = 'none';
                    el.style.visibility = 'hidden';
                });
            });
            
            // Hide any elements containing "Made with Streamlit" or similar text
            const allElements = document.querySelectorAll('*');
            allElements.forEach(el => {
                if (el.textContent && (
                    el.textContent.includes('Made with Streamlit') ||
                    el.textContent.includes('Streamlit') ||
                    el.textContent.includes('by Streamlit')
                )) {
                    el.style.display = 'none';
                    el.style.visibility = 'hidden';
                }
            });
        });
        
        // Run periodically to catch dynamically added elements
        setInterval(() => {
            const elementsToHide = [
                '.stDeployButton',
                '[data-testid="stFooter"]'
            ];
            
            elementsToHide.forEach(selector => {
                const elements = document.querySelectorAll(selector);
                elements.forEach(el => {
                    el.style.display = 'none';
                    el.style.visibility = 'hidden';
                });
            });
        }, 1000);
    </script>
    """, unsafe_allow_html=True)

def create_progress_ring(percentage: float, title: str) -> go.Figure:
    """Create a circular progress indicator with black theme colors"""
    fig = go.Figure(data=[go.Pie(
        values=[percentage, 100 - percentage],
        hole=0.7,
        showlegend=False,
        textinfo='none',
        marker_colors=['#22c55e' if percentage >= 70 else '#fbbf24' if percentage >= 40 else '#ef4444', '#1a1a1a']
    )])
    
    fig.add_annotation(
        text=f"{percentage}%",
        x=0.5, y=0.5,
        font_size=20,
        font_color='#ffffff',
        showarrow=False
    )
    
    fig.add_annotation(
        text=title,
        x=0.5, y=0.3,
        font_size=12,
        font_color='#999999',
        showarrow=False
    )
    
    fig.update_layout(
        height=200,
        margin=dict(t=20, b=20, l=20, r=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='#ffffff'
    )
    
    return fig

def create_skill_bar_chart(matched_skills: List[str], missing_skills: List[str]) -> go.Figure:
    """Create a bar chart showing matched vs missing skills with black theme"""
    categories = ['Matched Skills', 'Missing Skills']
    values = [len(matched_skills), len(missing_skills)]
    colors = ['#22c55e', '#ef4444']
    
    fig = go.Figure(data=[
        go.Bar(
            x=categories,
            y=values,
            marker_color=colors,
            text=values,
            textposition='auto',
            textfont_color='#ffffff'
        )
    ])
    
    fig.update_layout(
        title="Skill Match Overview",
        title_font_color='#ffffff',
        xaxis_title="Skill Status",
        xaxis_title_font_color='#999999',
        yaxis_title="Number of Skills",
        yaxis_title_font_color='#999999',
        height=400,
        showlegend=False,
        plot_bgcolor='#1a1a1a',
        paper_bgcolor='#0f0f0f',
        font_color='#ffffff',
        xaxis=dict(
            tickfont_color='#999999',
            gridcolor='#333333'
        ),
        yaxis=dict(
            tickfont_color='#999999',
            gridcolor='#333333'
        )
    )
    
    return fig

def create_skill_radar_chart(skill_analysis: Dict, skill_categories: Dict) -> go.Figure:
    """Create a radar chart for skill categories with black theme"""
    if not skill_categories:
        return go.Figure()
    
    categories = list(skill_categories.keys())
    values = [cat_data['match_percentage'] for cat_data in skill_categories.values()]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Skill Coverage',
        line_color='#ffffff',
        fillcolor='rgba(255, 255, 255, 0.1)',
        textfont_color='#ffffff'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont_color='#999999',
                gridcolor='#333333',
                linecolor='#666666'
            ),
            angularaxis=dict(
                tickfont_color='#999999',
                gridcolor='#333333',
                linecolor='#666666'
            )
        ),
        title="Skill Coverage by Category",
        title_font_color='#ffffff',
        height=500,
        plot_bgcolor='#1a1a1a',
        paper_bgcolor='#0f0f0f',
        font_color='#ffffff',
        legend=dict(
            font_color='#ffffff'
        )
    )
    
    return fig

def display_skill_cards(skills: List[str], title: str, color_class: str):
    """Display skills as cards with better validation"""
    if not skills:
        st.markdown(f"""
        <div class="metric-card" style="opacity: 0.7; border-left-color: #64748b;">
            <h4 style="color: #94a3b8; margin: 0;">{title}</h4>
            <p style="color: #64748b; margin: 0.5rem 0 0 0;">No skills found</p>
        </div>
        """, unsafe_allow_html=True)
        return
    
    st.markdown(f"**{title} ({len(skills)})**")
    
    # Create columns for skill cards (max 4 per row)
    cols = st.columns(min(4, max(1, len(skills))))
    
    for i, skill in enumerate(skills):
        if skill and skill.strip():  # Ensure skill is not empty
            col_idx = i % len(cols)
            with cols[col_idx]:
                st.markdown(f"""
                <div class="metric-card">
                    <span class="{color_class}">{skill.strip()}</span>
                </div>
                """, unsafe_allow_html=True)
