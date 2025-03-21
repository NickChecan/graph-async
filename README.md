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

Controlling different execution paths in a graph.

```mermaid
%%{init: {'flowchart': {'curve': 'linear'}}}%%
graph TD;
	__start__([<p>__start__</p>]):::first
	a(a)
	b(b)
	b2(b2)
	c(c)
	d(d)
	__end__([<p>__end__</p>]):::last
	__start__ --> a;
	a --> b;
	a --> c;
	b --> b2;
	b2 --> d;
	c --> d;
	d --> __end__;
	classDef default fill:#f2f0ff,line-height:1.2
	classDef first fill-opacity:0
	classDef last fill:#bfb6fc
```

Conditional Branching with async execution:

```mermaid
%%{init: {'flowchart': {'curve': 'linear'}}}%%
graph TD;
	__start__([<p>__start__</p>]):::first
	a(a)
	b(b)
	c(c)
	d(d)
	e(e)
	__end__([<p>__end__</p>]):::last
	__start__ --> a;
	b --> e;
	c --> e;
	d --> e;
	e --> __end__;
	a -.-> b;
	a -.-> c;
	a -.-> d;
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

### Drawbacks

- State Conflicts: The nodes in the graph may share and change the same state, which can lead to conflicts.
- Debugging asynchronous code can be difficult.

The best practice is to isolate state updates. Each node should write to a different attribute of the state object to conserve data integrity and prevents overwriting values.
### References

[How to create branches for parallel node execution](https://langchain-ai.github.io/langgraph/how-tos/branching/)