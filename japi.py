{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Stock Symbol or QUIT to exit:  AAPL\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{\n",
      "    \"Global Quote\": {\n",
      "        \"01. symbol\": \"AAPL\",\n",
      "        \"02. open\": \"255.9400\",\n",
      "        \"03. high\": \"270.0000\",\n",
      "        \"04. low\": \"248.0000\",\n",
      "        \"05. price\": \"248.2300\",\n",
      "        \"06. volume\": \"102420440\",\n",
      "        \"07. latest trading day\": \"2020-03-12\",\n",
      "        \"08. previous close\": \"275.4300\",\n",
      "        \"09. change\": \"-27.2000\",\n",
      "        \"10. change percent\": \"-9.8755%\"\n",
      "    }\n",
      "}\n",
      "\n",
      "The current price of AAPL is: 248.2300\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Stock Symbol or QUIT to exit:  MCD\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{\n",
      "    \"Global Quote\": {\n",
      "        \"01. symbol\": \"MCD\",\n",
      "        \"02. open\": \"174.7800\",\n",
      "        \"03. high\": \"179.8400\",\n",
      "        \"04. low\": \"169.3800\",\n",
      "        \"05. price\": \"170.1300\",\n",
      "        \"06. volume\": \"8997015\",\n",
      "        \"07. latest trading day\": \"2020-03-12\",\n",
      "        \"08. previous close\": \"188.2500\",\n",
      "        \"09. change\": \"-18.1200\",\n",
      "        \"10. change percent\": \"-9.6255%\"\n",
      "    }\n",
      "}\n",
      "\n",
      "The current price of MCD is: 170.1300\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Stock Symbol or QUIT to exit:  K\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{\n",
      "    \"Global Quote\": {\n",
      "        \"01. symbol\": \"K\",\n",
      "        \"02. open\": \"58.5200\",\n",
      "        \"03. high\": \"60.0000\",\n",
      "        \"04. low\": \"56.8400\",\n",
      "        \"05. price\": \"58.1900\",\n",
      "        \"06. volume\": \"3818564\",\n",
      "        \"07. latest trading day\": \"2020-03-12\",\n",
      "        \"08. previous close\": \"61.6900\",\n",
      "        \"09. change\": \"-3.5000\",\n",
      "        \"10. change percent\": \"-5.6735%\"\n",
      "    }\n",
      "}\n",
      "\n",
      "The current price of K is: 58.1900\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Stock Symbol or QUIT to exit:  KL\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{\n",
      "    \"Global Quote\": {\n",
      "        \"01. symbol\": \"KL\",\n",
      "        \"02. open\": \"25.3100\",\n",
      "        \"03. high\": \"27.9000\",\n",
      "        \"04. low\": \"23.8400\",\n",
      "        \"05. price\": \"25.2200\",\n",
      "        \"06. volume\": \"4042606\",\n",
      "        \"07. latest trading day\": \"2020-03-12\",\n",
      "        \"08. previous close\": \"30.3100\",\n",
      "        \"09. change\": \"-5.0900\",\n",
      "        \"10. change percent\": \"-16.7931%\"\n",
      "    }\n",
      "}\n",
      "\n",
      "The current price of KL is: 25.2200\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Stock Symbol or QUIT to exit:  KO\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{\n",
      "    \"Global Quote\": {\n",
      "        \"01. symbol\": \"KO\",\n",
      "        \"02. open\": \"48.5400\",\n",
      "        \"03. high\": \"49.9300\",\n",
      "        \"04. low\": \"46.6900\",\n",
      "        \"05. price\": \"47.1600\",\n",
      "        \"06. volume\": \"31781777\",\n",
      "        \"07. latest trading day\": \"2020-03-12\",\n",
      "        \"08. previous close\": \"52.2100\",\n",
      "        \"09. change\": \"-5.0500\",\n",
      "        \"10. change percent\": \"-9.6725%\"\n",
      "    }\n",
      "}\n",
      "\n",
      "The current price of KO is: 47.1600\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Stock Symbol or QUIT to exit:  QUIT\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "End of Program\n",
      "\n",
      "The current price of AAPL is: 248.2300\n",
      "The current price of MCD is: 170.1300\n",
      "The current price of K is: 58.1900\n",
      "The current price of KL is: 25.2200\n",
      "The current price of KO is: 47.1600\n"
     ]
    }
   ],
   "source": [
    "import json\n",
    "import urllib.request\n",
    "\n",
    "def getStockData(symbol):\n",
    "\n",
    "    try:\n",
    "        alphaURL = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='+ symbol +'&apikey=NXF67B9W86Q4H6VB'\n",
    "        connection = urllib.request.urlopen(alphaURL)\n",
    "        responseString = connection.read().decode()\n",
    "        return str(responseString)\n",
    "    except:\n",
    "        return \"Stock Symbol Unknown.\"\n",
    "\n",
    "def main(): \n",
    "    \n",
    "    \n",
    "    x=True\n",
    "    while x==True :\n",
    "        file = open(\"stockFile.txt\", \"a\")\n",
    "        userInput = input(\"Enter Stock Symbol or QUIT to exit: \").upper()\n",
    "        if userInput != \"QUIT\":\n",
    "            stockData = getStockData(userInput)\n",
    "            print(stockData)\n",
    "            print(\"Stock Quotes retrived successfully\")\n",
    "            theData = json.loads(stockData)\n",
    "            resultsData = '\\nThe current price of '+ userInput + ' is: ' + (theData[\"Global Quote\"][\"05. price\"])\n",
    "            print(resultsData)\n",
    "            file.write(resultsData)\n",
    "            file.close()\n",
    "        else:\n",
    "            print(\"End of Program\")\n",
    "            f = open(\"stockFile.txt\", \"r\")\n",
    "            print(f.read())\n",
    "            break\n",
    "            \n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
