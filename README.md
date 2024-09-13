# 🧑‍💻IDA (IDX Data Assitant)

## 📜Overview of the App

IDA is a chatbot AI that have connection to IDX data. IDA get data from sectors.app API and process it according to the user queries. IDA will help you to drill down some of IDX data. Let's ask IDA what it can do:

> 🧑‍💻 Hi! This is IDA speaking. I can assist you with various queries **related to the IDX data**. Here are some of the things I can do:
>
> 1.  **Get Company Overview**: I can provide an overview of a company listed on the IDX, including its listing board, industry, sub-industry, sector, sub-sector, market capitalization, market capitalization rank, address, number of employees, listing date, website, phone number, email, last closing price, and the latest closing date.
> 2.  **Get Top Companies by Transaction Volume**: I can find the top companies by transaction volume within a specified date range.
>
> 3.  **Get Daily Transaction Data**: I can retrieve daily transaction data for a specific stock, including closing price, transaction volume, and market capitalization, within a given date range.
>
> 4.  **Get Top Companies by Growth**: I can identify the top companies by earnings growth or revenue growth within a specific sub-sector.
>
> 5.  **Get Subsector**: I can list all the subsectors available in the IDX data.
>
> 6.  **Get Company Performance since IPO**: I can provide the listing performance of a stock since its Initial Public Offering (IPO).
>
> 7.  **Get Top Companies Ranked**: I can rank the top companies by market capitalization, dividend yield, earnings, revenue, and total dividend for a specific year.
>
> Please let me know how I can assist you further with your queries.

Ask IDA yourself. Let's do the demo.

## 💻 Demo App

First of all you should get sectors API key and also chatgroq API key since we will used it as part of our chatbot. To get both API key you can get it from here:

- [Sectors App API](https://sectors.app/api)
- [Chat Groq API](https://console.groq.com/keys)

After get the API key you can use the key to ask IDA in [IDA (IDX Data Assistant)](https://idx-data-assistant.streamlit.app/). Insert your own key to the sidebar.

There are two pages for this chatbot.

1. **IDX Data Assistant**
   - This page will return chatbot that **retrieve IDX data** from **sectors app API** and answer all the queries based on the data retrieve.
   - It uses **RAG system** to response based on the tool used.
   - LLM model that's being used is **llama3-groq-70b-8192-tool-use-preview**
2. **General Assistant**
   - This page will return chatbot that response based on the **llm knowledge**.
   - LLM model that's being used is **llama3-8b-8192**

## 💾 Run Locally

You can try to run it locally by clone all the github code and first of all install the dependencies locally.

```bash
pip install -r requirements.txt
```

After that run the streamlit app by running the code below.

```bash
streamlit run IDX_Data_Assistant.py
```

Now you can chat with IDA and ask all about IDX data. Happy Chatting! 😁😁.
