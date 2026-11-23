#!/usr/bin/env python3
"""Checks every skill against the Agent Skills spec and this pack's own limits. Exit 1 on any problem."""
import os, re, sys, hashlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = os.path.join(ROOT, "skills"); bad = []; total = 0
TOOLS = {"ad_movers","boards","category_trends","creative_tests","describe_data","fetch","folders","get_ad","get_brand","get_brand_ads","get_brand_pages",
         "get_brief","get_page","get_usage","list_tracked","next_tests","save_to_board","search","search_ads","search_brands","search_pages","show_ad","show_page",
         "suggest_competitors","top_ads","track_brand","export_ads","competitor_overview","killed_ads","weekly_changes","category_top_ads","brand_words"}
names = sorted(d for d in os.listdir(S) if os.path.isdir(os.path.join(S, d)))
shared = hashlib.md5(open(os.path.join(ROOT, "shared/radar-data.md"), "rb").read()).hexdigest()
# Markets (server markets.mjs COUNTRIES): the tools that take `market`, and the countries a member can track a brand in
MARKET_TOOLS = {"top_ads","export_ads","brand_words","killed_ads","creative_tests","ad_movers","get_brand","get_brand_ads","next_tests","get_brief",
                "competitor_overview","weekly_changes","track_brand"}
COUNTRIES = {"US": "United States", "GB": "United Kingdom", "CA": "Canada", "AU": "Australia", "IN": "India", "IE": "Ireland", "NZ": "New Zealand",
             "DE": "Germany", "FR": "France", "NL": "Netherlands", "ES": "Spain", "AE": "United Arab Emirates"}
sh = open(os.path.join(ROOT, "shared/radar-data.md")).read()
# every skill opens with the same compact rules block (shared/rules-block.md, written by sync-shared.sh)
block = open(os.path.join(ROOT, "shared/rules-block.md")).read().strip()
for n0 in sorted(d for d in os.listdir(S) if os.path.isdir(os.path.join(S, d))):
    t0 = open(os.path.join(S, n0, "SKILL.md")).read()
    m0 = re.search(r"<!-- rules -->\n(.*?)\n<!-- /rules -->", t0, re.S)
    if not m0: bad.append(f"{n0}: no rules block")
    elif m0.group(1).strip() != block: bad.append(f"{n0}: rules block out of sync (run scripts/sync-shared.sh)")
    elif t0.index("<!-- rules -->") > t0.index("\n# ") + 200: bad.append(f"{n0}: rules block is not at the top of the body")
    for bare in re.findall(r"^\|.*\| Days \|", t0, re.M): bad.append(f"{n0}: a table column named only 'Days'")
    if re.search(r"still new|not spend or sales", t0): bad.append(f"{n0}: banned phrase")
mk = re.search(r"^## Markets\n(.*?)(?=^## )", sh, re.S | re.M)
if not mk: bad.append("shared/radar-data.md: no Markets section")
else:
    for tool in MARKET_TOOLS:
        if f"`{tool}`" not in mk.group(1): bad.append(f"shared/radar-data.md: Markets does not list `{tool}`")
    for cc, name in COUNTRIES.items():
        if f"{name} `{cc}`" not in mk.group(1): bad.append(f"shared/radar-data.md: Markets is missing {name} `{cc}`")
for n in names:
    p = os.path.join(S, n, "SKILL.md")
    if not os.path.exists(p): bad.append(f"{n}: no SKILL.md"); continue
    t = open(p).read()
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    if not m: bad.append(f"{n}: no frontmatter"); continue
    fm = m.group(1)
    nm = re.search(r"^name: *(.+)$", fm, re.M); ds = re.search(r'^description: *"(.*)"$', fm, re.M)
    if not nm or nm.group(1).strip() != n: bad.append(f"{n}: name does not match folder")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", n) or len(n) > 64: bad.append(f"{n}: bad name")
    if not ds: bad.append(f"{n}: description missing or not double-quoted"); continue
    d = ds.group(1); total += len(d)
    if not (1 <= len(d) <= 500): bad.append(f"{n}: description {len(d)} chars (max 500)")
    if not d.startswith("When the user"): bad.append(f"{n}: description should start 'When the user'")
    if not re.search(r"^  version: \d+\.\d+\.\d+$", fm, re.M): bad.append(f"{n}: metadata.version missing")
    if t.count("\n") > 500: bad.append(f"{n}: SKILL.md over 500 lines")
    for link in re.findall(r"\]\((references/[^)]+)\)", t):
        if not os.path.exists(os.path.join(S, n, link)): bad.append(f"{n}: missing {link}")
    rd = os.path.join(S, n, "references")
    for f in (os.listdir(rd) if os.path.isdir(rd) else []):
        if f"references/{f}" not in t: bad.append(f"{n}: references/{f} is not linked from SKILL.md")
        if f == "radar-data.md" and hashlib.md5(open(os.path.join(rd, f), "rb").read()).hexdigest() != shared: bad.append(f"{n}: radar-data.md out of sync (run scripts/sync-shared.sh)")
    for tool in set(re.findall(r"`([a-z]+(?:_[a-z]+)+)`", t)):
        if tool not in TOOLS and tool not in ("since_days", "per_brand", "min_days_live", "next_offset", "run_by", "transcripts_missing", "history_nights", "watch_url_template", "library_url", "launched_after", "advertiser_content", "min_days_lived", "transcript_chars", "rank_now", "est_share_pct", "days_live", "live_copies", "end_check", "hook_source", "ad_id", "text", "size_note", "busiest_end_dates", "not_on_library_pages", "days_lived", "best_rank", "longest_days", "ad_ids", "brand_id", "also_tracked", "max_days_lived", "groups_rule", "page_url_template", "watch_url", "page_id", "also_tracked_markets", "my_brand_note", "list_rule", "reach_note", "creatives_counted", "only_this_brand", "ad_saying_it", "lived_7_days_or_less", "lived_30_days_or_more", "sections_total", "launched_after", "best_rank_now", "longest_creative_days_live", "creative_days_live", "creative_days_lived", "creative_started", "started", "lead_ad_id", "moved_ad_id"):
            bad.append(f"{n}: unknown tool or field `{tool}`")
    # a skill that names a brand to a market tool must point at the Markets rules (radar-brand.md's Market line)
    if n != "radar-setup" and MARKET_TOOLS & set(re.findall(r"`([a-z]+(?:_[a-z]+)+)`", t)) and "Market" not in t:
        bad.append(f"{n}: calls a brand tool but never mentions the Market line or Markets")
    for other in re.findall(r"`([a-z]+(?:-[a-z]+)+)`", t):
        if other not in names and other not in ("radar-brand", ): bad.append(f"{n}: refers to unknown skill `{other}`")
    if re.search(r"\b(spend|ROAS|revenue)\b", re.sub(r"Never state or estimate.*|never.*", "", t, flags=re.I)) and n != "x": pass
print(f"{len(names)} skills, descriptions total {total} chars (pack limit 24000)")
if total > 24000: bad.append("descriptions exceed 24,000 characters in total")
for b in bad: print("PROBLEM:", b)
sys.exit(1 if bad else 0)
