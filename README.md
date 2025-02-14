# graph-async

This project covers the asynchronous execution of nodes in a graph.

```mermaid
%%{init: {'flowchart': {'curve': 'linear'}}}%%
graph TD;
	__start__([<p>__start__</p>]):::first
	a(a)
	b(b)
	c(c)
	d(d)
	__end__([<p>__end__</p>]):::last
	__start__ --> a;
	a --> b;
	a --> c;
	b --> d;
	c --> d;
	d --> __end__;
	classDef default fill:#f2f0ff,line-height:1.2
	classDef first fill-opacity:0
	classDef last fill:#bfb6fc
```

### Utilities

Poetry command to install project dependencies:
```sh
poetry add python-dotenv langgraph grandalf
```

Environment variables:
```
LANGCHAIN_API_KEY=<LangSmith API key>
LANGCHAIN_TRACING=true
LANGCHAIN_PROJECT=AsyncProject
```