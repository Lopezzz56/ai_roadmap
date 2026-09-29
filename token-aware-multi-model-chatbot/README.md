# Token-Aware Multi-Model Chatbot

## What this project is

This is a small command-line chatbot built to explore how language models work in practice. It can switch between Google Gemini and OpenRouter, stream replies, count the tokens in a prompt, and choose a model based on the prompt's token count.

## What I learned

Building this project helped me connect the ideas behind language models with the code that calls them:

- **How tokenization works:** Models process text as tokens rather than whole words. A familiar word may be one token or several; unusual spellings, punctuation, symbols such as `!@#`, and unfamiliar character sequences can be split into smaller pieces and use more tokens than expected. Token counts depend on the tokenizer.
- **How token counts affect cost:** API usage is commonly priced by the number of input and output tokens, with rates varying by model. Counting tokens helps estimate request size and manage a budget, although the `tiktoken` count in this project is an estimate and may differ from a provider's tokenizer.
- **Ways to use fewer tokens:** Keep prompts focused, remove repeated context, and include only the information needed for the task. For longer material, splitting it into useful chunks can help fit model context limits, but the right approach depends on the task.
- **Context windows and context engineering:** A model can only work with a limited amount of context at once. What goes into that context—and how it is organized—can affect the quality and relevance of the answer.
- **Sampling and output variation:** I explored temperature, top-k, and top-p. These settings influence how a model selects its next token. Higher temperature generally makes responses more varied; lower temperature makes them more predictable, but does not guarantee correctness or prevent hallucinations. Top-k limits choices to a fixed number of likely tokens, while top-p selects from a probability-based set.
- **Choosing models for different prompts:** The chatbot routes shorter and longer prompts to different configured models. This gave me a first look at balancing response needs, token budgets, and model choice.
- **Python and API integration:** I practiced using `try`/`except` for API errors, loading keys from environment variables, counting tokens with `tiktoken`, and calling Gemini and OpenRouter using their Python SDK interfaces. I also learned how streamed responses arrive in chunks and can be printed as they come in.

This README is my learning record for the project. I’ll add to it as I keep experimenting and understand these topics better.
