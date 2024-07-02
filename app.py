import streamlit as st
import streamlit.components.v1 as components

st.title("July PAN India meet (TADKA)")
# Vimeo embed URL with autoplay and muted parameters removed
vimeo_url = "https://player.vimeo.com/video/973685044?title=0&byline=0&portrait=0&badge=0&autopause=0&player_id=0&app_id=58479&autoplay=0"

# Embed the Vimeo video using an iframe
components.iframe(vimeo_url, width=640, height=360)
google_form_url = "https://forms.gle/3B7hxxtX2qZjZ7zf6"
meeting_minutes = """
1. Plan orientation sessions ASAP with your district coordinators. For more details, contact Kunal Singh Chauhan (NSC) and NSC desk members Akhsay and Narendra.
2. From now onwards, each State coordinator will take the lead on dissemination of content every week as per schedule.POC Subhodeep 
3. We will be aiming for a collective sankalpa of 8000 average clicks this month.POC Subhodeep 
4. We are launching a social media newsletter named "Satvified" this month for all stakeholders across India.POC Subhodeep 
5. Volunteers are needed for YouTube initiatives.POC Rishabh Purohit 
6. Connect with Kunal Ji for the fan page council.POC Kunal 
7. Discuss "wisdom of the week" and gather feedback.POC Subhodeep 
8. Refer to the above recording for more details.POC  Yourself
"""

# Use st.expander to create an expandable section
with st.expander("Meeting Minutes"):
    st.markdown(meeting_minutes)
    
with st.expander("Feedback form"):
    # Use st.markdown to display the Google Form within an iframe
    st.markdown(f'<iframe src="{google_form_url}" width="100%" height="600px" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>', unsafe_allow_html=True)

with st.expander("Contact us", expanded=False):
    st.markdown("""
    ### National Social Media Coordinators:
    - **Kunal Singh Chauhan**: 95950 50117
    - **Subhodeep**: 87894 37422
    - **Rishabh Purohit**: 99742 46013
    - **N. Manikandan**: 98943 20282

    ### Team NSC Office:
    - **Aksahy**: 70168 10955
    - **Narendra**: 76250 53713
    """)
