# 🚀 API de CEP

Esta API foi desenvolvida em **Python** utilizando o framework **FastAPI**. Ela foi projetada para ser extremamente rápida e eficiente, focando na recuperação de dados geográficos brasileiros (Endereços, UFs e Municípios) de forma escalável.

## ⚡ O que significa ser uma API Assíncrona?

A principal característica desta API é o uso de `async/await`. No modelo tradicional (síncrono), cada requisição "tranca" o processamento enquanto espera uma resposta do banco de dados ou de um serviço externo.

**No modelo Assíncrono:**

* **Non-blocking I/O:** Enquanto a API espera os dados do CEP chegarem, o processador fica livre para atender outras chamadas simultâneas.
* **Escalabilidade:** Permite que um único servidor lide com milhares de conexões ao mesmo tempo com baixo consumo de memória.
* **Concorrência:** Ideal para as buscas em massa por UF ou Município que você implementou, onde múltiplos registros são processados sem gargalos de espera.

---

## 🛠️ Funcionalidades Principal

A API oferece três endpoints principais para consulta, conforme visualizado na documentação Swagger:

### 1. Busca por CEP Individual

Retorna os detalhes completos de um endereço específico.

* **Endpoint:** `GET /{numero}`
* **Descrição:** Informe o CEP (apenas números) para obter logradouro, bairro, cidade e estado.

### 2. Busca Geral por UF

Ideal para levantamentos regionais ou automação de bases de dados.

* **Endpoint:** `GET /uf/{sigla_uf}`
* **Descrição:** Retorna uma lista de endereços/dados vinculados à unidade federativa informada (ex: `SP`, `GO`, `RJ`).

### 3. Busca por ID Município

Integração específica para sistemas que utilizam codificação municipal.

* **Endpoint:** `GET /municipio/{id_municipio}`
* **Descrição:** Filtra todos os registros pertencentes a um ID de município específico.

---

## 📦 Tecnologias Utilizadas

* **Python 3.11**
* **FastAPI:** Framework web moderno e de alta performance.
* **Uvicorn:** Servidor ASGI para suporte assíncrono.

**Link:** https://cep-pearl-five.vercel.app/docs#/

<img width="684" height="398" alt="image" src="https://github.com/user-attachments/assets/91b6097f-aa3e-42a7-bc0c-ed81d9cd6f8a" />
