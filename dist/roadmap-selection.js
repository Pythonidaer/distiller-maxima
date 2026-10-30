const dataAndAITopics = ["Data engineering and applied Python", "Machine learning and AI foundations", "AI Engineering", "AI-assisted development", "LLM applications and retrieval", "Agents, MCP and automation"];
const isDataAndAI = document.body.dataset.roadmap === 'data-ai';
const selectedReadingGroups = readingGroups.filter(group => dataAndAITopics.includes(group.title) === isDataAndAI);
