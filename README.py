#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `flatpak` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `flatpak` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings for configuring/installing/using the `flatpak` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `flatpak`
# 
# `Flatpak` é uma tecnologia de distribuição de aplicativos que visa fornecer uma maneira universal de empacotar, distribuir e executar aplicativos em diferentes distribuições `Linux`. Ele utiliza contêineres para isolar aplicativos de suas dependências do sistema operacional, permitindo que aplicativos sejam executados de forma mais segura e consistente em diferentes ambientes `Linux`. `Flatpak` facilita a instalação de aplicativos com suas dependências, oferece atualizações independentes do sistema e promove a distribuição de _software_ de forma mais eficiente e controlada.
# 

# ## 1. Como configurar/instalar/usar o `flatpak` no `Linux Ubuntu` [1][3]
# 
# Para configurar/instalar/usar o `flatpak` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.2 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.3 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
#     2.4 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.5 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update -y`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
# 
#     2.6 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.7 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

# 3. **Instalação do `Flatpak`**: Após atualizar o índice de pacotes, você pode instalar o `flatpak` usando o gerenciador de pacotes `apt`: `sudo apt install flatpak -y`
# 
# 4. **Adicionar o `Flathub` (opcional)**: O `Flathub` é um repositório de aplicativos `Flatpak` que contém uma ampla variedade de softwares. Adicionar o `Flathub` permite que você instale aplicativos adicionais via `Flatpak`: `flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo`
# 
# 5. **Verificação da Instalação**: Para verificar se o `flatpak` foi instalado corretamente, você pode usar o comando: `flatpak --version`
# 
#     Isso deve exibir a versão do `flatpak` instalada, confirmando que o processo de instalação foi concluído com sucesso.
# 
# Com esses passos, você terá instalado o `flatpak` no seu sistema Ubuntu e estará pronto para começar a instalar aplicativos utilizando esse formato de pacote.

# ### 1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `flatpak` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt clean                               
#     sudo apt autoclean
#     sudo apt autoremove
#     sudo apt update -y
#     sudo apt autoremove
#     sudo apt autoclean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo apt install flatpak -y
#     flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
#     flatpak --version
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Instalar flatpak no Ubuntu.*** Disponível em: <https://chatgpt.com/c/0f5f9689-6636-4dff-8a4e-fa3a8cf11b15> (texto adaptado). Acessado em: 18/03/2023 17:11.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 18/03/2024 17:10.
# 
