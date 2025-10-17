# KBS Checker
This is a prototype that uses LangChain and Ollama to scan apprentice portfolios for evidence of required skills, knowledge, and behaviours (KSBs).

To run this you will need to install Ollama (https://ollama.com/). The prototype uses OpenAI's open-weight model gpt-oss (https://ollama.com/library/gpt-oss) but this can easily be changed.

**Important**: The choice to use a locally running model was deliberate. While this may limit the size of model that can be used, it avoids sharing sensitive content (i.e. the apprentice's own work and information about their employer) with third parties.
