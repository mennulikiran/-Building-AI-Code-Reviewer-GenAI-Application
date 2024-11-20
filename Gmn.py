{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPuO2V1m+ohOvvuHEIE2SVT",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/mennulikiran/-Building-AI-Code-Reviewer-GenAI-Application/blob/main/Gmn.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Ud6AKOoA0wRH"
      },
      "outputs": [],
      "source": [
        "from dotenv import load_dotenv\n",
        "load_dotenv()\n",
        "\n",
        "import os\n",
        "import google.generativeai as genai\n",
        "from langchain_core.prompts import ChatPromptTemplate # L1\n",
        "from langchain_google_genai import ChatGoogleGenerativeAI # L2\n",
        "from langchain_core.output_parsers import StrOutputParser # L3\n",
        "\n",
        "import streamlit as st\n",
        "\n",
        "chat_model = ChatGoogleGenerativeAI(google_api_key=os.getenv(\"GOOGLE_API_KEY\"), model=\"gemini-1.5-flash\")\n",
        "\n",
        "prompt_template = ChatPromptTemplate.from_messages([\n",
        "    (\"system\", \"You are a helpful AI Tutor with expertise in Data Science and Artificial Intelligence. \"),\n",
        "    (\"human\", \"What is {topic}?\"),\n",
        "])\n",
        "\n",
        "output_parser = StrOutputParser()\n",
        "\n",
        "st.title(\"Code Repository Assistant\")\n",
        "\n",
        "name_of_algo = st.selectbox(\n",
        "    'Choose an Algorithm',\n",
        "    ('Linear Regression', 'SVC', 'Decision trees', 'XG-Boost')\n",
        ")\n",
        "\n",
        "button = st.button(\"See the implementation\")\n",
        "\n",
        "if button:\n",
        "    try:\n",
        "        chain = prompt_template | chat_model | output_parser\n",
        "        input_data = {\"topic\": name_of_algo}\n",
        "        result = chain.invoke(input_data)\n",
        "        st.write(result)\n",
        "    except Exception as e:\n",
        "        st.error(f\"Error: {e}\")"
      ]
    }
  ]
}