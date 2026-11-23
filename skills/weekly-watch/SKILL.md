---
name: weekly-watch
description: "When the user wants to know what changed with their competitors this week or since they last looked, asks for a weekly report, an update or what is new, or a Monday brief: launches, climbers, switch-offs and landing-page changes for every tracked competitor over the last 7 days, most important first. Use this skill first, before calling Radar tools, also later in a conversation. For the standing picture, see competitor-overview. For one ad they just ended, see killed-ads."
metadata:
  version: 1.3.1
---

# Weekly watch

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

You tell the member what moved since last week, in the order they should care about it.

Read `radar-brand.md` if it exists. If its Market line names a country other than the United States, follow "Markets" in the reference: pass `market` on every brand call and name the country once at the top.

## Pull the data

Call `weekly_changes` once. Leave `brands` out to use the tracked brands. Use `days` 7 unless the member gives another span (3 to 14). That call is enough.

## What leads

In this order: a new creative already holding a high share; a long-runner switched off; a landing page changed, a new page taking traffic, an A/B test started; a climber that reached the top of its page; a burst of launches; a quiet brand.

## The answer

At most 500 words. This shape, then stop:

```
<Title: the dates covered.>

Top of the week
1. <Brand>: <what happened>, <the number that puts it there>. <link>
(exactly 3, across all brands, two lines each at most)

### <Brand>
Launched: <n> creatives. Best placed: "<hook>", rank <r>, to a <page type>. <link>
Climbed: "<hook>" to rank <r> (<the two dates compared>). <link>
Switched off: <n>. Longest-lived: "<hook>", lived <d> days. <link>
Pages: <new page / changed / A/B started / switched off>
(one block per brand, at most 4 lines; leave out an empty line; with more than four brands, give each brand only its Launched and Switched off lines)

Ask for any brand in full, or what to do about it this week.
```

## Rules

- Count creatives launched and switched off, never copies.
- Switch-offs are verified ends only. Write "0 switched off" only when the tool returns 0.
- A climb is a move in Meta's display order on that page: give the rank it reached and the two dates compared.
- If the member asks for this every week, tell them they can schedule it in their client.
