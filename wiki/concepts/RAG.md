# RAG

**定义**: Retrieval-Augmented Generation，检索增强生成，一种让大模型在回答时动态检索外部文档的技术  
**相关领域**: 人工智能、NLP、知识管理  
**首次提及**: [[2025-04-13_karpathy_llm_wiki]]  
**标签**: #ai #llm #retrieval #nlp

## 详细解释

RAG 的工作流程：
1. 将原始文档切分成小块（chunks）
2. 计算每个 chunk 的向量嵌入（embedding）
3. 用户提问时，检索与问题相关的 chunks
4. 将检索结果作为上下文，让 LLM 生成回答

## 局限性

- **没有知识积累** — 每次回答都是从零开始
- **片段化问题** — 难以跨越多篇文档进行深度综合
- **上下文窗口限制** — 受模型上下文长度约束
- **维护成本** — 难以发现和处理文档间的矛盾

## 与其他概念的关系
- vs [[LLM Wiki]]: RAG 是动态检索，LLM Wiki 是静态编译
- + [[Vector Database]]: RAG 通常依赖向量数据库进行检索

## 应用实例
- NotebookLM
- ChatGPT 文件上传功能
- 企业内部文档问答系统

## 所有提及此概念的来源
- [[2025-04-13_karpathy_llm_wiki]]
