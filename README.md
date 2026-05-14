# Enterprise RAG System | 企业级 RAG 系统

An enterprise-style Retrieval-Augmented Generation (RAG) platform built with FastAPI, ChromaDB, LangChain, and DeepSeek API.
基于 FastAPI、ChromaDB、LangChain 和 DeepSeek API 构建的企业级检索增强生成（RAG）平台。

Supports multi-source document ingestion, semantic retrieval, multi-turn conversation memory, metadata tracking, and persistent vector storage.
支持多源文档导入、语义检索、多轮对话记忆、元数据追踪，以及持久化向量存储。

## Features | 功能特性

- Multi-source document ingestion (PDF / TXT / URL) | 多源文档导入
- Semantic retrieval with ChromaDB | 基于 ChromaDB 的语义检索
- Persistent vector database | 持久化向量数据库
- Multi-turn RAG conversation memory | 多轮 RAG 对话记忆
- Metadata tracking | 元数据追踪
- User isolation support | 用户隔离支持
- PromptTemplate-based prompt engineering | 基于 PromptTemplate 的提示工程
- Enterprise-style modular architecture | 企业级模块化架构
- Logging system for retrieval debugging | 检索调试日志系统
- ## Tech Stack|技术栈
- FastAPI
- ChromaDB
- LangChain
- DeepSeek API
- Python
- RecursiveCharacterTextSplitter
- #项目结构
- app/
├── core/
├── rag/
├── routes/
└── main.py
#RAG 架构图
<img width="1488" height="584" alt="2aadafb8-7350-4252-b8f9-88cb50e5c52c" src="https://github.com/user-attachments/assets/3ce4f159-028a-41b0-b989-b858006ba862" />

#安装说明
pip install -r requirements.txt
uvicorn app.main:app --reload
