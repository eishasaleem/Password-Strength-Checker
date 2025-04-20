import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

st.title("🔐 Password Strength Checker")

# User input
password = st.text_input("Enter your password", type="password")

# Password strength checker function
def check_password_strength(pw):
    suggestions = []
    score = 0

    # Criteria checks
    if len(pw) >= 8:
        score += 1
    else:
        suggestions.append("➤ Use at least 8 characters")

    if re.search(r"[A-Z]", pw) and re.search(r"[a-z]", pw):
        score += 1
    else:
        suggestions.append("➤ Include both uppercase and lowercase letters")

    if re.search(r"\d", pw):
        score += 1
    else:
        suggestions.append("➤ Add at least one digit")

    if re.search(r"[!@#$%^&*]", pw):
        score += 1
    else:
        suggestions.append("➤ Add a special character (!@#$%^&*)")

    # Add +1 if all criteria are met
    if score == 4:
        score += 1

    # Determine strength level
    if score <= 2:
        strength = "Weak 🔴"
    elif score <= 4:
        strength = "Moderate 🟠"
    else:
        strength = "Strong 🟢"

    return strength, score, suggestions

# Display results
if password:
    strength, score, feedback = check_password_strength(password)

    st.markdown(f"### Password Strength: **{strength}**")
    st.markdown(f"**Score:** {score} / 5")

    if score < 5:
        st.warning("💡 Suggestions to improve your password:")
        for tip in feedback:
            st.markdown(f"- {tip}")
    else:
        st.success("✅ Your password is strong! Great job!")
