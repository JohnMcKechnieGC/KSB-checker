template = """
An apprentice has submitted the following text as part of their portfolio. Note that
images were included in the portfolio, but they are not included in the text below.
Here is the portfolio text:

{portfolio_text}

Your task:
Please now determine if any of the following Knowledge, Skills, and Behaviours (KSBs) have
been met, including whether the apprentice has fulfulled the pass or distinction criteria.
I would like this in the format of a table showing, for each KSB:
- highlights of any evidence from the portfolio,
- whether the pass criteria have been met,
- whether the distinction criteria have been met (if applicable), and
- suggestions for how the evidence could be strengthend.

Please use gender neutral pronouns like 'they' and 'them' if referring to the apprentice. Some
external examiners are quite hard to please. So please only indicate that criteria have been
met when there's little doubt that it's true.

KSBs:
{ksbs}
"""