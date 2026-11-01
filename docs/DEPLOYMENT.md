# Deployment status — 1 November 2026

- Public repository: https://github.com/abidtashifain-maker/GradeTargetCalc
- Latest deployed source commit: 37eca4b91efa8b2cfc24f9481ad95cce92d025b4.
- GitHub Pages source: GitHub Actions. Workflow run 41333001102 completed successfully, including build, tests and deployment.
- Custom domain configured: gradetargetcalc.com.
- IONOS DNS: apex A records 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 (TTL 300); www CNAME abidtashifain-maker.github.io (TTL 300).
- Default Site parking records replaced. Existing mail MX/SPF/DKIM/DMARC/autodiscover and Domain Connect records preserved.
- Registration contact-email confirmation completed by owner and confirmed in IONOS: verification warning removed; domain shows user-defined DNS targets.
- Latest GitHub DNS validation still reports NotServedByPagesError. Correct values are saved in IONOS, but successful public resolution/routing is not established; propagation may still be pending.
- GitHub certificate requested after DNS Check again. Current status: TLS provisioning, stage 1 of 3, Certificate Requested. HTTPS enforcement is disabled until issuance completes. Do not reset/remove the domain merely while issuance is pending.
- Google Search Console domain property sc-domain:gradetargetcalc.com created and ownership VERIFIED using the exact TXT record supplied by Google, saved at the apex in IONOS. Keep that DNS record. No third-party account permissions or automated DNS delegation were added.
- https://gradetargetcalc.com/sitemap.xml submitted; Google accepted the submission but its fetch status is Couldn't fetch. Do not describe this as successful sitemap processing or indexing.
- Google's live homepage test at 8:51 PM Riyadh: page fetch failed with Invalid server SSL certificate. Crawl allowed: Yes. Homepage not indexed. HTTPS browser visit also did not load successfully.
- Pending: certificate issuance, enable Enforce HTTPS, verify apex/www/HTTP redirects and live calculator behavior, robots and sitemap, rerun Google live test, confirm sitemap processing, then request indexing only if live test passes.
- Google Analytics remains off. AdSense is not configured or submitted; mailbox delivery, owner policy review, ad consent/CMP, publisher details and remaining QA must be confirmed before ads.
