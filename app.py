import streamlit as st
import streamlit.components.v1 as components

st.title("July PAN India meet (TADKA)")
# Vimeo embed URL with autoplay and muted parameters removed
vimeo_url = "https://player.vimeo.com/video/973685044?title=0&byline=0&portrait=0&badge=0&autopause=0&player_id=0&app_id=58479&autoplay=0"

# Embed the Vimeo video using an iframe
components.iframe(vimeo_url, width=640, height=360)


with st.expander("National Social Media Coordinators", expanded=False):
    st.markdown("""
    ### National Social Media Coordinators:
    - **Kunal Singh Chauhan**: 95950 50117
    - **Subhodeep**: 87894 37422
    - **Rishabh Purohit**: +91 99742 46013
    - **N. Manikandan**: 98943 20282

    ### Team NSC Office:
    - **Aksahy**: 70168 10955
    - **Narendra**: 76250 53713
    """)
