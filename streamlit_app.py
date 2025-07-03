import streamlit as st
from contact_utils import get_label, generate_number_list, export_vcard
import os

# st.set_page_config(page_title="Hart's Contact Range Generator", layout="centered")

st.set_page_config(
    page_title="Hart's Contact Generator",
    page_icon="📵",
    layout="centered"
)

st.title("📵 Hart’s Number Range Generator")
st.markdown("Create a contact with every phone number in a range - and block them all at once.")


# st.markdown("# Welcome to Hart’s Number Range Generator!")
st.markdown(
    """   
    
    This tool creates a **.vcf contact file** containing every phone number in the requested range.  
    Add the contact to your device and block it to silence entire number blocks.

    ---
    """
)



# st.title("Welcome to Hart's range contact generator!")
# print()  
# st.markdown("This program will generate a contact with every phone number in the requested range.")
# st.markdown("To block a range: add the contact to your device, and block the contact!")
# st.markdown("Enter a partial phone number")
# prefix = st.text_input("Enter a partial phone number:", max_chars = 9)

with st.form("block_form"):
    prefix = st.text_input("Enter a partial phone number:", max_chars=9)
    submitted = st.form_submit_button("Generate Contact")

if submitted:
    if not prefix.isdigit():
        st.error("Please enter digits only.")
    elif int(prefix) < 1000:
        st.error("Please enter at least 4 digits (up to 1,000,000 numbers).")
    else:
        number = int(prefix)
        label = get_label(number)
        numbers = generate_number_list(number)
        export_vcard(numbers, label)

        with open(f"{label}.vcf", "rb") as f:
            st.download_button(
                label="📥 Download VCARD",
                data=f,
                file_name=f"{label}.vcf",
                mime="text/vcard"
            )
        st.success(f"✅ Contact file generated: `{label}.vcf`")
        if number < 1000000:
            range_power = 10-len(str(number))
            block_len = 10**(range_power)
            st.warning(f"⚠️ Warning: File contains {block_len:,} numbers. Most mobile devices are incapable of handling contacts of this size. Proceed with caution.")
            # st.info("Proceed with caution.")

st.markdown("---")  # horizontal line for clarity

st.subheader("Example")

st.markdown("""
Spam calls might come from:

- `202-555-1212`  
- `202-555-1234`  
- `202-555-1010`

If you enter *20255512* the app will generate a contact with 100 numbers in the range `202-555-12XX`:

- `202-555-1200`  
- `202-555-1201`  
- `...`  
- `202-555-1299`

You can then save and block this single contact to cover the entire range.
This would, however, still allow calls from `202-555-1010`.

Entering *2025551* would generate a similar contact with 1000 numbers, successfully blocking the three above numbers and any others the range `202-555-1XXX`:

- `202-555-1000`  
- `202-555-1001`  
- `...`  
- `202-555-1999`

⚠️ Caution: exported file size increases exponentially. Most mobile devices will struggle to import contacts this large. 

Entering at least 7 digits (1000 numbers or less) is recommended if using a mobile device.
"""
           )




        # Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; font-size: 0.9em;">
        © 2025 Michael Hart  
        <br>
        <a href="https://github.com/OMGHart/range-contact-generator" target="_blank">
            Source Code: GitHub
        </a>
        <br><br>
    </div>
    """,
    unsafe_allow_html=True
)
            
                   
