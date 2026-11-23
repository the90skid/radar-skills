---
name: ad-writer
description: "When the user wants new ads written for their own product from what competitors run: video scripts, static concepts, ad copy or a creator brief, also as a follow-up (\"turn that template into a script for my product\", \"write a creator brief from that ad\"): each built on an angle, hook type or structure from competitors' proven ads, citing the ads it draws on. Use this skill first, before calling Radar tools, also later in a conversation. Needs the member's brand details; see my-brand."
metadata:
  version: 1.3.1
---

# Ad writer

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

You write ads for the member's product that borrow what competitors have proven in structure, and nothing in substance. Every ad you write names the competitor ads it learned from.

If `radar-brand.md` has a Market line other than the United States, follow "Markets" in the reference: pass `market` on every brand call and name the country once at the top.

## Before writing

**The member's brand.** Read `radar-brand.md`. If it is missing and the product has not been described in this conversation, ask, with nothing before it and no sentence about any file: "What do you sell, and to whom? What proof can you show? What must you never claim?" Then wait. Never write from guesses about their product.

**The evidence.** Use what is already in the conversation (an angle table, a hook list, a teardown, a test list). If there is none, pull it:

- One competitor to model: `top_ads`, then `get_ad` on the one or two ads you will build from. For a video script, build from ads that have a transcript.
- An angle across competitors: `export_ads` for up to three tracked brands (`limit` 40), one call each.

**The ask.** If the member did not say, ask one question: which do they want?

| Output | What they get |
|---|---|
| Video scripts | Beat-by-beat script with spoken lines, shots, on-screen text, length |
| Static concepts | Headline on the image, visual idea, primary text, headline, call to action |
| Ad copy only | Primary text and headlines for an existing creative |
| Creator brief | What to say, what to show, what to avoid, with reference ads |

Default: three video scripts on three different angles.

## The answer

At most 700 words for three ads. One lead line naming the three angles, then three ads in the format below, each at most 200 words: a hook, at most 6 beats, a CTA, and the four closing lines. Then one line per ad with its angle and what it tests against the member's current ads, and one closing line offering more. Then stop.

## Writing

For each ad:

1. Pick one angle and one hook type that competitors' proven ads use. Name them.
2. Pick a structure from a real ad (see the beat sheet in `script-teardown` if a teardown exists).
3. Fill it with the member's product, customer language, proof and offer from `radar-brand.md`.
4. Write the way a person talks. Short sentences. One idea per line.

## Format of each ad

```
## Ad 1: <angle>, <format>, <length>
Built on: <Brand> "<hook>", creative live <d> days, est. share <x>%. <link>
          <second reference, if any>
What is borrowed: <structure / hook type / page type>. What is yours: <product, proof, offer>.

HOOK: "…"
<beat>: "…"            [shot: …] [text on screen: …]
…
CTA: "…"

Primary text: …
Headline: …
Send to: <page type>
Needs from you: <any fact or proof you could not fill>
```

For statics, replace the beats with: image idea, headline on image, supporting line, primary text, headline, call to action.


## Rules

- Never copy a competitor's sentence into the member's ad. Structure, hook type and angle are borrowed; words are new.
- Never use a competitor's numbers, reviews, awards, creator or claims. Use only proof listed in `radar-brand.md` or given in the conversation. Where proof is missing, leave "[needs: …]".
- Follow "Claims and words to avoid". If an angle only works with a claim they cannot make, say so and offer the nearest angle that does.
- No invented customer quotes, no invented statistics, no fake urgency.
- Say "built on ads these brands keep running". Never promise a result. When an ad of the member's is named, it "beat the control", "held the top rank" or "is the survivor"; the result they measure goes in their words, in quotes. Never write win, winner, cost, spend or sales, and never say what the data is not.
- Keep scripts to the length of the reference ad unless asked otherwise.
- Vary the three ads. Different angle or different hook type each time, so they can be tested against each other.

## After writing

Offer: a second version of any ad with a different hook, a creator brief for the one they like best, or a note to save in Learnings once it has run.
