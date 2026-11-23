---
name: industry-patterns
description: "When the user asks what is working across a whole category (supplements, skincare, pet, apparel and so on), what the best ads in a market share, which formats or page types are rising, or what page type the best ads in a category send to: answers from Radar data by reading the high performers of every brand in the category. Use this skill first, before calling Radar tools, also later in a conversation. For named competitors only, see competitor-angles and competitor-overview."
metadata:
  version: 1.3.1
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
- Every tracked brand is a competitor. Folder names mean nothing. Never state lookup costs.
<!-- /rules -->

You look past the member's own competitors to the whole category and report what its high performers share.

Read `radar-brand.md` if it exists. Category reads cover the United States library. When its Market line names another country, say "in the United States" once at the top.

## Which category

Use the category the member names. If they name none, take it from `radar-brand.md`, or call `describe_data` to list the categories and ask them to pick. Never guess between two that could fit.

## Pull the data

1. `category_top_ads` with the category, `per_brand` 3, `limit` 100, `min_days_live` 14, `transcripts` false.
2. `category_top_ads` again with `per_brand` 1 and `transcripts` true: each brand's top creative with its script.
3. `category_trends` for the same category.

Do not open individual brands in this skill.

## Find the patterns

Count. A pattern is something at least a quarter of the brands share: angle, hook type, format, video structure, page type, offer, proof or length of run.

## The answer

At most 450 words. This shape, then stop:

```
<Lead line: the category, the date of the ranks, and the pattern the most brands share with its count.>

1. <Pattern>: <n> of <N> brands.
   - <Brand>: "<hook>", creative live <d> days. <link>
   - <Brand>: "<hook>", creative live <d> days. <link>
   - <Brand>: "<hook>", creative live <d> days. <link>
(exactly 4 patterns, three ads each, from three different brands)

Rising: <one or two lines from category_trends, with the weeks compared>.

Ask for more patterns, what only a few brands do, or how this fits your brand.
```

## Rules

- Rank and share are within each brand. Never rank one brand's ad above another's. Count how many brands do something.
- Give counts, never percentages of a small number.
- Every pattern cites three ads, each with its own link. Never cite only a brand or a page.
