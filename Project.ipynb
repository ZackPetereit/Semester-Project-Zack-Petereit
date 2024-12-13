{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "id": "EogAngerk1sK"
      },
      "outputs": [],
      "source": [
        "import requests\n",
        "import json\n",
        "import prettytable\n",
        "import datetime\n",
        "\n",
        "\n",
        "headers = {'Content-type': 'application/json'}\n",
        "current_year = datetime.datetime.now().year #get current year\n",
        "\n",
        "#retreieve data between 2023 and current year\n",
        "data = json.dumps({\"seriesid\": ['LNS14000000','CES0000000001', 'CES0500000002', 'CES0500000003', 'PRS85006092'],\"startyear\":\"2023\", \"endyear\":str(current_year)})\n",
        "p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)\n",
        "json_data = json.loads(p.text)\n",
        "for series in json_data['Results']['series']:\n",
        "    x=prettytable.PrettyTable([\"series id\",\"year\",\"period\",\"value\",\"footnotes\"])\n",
        "    seriesId = series['seriesID']\n",
        "    for item in series['data']:\n",
        "        year = item['year']\n",
        "        period = item['period']\n",
        "        value = item['value']\n",
        "        footnotes=\"\"\n",
        "        for footnote in item['footnotes']:\n",
        "            if footnote:\n",
        "                footnotes = footnotes + footnote['text'] + ','\n",
        "        if 'M01' <= period <= 'M12':\n",
        "            x.add_row([seriesId,year,period,value,footnotes[0:-1]])\n",
        "    output = open(seriesId + '.txt','w')\n",
        "    output.write (x.get_string())\n",
        "    output.close()\n",
        "\n",
        "\n",
        "\n"
      ]
    }
  ]
}