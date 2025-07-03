Copyright 2025
Michael Hart

Generates a complete range of numbers based on a partial phone number. 
Spam callers often spoof similar-looking numbers. This tool helps you generate contacts covering those similar numbers so you can block them all at once.

### Example

Spam calls might come from:
202-555-1212
202-555-1234
202-555-1010

If you enter <20255512> the app will generate a contact with 100 numbers in the range 202-555-12XX:

202-555-1200
202-555-1201
202-555-1202
...
202-555-1299

You can then block this single contact to cover the entire range.

This will, however, still allow calls from the x1010 range.

Entering <2025551> would generate a similar contact with 1000 numbers:

202-555-1000
202-555-1001
202-555-1002
...
202-555-1999

Caution: exported file size increases exponentially. Most devices will struggle to import contacts this large. 

Entering at least 7 digits (1000 numbers or less) is recommended.



Live app:
https://harts-contact-generator.streamlit.app

Run locally:
git clone https://github.com/OMGHart/range-contact-generator.git
cd range-contact-generator
pip install -r requirements.txt
streamlit run streamlit_app.py

Tip jar, if this has helped you block some spam:
PayPal/@OMGHart
Venmo/@OMGHart
Cashapp/$OMGHart
