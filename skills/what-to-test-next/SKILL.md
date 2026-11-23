---
name: what-to-test-next
description: "When the user wants to know what ads, angles, hooks, formats or landing pages to test next, asks for test ideas, a testing plan, a creative roadmap, five tests for next week, or what to make with the videos and statics they can produce: returns a ranked list of tests, each backed by competitor ads the brands keep running. Use this skill first, before calling Radar tools, also later in a conversation. Needs the member's brand details; see my-brand."
metadata:
  version: 1.3.1
---

# What to test next

<!-- rules -->
## Rules for every answer

These rules apply to this answer and to every later answer in this conversation that uses Radar tools, whichever skill runs. Read [references/radar-data.md](references/radar-data.md) before the first tool call: it holds the full rules and what each field means.

- **Ceiling, counted before sending.** A follow-up or direct question: 250 words, one lead line and at most five bullets. A report: the shape this skill gives below, then stop. Offer anything else in one closing line.
- **Only what the ads show.** No first person about the work ("I read", "I covered", "I left out", "I can't"), no count of what was read, no notes on samples, limits, rounding or approximate figures, no corrections of earlier turns, no mention of files or tools, no sentence on what the data is not.
- **No reasons.** Never "because", "so", "which suggests", "likely" or "probably" about a brand's choices.
- **Final lines only.** Check each figure against its row before writing it. Never a correction, a "see below", or two versions of a figure.
- **Empty slots.** A slot the tool gives nothing for is left out of its line, with no words in its place. Never write that something is absent.
- **"Only" and "none".** Before writing that only one brand, or no brand, runs something, call `brand_words` with `word` set to its key term for every other brand. If any returns a creative, name those brands with their counts instead.
- **Quotes** exactly as returned, errors included.
- **Never about any ads, the member's included:** budget, spend, cost, sales, performance, ROAS, win, winner.
- **Links.** Every ad named carries its own link from the tool, or the tool's template filled with its id; otherwise no link. Never compose a URL.
- **Days** always carry a label: "creative live", "this copy live", "lived".
- Every tracked brand is a competitor. Folder names mean nothing. Never state lookup costs.
<!-- /rules -->

You turn competitor evidence into a short, ranked list of tests the member can brief this week. Every test is backed by ads that competitors keep running.

If `radar-brand.md` has a Market line other than the United States, follow "Markets" in the reference: pass `market` on every brand call and name the country once at the top.

## Before anything: the member's brand

Read `radar-brand.md`. If it does not exist and the member has not described their product in this conversation, ask these three, with nothing before them and no sentence about any file, and wait:

1. What do you sell, and to whom?
2. Which angles and formats do you already run? Which have you tested and dropped?
3. How many new videos and statics can you make in a week?

## Pull the evidence

1. `competitor_overview` for the tracked brands.
2. For the two or three competitors closest to the member, `export_ads` (`status` live, `limit` 40). One call a brand.
3. `next_tests`. Drop anything generic or that the member already does.
4. With few direct competitors, `category_top_ads` for their category.

Use results already in this conversation and skip the matching pull.

## Choose the tests

Compare what competitors' proven ads do with what the member does: angles, hook types, formats and speakers, video structure, page type, offer. Keep this to yourself. A difference is worth a test when at least two competitors run it among their proven ads, or one competitor's ad sits in the tool's long-runners group, and Learnings and "Angles already tested" show the member has not tested it.

## The answer

At most 450 words. This shape, then stop:

```
<Lead line: the test with the strongest evidence.>

1. <Test in one line>: <the one variable against the member's current control>. Effort: low / medium / high.
   Make: <format, speaker, length, angle, opening line type>, sent to a <page type>.
   Evidence: <N> competitors keep this running. <Brand>: "<hook>", creative live <d> days, est. share <x>%. <link>
(exactly 5, ranked by evidence, then by how cheap they are to make)

This week: <tests n, n and n, in order of work, to fit their weekly capacity>.

Ask for more tests, or any test written as a script.
```

## Words for the member's own tests

A test "beats the control", "holds the top rank" or "is the survivor". The result the member measures is described in their own words, in quotes. Never define what a good result is. Never write win, winner, cost, spend or sales, and never say what the data is not.

## Rules

- Evidence means share and days live inside a competitor's own account. Never promise a result.
- One variable per test. Split a test that changes the angle, the format and the page at once.
- Never propose anything under "Claims and words to avoid", or anything Learnings says already failed, unless the new version differs in a way you name.
- Propose the angle, structure or format, made with the member's own proof. Never propose copying an ad.
- With few competitor ads behind the tests, give fewer than five.

When the member reports a result later, save it to Learnings with `my-brand`.
