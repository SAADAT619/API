{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled25.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMcaQy89ht4oD8g2JoqP6fV",
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
        "<a href=\"https://colab.research.google.com/github/SAADAT619/API/blob/master/login_form_using_python.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SKoAZc2XTlU6",
        "outputId": "9f74414b-a50b-43de-80d3-1debcb9545c0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Create your account\n",
            "Enter username: Samin\n",
            "Enter password: eee\n",
            "Your account has been created\n",
            "Login now\n",
            "Enter username: Samii\n",
            "Enter password: eee\n",
            "credential error!!\n"
          ]
        }
      ],
      "source": [
        "print(\"Create your account\")\n",
        "username = input(\"Enter username: \")\n",
        "password = input(\"Enter password: \")\n",
        "print(\"Your account has been created\")\n",
        "\n",
        "print(\"Login now\")\n",
        "username2 = input(\"Enter username: \")\n",
        "password2 = input(\"Enter password: \")\n",
        "\n",
        "if username == username2 and password == password2:\n",
        "  print(\"Login successfully\")\n",
        "else:\n",
        "  print(\"credential error!!\")"
      ]
    }
  ]
}