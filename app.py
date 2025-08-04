import streamlit as st

# Title and intro
st.title("🌸 My Love Story 🌸")

# Session state to keep track of attempts
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

# Correct password
correct_password = "pillu1438"

# Love language clues for password
clues = [
    "1️⃣ Infinite love is comprised in this number - ?",
    "2️⃣ It's YOU but in number - ?",
    "3️⃣ My birthday second digit - previous answer == ?",
    "4️⃣ If I am 99, you are that... - ?",
    "5️⃣ It’s a letter but it's always second here, as well as in letters of the last group trip we visited - ?",
    "6️⃣ It’s two letters consecutively that appear as 2 in Roman numerals",
    "7️⃣ One ___ sees, the other feels — it's a letter -- Fill in the blanks",
    "8️⃣ Your nickname’s first letter -- ?",
    "🔁 Now reverse it (Note!!! all letters are in small case)"
]

# Show password input only if not yet unlocked
if not st.session_state.unlocked:
    st.subheader("Enter the password with love 💖")
    password_input = st.text_input("Password", type="password")

    if st.button("Submit"):
        if password_input == correct_password:
            st.session_state.unlocked = True
            st.balloons()
            st.success("Access granted! 💕")
        else:
            st.session_state.attempts += 1
            st.error("Wrong password 💔")
            # if st.session_state.attempts >= 3:
            #     st.info("Hint: My birthday first digit + your birthday first digit")

# Show love letter if password is correct
if st.session_state.unlocked:
    st.markdown("## 💌 My Love Letter to You")
    love_letter = """
I first met Pillu at MJ Avyana. She was shy, and though everyone was forcing her to dance, she just did a few moves and left.  
She caught my eye when she took my side during Amal and Nandana’s debate.  
I fell more in love with her when she got angry at me and said, “Sochte hi reh phir,” and went alone to watch Sanam Teri Kasam.

I fell even deeper when, after Qissa, she went with Preetam and was still ready to drive me to Manyata afterward.

With each step, I kept falling more and more in love with her.  
In *Chikmagalur*, every moment — especially that night with Mirinda and deep conversations — made me fall for her all over again.  
Her smile, the way she looked into my eyes, the way she cared — I kept falling more.

*Chennai* became truly special to me.  
The date *01/03* was incredibly special — just pure love, no physical touch.  
The Milano, Bueno chocolates, sunflowers, Van Gogh diary, keychain — I have them all.  
I’m constantly falling for her — with every action.

Food makes her happy. For that, I went to *Kalyan Nagar*, explored different restaurants with her.  
Just us, discovering something new. Movies, Meet sessions, anime nights — memories I cherish deeply.

She sends me snaps, surprised me near Shanky Tank Park — how could I not love her madly?  
The moment in *Hampi*, when I fed her prasad and she looked like an angel — it overwhelmed me.

Her happiness lifts me. Her sadness sinks me.  
Despite my mistakes — Pillu, one thing never changed: my love for you.

From a drop to an *ocean*, my love has only grown.

I just want you to be *happy*. Always.
"""
    st.markdown(love_letter)

# Optionally, display the clues below the password box
with st.expander("💡 Want clues for the password?"):
    for clue in clues:
        st.markdown(clue)