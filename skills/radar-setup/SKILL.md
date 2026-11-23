---
name: radar-setup
description: "When the user wants to set up or connect Radar (the Funnel Library by DTC Daily), asks how to start, says the Radar tools are missing or not signed in, wants to pick or change the competitors they track or their country, or to track a brand in a country: connects the MCP, checks sign-in, sets the country, picks competitors and runs the first overview. Use this skill first, before calling Radar tools directly. For the member's own brand details, see my-brand."
metadata:
  version: 1.5.0
---

# Radar setup

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

You get a member from nothing to their first competitor overview in one sitting. Keep every message short, about 120 words: one step, what to do, what to tell you when it is done. Say nothing about what you checked or which tool you called.

## Step 1: Is Radar connected?

Look for the Radar tools (`get_brief`, `top_ads`, `competitor_overview`, `list_tracked`). If your client loads tools on demand, search for "DTC Funnels" or "Funnel Library".

**Tools present:** call `get_usage`. If it answers, go to Step 2. If it says sign-in is needed, ask the member to sign in through their client's connector screen, then try again.

**Tools absent:** first search for them by name (`top_ads`, `competitor_overview`, "DTC Funnels", "Funnel Library") and try `get_usage`. Only when the search finds nothing, or the call says the connection is not set up, give the steps for their client, then wait.

- **Claude (web, desktop, mobile):** Settings, then Connectors, then Add custom connector. Name: Radar. Address: `https://radar.dtcdailynews.com/mcp`. Press Connect and sign in with the DTC Daily account.
- **Claude Code:** run `claude mcp add --transport http radar https://radar.dtcdailynews.com/mcp`, then `/mcp`, choose radar, Authenticate.
- **ChatGPT:** Settings, Apps, Advanced, turn on developer mode. Create an app named Radar with the address `https://radar.dtcdailynews.com/mcp`, then sign in.
- **Other clients:** add a remote MCP server at the same address. Sign-in is OAuth in the browser.

Never ask the member to paste a password or key into the chat. If they have no account, send them to `https://radar.dtcdailynews.com/` to create one.

## Step 2: Which country?

Call `list_tracked`. Each brand tracked outside the United States shows its `market`.

If `radar-brand.md` has a "Market" line, or every tracked brand is in one country, use that country and go on. Otherwise ask one question:

"Which country do you compete in? I'll use United States unless you say otherwise."

The countries Radar tracks: United States, United Kingdom, Canada, Australia, India, Ireland, New Zealand, Germany, France, Netherlands, Spain, United Arab Emirates. Each has a code for `market` (see "Markets" in the reference).

Save the answer on the "Market" line of `radar-brand.md`, for example `Market: United Kingdom (GB)`. If the file does not exist yet, create it with the brand's name or website and that line. Later skills read it and never ask again.

## Step 3: Who are the competitors?

- **They already track brands in that country:** show the list and ask whether to keep it or change it.
- **They track none there:** ask for their own website. Call `suggest_competitors` with it. Show up to eight suggestions, one line each with the reason the tool gives. Call `get_usage` or `list_tracked` for the number of brands the plan tracks, and tell the member that number. Ask them to pick that many, or fewer, or to name others. Never state a price.

Track the chosen brands with `track_brand`, one call each, up to the number the plan tracks. When a tool says the slots are full or a swap is needed, repeat its line and ask before swapping. For a country other than the United States, pass `market` with its code on each call. Tracking changes the member's account, so only track brands they named or picked.

If a brand is not in the library, `track_brand` with its website adds it. That uses one of the member's monthly adds and takes about an hour. Pass `market` here too, so it is tracked in their country once it is added. Ask before using an add.

## Step 4: Their own brand

If `radar-brand.md` holds only the Market line, or does not exist, offer the `my-brand` skill in one line and carry on without it if they decline.

## Step 5: First overview

For the United States, call `competitor_overview` with no brands (it uses the tracked ones). For another country, pass `brands` set to the `brand_id` of each brand tracked there and `market` with its code. Present it the way the `competitor-overview` skill lays it out: one short block per competitor, then what stands out across them. Name the country once at the top when it is not the United States.

A brand being read for the first time in its country answers with one line. Repeat that line for that brand and carry on with the others.

## Step 6: What to ask next

End with three questions that fit what the overview showed, for example:

- "What angles are they using?"
- "Break down [the brand pushing hardest]."
- "What should I test next?"

## If something fails

- **Requests used up:** when a tool says requests are used up, repeat its line (it carries the reset date) and stop.
- **A tool says AI access comes with a paid plan:** repeat its line and stop.
- **A tool errors:** quote the error in one line, try once more, then stop and say what happened.
