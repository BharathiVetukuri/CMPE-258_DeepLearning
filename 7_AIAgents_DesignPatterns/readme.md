# 🤖 Assignment 7: Effective AI Agent Design Patterns using LangGraph and CrewAI

This project demonstrates several foundational agent design patterns described in **"Building Effective Agents"**, implemented using two frameworks: [LangGraph](https://langchain-ai.github.io/langgraph/tutorials/workflows) and [CrewAI](https://github.com/joaomdmoura/crewAI). The goal is to explore and compare these frameworks while building intelligent multi-agent systems.

---

## 🧠 Assignment Objective

- Implement AI Agent Patterns covered in:
  - [🔗 YouTube: Building Effective Agents](https://www.youtube.com/watch?v=aHCDrAbH_go&t=5s)
  - [🔗 LangGraph Docs](https://langchain-ai.github.io/langgraph/tutorials/workflows)
  - [🔗 DeepLearning.AI Course](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/)

- Demonstrated the following patterns:
  - ✅ ReAct (Reasoning + Acting)
  - ✅ Plan-and-Execute
  - ✅ Tool-Use (Agent with Tools)
  - ✅ Multi-Agent Collaboration / Delegation
  - ✅ Memory-Augmented Agent

---

## 🚀 Notebooks Included

### 📘 1. `LangGraph_Agent_Patterns.ipynb`
- Implements all agent patterns using LangGraph.
- Logs agent traces to [LangSmith](https://smith.langchain.com) for analysis.
- Includes inline screenshots of trace outputs.

### 📗 2. `CrewAI_Agent_Patterns.ipynb`
- Implements same patterns using [CrewAI](https://github.com/joaomdmoura/crewAI).
- Demonstrates task planning, multi-agent delegation, and dynamic tool usage.

---

## 🖼 LangSmith Trace Screenshots

### 🔧 ReAct Agent Trace  
![ReAct Trace](./assets/react_trace.png)

### 🧠 Memory-Augmented Agent Trace  
![Memory Agent Trace](./assets/memory_trace.png)

---

## 🎥 Walkthrough Video

📺 **Watch here**: [Walkthrough Video (YouTube/Drive)](https://your-video-link-here.com)

Covers:
- Agent architecture in both frameworks
- Differences in APIs and behavior
- Output analysis and debug traces

---

## 🛠 Technologies Used

- `langgraph`
- `crewai`
- `langchain`
- `openai`
- `langsmith`
- `duckduckgo-search`, `wikipedia`

---

## 📌 Instructions

1. Clone this repo
2. Run the Colab notebooks (`.ipynb`) in Google Colab
3. Add your OpenAI & LangSmith API keys when prompted
4. View LangSmith traces after agent execution
5. Check the output visualizations and screenshots

