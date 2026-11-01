# GradeTargetCalc: research, launch strategy and 90-day roadmap
Research date: 1 November 2026. Status: working strategy, not a traffic forecast.

## Evidence and limits
Live web discovery and direct competitor-page inspection were completed before implementation. This is qualitative discovery, not a localized rank-tracking or paid keyword-data study. No connected SEO dataset supplied monthly volume, country volumes, CPC, backlink authority or keyword difficulty. All those metrics remain **unverified**, including long-tail terms. Search result presence establishes existing supply and recognizable intent, not search volume. No keyword is certified easy to rank. Gemini integration discovery returned no matching plugin; Gemini was not used. An Ahrefs connection has been suggested, with no purchase authorized.

Before claiming metrics: obtain a permitted Ahrefs or Keyword Planner export for US/UK/Canada separately. Record source, collection date, exact query, match definition, country, volume estimate, KD method, top results and seasonality. Cross-check a second independent dataset or Trends where coverage permits; Trends is a relative index, not monthly volume. For new queries with no data, record unknown rather than zero. Do not delay building useful basic functionality while data access is pending.

## Launch decision
Lead with final-exam target planning and transparent grading assumptions. General head terms are contested by mature, specialized and broad calculator sites. Build supporting basic tools for user journeys, not on a claim that they are easy SEO wins. Long-tail scenarios are hypotheses to test using country-specific data and eventual Search Console impressions. Existing competitors already offer target planning and advanced functions, so these features alone are not novel.

## Keyword opportunity map
Every numeric monthly volume and KD value in this table is UNKNOWN. Competition assessments are editorial inferences from observed result pages, not measured keyword difficulty. Country assignments describe audience fit, not measured national demand.

| Cluster / query candidates | Intent | Audience fit | Qualitative competition / priority | Destination |
|---|---|---|---|---|
| final grade calculator; final exam calculator | Immediate exam target | US/Canada, some UK modules | Strong established incumbents; core user task, P1 | /final-grade-calculator/ |
| what grade do I need on my final to pass; final worth 30 percent calculator; need over 100 on final | Specific target or feasibility | US/Canada/UK | Long-tail hypothesis; P1, not proven low KD | Final tool plus pass guide; no separate pages for each weight |
| weighted grade calculator; grade calculator with weights | Combine assessment categories | All three | Many dedicated competitors; P1 utility | /weighted-grade-calculator/ |
| weighted grade calculator weights less than 100; current grade excluding ungraded assignments | Incomplete-course interpretation | All three | Specific problem hypothesis; P1 content | Weighted tool, partial-weight explanation |
| module credit weighted average calculator; university weighted average marks | Credit-weighted percentage | UK/Canada | Dedicated UK competitors exist; P2 validation | Weighted tool credit mode |
| GPA calculator; college GPA calculator | Credit-weighted grade points | Primarily US; selected Canadian systems | Strong specialists; P2 utility, not first ranking target | /gpa-calculator/ |
| semester GPA calculator with credits; GPA calculator numeric grade points | Calculate a term using a known scale | US/Canada | Useful specific intent; P2 | Same GPA page, avoid duplication |
| cumulative GPA calculator; combine semester GPAs different credits | Combine academic history | US/Canada | Existing specialists; P2 | /cumulative-gpa-calculator/ |
| grade percentage calculator; marks obtained out of total percentage | Convert points to percentage | All three | Broad calculator competition; P2 support | /grade-percentage-calculator/ |
| test score calculator questions wrong; 6 wrong out of 40 | Equal-value question score | US/Canada/UK | Existing EZ grader tools; P2 support | /test-score-calculator/ |
| grade average calculator; average grades equal weight | Arithmetic mean | All three | Broad intent, P2 support | /grade-average-calculator/ |
| weighted grades vs total points; why my grade calculator differs from gradebook | Explain method differences | All three | Specific informational hypothesis; P1 guide | /guides/weighted-vs-points-grades/ |
| Canadian percentage to GPA; UK percentage to US GPA | Conversion / applications | Canada/UK/US | Policy-dependent; do not offer universal conversion | /guides/gpa-scales-us-uk-canada/ |
| university grading calculator [institution] | Official-policy calculation | Country-specific | Deferred: verify each institution's current rules and cohort | Future only after primary-source policy review |
| final replaces lowest test calculator; drop lowest quiz calculator | Nonstandard course rules | US/Canada | RogerHub already handles many cases; P3 validate | Future tested feature, not a thin landing page |
| target GPA next semester; GPA needed for scholarship | Future target planning | US/Canada | Existing competition; P3 validate | Future target-GPA tool after demand evidence |

## Competitor review
Directly inspected:
- RogerHub final calculator: https://rogerhub.com/final-grade-calculator/ and formula sheet https://rogerhub.com/~r/final/formula.pdf . Clear core task plus advanced modes: final inside test category, multiple parts, dropped tests. Strong history, not an easy incumbent to displace. Opportunity hypothesis: approachable mobile explanation of the exact current-grade assumption and plainly worded impossible-target outcomes. Do not claim the advanced functionality is absent.
- Calculator.net grade calculator: https://www.calculator.net/grade-calculator.html . Broad grade functionality, category weighting and supporting explanations. Competes through breadth. Differentiate by a focused academic journey and visible incomplete-course interpretation. No live speed or backlink weakness was measured.
- GPACalculator.net: https://gpacalculator.net/college-gpa-calculator/ . Rich semester/cumulative features, custom scales, institutions and planning. Numeric custom-grade-point input is useful but not a unique market feature. Launch with narrower, auditable scope rather than claim superior institutional coverage.
Discovered in results, not fully UX-audited:
- https://universitygradecalculator.co.uk/ : UK weighted averages and conversion cautions.
- https://gradehub.io/ : UK degree weighting and GPA context.
- https://www.gpacalculators.ca/ : Canadian university-specific scales.
These indicate country-specific competition, not a vacant niche. No competitor's technical SEO defects, mobile scores or rankings are asserted without a corresponding audit. No competitor wording was copied into site content.

## Architecture
17 normal HTML pages plus a custom 404. Seven calculator URLs cover the eight requested candidate use cases: general and semester GPA share one page. Homepage has a working final-grade tool; the dedicated page adds full instructions, formula, example and FAQs. Three explanatory guides connect to tools. About, contact, privacy, terms and methodology are included.
All content is static HTML, with crawlable links. JavaScript handles only calculation and theme. No SPA router, external fonts, analytics, ad scripts, dependencies or images required. Canonicals and sitemap use https://gradetargetcalc.com/. Production hosting must redirect www and HTTP consistently. The draft is noindex until contact and launch details are verified; never submit the draft sitemap to Search Console.

## Content quality and international approach
Use one English page per mathematical intent rather than near-duplicate country or exam-weight pages. No hreflang until genuinely distinct regional content exists. US messaging uses credits and final exams; UK use cases explain modules and credit-weighted marks without awarding a degree classification; Canadian guidance avoids universal GPA conversion. Country-specific demand shares remain unknown. Cite institutional policies and refresh them when adding institution-specific tools. Do not use fake experts, testimonials, admissions guarantees, minimum-word targets or mass-generated keyword pages.

## Technical implementation
Unique title, description and H1 on every page; absolute canonical; XML sitemap; robots.txt; Open Graph text metadata; favicon; WebSite/WebPage/WebApplication and breadcrumb JSON-LD. No fabricated ratings and no FAQ rich-result promises. Native labels, visible focus, skip link, live result regions, keyboard controls and reduced-motion styling. Mobile CSS breakpoints at 850px and 620px; a 390px iframe layout and calculation were checked in Chrome; physical-phone and Safari/Firefox checks remain to be completed. Measure production Core Web Vitals after deployment; small asset size is not a verified CWV pass.

## AdSense preparation and launch gates
Google requires original valuable content and policy compliance; it does not promise approval for a fixed number of pages. Apply only after a public useful site, real contact channel and accurate owner-approved policies are in place. Confirm the AdSense account owner and eligibility through the secure account workflow. Never fabricate a publisher ID or ads.txt line.
Current build has no ads or analytics. Before enabling ads, update the policy for actual vendors, cookies and data uses. Google requires a certified TCF-integrated CMP for personalized ads in EEA/UK/Switzerland. Implement and verify consent before loading affected services; do not substitute a decorative accept button. Review applicable privacy obligations with the actual operator details and traffic. Keep ads away from form controls, never ask visitors to click, and inspect mobile layout after ad insertion. Start sparingly and monitor layout shifts. Privacy/terms are operational drafts, not a claim of legal compliance.
GitHub Pages supports static sites and custom-domain HTTPS, but its limits exclude sites primarily directed at commercial transactions or commercial SaaS. This free educational utility has no checkout; do not assume indefinite eligibility if its business model changes. Reassess hosting suitability before a material commercial expansion.

## Deployment plan (agent-operated after access)
1. Securely connect GitHub; identify account and confirm a new public repository named gradetargetcalc. No changes to existing repositories.
2. Confirm owner-approved public contact email, domain registrar and public launch approval. No secrets in chat.
3. Remove preview mode using PUBLIC_RELEASE=1 and verified CONTACT_EMAIL, regenerate and retest. Update privacy hosting description for actual deployment.
4. Create repository, push complete source, tests and dist. Enable Pages using the included GitHub Actions workflow; inspect the completed deploy job.
5. Verify domain ownership first, bind custom domain in Pages, then update authorized DNS records. Do not overwrite unrelated MX/TXT records. Use no wildcard.
6. Apex A: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153. www CNAME to the actual account's USERNAME.github.io (not an invented account). Recheck current GitHub guidance before changes. Optional IPv6 records per official docs.
7. Confirm public DNS and certificate issuance, enforce HTTPS and check apex/www/HTTP redirects. Check live HTML, JavaScript, robots, sitemap, 404s, inputs and mobile UI.
8. Securely authorize Search Console; add domain property, publish the returned DNS TXT, verify, submit /sitemap.xml and inspect representative URLs. Never invent verification tokens.
9. Prefer Search Console first. GA4 is optional and remains off until an owner-approved measurement plan and consent/privacy implementation exist. Do not send grades, GPA, student identifiers or input values as events.
10. Apply for AdSense only after outstanding quality and policy checks. Add actual publisher verification, CMP and ads.txt only from verified account data, with approval.

## 90-day roadmap (relative to verified launch)
| Period | Actions | Evidence / decision gate |
|---|---|---|
| Days 1–7 | Deploy, verify DNS/HTTPS, complete Search Console, inspect primary tools, test accessibility and phone layout, confirm contact delivery | Deployment run, successful HTTP checks, GSC ownership and sitemap status; no ranking promises |
| Days 8–14 | Obtain authorized keyword estimates for US/UK/Canada; compare final-pass and incomplete-weight clusters; review query intent manually | Dated source-specific metrics; mark unavailable data unknown |
| Days 15–30 | Review early indexing/errors weekly; have students independently try tools; revise confusing inputs and guides; ask relevant tutors for feedback | Issues reproduced and fixed; usability feedback, indexed pages; traffic may be minimal |
| Days 31–45 | Choose one additional scenario from measured queries (e.g., remaining-assignment target or dropped score); write formula and regression cases before development | Search demand or repeat user requests plus clear mathematical scope |
| Days 46–60 | Publish one tested new tool/feature and one supporting guide if evidence supports it; improve titles for actual impressions; add contextual internal links | Distinct purpose, tested examples, no duplicate intent; compare page/query performance |
| Days 61–75 | Review performance and device issues; prepare AdSense application if public contact/content/consent gates pass; evaluate one institution-specific page only with official cohort rules | Accurate policy sources, known operator, verified account/CMP setup; approval not assumed |
| Days 76–90 | Compare periods, prioritize useful pages, merge weak overlapping content, plan next quarter from queries and feedback | GSC clicks/impressions/CTR by country/device/page; no paid traffic or revenue projections |

### Monitoring and ethical outreach
Weekly: indexing exclusions, crawl failures, tool error reports, GSC queries by target country/device. Monthly: compare 28-day periods with seasonality caveats; low sample sizes cannot prove causality. Once field data exists, examine LCP, INP and CLS; address actual regressions. Do not measure success by page count.
Offer a short original grading-method handout to teachers and tutoring centers; request genuine feedback and permit voluntary resource links. Contribute useful answers in communities where linking is allowed; disclose ownership and avoid repetitive promotion. Do not buy links, use PBNs, spam comments or submit to bulk directories. Never send outreach messages without explicit user authorization.

## Primary-source references reviewed
- Google Search Essentials: https://developers.google.com/search/docs/essentials
- Helpful content guidance: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- AdSense eligibility: https://support.google.com/adsense/answer/9724?hl=en
- Advertising privacy disclosures: https://support.google.com/adsense/answer/1348695?hl=en
- CMP requirements: https://support.google.com/adsense/answer/13554116?hl=en
- GitHub domain setup: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
- GitHub HTTPS: https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https
- GitHub usage limits: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
- Illinois GPA: https://www.registrar.illinois.edu/courses-grades/calculate-your-gpa/
- UBC grades: https://students.ok.ubc.ca/academic-success/grades-performance/
- Manchester grading: https://www.manchester.ac.uk/study/international/study-abroad-exchange/support/grading-assessment/

## Owner updates
GitHub connection verified: abidtashifain-maker. Registrar confirmed: IONOS.com. Use Info@gradetargetcalc.com for all public project contact references. Mailbox existence/delivery is not verified; no test email sent. Public repository/launch approval remains pending. The connector currently exposes no operation to create repositories or configure Pages; secure browser interaction may be needed for those steps.

## Publishing approval
Owner approved a public repository named GradeTargetCalc, publishing, and IONOS custom-domain connection. Initial GitHub secure browser authentication was declined. Do not retry credential collection unless the user asks. Production files are ready; no live deployment or DNS changes have occurred.
