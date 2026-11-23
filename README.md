# Radar skills

Skills that let your own AI work out what your competitors' ads are doing: their angles, hooks, scripts, landing pages, what they killed and what to test next.

The skills run on Radar, part of the [Funnel Library by DTC Daily](https://funnels.dtcdailynews.com/). Radar reads your competitors' Meta ads every night and joins each ad to the landing page it sends people to. The skills tell your AI how to read that record. Your AI does the thinking; Radar supplies the data.

Works with Claude Code, Claude (web and desktop), Codex, Cursor and any agent that supports the [Agent Skills format](https://agentskills.io).

## What you can ask

| Ask | Skill |
|---|---|
| "Set me up on Radar" | `radar-setup` |
| "Here is my brand" | `my-brand` |
| "What are my competitors doing?" | `competitor-overview` |
| "Break down Grüns" | `brand-deep-dive` |
| "What angles are they using?" | `competitor-angles` |
| "What hooks open their best ads?" | `competitor-hooks` |
| "What did they try and kill?" | `killed-ads` |
| "What changed this week?" | `weekly-watch` |
| "What is working in my category?" | `industry-patterns` |
| "Break down the page behind their top ad" | `landing-page-teardown` |
| "Turn this ad into a script template" | `script-teardown` |
| "What should I test next?" | `what-to-test-next` |
| "Write three ads for my product from this" | `ad-writer` |

[QUESTIONS.md](QUESTIONS.md) has 50 questions that get the most out of it.

## Install

You need a DTC Daily account with Radar. The skills are free; the data comes through your account.

### Claude Code (skills and the Radar connection in one step)

```bash
claude plugin marketplace add the90skid/radar-skills
claude plugin install radar-skills@radar-skills
```

Then run `/mcp`, choose **radar**, and sign in with your DTC Daily account.

### Any agent that supports skills

```bash
npx skills add the90skid/radar-skills
```

Then connect Radar as a remote MCP server at `https://funnels.dtcdailynews.com/mcp` and sign in.

### Claude on the web or desktop

1. Settings → Connectors → Add custom connector. Name it Radar, paste `https://funnels.dtcdailynews.com/mcp`, press Connect and sign in.
2. Download the skill ZIPs from the latest release and add each under Customize → Skills → Upload a skill.

### ChatGPT

ChatGPT connects to Radar as an app (Settings → Apps → Advanced → developer mode → create an app with the address above). It does not load skills; ask the questions in [QUESTIONS.md](QUESTIONS.md) directly.

## First run

Say: **"Set me up on Radar. My site is mybrand.com."**

Your AI checks the connection, suggests competitors, tracks the ones you pick and gives you your first overview.

## Countries

Radar reads the ads Meta shows in the United States. You can also track a competitor in the country you sell in: United Kingdom, Canada, Australia, India, Ireland, New Zealand, Germany, France, Netherlands, Spain or United Arab Emirates. That brand's live ads, ranks and shares are then for that country. `radar-setup` asks for your country once, and every skill uses it.

## How the skills read the data

- An ad's **rank** is its place in the order Meta shows a brand's ads. Meta decides delivery, so an ad it keeps showing is one that keeps earning its place.
- **Days live** is how long the brand has kept the ad running.
- An ad with both a high share and a long run is one of **that brand's high performers**. That is a statement about the brand's own ads, and ranks are never compared across brands.
- The data holds no spend, ROAS or sales figures, and the skills never state them.
- When a figure is not in the data, the skills leave it out. They never fill it with a guess or a zero.

## Privacy

The skills are text files that run inside your AI. Radar receives only the tool calls your AI makes (which brand, which page). It never sees your conversation. [Privacy policy](https://funnels.dtcdailynews.com/privacy/).

## Licence

MIT. Edit the skills to fit how you work.
