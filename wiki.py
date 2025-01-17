import streamlit as st
from bs4 import BeautifulSoup
import pandas as pd
import requests
st.title("Wikipedia Table Scraper")
url = st.text_input("Enter Wikipedia URL (must start with 'https://en.wikipedia.org'): ")
if st.button("SCRAPE"):
    if url.startswith("https://en.wikipedia.org"):  
        try:
        
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

           
            tables = soup.find_all("table", {"class": "wikitable"})

            if tables:
                st.success(f"Found {len(tables)} table(s) on the page.")
                
                
                for i, table in enumerate(tables, 1):
                    st.write(f"Table {i}:")

                    headers = [header.text.strip() for header in table.find_all("th")]

                    rows = table.find_all("tr")
                    data = []
                    for row in rows:
                        cells = row.find_all(["td", "th"]) 
                        data.append([cell.text.strip() for cell in cells])

                    max_columns = max(len(row) for row in data) 
                    if not headers or len(headers) != max_columns:
                        headers = [f"Column {j+1}" for j in range(max_columns)]  
                    
                    df = pd.DataFrame(data, columns=headers[:max_columns])

                    
                    st.write(df)

            else:
                st.warning("No tables found on this Wikipedia page.")

        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching the URL: {e}")
        except ValueError as e:
            st.error(f"Error processing the table: {e}")
    else:
        st.warning("Please enter a valid Wikipedia URL starting with 'https://en.wikipedia.org'.")
        
st.markdown("Developed by : Samyog :smile:") 
