---
name: brand-deep-dive
description: "When the user wants one competitor broken down, asks what a brand's ad strategy is, its highest performers and what they share, which of its ads ran longest, what it is testing, or how its ads and pages fit together, also as a follow-up about a brand already named: high performers, tests, kills, long-runners and pages for one brand. Use this skill first, before calling Radar tools, also later in a conversation. For several brands at once, see competitor-overview."
metadata:
  version: 1.5.0
---

# Brand deep dive

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
- **Tracked brands.** Deep answers cover tracked brands. When a tool answers `tracked` false or carries `track_line`, give the library answer you have, then that one line, and offer to track the brand. Track only when the member says yes; if a swap is needed, repeat the tool's line and ask first. When requests are used up, repeat the tool's line and stop.
- Every tracked brand is a competitor. Folder names mean nothing. Never state what a call costs.
<!-- /rules -->

You brief the member on one brand's ad account: what it runs, what it pushes hardest, what it tried and dropped, and where the traffic goes.

Read `radar-brand.md` if it exists. If its Market line names a country other than the United States, follow "Markets" in the reference: pass `market` on every brand call and name the country once at the top.

Check `list_tracked` first. When the brand named is not tracked, answer with what library depth supports: `get_brand_ads` (view list, sorted `longest_running`), `get_brand_pages` and the ads' own copy, and give the track line once at the end. Leave out the parts that need ranks, shares, tests or switched-off ads.

## Pull the data

For the full breakdown:

1. `top_ads`: proven, being tested and long-runners, with the tool's labels.
2. `ad_movers`: what climbed, fell, launched and ended.
3. `killed_ads` with `since_days` 30.
4. `creative_tests`: tests and survivors.
5. `get_brand_pages` (United States only; for another market take the pages from the ads you already have).

For "which ads have run the longest", or any question about all of a brand's ads, call `export_ads` (compact rows) with `sort` set to `days_live`. A narrow question needs only the one call that answers it. For angles or script structure, hand over to `competitor-angles` or `script-teardown`.

## The answer

A narrow question ("what are they testing?", "which ran longest?") gets the lead line and at most four bullets, 250 words at most. The full breakdown is at most 600 words, in this shape, then stop:

```
<Lead line: live creatives, format mix, the date the ranks are from.>

Proven
- "<hook>": <format>, creative live <d> days, est. share <x>%, to a <page type>. <link>
(up to 3, then one line on what they share, with counts)

Being tested
- "<hook>": <format>, creative live <d> days, rank <r>. <link>
(up to 3)

Switched off in 30 days: <n>, median lived <d> days. Longest: "<hook>", lived <d> days. <link>

Long-runners
- "<hook>": creative live <d> days, est. share <x>%. <link>
(up to 3)

Where the traffic goes
- <page type>: <n> live ads<, A/B test live><, changed on <date>>. <link>
(up to 3)

For your brand: <two lines; only when radar-brand.md exists>

Ask for any part in full.
```

The part headings are the group names alone (Proven, Being tested, Long-runners), with no rule or number beside them. A slot the tool gives nothing for is left out of its line.

## Rules

- Every ad named carries its own link.
- State only what the data shows. Give no reason for the brand's choices.
