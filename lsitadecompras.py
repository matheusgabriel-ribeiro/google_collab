{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOia/DpzHVMR8tbzrmkHib8",
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
        "<a href=\"https://colab.research.google.com/github/matheusgabriel-ribeiro/google_collab/blob/main/lsitadecompras.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "d_vEcLXsDeJV"
      },
      "outputs": [],
      "source": [
        "compras = []\n",
        "\n",
        "def adicionar(adc):\n",
        "    compras.append(adc)\n",
        "    print(f\"'{adc}' foi adicionado à lista!\")\n",
        "\n",
        "def remover(rmv):\n",
        "    try:\n",
        "        compras.remove(rmv)\n",
        "        print(f\"'{rmv}' foi removido da lista!\")\n",
        "    except ValueError:\n",
        "        print(f\"ERRO: '{rmv}' não está na lista.\")\n",
        "\n",
        "def listar():\n",
        "    try:\n",
        "        if not compras:\n",
        "            print(\"A lista de compras está vazia.\")\n",
        "        else:\n",
        "            print(\"Lista de compras:\", compras)\n",
        "    except Exception as erro:\n",
        "        print(f\"ERRO ao listar: {erro}\")\n",
        "\n",
        "def clear():\n",
        "    compras.clear()\n",
        "    print(\"Lista de compras limpa.\")\n",
        "\n",
        "def main():\n",
        "    while True:\n",
        "        print(\"\"\"\n",
        "        ====== MENU ======\n",
        "        1. Adicionar itens\n",
        "        2. Remover itens\n",
        "        3. Ver lista\n",
        "        4. Limpar lista\n",
        "        5. Sair\n",
        "        \"\"\")\n",
        "\n",
        "        try:\n",
        "            opc = int(input(\"Digite sua opção: \"))\n",
        "\n",
        "            if opc < 1 or opc > 5:\n",
        "                print(\"Digite um valor válido (1 a 5).\")\n",
        "\n",
        "            elif opc == 1:\n",
        "                adc = input(\"Digite o que você quer adicionar: \").strip()\n",
        "                if adc:\n",
        "                    adicionar(adc)\n",
        "                else:\n",
        "                    print(\"ERRO: O item não pode estar vazio.\")\n",
        "\n",
        "            elif opc == 2:\n",
        "                rmv = input(\"Digite o que você quer remover: \").strip()\n",
        "                remover(rmv)\n",
        "\n",
        "            elif opc == 3:\n",
        "                listar()\n",
        "\n",
        "            elif opc == 4:\n",
        "                clear()\n",
        "\n",
        "            elif opc == 5:\n",
        "                exit(programa encerrado)\n",
        "\n",
        "        except ValueError:\n",
        "            print(\"ERRO: Digite apenas números para escolher uma opção.\")\n",
        "\n",
        "        except Exception as erro:\n",
        "            print(f\"ERRO inesperado: {erro}\")\n",
        "\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    main()"
      ]
    }
  ]
}