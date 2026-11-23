---
name: competitor-hooks
description: "When the user wants the hooks or opening lines competitors use, how their best ads open, the new hooks they launched, or hook templates, also as a follow-up about brands already named: groups each ad's first line by type, ranks them by how hard they are pushed and how long they ran, and turns the strongest into fill-in templates. Use this skill first, before calling Radar tools, also later in a conversation. For the reason to buy behind the ad, see competitor-angles."
metadata:
  version: 1.3.1
---

# Competitor hooks

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

The hook is the first line a viewer hears or reads. You show which openings the competitors' high performers use and hand back templates the member can fill in.

Read [references/hook-types.md](references/hook-types.md). Read `radar-brand.md` if it exists. If its Market line names a country other than the United States, follow "Markets" in the reference: pass `market` on every brand call and name the country once at the top.

## Pull the ads

- **One or a few brands:** `export_ads` per brand with `status` live, `limit` 150. Each creative's hook is in `advertiser_content`; `hook_source` says whether it is the spoken opening line or the headline.
- **"New hooks this fortnight":** `export_ads` per brand with `sort` set to `newest`, `limit` 30. Only when the member asks.
- **A phrase across the library:** `search_ads` with the text, grouped by hook.
- **A whole category:** hand over to `industry-patterns`.

With no brands named, use `list_tracked`.

## Group and rank

Take each creative's opening line in its exact words, give it a type from [references/hook-types.md](references/hook-types.md), collapse identical lines (keep the count), and rank within each brand: high share and long run first.

## The answer

At most 450 words. This shape, then stop:

```
<Lead line: the hook type the top hooks share most, with its count.>

| Hook | Brand | Type | Creative live | Est. share | Link |
|---|---|---|---|---|---|
(at most 8 rows: up to 5 for one brand, up to 3 per brand for several; mark headline hooks "(headline)")

Templates
1. "<template with [slots]>"
   From: "<hook>", <Brand>, creative live <d> days. <link>
   For you: "<the template filled for the member's product>"
(exactly 3; write the "For you" line only when radar-brand.md exists or the member described their product)

Ask for more templates, the hook types by brand, or the new hooks of the last two weeks.
```

## Rules

- A hook is strong for a brand when its ads hold share and keep running. Many copies of a new ad is a push, and it is not proof yet.
- Their words go in quotes; yours go under "For you". Never present a rewritten line as theirs.
- Templates keep the structure and drop the competitor's claim. Never carry a competitor's numbers, reviews or medical claims into the member's version.
- Respect "Claims and words to avoid" in `radar-brand.md`.
