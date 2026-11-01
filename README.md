# pihole-blocklist-analyzer

Uncommon homelab pain: You add 12 Pi-hole blocklists, DNS gets slower, and you have no idea which lists overlap, which are dead, or which are costing you queries.

This tool audits Pi-hole gravity lists locally:
- Overlap matrix between lists
- Domain count per list and unique domains across all lists
- Estimated memory/query cost
- Stale/404 lists detection
- Duplicate entries and wildcard bloat

### Why not common
No starter todo. This is ops hygiene that Pi-hole UI doesn't give you.

### Usage
```bash
pip install -r requirements.txt
python -m pihole_blocklist_analyzer /etc/pihole/adlists.list --output ./report
```

Output:
- `report.json` – machine readable stats
- `overlap.html` – heatmap
- `summary.md` – human readable findings

License: MIT
