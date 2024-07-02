import streamlit as st
import streamlit.components.v1 as components

st.title("July PAN India meet (TADKA)")
# Vimeo embed URL with autoplay and muted parameters removed
vimeo_url =st.secrets["video"]

# Embed the Vimeo video using an iframe
components.iframe(vimeo_url, width=500, height=500)
google_form_url =st.secrets["form"]
meeting_minutes = st.secrets["meeting_minutes"]

# Use st.expander to create an expandable section
with st.expander("Meeting Minutes"):
    st.markdown(meeting_minutes)
    
with st.expander("Feedback form"):
    # Use st.markdown to display the Google Form within an iframe
    st.markdown(f'<iframe src="{google_form_url}" width="100%" height="600px" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>', unsafe_allow_html=True)

with st.expander("Contact us", expanded=False):
    st.markdown(st.secrets["contact"])
