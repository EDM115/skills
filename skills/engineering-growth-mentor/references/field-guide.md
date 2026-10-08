# Field guide: findings and reusable prompts

Source: Elise Baturone, [*Forever Junior: The Skills AI Can't Develop For You*](https://tech.criteo.com/blog/human-skills-ai-cant-develop-junior-engineers/), Criteo Tech Community, October 7, 2026.

The article is an engineer's first-person account of experimenting with agent instructions while developing as a junior engineer. Its results are anecdotal, not a controlled measurement of productivity or skill acquisition. The author describes a promotion nomination, not proof that these prompts cause promotion.

## Extracted ideas

| Human capacity | Article's practical observation | Agent behavior this skill implements |
| --- | --- | --- |
| Curiosity and intellectual ownership | Asking why a plan works develops the ability to defend decisions and find suspicious reasoning. | Request one grounded explanation, counterfactual, or failure trace at useful points. |
| Reviewer judgment | Comments from experienced colleagues reveal codebase-specific expectations. | Find nearby implementations and real review evidence; challenge unjustified departures. |
| Autonomous execution | Rare, purposeful hand-written changes exercise design and algorithmic intuition. | Reserve safe, scoped tasks for the engineer and give feedback only after their attempt. |
| Appropriate delegation | Deep familiarity with a codebase helps determine whether an IDE, human, or agent is most efficient. | Match the tool to task complexity and keep work proportionate. |
| Collaboration | Team expertise cannot be recreated by an AI prompt; asking another engineer is an engineering skill. | Flag human-owned decisions and help refine the engineer's own questions. |

## Three prompt families shown in the article (reconstructed)

The article includes example fragments of the author's own `skill.md`. The following are **new formulations of those patterns**, not verbatim excerpts.

### A. Comprehension check after implementation

```text
After significant work, choose one meaningful concept from the actual change.
Ask me to explain how it works, defend a decision, or diagnose a plausible failure.
Vary the question and focus on understanding rather than recall.
Give specific corrections if my explanation misses something.
Apply the same guardrails to any delegated agent.
```

### B. Find a codebase analogue before designing

```text
Before introducing an important feature, look for a similar existing feature.
Show the closest examples and what can be reused.
Identify deviations, ask for a choice only if the alternatives matter, and
preserve the reference when planning and reviewing the implementation.
If no example fits, state that the design is new rather than pretending otherwise.
```

### C. Separate investigation from mutations

```text
You may inspect and reason about the repository without authorization.
Before any file edits, dependency changes, migrations, commits, deployments,
or commands with side effects, present a concrete change plan and obtain
explicit approval. Scope approvals to the plan, including the verification
commands that may write artifacts. Delegated agents follow the same boundary.
```

## Additional reusable user prompts

**Defend the design**

> I want to understand this implementation well enough to maintain it without you. Explain the strongest argument for the chosen approach, the strongest alternative, and one situation that would make us reconsider.

**Pre-PR review**

> Compare my diff with the closest existing pattern and the team's documented conventions. Give a prioritized review: blockers first, then risks, then optional improvements. Cite evidence for every claimed convention.

**Find the edge case**

> Don't rewrite the code yet. Give me an input or failure scenario that could invalidate our approach, and let me predict the behavior before showing the answer.

**Human-only mini-challenge**

> Select one low-risk follow-up change. I will write the code. Provide success criteria and how to test it, but no patch or solution unless I request one.

**Senior handoff**

> I will write the message to the component owner. Check whether my summary identifies the decision, the constraints, what I tried, and the precise question. Correct my misunderstanding without inventing their decision.

**Review comment extraction**

> I am providing historical review comments. Group recurring concerns, identify which seem team-specific, and turn them into a five-item checklist I can use on my next PR. Quote or cite the examples I actually supplied.

## Practical cautions

- A model can generate convincing explanations for flawed designs; verify using code, tests, and trusted documentation.
- Questions should follow useful milestones, not every tiny edit; excessive quizzes interrupt work without improving learning.
- A similar file is evidence of a local pattern, not proof that its architecture is correct.
- Protect time for human mentors and exercise judgment yourself. Agent prompts cannot replace direct experience or team feedback.
- Continue normal implementation after explicit approval; avoid turning an educational guardrail into constant repetitive permission requests.
