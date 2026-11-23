# Versions

### 1.5.0 (unreleased)
Plans v2 (23 Nov 2026). Every paid DTC Daily plan includes AI access: requests replace lookups, and deep answers (ranks, estimated share, top ads, movers, weekly changes, switched-off ads, tests, words, bulk export) cover the brands the member tracks. Any other brand answers at library depth with one `track_line`. The shared rules carry a "Tracked brands" section: give the library answer, then that one line, and track only when the member says yes (a swap is asked about first); when requests are used up, repeat the tool's line and stop. `category_top_ads` and `category_trends` are no longer in member plans: industry-patterns now reads the patterns across the brands the member tracks (`competitor_overview`, `export_ads`, `brand_words`), what-to-test-next uses `next_tests` over the tracked brands alone, and QUESTIONS reads "across my competitors". Skills that name a brand check `list_tracked` first. radar-setup uses the address `https://radar.dtcdailynews.com/mcp` and says how many brands the plan tracks, never a price; the old `funnels.dtcdailynews.com` address keeps working. landing-page-teardown: a stale second copy of the skill body is removed and its Rules section restored. `validate.py` fails on the removed tools, on "lookups" and on the old address.

| Skill | Version |
|---|---|
| radar-setup | 1.5.0 |
| my-brand | 1.5.0 |
| competitor-overview | 1.5.0 |
| brand-deep-dive | 1.5.0 |
| competitor-angles | 1.5.0 |
| competitor-hooks | 1.5.0 |
| killed-ads | 1.5.0 |
| weekly-watch | 1.5.0 |
| industry-patterns | 1.5.0 |
| landing-page-teardown | 1.5.0 |
| script-teardown | 1.5.0 |
| what-to-test-next | 1.5.0 |
| ad-writer | 1.5.0 |

### 1.4.1 (unreleased)
Fixes after the third retest. Rules block: final lines only (each figure checked against its row, never a correction or two versions of a figure); a slot the tool gives nothing for is left out with no words in its place; "only one brand" or "none of them" only after `brand_words` with `word` returns nothing for every other brand. The shared file adds the same three rules and searches for deferred Radar tools and tries one call before saying they are missing. competitor-angles: words answers give the top ad for each of the top 3 terms; the multi-brand "only one brand runs" line is replaced. landing-page-teardown: an Offer block always comes first, the second `show_page` call is aimed at the buy box, and the section table groups neighbouring sections. killed-ads: the 7-day and 30-day counts from the tool's summary in the lead line. competitor-overview: a Pages slot on each brand's last line. brand-deep-dive: a narrow question gets at most four bullets; headings carry no rule. script-teardown: "Your version" replaces the template. what-to-test-next: three lines per test. my-brand: a learning saved with no brand file creates the file.

| Skill | Version |
|---|---|
| radar-setup | 1.3.1 |
| my-brand | 1.3.1 |
| competitor-overview | 1.3.1 |
| brand-deep-dive | 1.3.1 |
| competitor-angles | 1.4.1 |
| competitor-hooks | 1.3.1 |
| killed-ads | 1.3.1 |
| weekly-watch | 1.3.1 |
| industry-patterns | 1.3.1 |
| landing-page-teardown | 1.3.1 |
| script-teardown | 1.3.1 |
| what-to-test-next | 1.3.1 |
| ad-writer | 1.3.1 |

### 1.4.0 (unreleased)
Answers after the 57-session retest. Every skill opens with the same compact rules block (`shared/rules-block.md`, written in by `sync-shared.sh`), which applies to every later Radar answer in the conversation even when no skill fires. Each skill's answer is a fixed shape (one lead line, a capped number of items, one closing line that offers more, then stop) sized to its word ceiling; a follow-up question gets 250 words, a lead line and at most five bullets. Optional parts (new hooks, approximate ends, dropped angles, "For your brand" without the brand file) left the default output. Rule 7 bans first-person accounts of the work, corrections of earlier turns and notes on rounding or approximation; counts are stated about the brand. Words for the member's own tests: "beat the control", "held the top rank", "is the survivor". "Still new" is gone; ads outside the tools' groups get share, rank and age only. Links follow a fixed order and are never composed. Every number of days carries a label ("creative live", "this copy live", "lived"). landing-page-teardown calls `show_page` at most twice and tears down the best-placed page the tools return when one cannot be opened; script-teardown numbers beats without remark when there are no timestamps. `validate.py` checks the rules block, bare "Days" columns and banned phrases.

| Skill | Version |
|---|---|
| radar-setup | 1.3.0 |
| my-brand | 1.3.0 |
| competitor-overview | 1.3.0 |
| brand-deep-dive | 1.3.0 |
| competitor-angles | 1.4.0 |
| competitor-hooks | 1.3.0 |
| killed-ads | 1.3.0 |
| weekly-watch | 1.3.0 |
| industry-patterns | 1.3.0 |
| landing-page-teardown | 1.3.0 |
| script-teardown | 1.3.0 |
| what-to-test-next | 1.3.0 |
| ad-writer | 1.3.0 |

### 1.3.0 (unreleased)
Answers after the 53-session test on staging. Shared rules: a length budget (lead with the main finding; about 250 words for a direct question, about 500 for a report); answers never describe their own reading, samples, limits or skipped sections; facts are never joined with "because", "so" or "likely"; quotes are copied exactly; no budget, spend, performance, ROAS or winner about anyone's ads; every tracked brand is a competitor and folder names mean nothing; no lookup costs; links go to the ad itself, from the tools only; days carry the tool's own label (a creative's age or one copy's). Skills use the tools' labels (proven, being tested, long-runners) and no day thresholds of their own. killed-ads reads the shortest-lived and the longest-lived; brand-deep-dive uses `export_ads` for longest-running; industry-patterns cites three ads per pattern; script-teardown never repairs a quote; my-brand saves test results to Learnings. Descriptions cover follow-up questions in a conversation.

| Skill | Version |
|---|---|
| radar-setup | 1.2.0 |
| my-brand | 1.2.0 |
| competitor-overview | 1.2.0 |
| brand-deep-dive | 1.2.0 |
| competitor-angles | 1.3.0 |
| competitor-hooks | 1.2.0 |
| killed-ads | 1.2.0 |
| weekly-watch | 1.2.0 |
| industry-patterns | 1.2.0 |
| landing-page-teardown | 1.2.0 |
| script-teardown | 1.2.0 |
| what-to-test-next | 1.2.0 |
| ad-writer | 1.2.0 |

### 1.2.0 (unreleased)
Countries. `radar-setup` asks which country the member competes in (default United States), tracks competitors there with `market` and saves it on the "Market" line of `radar-brand.md`. Every skill that names a brand passes `market` for a country other than the United States, names the country once and keeps one country per table. The shared reference has a "Markets" section. Skills report facts only: reason-giving lines removed from killed-ads, industry-patterns, landing-page-teardown and three references. Questions 2 and 45 are new; two questions that invited a guess were reworded.

| Skill | Version |
|---|---|
| radar-setup | 1.1.0 |
| my-brand | 1.1.0 |
| competitor-overview | 1.1.0 |
| brand-deep-dive | 1.1.0 |
| competitor-angles | 1.2.0 |
| competitor-hooks | 1.1.0 |
| killed-ads | 1.1.0 |
| weekly-watch | 1.1.0 |
| industry-patterns | 1.1.0 |
| landing-page-teardown | 1.1.0 |
| script-teardown | 1.1.0 |
| what-to-test-next | 1.1.0 |
| ad-writer | 1.1.0 |

### 1.1.0 (unreleased)
competitor-angles 1.1.0: "What are the main angles [brand] is pushing?" starts from `brand_words`, then reads the ads behind the strongest words.

### 1.0.0
First release: 13 skills.

| Skill | Version |
|---|---|
| radar-setup | 1.0.0 |
| my-brand | 1.0.0 |
| competitor-overview | 1.0.0 |
| brand-deep-dive | 1.0.0 |
| competitor-angles | 1.0.0 |
| competitor-hooks | 1.0.0 |
| killed-ads | 1.0.0 |
| weekly-watch | 1.0.0 |
| industry-patterns | 1.0.0 |
| landing-page-teardown | 1.0.0 |
| script-teardown | 1.0.0 |
| what-to-test-next | 1.0.0 |
| ad-writer | 1.0.0 |
