{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPznj3pjguyEZjVFAzURZpT",
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
        "<a href=\"https://colab.research.google.com/github/mennulikiran/-Building-AI-Code-Reviewer-GenAI-Application/blob/main/ai.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
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
        "import streamlit as st\n",
        "import google.generativeai as genai\n",
        "\n",
        "genai.configure(api_key=\"AIzaSyDMLTyTHm434cCiU6wqisAbpNZ2jiz4kd4\")\n",
        "\n",
        "\n",
        "llm = genai.GenerativeModel(\"models/gemini-1.5-flash\")\n",
        "\n",
        "if \"history\" not in st.session_state:\n",
        "\n",
        "    st.session_state.history = []\n",
        "def format_history_for_model(history):\n",
        "    \"\"\"Format history entries to match the model's expected structure.\"\"\"\n",
        "\n",
        "    formatted_history = []\n",
        "\n",
        "    for entry in history:\n",
        "\n",
        "        formatted_history.append({\n",
        "\n",
        "            \"role\": entry[\"role\"],\n",
        "\n",
        "            \"parts\": [{\"text\": entry[\"content\"]}]\n",
        "\n",
        "        })\n",
        "\n",
        "    return formatted_history\n",
        "\n",
        "\n",
        "\n",
        "def get_response(message):\n",
        "\n",
        "    # Format history for model and initialize chatbot\n",
        "\n",
        "    formatted_history = format_history_for_model(st.session_state.history)\n",
        "\n",
        "    chatbot = llm.start_chat(history=formatted_history)\n",
        "\n",
        "    response = chatbot.send_message(message)\n",
        "\n",
        "\n",
        "\n",
        "    # Append user message and AI response to history\n",
        "\n",
        "    st.session_state.history.append({\"role\": \"user\", \"content\": message})\n",
        "\n",
        "    st.session_state.history.append({\"role\": \"model\", \"content\": response.text})\n",
        "\n",
        "    return response.text\n",
        "st.title(\"Welcome to the Chatbot\")\n",
        "\n",
        "\n",
        "#st.chat_message(\"ai\").write(entry[\"content\"])\n",
        "\n",
        "st.chat_message(\"ai\").write(\"Hi there! I am a helpful AI Assistant. How can I help you today?\")\n",
        "\n",
        "# Display the previous chat history\n",
        "\n",
        "for entry in st.session_state.history:\n",
        "\n",
        "    if entry[\"role\"] == \"user\":\n",
        "\n",
        "        st.chat_message(\"human\").write(entry[\"content\"])\n",
        "\n",
        "    else:\n",
        "\n",
        "        st.chat_message(\"ai\").write(entry[\"content\"])\n",
        "\n",
        "human_prompt = st.chat_input(\"Say Something...\")\n",
        "\n",
        "if human_prompt:\n",
        "    st.chat_message(\"human\").write(human_prompt)\n",
        "    response = get_response(human_prompt)\n",
        "    st.chat_message(\"ai\").write(response)\n"
      ]
    }
  ]
}
