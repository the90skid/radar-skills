---
name: my-brand
description: "When the user wants to tell Radar about their own brand, product, customer, offer or country, or update it, or reports a test result or a learning to keep (\"we tested the GLP-1 angle and it beat our control, save that\"): creates or updates radar-brand.md, the brand file every other Radar skill reads first, and its Learnings. Use this skill first, also later in a conversation. Run it once before what-to-test-next or ad-writer."
metadata:
  version: 1.5.0
---

# My brand

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

You create and keep one short file, `radar-brand.md`, in the working folder. Every other Radar skill reads it so the member never repeats themselves. In a client with no files, keep the same content in the conversation and tell the member to paste it at the start of a new chat.

If the member is reporting a test result or a learning, go straight to "Learnings" at the end.

## If the file exists

Read it. Summarise it in five lines. If it has no "Market" line, ask which country they compete in (default United States). Ask what changed. Update only those parts, add one line to the change log with the date, and stop.

## If it does not exist

Offer two ways:

1. **Draft it from their website** (faster). Ask for the address, read the homepage and the best-selling product page, draft the file, then ask them to correct it.
2. **Answer questions.** Ask the questions below, a few at a time.

Never invent a fact about their brand. A blank line is better than a guess; mark it "to fill in".

## The questions

**Product**
- What do you sell, in one sentence a customer would say?
- Price, and the offer you run most (bundle, subscription, discount, gift)?
- What does it do better than the alternatives? Give the proof you can show (results, reviews, numbers, tests).

**Customer**
- Who buys it? Age, life stage, the moment they need it.
- What problem are they trying to fix, in their own words?
- What stopped them buying before? List the top three objections.

**Ads today**
- Which formats do you run (creator video, founder video, static, carousel)?
- Which angles have you already tested? Which worked, which failed?
- Where do your ads send people (product page, advertorial, listicle, quiz)?
- What can you produce each week (how many videos, how many statics)?

**Rules**
- Claims you cannot make (medical, legal, platform rules).
- Words or tones to avoid. Brand voice in three words.

**Market**
- Which country do you compete in? Default: United States. Radar tracks United States, United Kingdom, Canada, Australia, India, Ireland, New Zealand, Germany, France, Netherlands, Spain and United Arab Emirates.

**Competitors**
- Who do you lose customers to? If Radar is connected, call `list_tracked` and confirm the list instead of asking.

## The file

Write `radar-brand.md` with this shape:

```markdown
# Brand: <name>
Updated: <date>
Market: <country> (<code>)

## Product
## Offer
## Proof we can show
## Customer
## Their problem, in their words
## Objections
## Ads we run today
## Angles already tested (worked / failed)
## Landing pages we use
## Weekly production capacity
## Claims and words to avoid
## Voice
## Competitors
## Learnings
(dated notes other Radar skills add: what was tested, what happened)

## Change log
```

Write the Market line as the country's name and its code from "Markets" in [references/radar-data.md](references/radar-data.md), for example `Market: United Kingdom (GB)`. Other skills pass that code to the Radar tools.

Keep it under 120 lines. After saving, say "Saved." and offer, in one line, to find what to test next.

## Learnings

When the member reports a result or a learning ("We tested the GLP-1 angle and it beat our control. Save that."), add one dated line under Learnings in `radar-brand.md`: `- <date>: "<the member's own words>"`. Confirm with "Saved to Learnings." and nothing more. When the file did not exist, create it with the brand file shape, put the line under Learnings, and say only: "Saved to Learnings. Your brand file is new: tell me what you sell and who buys it and I'll fill in the rest." Ask nothing unless the result names no angle, format or page. Never turn their words into win, winner, cost, spend, sales or performance; a test "beat the control", "held the top rank" or "is the survivor" only when those are their words. Other skills read Learnings so they do not propose a test that has already been run.
