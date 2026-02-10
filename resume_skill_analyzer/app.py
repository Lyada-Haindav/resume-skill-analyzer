"""
AI Resume Skill Gap Analyzer
Single-page application with home and analysis sections
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
import sys
import os
from typing import Dict, List

# Add modules to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'nlp_modules'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

from nlp_modules.skill_extractor import SkillExtractor
from utils.pdf_extractor import PDFExtractor
from utils.skill_analyzer import SkillAnalyzer
from utils.shared import set_custom_css, create_progress_ring, create_skill_bar_chart, create_skill_radar_chart, display_skill_cards

# Page configuration
st.set_page_config(
    page_title="AI Resume Skill Gap Analyzer",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={}
)

# Hide sidebar completely with CSS
hide_sidebar_style = """
<style>
    [data-testid="stSidebar"] {
        display: none !important;
    }
    .stMain {
        max-width: 100% !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }
</style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)

# Initialize session state for navigation
if 'current_section' not in st.session_state:
    st.session_state.current_section = 'home'

if 'analysis_complete' not in st.session_state:
    st.session_state.analysis_complete = False
if 'resume_text' not in st.session_state:
    st.session_state.resume_text = ""
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = None

# Set custom styling
set_custom_css()

# Navigation
if st.session_state.current_section == 'home':
    # HOME PAGE
    st.markdown('<h1 class="main-header">AI Resume Skill Gap Analyzer</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Transform your career with AI-powered skill analysis and personalized recommendations</p>', unsafe_allow_html=True)
    
    # Features Section
    st.markdown('<h2 class="sub-header">Why Choose Our AI Analyzer?</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card animate-fade-in">
            <div class="feature-icon">🧠</div>
            <div class="feature-title">Advanced NLP</div>
            <div class="feature-description">
                Cutting-edge natural language processing extracts skills with 95% accuracy using TF-IDF, tokenization, and semantic analysis
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card animate-fade-in">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Smart Analytics</div>
            <div class="feature-description">
                Interactive visualizations and comprehensive gap analysis with personalized learning recommendations
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card animate-fade-in">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Career Insights</div>
            <div class="feature-description">
                15+ job roles with salary ranges, growth potential, and detailed skill requirements
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Statistics Section
    st.markdown('<h2 class="sub-header">Platform Statistics</h2>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="stat-item">
            <div class="stat-number">15+</div>
            <div class="stat-label">Job Roles</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-item">
            <div class="stat-number">200+</div>
            <div class="stat-label">Skills Tracked</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-item">
            <div class="stat-number">95%</div>
            <div class="stat-label">Accuracy Rate</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stat-item">
            <div class="stat-number">24/7</div>
            <div class="stat-label">Available</div>
        </div>
        """, unsafe_allow_html=True)
    
    # How It Works Section
    st.markdown('<h2 class="sub-header">How It Works</h2>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #ffffff; margin-bottom: 1rem;">Step 1</h3>
            <p style="color: #999999; margin: 0;">Upload your resume in PDF or text format</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #ffffff; margin-bottom: 1rem;">Step 2</h3>
            <p style="color: #999999; margin: 0;">Select your target job role from our database</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #ffffff; margin-bottom: 1rem;">Step 3</h3>
            <p style="color: #999999; margin: 0;">AI analyzes your skills against requirements</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #ffffff; margin-bottom: 1rem;">Step 4</h3>
            <p style="color: #999999; margin: 0;">Get detailed insights and recommendations</p>
        </div>
        """, unsafe_allow_html=True)
    
    # CTA Section
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 3rem 0;">
            <h2 style="color: #ffffff; margin-bottom: 1rem;">Ready to Transform Your Career?</h2>
            <p style="color: #999999; margin-bottom: 2rem; font-size: 1.1rem;">
                Get personalized skill analysis and career recommendations in minutes
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Start Analysis", type="primary", use_container_width=True):
            st.session_state.current_section = 'analysis'
            st.rerun()

else:
    # ANALYSIS PAGE
    st.markdown('<h1 class="main-header">Resume Analysis</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Upload your resume and get AI-powered skill analysis</p>', unsafe_allow_html=True)
    
    # Navigation buttons
    col1, col2 = st.columns([1, 3])
    
    with col1:
        if st.button("Home", use_container_width=True):
            st.session_state.current_section = 'home'
            st.rerun()
    
    # Configuration Section
    st.markdown('<h2 class="sub-header">Configuration</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Upload Resume**")
        uploaded_file = st.file_uploader(
            "Choose a file",
            type=['pdf', 'txt'],
            help="Upload your resume in PDF or text format"
        )
    
    with col2:
        st.markdown("**Select Job Role**")
        job_skills_path = os.path.join(os.path.dirname(__file__), 'data', 'job_skills.json')
        
        try:
            skill_extractor = SkillExtractor(job_skills_path)
            job_roles = skill_extractor.get_all_job_roles()
            selected_job_role = st.selectbox(
                "Choose your target role",
                job_roles,
                help="Select the job role you want to analyze your resume against"
            )
            
            # Display job role details
            job_data = skill_extractor.job_skills_data['job_roles'][selected_job_role]
            st.markdown(f"""
            <div class="job-role-card">
                <div class="job-role-title">{selected_job_role}</div>
                <div class="job-role-meta">
                    <span class="job-role-badge">{job_data['experience_level']}</span>
                    <span class="job-role-badge">{job_data['salary_range']}</span>
                    <span class="job-role-badge">{job_data['growth_potential']} Growth</span>
                </div>
                <div class="job-role-description">{job_data['description']}</div>
            </div>
            """, unsafe_allow_html=True)
                
        except Exception as e:
            st.error(f"Error loading job roles: {e}")
            selected_job_role = None
    
    # Analyze button
    if uploaded_file is not None and selected_job_role:
        analyze_button = st.button(
            "🔍 Analyze Resume",
            type="primary",
            use_container_width=True,
            help="Click to start the skill gap analysis"
        )
        
        if analyze_button:
            # Validate file before processing
            if uploaded_file.size == 0:
                st.error("📄 The uploaded file is empty. Please choose a valid file.")
            elif uploaded_file.name.lower().endswith('.pdf') and uploaded_file.size < 1000:
                st.warning("⚠️ The PDF file seems too small. Please ensure it contains your resume content.")
            else:
                # Extract text from uploaded file
                with st.spinner("📄 Extracting text from resume..."):
                    resume_text = PDFExtractor.extract_text_from_uploaded_file(uploaded_file)
                    
                    if resume_text is None or resume_text.strip() == "":
                        st.error("❌ Failed to extract text from the uploaded file. The file might be corrupted or empty. Please try a different file.")
                    elif len(resume_text.strip()) < 50:
                        st.warning("⚠️ The extracted text seems very short. Please ensure your resume contains sufficient content for analysis.")
                    else:
                        st.session_state.resume_text = resume_text
                        st.success(f"✅ Successfully extracted {len(resume_text)} characters from your resume!")
                        
                        # Perform skill extraction and analysis
                        with st.spinner("🧠 Analyzing skills with NLP..."):
                            try:
                                # Extract skills from resume
                                resume_skills = skill_extractor.extract_skills_combined(resume_text)
                                
                                # Validate extracted skills
                                if not resume_skills:
                                    st.error("❌ No skills could be extracted from your resume. Please ensure your resume contains technical skills and keywords.")
                                else:
                                    # Get required skills for selected job
                                    required_skills = skill_extractor.get_job_role_skills(selected_job_role)
                                    
                                    # Validate required skills
                                    if not required_skills:
                                        st.error(f"❌ No required skills found for the job role: {selected_job_role}")
                                    else:
                                        # Perform skill gap analysis
                                        skill_analyzer = SkillAnalyzer()
                                        analysis_results = skill_analyzer.analyze_skill_gaps(resume_skills, required_skills)
                                        
                                        # Validate analysis results
                                        if not analysis_results:
                                            st.error("❌ Analysis failed to produce results. Please try again.")
                                        else:
                                            # Get category analysis
                                            skill_categories = skill_extractor.categorize_skills(list(resume_skills.keys()))
                                            category_analysis = skill_analyzer.get_skill_category_analysis(
                                                resume_skills, required_skills, skill_extractor.job_skills_data['technical_skills_database']
                                            )
                                            
                                            # Store results
                                            analysis_results['category_analysis'] = category_analysis
                                            analysis_results['resume_skills'] = resume_skills
                                            analysis_results['required_skills'] = required_skills
                                            st.session_state.analysis_results = analysis_results
                                            st.session_state.analysis_complete = True
                                            
                                            # Show success message with details
                                            st.success(f"✅ Analysis completed! Found {len(resume_skills)} skills in your resume and analyzed against {len(required_skills)} required skills.")
                                            
                            except Exception as e:
                                st.error(f"❌ Error during analysis: {str(e)}")
                                st.info("💡 Please ensure your resume is in a supported format (PDF/TXT) and contains readable text content.")
    
    # Display results
    if st.session_state.analysis_complete and st.session_state.analysis_results:
        results = st.session_state.analysis_results
        
        # Success message
        st.success("✅ Analysis completed successfully!")
        
        # Key metrics row
        st.markdown('<h2 class="sub-header">📊 Analysis Summary</h2>', unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            fig1 = create_progress_ring(results['match_percentage'], "Match Rate")
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            fig2 = create_progress_ring(int(results['similarity_score'] * 100), "Similarity")
            st.plotly_chart(fig2, use_container_width=True)
        
        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <h3 style="color: {results['proficiency_color']}; margin: 0;">
                    {results['proficiency_level']}
                </h3>
                <p style="margin: 0.5rem 0 0 0; color: #6b7280;">Proficiency Level</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="metric-card">
                <h3 style="color: #3b82f6; margin: 0;">
                    {results['total_matched_skills']}/{results['total_required_skills']}
                </h3>
                <p style="margin: 0.5rem 0 0 0; color: #6b7280;">Skills Matched</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Skills breakdown
        st.markdown('<h2 class="sub-header">🎯 Skills Breakdown</h2>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            display_skill_cards(results['matched_skills'], "✅ Matched Skills", "skill-match")
        
        with col2:
            display_skill_cards(results['missing_skills'], "❌ Missing Skills", "skill-missing")
        
        # Visualizations
        st.markdown('<h2 class="sub-header">📈 Visual Analytics</h2>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig_bar = create_skill_bar_chart(results['matched_skills'], results['missing_skills'])
            st.plotly_chart(fig_bar, use_container_width=True)
        
        with col2:
            if results['category_analysis']:
                fig_radar = create_skill_radar_chart(results, results['category_analysis'])
                st.plotly_chart(fig_radar, use_container_width=True)
        
        # Recommendations
        if results['recommendations']:
            st.markdown('<h2 class="sub-header">💡 Recommendations</h2>', unsafe_allow_html=True)
            
            for i, recommendation in enumerate(results['recommendations'], 1):
                st.markdown(f"""
                <div class="recommendation-box">
                    <strong>{i}.</strong> {recommendation}
                </div>
                """, unsafe_allow_html=True)


# Footer
st.markdown("---")
st.markdown("""
<div class="custom-footer">
    <strong>🎯 AI Resume Skill Gap Analyzer</strong><br>
    <span style="color: #94a3b8;">Powered by Advanced NLP Technology</span>
</div>
""", unsafe_allow_html=True)
