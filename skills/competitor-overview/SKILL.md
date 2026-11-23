---
name: competitor-overview
description: "When the user wants to know what their competitors are doing in ads, asks for an overview or a competitor report, who is pushing what, to compare several brands side by side, or to run the overview again after adding a brand: top ads, formats, hooks and landing pages for every tracked competitor in one read. Use this skill first, before calling Radar tools, also later in a conversation. For one brand in depth, see brand-deep-dive. For what changed this week, see weekly-watch."
metadata:
  version: 1.3.1
---

# Competitor overview

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

You give the member the state of their competitors in one read: what each is pushing, in what format, to which kind of page, and what stands out across them.

Read `radar-brand.md` if it exists. If its Market line names a country other than the United States, follow "Markets" in the reference: pass `market` on every brand call and name the country once at the top.

## Steps

1. Call `competitor_overview`. Pass `brands` only if the member named specific brands; otherwise leave it out and it uses the brands they track. If they track none, switch to `radar-setup`.
2. Call no other tool for the first answer.

## The answer

At most 500 words. This shape, then stop:

```
<Lead line: the one fact that matters most across them, and the date the ranks are from.>

### <Brand>: <N> live creatives (<video>% video, <image>% image)
Pushing hardest: "<hook>", <format>, creative live <d> days, est. share <x>%, to a <page type>. <link>
Also high: "<hook>", est. share <x>%. <link> (at most 2)
This week: <n> new creatives, <n> switched off. Pages: <page type> <live ads>, <page type> <live ads>.
(one block per brand, biggest advertiser first; with more than four brands, give each brand only its first two lines; a slot the tool gives nothing for is left out of its line)

Across them
- <one fact naming the brands, with one ad and its link>
- <one fact>
(exactly 2)

Ask "What angles are they using?", "Break down <brand>." or "What should I test next?"
```

Leave out any line the answer has no figure for. If a brand the member named is not in the library, give it one line offering to add it with `track_brand` and its website. A brand that answers with one line (first read, or no live ads that night): repeat that line as its block.

## Rules

- Count creatives; mention copies only as a sign of scale.
- Rank and share are within each brand. Never say brand A's ad "outranks" brand B's.
- Use the labels the tools return; for anything else give share, rank and the creative's age.
