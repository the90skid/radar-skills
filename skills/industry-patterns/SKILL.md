---
name: industry-patterns
description: "When the user asks what is working across the competitors they track, what their best ads share, which hooks, formats or page types show up across brands, or what the best ads of all their competitors send people to: answers from Radar data by reading the tracked brands side by side. Use this skill first, before calling Radar tools, also later in a conversation. For one named brand, see brand-deep-dive."
metadata:
  version: 1.5.0
---

# Industry patterns

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

You look across the brands the member tracks and report what their high performers share.

Read `radar-brand.md` if it exists. If its Market line names a country other than the United States, follow "Markets" in the reference: pass `market` on every brand call and name the country once at the top.

## Which brands

The brands the member tracks (`list_tracked`). If the member names a group ("my skincare competitors"), use the tracked brands that fit it. Never read a brand the member does not track. When they name one, give the track line once and read the others.

## Pull the data

1. `competitor_overview` for the tracked brands.
2. `export_ads` (compact rows, `status` live, `limit` 40) for each tracked brand. One call a brand, or two for a brand with a long list.
3. `brand_words` for each tracked brand, to confirm what the brands say in common.

## Find the patterns

Count brands, not ads. A pattern is something at least a quarter of the tracked brands share (two, when three are tracked): angle, hook type, format, video structure, page type, offer, proof or length of run. Read each brand's high performers: the rows with the highest `est_share_pct` and the longest `creative_days_live`.

## The answer

At most 450 words. This shape, then stop:

```
<Lead line: the date of the ranks and the pattern the most tracked brands share, with its count.>

1. <Pattern>: <n> of <N> tracked brands.
   - <Brand>: "<hook>", creative live <d> days. <link>
   - <Brand>: "<hook>", creative live <d> days. <link>
   - <Brand>: "<hook>", creative live <d> days. <link>
(exactly 4 patterns, three ads each, from three different brands; with fewer brands, one ad per brand)

Ask for more patterns, what only one brand does, or how this fits your brand.
```

## Rules

- Rank and share are within each brand. Never rank one brand's ad above another's. Count how many brands do something.
- Give counts, never percentages of a small number.
- Every pattern cites its ads, each with its own link. Never cite only a brand or a page.
- A line saying only one brand does something, or none does, comes after `brand_words` with `word` for every other brand.
