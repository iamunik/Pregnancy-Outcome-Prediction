import streamlit as st

# Page Navigation
homepage = st.Page("webpages/homepage.py", title="Welcome", icon=":material/home:")
delivery_page = st.Page("webpages/prediction.py", title="Delivery Prediction Portal", icon=":material/local_hospital:")
# team_page = st.Page("webpages/the_team.py", title="The team", icon=":material/groups:")
# verify_page = st.Page("webpages/verify_users.py", title="User Verification", icon=":material/verified_user:")

pg = st.navigation([homepage, delivery_page,])

pg.run()
