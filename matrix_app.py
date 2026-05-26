import streamlit as st
import numpy as np

# 1. सॉफ्टवेयर की हेडिंग
st.set_page_config(page_title="Matrix Solver", page_icon="🧮")
st.title("🧮 Matrix Solver & Explorer")
st.write("Created by M.Sc. Math & Computing Student")

st.markdown("---")
st.subheader("Enter your 2x2 Matrix Elements:")

# 2. यूजर से नंबर इनपुट कराने के बॉक्स
col1, col2 = st.columns(2)
with col1:
    a11 = st.number_input("Element (1,1)", value=1.0)
    a21 = st.number_input("Element (2,1)", value=3.0)
with col2:
    a12 = st.number_input("Element (1,2)", value=2.0)
    a22 = st.number_input("Element (2,2)", value=4.0)

# मैट्रिक्स बनाना
matrix = np.array([[a11, a12], [a21, a22]])
st.write("### Your Matrix:")
st.write(matrix)

st.markdown("---")

# 3. कैलकुलेशन का बटन और मैथ का लॉजिक
if st.button("⚡ Solve Matrix Now"):
    st.subheader("📊 Results:")
    det = np.linalg.det(matrix)
    st.metric(label="Determinant (सारणिक)", value=f"{det:.2f}")
    st.write("**Transpose Matrix:**")
    st.write(matrix.T)
    if det != 0:
        st.write("**Inverse Matrix:**")
        st.write(np.linalg.inv(matrix))
    else:
        st.error("Inverse does not exist because Determinant is 0!")
