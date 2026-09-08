---
name: discriminating-testing
description: Design high-information tests that distinguish correct behavior from plausible wrong implementations. Use when implementing, modifying, debugging or reviewing nontrivial code; when writing unit, integration, property-based, fuzz, differential, snapshot, metamorphic or formal checks; or when a bug fix depends on subtle semantics, boundaries, ordering, state, encoding, arithmetic or protocol behavior.
metadata:
  author: EDM115
  source: https://danluu.com/agentic-testing/
---

# Discriminating Testing
Optimize for tests that catch plausible bugs, not for test count, framework usage or ritual compliance.

## Core rule
For every important test, be able to answer:
1. What plausible mistake or alternative interpretation does this target?
2. Would this exact input make the correct and wrong implementations behave differently?
3. Is the expected result derived independently of the implementation under test?

If not, redesign or remove the test.

## Workflow
### 1. Map the risk surface
Before or while implementing, identify the few areas most likely to hide subtle bugs. Focus on semantics such as:
- ordering, association, reversal, indexing and mapping
- boundaries and both sides of a boundary
- state transitions and interactions between states
- length, offset, overflow, truncation, precedence and bit/byte arithmetic
- parsing, serialization, encodings, framing and partial inputs
- duplicate, empty, singleton, maximal and non-uniform cases
- concurrency, retries, cancellation, caching and stale state
- places where the specification admits multiple plausible readings

Do not spend equal effort everywhere. Concentrate tests on code whose wrong implementation could still look reasonable.

### 2. Invent the wrong version first
For each high-risk area, state one or more plausible bugs or alternate interpretations. Then construct the smallest check that makes them disagree with the intended behavior. Prefer inputs that destroy accidental symmetry:
- different values instead of repeated values
- non-palindromic sequences when direction matters
- unequal lengths when association matters
- values immediately below, at and above boundaries
- state sequences where reordering changes the result
- data that exercises distinct branches rather than one repeated path

Avoid easy examples that allow multiple implementations to pass.

### 3. Build an independent oracle
Derive expected behavior from the specification, mathematics, a trusted external implementation, a separately reasoned model or a hand-worked example. Do not:
- copy the current implementation's output into the test
- call production helpers to compute the expected value when those helpers share the logic being tested
- duplicate the same algorithm twice and call it differential testing
- weaken an assertion merely to make the current code pass

If an expected result is hard to derive, that is a signal to reason more carefully about the contract, not to assert less.

### 4. Use testing techniques for their leverage, not their names
Choose a technique only when it improves discrimination against a concrete failure mode.
- **Property/randomized testing:** generate structured, mostly valid inputs that reach interesting states. Bias toward boundaries, rare combinations and state transitions. Assert semantic properties, not only "does not crash". Use shrinking when available.
- **Fuzzing:** avoid spending the budget on random bytes that all hit the same rejection path. Seed or construct valid structures, then mutate meaningful fields.
- **Differential testing:** compare against a genuinely independent oracle or implementation. Shared logic, helpers, copied structure or the same interpretation twice are not independent.
- **Metamorphic testing:** choose transformations related to risky semantics, not merely properties that are easy to state.
- **Snapshot/golden testing:** ensure the golden value comes from an independently trusted source; do not bless unexplained current output.
- **Formal methods/model checking:** model or prove a property connected to the actual bug-prone production semantics. Do not spend effort proving easy, vacuous or irrelevant facts.

Do not force TDD or any framework-specific ceremony. Tests may be designed before or after inspecting implementation details; for complex machinery, white-box knowledge can reveal the cases worth distinguishing.

### 5. Audit the tests, not just the code
After implementation or a bug fix, inspect the risky areas again and ask:
- What plausible one-line bug would survive these tests?
- Which assumption did the implementation make that no test challenges?
- Are any inputs symmetric, identical, trivial or otherwise unable to expose ordering/association mistakes?
- Do randomized tests actually reach distinct valid states and code paths?
- Could the oracle contain the same misunderstanding as the implementation?

Add or replace tests based on these answers. Do not add tests merely to increase coverage or count.

## Anti-patterns
Avoid these common agent failure modes:
- many tiny tests with little discriminatory power
- repeated test-code-test loops that merely overfit implementation behavior
- asserting only success, non-panic or non-crash for complex semantics
- random inputs dominated by invalid/rejection cases
- identical values in multi-stream, multi-field ordering or mapping tests
- round-trip tests only for easy paths while risky paths remain unchecked
- proving/modeling convenient properties instead of properties tied to likely bugs
- treating the use of a named library or technique as evidence of test quality

## Completion criterion
Before declaring correctness, ensure each high-risk semantic area has at least one test or check that would fail for a specific plausible wrong implementation, with an oracle that does not simply reuse that implementation's reasoning.  
Prefer a small set of such tests over a large suite of low-information checks.
